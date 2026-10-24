#!/usr/bin/env python3
"""Safely translate an ML4T unit while preserving English-source LaTeX verbatim.

prepare: extract original markdown from a validated source, mask math spans,
         create a text-only translation task and a checksum-locked math map.
restore: restore exact original math into a normalized AI reply after strict
         marker, ID, placeholder and source-sha checks. Never edits originals.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

UID = re.compile(r"c\d{4}-p\d{3}\Z")
BEGIN = re.compile(r"<<<ML4T-ZH-BEGIN:(c\d{4}-p\d{3})>>>")
END = re.compile(r"<<<ML4T-ZH-END:(c\d{4}-p\d{3})>>>")
MARKER_LINE = re.compile(r"\s*(?:\\?<escape>)?(?:<<<|<<\\<)ML4T-ZH-(BEGIN|END):(c\d{4}-p\d{3})>>>\\?\s*")
TOKEN_PATTERN = re.compile(r"\[\[ML4T_MATH_\d{3}\]\]")
MATH = re.compile(
    r"(?s)(?<!\\)\$\$.*?(?<!\\)\$\$|"
    r"(?<!\\)\$(?:\\.|[^$\\])*?(?<!\\)\$|"
    r"\\\[.*?\\\]|\\\(.*?\\\)"
)

class Invalid(ValueError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def work_data(root: Path, source: str, uid: str):
    src = (root / source).resolve()
    if not src.is_relative_to(root) or src.suffix != ".ipynb" or src.stem.endswith("_zh"):
        raise Invalid("source 必須是專案內英文 .ipynb")
    if not UID.fullmatch(uid):
        raise Invalid("翻譯單元 ID 格式錯誤")
    if not src.is_file():
        raise Invalid("找不到英文 Notebook")
    rel = src.relative_to(root)
    work = root / "translations/work" / rel.with_suffix("")
    manifest = json.loads((work / "manifest.json").read_text("utf-8"))
    if manifest.get("source") != rel.as_posix() or manifest.get("source_sha256") != sha(src.read_bytes()):
        raise Invalid("英文來源與 manifest 不一致，停止處理")
    unit = next((u for u in manifest["units"] if u["id"] == uid), None)
    if unit is None:
        raise Invalid(f"未找到 {uid} 翻譯單元")
    packs = json.loads((work / "pack_manifest.json").read_text("utf-8"))
    pack_num = next((p["number"] for p in packs["packs"] if uid in p["ids"]), None)
    if pack_num is None or packs.get("source_sha256") != manifest["source_sha256"]:
        raise Invalid("Pack manifest 不匹配")
    if (work / "responses" / f"{uid}.md").exists():
        raise Invalid(f"{uid} 已有 response；請先確認是否已完成")
    nb = json.loads(src.read_text("utf-8"))
    cell = nb["cells"][unit["cell_index"]]
    text = cell["source"]
    text = "".join(text) if isinstance(text, list) else text
    original = text[unit["start"]:unit["end"]]
    if sha(original.encode("utf-8")) != unit["source_sha256"]:
        raise Invalid("單元原文 SHA256 不一致")
    return work, original, unit, pack_num


def mask_math(original: str):
    replacements = {}
    def replace(m):
        key = f"[[ML4T_MATH_{len(replacements)+1:03d}]]"
        if key in original:
            raise Invalid("來源已有保留的公式佔位符，停止")
        replacements[key] = m.group()
        return key
    masked = MATH.sub(replace, original)
    if not replacements:
        raise Invalid("此單元沒有偵測到 $...$ 或 $$...$$ 公式，請先檢查來源格式")
    # Prevent an unbalanced delimiter being sent to AI and triggering the same issue.
    if "\\frac" in masked:
        raise Invalid("來源含公式區塊外的 \\frac，請人工檢查，避免遺漏數學式")
    return masked, replacements


def write_new_or_same(p: Path, body: bytes):
    if p.exists():
        if p.read_bytes() != body:
            raise Invalid(f"檔案已存在且內容不同，拒絕覆寫：{p}")
        return False
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(body)
    return True


def prepare(root: Path, source: str, uid: str):
    work, original, unit, pack_num = work_data(root, source, uid)
    masked, replacements = mask_math(original)
    meta = {"source": source, "uid": uid, "source_sha256": unit["source_sha256"],
            "replacements": replacements}
    task = (
        f"# ML4T 單元 {uid} 的純文字翻譯任務\n\n"
        "將下面英文 Markdown 譯成台灣繁體中文，忠實保留段落、標題和非公式 Markdown。\n"
        "重要：原文所有 LaTeX 公式已移除並改成 [[ML4T_MATH_001]] 等佔位符。\n"
        "你只能原樣複製佔位符，不要輸出任何 LaTeX 公式、反斜線命令或數學推導。\n"
        "不要增加或刪除任何佔位符；每個原樣出現一次並保持次序。\n"
        "只輸出 BEGIN/END 及其間的中文譯文，標記獨占一行，無額外解說。\n\n"
        "## 原文（公式已遮蔽）\n\n"
        "~~~~~~markdown\n" + masked.rstrip("\n") + "\n~~~~~~\n\n"
        f"<<<ML4T-ZH-BEGIN:{uid}>>>\n"
        "（請以中文譯文取代本行，保留全部公式佔位符）\n"
        f"<<<ML4T-ZH-END:{uid}>>>\n"
    )
    task_path = work / "packs" / f"math_safe_{uid}.md"
    meta_path = work / "packs" / f"math_safe_{uid}.json"
    # Preflight both files before writing either.
    pending = [(task_path, task.encode("utf-8")), (meta_path, (json.dumps(meta, ensure_ascii=False, indent=2)+"\n").encode("utf-8"))]
    for p, data in pending:
        if p.exists() and p.read_bytes() != data:
            raise Invalid(f"準備檔已存在且不同，停止：{p}")
    for p, data in pending:
        write_new_or_same(p, data)
    print(f"已建立純文字翻譯任務：{task_path.relative_to(root)}")
    print(f"遮蔽數學區塊：{len(replacements)} 處（還原時會原樣保留）")
    print(f"請把 GPT 回覆另存：{(work/'inbox'/f'math_safe_{uid}_reply.txt').relative_to(root)}")
    print(f"本單元原屬 Pack {pack_num:03d}，完成後用 --pack {pack_num} --partial 匯入")


def normalize_and_extract(raw: str, uid: str):
    chunks = []
    opened = False
    ended = False
    for lineno, line in enumerate(raw.splitlines(keepends=True), 1):
        body = line.rstrip("\r\n")
        marker = MARKER_LINE.fullmatch(body)
        if marker:
            kind, found = marker.group(1), marker.group(2)
            if found != uid:
                raise Invalid(f"第 {lineno} 行 ID 錯誤：{found}")
            if kind == "BEGIN":
                if opened or ended:
                    raise Invalid(f"第 {lineno} 行重複 BEGIN")
                opened = True
            else:
                if not opened or ended:
                    raise Invalid(f"第 {lineno} 行 END 沒有對應 BEGIN")
                opened = False
                ended = True
            continue
        if "ML4T-ZH-" in body:
            raise Invalid(f"第 {lineno} 行標記格式無法辨識")
        if opened:
            chunks.append(line)
        elif body.strip() and body.strip() != "\\":
            raise Invalid(f"第 {lineno} 行標記外有多餘文字")
    if opened or not ended:
        raise Invalid("回覆不完整：缺少 END 標記")
    result = "".join(chunks).strip()
    if not result:
        raise Invalid("翻譯內容為空")
    return result


def restore(root: Path, source: str, uid: str):
    work, original, unit, pack_num = work_data(root, source, uid)
    meta_path = work / "packs" / f"math_safe_{uid}.json"
    meta = json.loads(meta_path.read_text("utf-8"))
    if meta.get("source") != source or meta.get("uid") != uid or meta.get("source_sha256") != unit["source_sha256"]:
        raise Invalid("公式對照資料與原始來源不一致")
    masked, replacements = mask_math(original)
    if replacements != meta["replacements"]:
        raise Invalid("公式對照資料與原始來源不同")
    reply_path = work / "inbox" / f"math_safe_{uid}_reply.txt"
    raw = reply_path.read_text("utf-8-sig")
    translation = normalize_and_extract(raw, uid)
    found = TOKEN_PATTERN.findall(translation)
    if found != list(replacements):
        raise Invalid(f"公式佔位符數量或順序錯誤：應有 {list(replacements)}，實際 {found}")
    for key, math in replacements.items():
        translation = translation.replace(key, math)
    out_path = work / "inbox" / f"math_safe_{uid}_restored.txt"
    output = f"<<<ML4T-ZH-BEGIN:{uid}>>>\n{translation}\n<<<ML4T-ZH-END:{uid}>>>\n"
    write_new_or_same(out_path, output.encode("utf-8"))
    print(f"PASS：已原樣還原 {len(replacements)} 處公式，且單元 ID 正確")
    print(f"已產生可匯入回覆：{out_path.relative_to(root)}")
    print("匯入指令：")
    print(f"python3 translation_tools/collect_translation.py {source} --pack {pack_num} --file {out_path.relative_to(root)} --partial")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "restore"])
    parser.add_argument("source", help="英文 Notebook 路徑")
    parser.add_argument("unit_id", help="例如 c0021-p000")
    args = parser.parse_args()
    root = Path.cwd().resolve()
    try:
        if args.action == "prepare":
            prepare(root, args.source, args.unit_id)
        else:
            restore(root, args.source, args.unit_id)
    except (Invalid, OSError, ValueError, KeyError, IndexError) as exc:
        print("ERROR：" + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
