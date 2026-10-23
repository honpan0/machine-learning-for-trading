#!/usr/bin/env python3
"""Read-only ML4T translation progress scanner.  Python standard library only.

Usage (run at repository root):
    python3 translation_tools/progress_dashboard.py
    python3 translation_tools/progress_dashboard.py --write

Existing translation data, English notebooks, and Chinese notebooks are never modified.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

# Import the exact same notebook safety checks used by the existing build/verify tool.
import nb_zh

IGNORED_DIRS = {
    ".git", ".venv", ".venvs", ".ipynb_checkpoints", "translations",
    "node_modules", "__pycache__", "build", "dist", ".tox", ".mypy_cache",
}
STATE_LABELS = {
    "not_started": "未開始",
    "in_progress": "翻譯中",
    "ready": "已翻完／待組裝",
    "built_unchecked": "已組裝／尚未驗證",
    "verified": "已組裝／驗證通過",
    "broken": "需要檢查",
    "stale": "原版已變更",
}


@dataclass
class Record:
    source: str
    group: str
    state: str
    completed: int = 0
    total: int = 0
    batches_done: int = 0
    batches_total: int = 0
    output: bool = False
    note: str = ""

    @property
    def ratio(self) -> str:
        return f"{self.completed}/{self.total}" if self.total else "—"


def root_dir() -> Path:
    here = Path.cwd().resolve()
    for item in (here, *here.parents):
        if (item / ".git").exists() and (item / "pyproject.toml").exists():
            return item
    raise RuntimeError("請先 cd 到 ML4T 根目錄（包含 .git 與 pyproject.toml）。")


def group_for(relative: Path) -> str:
    first = relative.parts[0]
    if re.match(r"^\d{2}_", first):
        return first
    if first == "case_studies" and len(relative.parts) >= 3:
        return "case_studies/" + relative.parts[1]
    if first == "case_studies":
        return "case_studies/(root)"
    if first == "data":
        return "data"
    return first


def find_sources(root: Path) -> list[Path]:
    """Only original .ipynb with an existing same-basename Jupytext .py.

    This mirrors the 483 paired notebooks from the project's sync check, and
    deliberately ignores derivative *_zh.ipynb and translation workspaces.
    """
    found: list[Path] = []
    for ipynb in root.rglob("*.ipynb"):
        rel = ipynb.relative_to(root)
        if any(part in IGNORED_DIRS for part in rel.parts[:-1]):
            continue
        if ipynb.stem.endswith("_zh"):
            continue
        if ipynb.with_suffix(".py").is_file():
            found.append(rel)
    return sorted(found)


def read_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8").strip() if p.is_file() else ""


def inspect(root: Path, rel: Path, check_output: bool = True) -> Record:
    src = root / rel
    work = root / "translations" / "work" / rel.with_suffix("")
    manifest_p = work / "manifest.json"
    out = src.with_name(src.stem + "_zh.ipynb")
    rec = Record(rel.as_posix(), group_for(rel), "not_started", output=out.exists())
    if not manifest_p.exists():
        if out.exists():
            rec.state, rec.note = "broken", "找到 _zh.ipynb，但缺少 manifest.json"
        return rec
    try:
        m = read_manifest(manifest_p)
        if m.get("version") != nb_zh.VERSION or m.get("source") != rec.source:
            raise ValueError("manifest 版本或 source 路徑不符合目前工具")
        units = m["units"]
        batches = m["batches"]
        if not isinstance(units, list) or not units or not isinstance(batches, list):
            raise ValueError("manifest units/batches 無效")
        unit_ids = [u["id"] for u in units]
        if len(unit_ids) != len(set(unit_ids)) or set(unit_ids) != set(uid for batch in batches for uid in batch):
            raise ValueError("manifest 有重複或缺失的翻譯單元 ID")
        rec.total = len(unit_ids)
        done = {uid for uid in unit_ids if read_text(work / "responses" / f"{uid}.md")}
        rec.completed = len(done)
        rec.batches_total = len(batches)
        rec.batches_done = sum(bool(batch) and all(uid in done for uid in batch) for batch in batches)
        actual_sha = hashlib.sha256(src.read_bytes()).hexdigest()
        if actual_sha != m.get("source_sha256"):
            rec.state, rec.note = "stale", "英文來源檔已不同於 prepare 時；請勿直接重設進度"
            return rec
        if rec.completed != rec.total:
            if out.exists():
                rec.state, rec.note = "broken", "仍有未完成的翻譯，但已存在 _zh.ipynb"
            else:
                rec.state = "in_progress"
            return rec
        if not out.exists():
            rec.state = "ready"
            return rec
        if not check_output:
            rec.state, rec.note = "built_unchecked", "中文版已存在，但本次沒有進行完整驗證"
            return rec
        nb_zh.verify_notebook(src, out, m, work)
        # Stronger rebuildability guarantee: derivative prose must match saved responses.
        derived = nb_zh.read_json(out)
        original = nb_zh.read_json(src)
        cells = defaultdict(list)
        for u in units:
            cells[u["cell_index"]].append(u)
        for i, grouped in cells.items():
            expected = nb_zh.translated_text(original["cells"][i], grouped, work)
            actual = nb_zh.text_of(derived["cells"][i])
            if actual != expected:
                raise ValueError(f"Markdown 儲存格 {i} 與 responses 不一致（可能曾手動改中文版）")
        rec.state = "verified"
    except (ValueError, OSError, KeyError, IndexError, TypeError, json.JSONDecodeError, nb_zh.PipelineError) as exc:
        rec.state = "broken"
        rec.note = str(exc).replace("\n", " ")[:230]
    return rec


def summary(records: list[Record]) -> str:
    total = len(records)
    counts = Counter(rec.state for rec in records)
    initiated = total - counts["not_started"]
    completed_units = sum(rec.completed for rec in records)
    total_units = sum(rec.total for rec in records)
    base = [
        "ML4T 中英對照翻譯總覽（只讀掃描）",
        "=" * 55,
        f"已發現原始配對 Notebook：{total} 份（預期原專案為 483 份）",
        f"已啟動：{initiated}｜未開始：{counts['not_started']}｜翻譯中：{counts['in_progress']}｜待組裝：{counts['ready']}",
        f"已驗證：{counts['verified']}｜未驗證：{counts['built_unchecked']}｜來源已變更：{counts['stale']}｜需要檢查：{counts['broken']}",
        f"翻譯單元完成：{completed_units}/{total_units}（僅統計已 prepare 的 Notebook）",
        "",
        "分類總數：",
    ]
    chapters = sum(rec.group[:2].isdigit() and re.match(r"^\d{2}_", rec.group) is not None for rec in records)
    cases = sum(rec.group.startswith("case_studies/") for rec in records)
    data = sum(rec.group == "data" for rec in records)
    base += [f"  章節：{chapters}｜案例研究：{cases}｜data：{data}｜其他：{total - chapters - cases - data}", ""]
    active = [r for r in records if r.state != "not_started"]
    if active:
        base.append("已啟動的 Notebook：")
        for r in active:
            base.append(f"  {r.source} | {r.ratio} 單元 | {r.batches_done}/{r.batches_total} 批 | {STATE_LABELS[r.state]}")
            if r.note:
                base.append(f"    注意：{r.note}")
    else:
        base.append("尚未啟動任何翻譯任務。")
    if total != 483:
        base += ["", "注意：原始配對 Notebook 數量不是 483，請確認當前路徑、repo 版本或新增檔案。"]
    return "\n".join(base) + "\n"


def group_summary(records: list[Record]) -> str:
    groups = defaultdict(list)
    for rec in records:
        groups[rec.group].append(rec)
    lines = ["各章節／案例研究進度：", "分類 | 原版數 | 已啟動 | 翻譯中 | 待組裝 | 已驗證 | 問題", "-" * 84]
    for name, items in sorted(groups.items()):
        stat = Counter(r.state for r in items)
        errors = stat["stale"] + stat["broken"]
        active = len(items) - stat["not_started"]
        lines.append(f"{name} | {len(items)} | {active} | {stat['in_progress']} | {stat['ready']} | {stat['verified']} | {errors}")
    return "\n".join(lines) + "\n"


def markdown_report(records: list[Record]) -> str:
    counts = Counter(r.state for r in records)
    lines = [
        "# ML4T 中英對照翻譯進度總覽", "",
        f"- 原始 Notebook：**{len(records)}** 份",
        f"- 已驗證：**{counts['verified']}** 份；翻譯中：**{counts['in_progress']}** 份；已翻完待組裝：**{counts['ready']}** 份",
        f"- 未開始：**{counts['not_started']}** 份；已組裝未驗證：**{counts['built_unchecked']}** 份；需要檢查：**{counts['broken'] + counts['stale']}** 份", "",
        "| Notebook | 翻譯單元 | 批次 | 狀態 | 備註 |",
        "|---|---:|---:|---|---|",
    ]
    for r in records:
        safe_note = r.note.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| `{r.source}` | {r.ratio} | {r.batches_done}/{r.batches_total} | {STATE_LABELS[r.state]} | {safe_note} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description="ML4T 全專案翻譯進度總覽（不修改原始 Notebook）")
    p.add_argument("--write", action="store_true", help="額外產生 translations/reports/progress.md 與 progress.csv")
    p.add_argument("--groups", action="store_true", help="顯示各章節與 case_studies 子目錄的進度")
    p.add_argument("--no-verify", action="store_true", help="不重新比對已組裝 Notebook 的內容；只供快速瀏覽")
    args = p.parse_args()
    try:
        root = root_dir()
        records = [inspect(root, rel, check_output=not args.no_verify) for rel in find_sources(root)]
        print(summary(records))
        if args.groups:
            print(group_summary(records))
        if args.write:
            report_dir = root / "translations" / "reports"
            report_dir.mkdir(parents=True, exist_ok=True)
            (report_dir / "progress.md").write_text(markdown_report(records), encoding="utf-8")
            with (report_dir / "progress.csv").open("w", encoding="utf-8-sig", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Notebook", "分類", "狀態", "完成單元", "總單元", "完成批次", "總批次", "中文版已存在", "備註"])
                for r in records:
                    writer.writerow([r.source, r.group, STATE_LABELS[r.state], r.completed, r.total,
                                     r.batches_done, r.batches_total, "是" if r.output else "否", r.note])
            print("已輸出：translations/reports/progress.md 和 progress.csv")
        return 1 if any(r.state in {"broken", "stale"} for r in records) else 0
    except (OSError, ValueError, RuntimeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
