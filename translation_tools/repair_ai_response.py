#!/usr/bin/env python3
"""Safely preflight and normalize AI translation reply markers for ML4T.

Usage:
    python3 translation_tools/repair_ai_response.py 01_process_is_edge/macro_regimes.ipynb
    python3 translation_tools/repair_ai_response.py 01_process_is_edge/macro_regimes.ipynb --fix
    python3 translation_tools/repair_ai_response.py 01_process_is_edge/macro_regimes.ipynb --batch 2 --fix

Default mode is read-only. --fix backs up originals to .txt.bak and only
changes standalone marker lines; no translation paragraphs are rewritten.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

UID = r"c\d{4}-p\d{3}"
TOKEN = re.compile(rf"(?P<prefix><<<|<<\\<|<escape><<<)ML4T-ZH-(?P<kind>BEGIN|END):(?P<uid>{UID})>>>")
MARKER_LINE = re.compile(rf"[ \t]*(?:{TOKEN.pattern}[ \t]*)+")
BEGIN = re.compile(rf"<<<ML4T-ZH-BEGIN:({UID})>>>")
END = re.compile(rf"<<<ML4T-ZH-END:({UID})>>>")
TASK_UNIT = re.compile(rf"(?m)^## 單元：[ \t]*({UID})[ \t]*$")


class RepairError(ValueError):
    pass


@dataclass(frozen=True)
class Inspection:
    path: Path
    original: bytes
    corrected: bytes
    replacements: int
    joins: int
    units: int

    @property
    def changed(self) -> bool:
        return self.corrected != self.original


def normalize(raw: str) -> tuple[str, int, int]:
    """Normalize only complete marker-only lines, leaving prose byte-for-byte intact."""
    result = []
    repaired = 0
    joins = 0
    for line in raw.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        ending = line[len(body):]
        if not MARKER_LINE.fullmatch(body):
            result.append(line)
            continue
        found = list(TOKEN.finditer(body))
        canonical = [f"<<<ML4T-ZH-{m['kind']}:{m['uid']}>>>" for m in found]
        repaired += sum(m["prefix"] != "<<<" for m in found)
        joins += max(0, len(found) - 1)
        sep = "\r\n" if ending == "\r\n" else "\n"
        result.append(sep.join(canonical) + ending)
    return "".join(result), repaired, joins


def validate(text: str, expected: list[str]) -> int:
    """Enforce exact IDs, paired markers, and no text outside translation blocks."""
    if not expected or len(expected) != len(set(expected)):
        raise RepairError("任務檔沒有有效且不重複的翻譯單元 ID")
    allowed = set(expected)
    seen: set[str] = set()
    active: str | None = None
    content: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        start = BEGIN.fullmatch(s)
        finish = END.fullmatch(s)
        if start:
            uid = start[1]
            if active is not None:
                raise RepairError(f"第 {lineno} 行：{active} 尚未結束，卻出現新 BEGIN")
            if uid not in allowed:
                raise RepairError(f"第 {lineno} 行：出現非本批次 ID {uid}")
            if uid in seen:
                raise RepairError(f"第 {lineno} 行：重複的 ID {uid}")
            active, content = uid, []
        elif finish:
            uid = finish[1]
            if active != uid:
                raise RepairError(f"第 {lineno} 行：END {uid} 與 BEGIN {active} 不相符")
            body = "\n".join(content).strip()
            if not body or body.startswith("（在此填寫"):
                raise RepairError(f"第 {lineno} 行：{uid} 缺少實際翻譯")
            seen.add(uid)
            active, content = None, []
        elif "ML4T-ZH-BEGIN:" in s or "ML4T-ZH-END:" in s:
            raise RepairError(f"第 {lineno} 行：無法安全識別的標記格式，拒絕自動修復")
        elif active is None:
            if s:
                raise RepairError(f"第 {lineno} 行：標記之外出現多餘文字：{s[:70]}")
        else:
            content.append(line)
    if active is not None:
        raise RepairError(f"單元 {active} 缺少 END 標記")
    missing = [uid for uid in expected if uid not in seen]
    if missing:
        raise RepairError("缺少翻譯單元：" + ", ".join(missing))
    return len(seen)


def expected_ids(task: Path) -> list[str]:
    if not task.is_file():
        raise RepairError(f"找不到任務檔：{task}")
    return TASK_UNIT.findall(task.read_text(encoding="utf-8-sig"))


def inspect(reply: Path, task: Path) -> Inspection:
    original = reply.read_bytes()
    try:
        raw = original.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise RepairError(f"{reply.name} 不是有效的 UTF-8：{exc}") from exc
    fixed, replacements, joins = normalize(raw)
    units = validate(fixed, expected_ids(task))
    corrected = fixed.encode("utf-8")
    return Inspection(reply, original, corrected, replacements, joins, units)


def apply(inspection: Inspection) -> Path | None:
    """Safeguard prior backup; write a fully validated replacement atomically."""
    if not inspection.changed:
        return None
    path = inspection.path
    if path.read_bytes() != inspection.original:
        raise RepairError(f"檔案檢查後已被其他程式修改：{path}")
    backup = path.with_name(path.name + ".bak")
    if not backup.exists():
        shutil.copy2(path, backup)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temp_name = handle.name
            handle.write(inspection.corrected)
        Path(temp_name).replace(path)
    finally:
        if temp_name:
            Path(temp_name).unlink(missing_ok=True)
    return backup


def work_for_source(root: Path, source: str) -> Path:
    p = Path(source)
    if p.is_absolute() or p.suffix != ".ipynb" or ".." in p.parts or not p.parts:
        raise RepairError("來源請使用專案內相對路徑，例如 01_process_is_edge/macro_regimes.ipynb")
    return root / "translations" / "work" / p.with_suffix("")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ML4T AI 回覆標記預檢／安全修復（預設唯讀）")
    parser.add_argument("source", help="英文 Notebook 的專案內相對路徑")
    parser.add_argument("--batch", type=int, help="只處理指定批次（預設所有現有回覆）")
    parser.add_argument("--fix", action="store_true", help="備份後修正；省略時僅檢查，不改檔")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    try:
        work = work_for_source(root, args.source)
        inbox, tasks = work / "inbox", work / "tasks"
        if args.batch is not None:
            if args.batch < 1:
                raise RepairError("--batch 必須大於零")
            files = [inbox / f"batch_{args.batch:03d}.txt"]
        else:
            files = sorted(inbox.glob("batch_[0-9][0-9][0-9].txt"))
        if not files:
            raise RepairError(f"沒有找到 AI 回覆檔：{inbox}")
        inspections: list[Inspection] = []
        errors: list[str] = []
        for reply in files:
            try:
                if not reply.is_file():
                    raise RepairError(f"找不到 AI 回覆檔：{reply}")
                item = inspect(reply, tasks / reply.name.replace(".txt", ".md"))
                inspections.append(item)
                status = "需修正" if item.changed else "已符合格式"
                print(f"{reply.name}：{status}；單元 {item.units}；錯誤標記 {item.replacements}；黏連標記 {item.joins}")
            except (RepairError, OSError) as exc:
                errors.append(f"{reply.name}：{exc}")
        if errors:
            for problem in errors:
                print("ERROR:", problem, file=sys.stderr)
            print("已拒絕修改任何檔案；請先修正上述無法安全判斷的問題。", file=sys.stderr)
            return 2
        need = [item for item in inspections if item.changed]
        if not args.fix:
            print(f"唯讀檢查完成：{len(inspections)} 批；{len(need)} 批需要修復。" if need else f"PASS：{len(inspections)} 批均已符合格式。")
            return 1 if need else 0
        for item in need:
            backup = apply(item)
            print(f"已修復 {item.path.name}；原始備份：{backup.name}")
        print(f"PASS：已驗證 {len(inspections)} 批，修復 {len(need)} 批。未執行 ingest。")
        return 0
    except (RepairError, OSError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
