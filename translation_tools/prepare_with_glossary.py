#!/usr/bin/env python3
"""Generate ML4T AI translation tasks with only relevant glossary terms.

Safe wrapper around the existing ``nb_zh.py prepare`` command. It does not modify
nb_zh.py, any original notebook, or any existing translation workspace.
Uses only Python stdlib and the existing nb_zh.py module.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import nb_zh

DEFAULT_GLOSSARY = "translations/glossary_zh_TW.md"


def glossary_rows(path: Path) -> list[tuple[str, str]]:
    """Read the two-column English/zh-TW tables in the user's Markdown glossary."""
    entries: list[tuple[str, str]] = []
    seen: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            continue
        english, chinese = cells
        if (not english or not chinese or english == "英文"
                or re.fullmatch(r":?-{2,}:?", english)
                or re.fullmatch(r":?-{2,}:?", chinese)):
            continue
        key = english.casefold()
        if key in seen:
            if seen[key] != chinese:
                raise nb_zh.PipelineError(f"術語表重複且譯法不一致：{english}")
            continue
        seen[key] = chinese
        entries.append((english, chinese))
    if not entries:
        raise nb_zh.PipelineError(f"找不到有效的英文／繁體中文術語表格：{path}")
    return entries


def matches_english(term: str, text: str) -> bool:
    """Case-insensitive whole-word-ish match; accept singular/plural forms.

    An entry such as 'Gaussian mixture model (GMM)' matches the full phrase
    or its acronym. It intentionally avoids matches within longer identifiers.
    """
    alias_match = re.fullmatch(r"(.+?)\s+\(([A-Za-z][A-Za-z0-9_-]*)\)", term)
    variants = [alias_match.group(1), alias_match.group(2)] if alias_match else [term]
    for variant in variants:
        words = variant.split()
        if not words:
            continue
        escaped = [re.escape(w) for w in words]
        last = escaped[-1]
        # Optionally match simple inflections (model/models, returns/return).
        if len(words[-1]) > 3 and words[-1].lower().endswith("s"):
            last = re.escape(words[-1][:-1]) + "s?"
        elif len(words[-1]) > 2 and words[-1].isalpha():
            last += "s?"
        escaped[-1] = last
        pattern = r"(?<![A-Za-z0-9_])" + r"\s+".join(escaped) + r"(?![A-Za-z0-9_])"
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False


def selected_for_batch(entries: list[tuple[str, str]], text: str, max_terms: int) -> list[tuple[str, str]]:
    matching = [(en, zh) for en, zh in entries if matches_english(en, text)]
    if len(matching) <= max_terms:
        return matching
    # Prefer more specific multiword expressions if many terms are present.
    priority = sorted(matching, key=lambda item: (-len(item[0].split()), -len(item[0]), item[0].casefold()))
    keep = set(priority[:max_terms])
    return [pair for pair in matching if pair in keep]


def prepare_glossary(args: argparse.Namespace) -> None:
    root = nb_zh.root_dir()
    glossary_path = (root / args.glossary).resolve()
    if not glossary_path.is_relative_to(root):
        raise nb_zh.PipelineError("術語表必須位於 ML4T 專案內。")
    if not glossary_path.is_file():
        raise nb_zh.PipelineError(f"找不到術語表：{glossary_path.relative_to(root)}")
    entries = glossary_rows(glossary_path)
    _, rel, work, _ = nb_zh.paths(root, args.source)
    if work.exists():
        raise nb_zh.PipelineError(f"工作區已存在，為保護原有進度而拒絕覆蓋：{work.relative_to(root)}")

    # Prepare using the exact, already-tested existing tool. It refuses to
    # overwrite any existing workspace, preserving previous AI translations.
    nb_zh.prepare(argparse.Namespace(source=args.source,
                                    max_chars=args.max_chars,
                                    batch_chars=args.batch_chars))
    manifest_file = work / "manifest.json"
    manifest = nb_zh.read_json(manifest_file)
    source_file, _ = nb_zh.source_path(root, args.source)
    nb = nb_zh.read_json(source_file)
    units = {u["id"]: u for u in manifest["units"]}
    total_terms = 0
    for number, batch in enumerate(manifest["batches"], 1):
        english_parts = []
        for uid in batch:
            u = units[uid]
            raw = nb_zh.text_of(nb["cells"][u["cell_index"]])[u["start"]:u["end"]]
            if nb_zh.digest(raw.encode("utf-8")) != u["source_sha256"]:
                raise nb_zh.PipelineError(f"來源驗證失敗：{uid}，請停止操作。")
            english_parts.append(raw)
        found = selected_for_batch(entries, "\n".join(english_parts), args.max_terms)
        total_terms += len(found)
        if not found:
            continue
        insert = [
            "## 本批次相關術語（由共用術語表篩選）",
            "",
            "以下是建議譯法；請按原文語境使用，不要在 AI 回覆中複製此表。",
            "原始程式碼、公式、檔案路徑及資料名稱一律不改。",
            "",
        ]
        insert.extend(f"- {en} → {zh}" for en, zh in found)
        insert.append("")
        addition = "\n".join(insert) + "\n"
        task = work / "tasks" / f"batch_{number:03d}.md"
        original = task.read_text(encoding="utf-8")
        anchor = "## 單元："
        at = original.find(anchor)
        if at < 0:
            raise nb_zh.PipelineError(f"找不到任務單元的起始位置：{task}")
        # Keep one trailing newline to satisfy git diff --check on new task files.
        new_text = (original[:at] + addition + original[at:]).rstrip("\n") + "\n"
        tmp = task.with_suffix(".md.tmp")
        tmp.write_text(new_text, encoding="utf-8", newline="\n")
        tmp.replace(task)

    manifest["glossary_info"] = {
        "path": glossary_path.relative_to(root).as_posix(),
        "sha256": hashlib.sha256(glossary_path.read_bytes()).hexdigest(),
        "entries": len(entries),
        "max_terms_per_batch": args.max_terms,
    }
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"術語表：{glossary_path.relative_to(root)}（{len(entries)} 條）")
    print(f"已為 {len(manifest['batches'])} 批任務加入相關術語（合計 {total_terms} 條批次術語）。")
    print("舊翻譯工作區未改動；請直接把新 tasks/batch_XXX.md 交給 AI。")


def main() -> None:
    parser = argparse.ArgumentParser(description="為新的 ML4T 翻譯工作區建立含精簡術語的 AI 任務")
    parser.add_argument("source", help="英文原始 .ipynb，相對專案根目錄")
    parser.add_argument("--max-chars", type=int, default=1800)
    parser.add_argument("--batch-chars", type=int, default=5000)
    parser.add_argument("--max-terms", type=int, default=25, help="每批最多附帶的術語數，預設 25")
    parser.add_argument("--glossary", default=DEFAULT_GLOSSARY, help="共用術語表的相對路徑")
    args = parser.parse_args()
    if args.max_chars < 200 or args.batch_chars < 200 or not (1 <= args.max_terms <= 100):
        parser.error("--max-chars 與 --batch-chars 至少 200；--max-terms 需介於 1 至 100。")
    try:
        prepare_glossary(args)
    except (nb_zh.PipelineError, OSError, ValueError, TypeError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
