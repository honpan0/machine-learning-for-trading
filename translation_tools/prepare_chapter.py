#!/usr/bin/env python3
"""ML4T A2 chapter-wide preparation and two-account offline work queue.

Stdlib only. Does not edit English notebooks, existing tasks, translated responses,
or *_zh.ipynb. --dry-run is the default and writes nothing.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import nb_zh
import pack_translation as packing
import prepare_with_glossary as glossary
import collect_translation as collector


@dataclass
class Job:
    source: str
    action: str
    packs: int = 0
    batches: int = 0
    units: int = 0
    note: str = ""


def sources_for(root: Path, chapter: str) -> list[str]:
    directory = (root / chapter).resolve()
    if not directory.is_relative_to(root) or not directory.is_dir():
        raise nb_zh.PipelineError(f"章節目錄不存在或不屬於專案：{chapter}")
    if directory in (root, root / 'translations') or (root / 'translations') in directory.parents:
        raise nb_zh.PipelineError("請指定原始 Notebook 章節目錄，不要選擇整個專案或 translations 目錄")
    notebooks = [p for p in directory.rglob('*.ipynb')
                 if not p.stem.endswith('_zh')
                 and '.ipynb_checkpoints' not in p.parts
                 and p.with_suffix('.py').is_file()]
    return [p.relative_to(root).as_posix() for p in sorted(notebooks)]


def estimate(root: Path, source: str, max_chars: int, batch_chars: int,
             max_batches: int, pack_chars: int) -> Job:
    src, rel = nb_zh.source_path(root, source)
    nb = nb_zh.read_json(src)
    if nb.get('nbformat') != 4 or not isinstance(nb.get('cells'), list):
        raise nb_zh.PipelineError(f"Notebook 格式不支援：{rel}")
    units: list[dict] = []
    for i, cell in enumerate(nb['cells']):
        if cell.get('cell_type') != 'markdown':
            continue
        for j, (begin, end) in enumerate(nb_zh.ranges(nb_zh.text_of(cell), max_chars)):
            original = nb_zh.text_of(cell)[begin:end]
            units.append({'id': f'c{i:04d}-p{j:03d}', 'chars': len(original)})
    if not units:
        raise nb_zh.PipelineError(f"Notebook 無需翻譯 Markdown：{rel}")
    batches: list[list[str]] = []
    active: list[str] = []
    active_chars = 0
    for u in units:
        if active and active_chars + u['chars'] > batch_chars:
            batches.append(active)
            active, active_chars = [], 0
        active.append(u['id'])
        active_chars += u['chars']
    if active:
        batches.append(active)
    work = root / 'translations' / 'work' / rel.with_suffix('')
    preview = packing.plan(work, {'batches': batches}, {u['id']: u for u in units},
                           max_batches, pack_chars, True)
    oversize = sum(1 for p in preview if p['oversize'])
    return Job(source, '待建立', len(preview), len(batches), len(units),
               f"{oversize} 個超長 Pack" if oversize else '')


def inspect_existing(root: Path, source: str, max_batches: int, pack_chars: int) -> Job:
    src, rel, work, zh = nb_zh.paths(root, source)
    if not work.exists():
        if zh.exists():
            raise nb_zh.PipelineError(f"{source} 已有中文版，卻找不到工作區，需人工檢查")
        return Job(source, '未建立')
    _, _, _, _, manifest = nb_zh.source_and_manifest(root, source)
    done = sum(packing.is_complete(work, u['id']) for u in manifest['units'])
    total = len(manifest['units'])
    if done == total:
        if zh.exists():
            nb_zh.verify_notebook(src, zh, manifest, work)
            return Job(source, '已完成', 0, len(manifest['batches']), total)
        return Job(source, '待組裝', 0, len(manifest['batches']), total,
                   '單元均已匯入；請手動 build/verify')
    if (work / 'pack_manifest.json').is_file():
        _, _, data, _ = collector.load_packs(root, source)
        return Job(source, '既有 Pack', len(data['packs']), len(manifest['batches']), total,
                   f'已匯入 {done}/{total} 單元')
    if (work / 'packs').exists() or any((work / 'inbox').glob('pack_*.txt')):
        raise nb_zh.PipelineError('找到殘留 packs/ 或 Pack 回覆，未有有效 pack_manifest.json；停止以避免覆寫')
    pending = packing.plan(work, manifest, {u['id']:u for u in manifest['units']},
                           max_batches, pack_chars, False)
    return Job(source, '待打包', len(pending), len(manifest['batches']), total,
               f'已匯入 {done}/{total} 單元')


def queue_rows(root: Path, source_list: list[str]) -> list[dict]:
    queue = []
    for source in source_list:
        _, rel, work, _ = nb_zh.paths(root, source)
        if not (work / 'pack_manifest.json').is_file():
            continue
        _, _, info, _ = collector.load_packs(root, source)
        for entry in info['packs']:
            completed = sum(packing.is_complete(work, uid) for uid in entry['ids'])
            reply = work / 'inbox' / f"pack_{entry['number']:03d}.txt"
            if completed == len(entry['ids']):
                state = '已匯入'
            elif reply.is_file():
                state = '回覆待匯入'
            elif completed:
                state = '部分完成'
            else:
                state = '待翻譯'
            queue.append({
                'notebook': source,
                'pack': entry['number'],
                'task': (work / 'packs' / entry['file']).relative_to(root).as_posix(),
                'reply': (work / 'inbox' / f"pack_{entry['number']:03d}.txt").relative_to(root).as_posix(),
                'units': len(entry['ids']),
                'done': completed,
                'english_chars': entry['chars'],
                'batches': ','.join(f"{b['batch']:03d}" for b in entry['batches']),
                'state': state,
                'account': '',
            })
    # Distribute untranslated packs between two accounts, approximating similar
    # workloads by source English character counts rather than raw pack counts.
    workloads = [0, 0]
    for row in sorted((r for r in queue if r['state'] == '待翻譯'),
                      key=lambda r: (-r['english_chars'], r['task'])):
        k = 0 if workloads[0] <= workloads[1] else 1
        row['account'] = 'A' if k == 0 else 'B'
        workloads[k] += row['english_chars']
    return queue


def write_queue(root: Path, chapter: str, rows: list[dict]) -> tuple[Path, Path]:
    reports = root / 'translations' / 'reports'
    reports.mkdir(parents=True, exist_ok=True)
    slug = Path(chapter).name
    csv_p = reports / f'{slug}_a2_queue.csv'
    md_p = reports / f'{slug}_a2_queue.md'
    fields = ['account','state','notebook','pack','task','reply','units','done','english_chars','batches']
    csv_stream = io.StringIO(newline='')
    writer = csv.DictWriter(csv_stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    csv_p.write_text(csv_stream.getvalue(), encoding='utf-8', newline='\n')
    pending = sum(r['state'] == '待翻譯' for r in rows)
    waiting = sum(r['state'] == '回覆待匯入' for r in rows)
    ready_count = sum(r['state'] == '已匯入' for r in rows)
    lines = [f'# {slug}｜A2 翻譯工作清單', '',
             f'- Pack 總數：{len(rows)}；待翻譯：{pending}；回覆待匯入：{waiting}；已匯入：{ready_count}',
             '- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。',
             '- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。',
             '- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。',
             '', '| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |',
             '|---|---|---|---:|---:|---:|---|']
    for row in rows:
        link = '../' + row['task'].replace('translations/', '', 1)
        lines.append(f"| {row['account'] or '—'} | {row['state']} | `{Path(row['notebook']).stem}` | "
                     f"{row['pack']:03d} | {row['done']}/{row['units']} | {row['english_chars']} | "
                     f"[pack_{row['pack']:03d}.md]({link}) |")
    lines.extend(['', '## 收件與匯入', '',
                  '請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。',
                  '逐份 Notebook 可用：', '', '```bash',
                  'python3 translation_tools/collect_translation.py <來源.ipynb> --all',
                  '```', '',
                  '上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。',
                  '收件後重新產生工作清單：', '', '```bash',
                  f'python3 translation_tools/prepare_chapter.py {chapter} --report-only',
                  '```', ''])
    md_p.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    return csv_p, md_p


def run(root: Path, args: argparse.Namespace) -> int:
    source_list = sources_for(root, args.chapter)
    if not source_list:
        raise nb_zh.PipelineError('指定目錄沒有原始英文／配對 .py 的 Notebook')
    if args.limit:
        source_list = source_list[:args.limit]
    print(f'章節 {args.chapter}：掃描 {len(source_list)} 份 Notebook。')
    successful = 0
    warnings: list[tuple[str,str]] = []
    for source in source_list:
        try:
            status = inspect_existing(root, source, args.max_batches, args.pack_chars)
            if status.action == '未建立':
                if args.prepare:
                    glossary.prepare_glossary(argparse.Namespace(source=source, max_chars=args.max_chars,
                        batch_chars=args.batch_chars, max_terms=args.max_terms, glossary=args.glossary))
                    packing.pack_all(root, source, args.max_batches, args.pack_chars, args.max_terms, False, False)
                    status = inspect_existing(root, source, args.max_batches, args.pack_chars)
                    successful += 1
                elif not args.report_only:
                    status = estimate(root, source, args.max_chars, args.batch_chars,
                                      args.max_batches, args.pack_chars)
            elif status.action == '待打包' and args.prepare:
                packing.pack_all(root, source, args.max_batches, args.pack_chars, args.max_terms, False, False)
                status = inspect_existing(root, source, args.max_batches, args.pack_chars)
                successful += 1
            print(f"  [{status.action}] {source}：{status.units} 單元／{status.batches} 批／{status.packs} Pack"
                  + (f"（{status.note}）" if status.note else ''))
        except (nb_zh.PipelineError, collector.CollectError, OSError, ValueError, TypeError, KeyError,
                IndexError, json.JSONDecodeError) as exc:
            warnings.append((source, str(exc)))
            print(f'  [需檢查] {source}：{exc}', file=sys.stderr)
    if args.prepare or args.report_only:
        try:
            queue = queue_rows(root, source_list)
            csv_p, md_p = write_queue(root, args.chapter, queue)
            print(f'工作清單：{csv_p.relative_to(root)} 和 {md_p.relative_to(root)}')
            print(f"待翻譯：{sum(r['state'] == '待翻譯' for r in queue)} 個 Pack；"
                  f"已有回覆：{sum(r['state'] == '回覆待匯入' for r in queue)} 個 Pack；"
                  f"已匯入：{sum(r['state'] == '已匯入' for r in queue)} 個 Pack。")
        except (nb_zh.PipelineError, collector.CollectError, OSError, ValueError, TypeError, KeyError,
                IndexError, json.JSONDecodeError) as exc:
            warnings.append(('工作清單', str(exc)))
            print(f'  [需檢查] 工作清單：{exc}', file=sys.stderr)
    if args.prepare:
        print(f'新建立 Pack 工作區：{successful} 份。')
    if warnings:
        print(f'注意：{len(warnings)} 項需要人工檢查；其他工作區已保留，可安全續跑。', file=sys.stderr)
        return 1
    if not (args.prepare or args.report_only):
        print('唯讀預覽：未修改任何檔案。如清單合理，再加上 --prepare。')
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='ML4T A2：整章安全批量準備與兩帳號翻譯工作清單')
    parser.add_argument('chapter', help='章節目錄，例如 02_financial_data_universe')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--prepare', action='store_true', help='執行 Prepare + Pack；安全跳過已存在的成果')
    mode.add_argument('--report-only', action='store_true', help='只刷新既有 Pack 工作清單，不重新產生任務')
    parser.add_argument('--limit', type=int, help='只處理排序後前 N 個原始 Notebook（小規模驗收用）')
    parser.add_argument('--max-chars', type=int, default=1800, help='單元最大建議字元數')
    parser.add_argument('--batch-chars', type=int, default=5000, help='Batch 最大建議字元數')
    parser.add_argument('--max-batches', type=int, default=2, help='每 Pack 最多合併 Batch 數')
    parser.add_argument('--pack-chars', type=int, default=10000, help='每 Pack 英文字元上限')
    parser.add_argument('--max-terms', type=int, default=25, help='每 Pack 最多相關術語')
    parser.add_argument('--glossary', default=glossary.DEFAULT_GLOSSARY)
    args = parser.parse_args(argv)
    if (args.limit is not None and args.limit < 1) or args.max_chars < 200 or args.batch_chars < 200 or args.pack_chars < 500 or not(1 <= args.max_batches <= 10) or not(1 <= args.max_terms <= 100):
        parser.error('限制值不合理：--limit > 0、--max-chars/--batch-chars >= 200、--pack-chars >= 500、--max-batches 1～10、--max-terms 1～100')
    try:
        return run(nb_zh.root_dir(), args)
    except (nb_zh.PipelineError, OSError, ValueError) as exc:
        print('ERROR：' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
