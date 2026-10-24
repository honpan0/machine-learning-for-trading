#!/usr/bin/env python3
"""ML4T A2: repair, preflight, split, and ingest translation packs without API.

Original AI reply bytes are NEVER modified. Ingested translations use the same
nb_zh.parse_answer validation and the same protected per-unit response format.
"""
from __future__ import annotations

import argparse
import subprocess
import json
import sys
from pathlib import Path

import nb_zh
import pack_translation as packing
import repair_ai_response as repair


class CollectError(nb_zh.PipelineError):
    pass


def load_packs(root: Path, source: str) -> tuple[Path, dict, dict, dict]:
    _, rel, work, manifest, _, units = packing.prepared(root, source)
    p = work / "pack_manifest.json"
    if not p.is_file():
        raise CollectError("未找到 pack_manifest.json，請先執行 pack_translation.py。")
    data = json.loads(p.read_text(encoding="utf-8"))
    if (data.get("version") != packing.VERSION or data.get("source") != rel.as_posix()
            or data.get("source_sha256") != manifest["source_sha256"]):
        raise CollectError("Pack 清單與英文來源不相符；停止匯入。")
    all_ids = set(units)
    assigned: set[str] = set()
    unit_batch = {uid: i for i, batch in enumerate(manifest["batches"], 1) for uid in batch}
    packs = data.get("packs")
    if not isinstance(packs, list) or not packs:
        raise CollectError("Pack 清單沒有有效內容。")
    for i, p_info in enumerate(packs, 1):
        if p_info.get("number") != i or p_info.get("file") != f"pack_{i:03d}.md":
            raise CollectError("Pack 序號或檔案名稱不正確。")
        task = work / "packs" / p_info["file"]
        if not task.is_file() or packing.sha(task.read_bytes()) != p_info["task_sha256"]:
            raise CollectError(f"Pack {i:03d} 任務被修改或遺失，停止匯入。")
        from_batches = [uid for b in p_info["batches"] for uid in b["ids"]]
        if from_batches != p_info["ids"] or not from_batches:
            raise CollectError(f"Pack {i:03d} 的單元對應表不一致。")
        for b in p_info["batches"]:
            if not isinstance(b["batch"], int) or not b["ids"]:
                raise CollectError(f"Pack {i:03d} 批次資訊不完整。")
            for uid in b["ids"]:
                if uid not in all_ids or unit_batch[uid] != b["batch"] or uid in assigned:
                    raise CollectError(f"Pack {i:03d} 包含重複、錯誤或跨 Batch 單元：{uid}")
                assigned.add(uid)
    return work, manifest, data, units


def safe_parse(text: str, allowed: list[str], partial: bool) -> tuple[dict[str, str], int, int, bool]:
    normalized, replaced, joins = repair.normalize(text)
    incomplete_tail = False
    if partial:
        # A truncated final block may be ignored, but NO malformed / unexpected
        # marker or nested BEGIN can be silently discarded.
        active = None
        cut = None
        pos = 0
        for line in normalized.splitlines(keepends=True):
            marker = line.strip()
            b = nb_zh.BEGIN.fullmatch(marker)
            e = nb_zh.END.fullmatch(marker)
            if b:
                if active is not None:
                    raise CollectError("回覆中有巢狀 BEGIN，拒絕部分匯入。")
                active, cut = b.group(1), pos
            elif e:
                if active != e.group(1):
                    raise CollectError("回覆中有不相符的 END，拒絕部分匯入。")
                active, cut = None, None
            elif "ML4T-ZH-BEGIN:" in line or "ML4T-ZH-END:" in line:
                raise CollectError("有未知的標記格式，拒絕部分匯入。")
            pos += len(line)
        if active is not None:
            if active not in allowed:
                raise CollectError(f"截斷單元 ID 不在本 Pack：{active}")
            normalized = normalized[:cut]
            incomplete_tail = True
    translations = nb_zh.parse_answer(normalized)
    if not translations:
        raise CollectError("沒有可安全匯入的完整翻譯單元。")
    if not set(translations) <= set(allowed):
        raise CollectError(f"出現非本 Pack 單元：{sorted(set(translations)-set(allowed))}")
    # repair.validate also rejects suspicious marker-like text inside translations.
    repair.validate(normalized, list(translations))
    if not partial and set(translations) != set(allowed):
        raise CollectError("Pack 缺少翻譯單元：" + ", ".join(sorted(set(allowed) - set(translations)))
                           + "。如 AI 因長度限制中止，可使用 --partial 保留已完成單元。")
    return translations, replaced, joins, incomplete_tail


def make_retry_task(root: Path, source: str, work: Path, manifest: dict, pack: dict,
                    missing: list[str]) -> Path:
    """Render a self-contained retry task for missing IDs; never overwrite a retry."""
    _, rel, _, source_manifest, nb, units = packing.prepared(root, source)
    group = []
    for b in pack["batches"]:
        selected = [uid for uid in b["ids"] if uid in missing]
        if selected:
            group.append({"batch": b["batch"], "ids": selected,
                          "chars": sum(units[uid]["chars"] for uid in selected)})
    pseudo = {"number": pack["number"], "batches": group,
              "ids": [uid for b in group for uid in b["ids"]]}
    body, _ = packing.render_pack(root, rel, source_manifest, nb, units, pseudo, 25)
    name = f"retry_pack_{pack['number']:03d}_{packing.sha(body.encode('utf-8'))[:10]}.md"
    path = work / "packs" / name
    if not path.exists():
        path.write_text(body, encoding="utf-8", newline="\n")
    elif path.read_text(encoding="utf-8") != body:
        raise CollectError(f"補翻檔名碰撞：{path}")
    return path


def collect_one(root: Path, source: str, work: Path, manifest: dict,
                info: dict, pack_num: int, raw_path: Path,
                partial: bool, finalize: bool) -> int:
    if pack_num < 1 or pack_num > len(info["packs"]):
        raise CollectError(f"Pack 序號須介於 1 至 {len(info['packs'])}")
    pack = info["packs"][pack_num - 1]
    if not raw_path.is_file():
        raise CollectError(f"找不到 AI 回覆：{raw_path}")
    raw_bytes = raw_path.read_bytes()
    try:
        raw = raw_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise CollectError("AI 回覆不是有效 UTF-8") from exc
    translations, replaced, joins, incomplete_tail = safe_parse(raw, pack["ids"], partial)
    pending = {}
    for uid, zh in translations.items():
        existing = nb_zh.response_file(work, uid)
        if existing.exists() and existing.read_text(encoding="utf-8").strip() != zh:
            raise CollectError(f"{uid} 已有不同翻譯，拒絕覆寫。請人工比較後再處理。")
        if not existing.exists() or not existing.read_text(encoding="utf-8").strip():
            pending[uid] = zh
    # Preflight archive collision before writing ANY output.
    archive = work / "inbox" / f"pack_{pack_num:03d}_{packing.sha(raw_bytes)[:12]}.txt"
    if archive.exists() and archive.read_bytes() != raw_bytes:
        raise CollectError(f"回覆封存檔衝突：{archive}")
    # All structural checks, collision checks and translation-preservation checks passed.
    archive.parent.mkdir(exist_ok=True)
    if not archive.exists():
        archive.write_bytes(raw_bytes)
    for uid, zh in pending.items():
        nb_zh.response_file(work, uid).write_text(zh + "\n", encoding="utf-8", newline="\n")
    done = set(translations)
    completed_in_pack = [uid for uid in pack["ids"] if packing.is_complete(work, uid)]
    missing = [uid for uid in pack["ids"] if uid not in completed_in_pack]
    print(f"Pack {pack_num:03d}：驗證 {len(done)} 個翻譯單元；新增匯入 {len(pending)} 個；"
          f"修復標記 {replaced}；黏連標記 {joins}；剩餘 {len(missing)}。")
    if incomplete_tail:
        print("  AI 回覆末尾有未完成單元；已忽略該單元，不匯入不完整的內容。")
    if missing:
        if partial:
            retry = make_retry_task(root, source, work, manifest, pack, missing)
            print(f"  補翻任務：{retry.relative_to(root)}（只包含缺漏單元）")
        else:
            # Unreachable in strict mode, included for explicit safety.
            raise CollectError("嚴格模式仍存在缺漏單元")
    if finalize:
        remaining = [u["id"] for u in manifest["units"] if not packing.is_complete(work, u["id"])]
        if not remaining:
            out = root / source
            zh = out.with_name(out.stem + "_zh.ipynb")
            if not zh.exists():
                nb_zh.build(argparse.Namespace(source=source, replace=False))
            nb_zh.verify(argparse.Namespace(source=source))
            print("全部單元已完成，中文版 Notebook 驗證成功。")
            dashboard = root / "translation_tools" / "progress_dashboard.py"
            if dashboard.is_file():
                check = subprocess.run([sys.executable, str(dashboard), "--write"], cwd=root,
                                       capture_output=True, text=True, encoding="utf-8")
                if check.returncode == 0:
                    print("全專案進度報表已更新。")
                else:
                    print("WARNING：Notebook 已通過驗證，但進度報表更新未成功；請單獨執行 progress_dashboard.py --write。")
        else:
            print(f"Notebook 還有 {len(remaining)} 個未翻譯單元；尚未組裝。")
    return len(pending)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="ML4T A2：自動修復 Pack 標記、分拆並匯入翻譯結果")
    ap.add_argument("source", help="原始英文 .ipynb 的相對路徑")
    choice = ap.add_mutually_exclusive_group(required=True)
    choice.add_argument("--pack", type=int, help="匯入指定 Pack（從 1 開始）")
    choice.add_argument("--all", action="store_true", help="匯入 inbox/ 中已存放的全部 Pack 回覆")
    ap.add_argument("--file", help="AI 回覆 UTF-8 檔案；--pack 使用，預設 inbox/pack_NNN.txt")
    ap.add_argument("--partial", action="store_true", help="明確允許安全匯入完整單元，並產生缺漏補翻任務")
    ap.add_argument("--no-finalize", action="store_true", help="全部完成後不要自動 build / verify")
    args = ap.parse_args(argv)
    if args.all and args.file:
        ap.error("--all 不支援 --file；請先把每份回覆放進 inbox/pack_NNN.txt。")
    try:
        root = nb_zh.root_dir()
        work, manifest, info, _ = load_packs(root, args.source)
        if args.all:
            jobs = [(p["number"], work / "inbox" / f"pack_{p['number']:03d}.txt")
                    for p in info["packs"] if (work / "inbox" / f"pack_{p['number']:03d}.txt").is_file()]
            if not jobs:
                raise CollectError("inbox/ 中沒有 pack_NNN.txt。")
        else:
            raw = Path(args.file).expanduser() if args.file else (work / "inbox" / f"pack_{args.pack:03d}.txt")
            jobs = [(args.pack, raw)]
        for idx, file in jobs:
            collect_one(root, args.source, work, manifest, info, idx, file, args.partial, not args.no_finalize)
        print("已完成匯入；英文 Notebook、原 Batch 任務與來源程式碼皆未修改。")
        return 0
    except (CollectError, nb_zh.PipelineError, repair.RepairError, OSError,
            ValueError, KeyError, TypeError, IndexError) as exc:
        print("ERROR：" + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
