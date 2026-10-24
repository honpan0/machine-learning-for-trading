#!/usr/bin/env python3
"""Prepare and collect math-safe, small retry batches for an existing ML4T A2 Pack.

Requires translation_tools/ml4t_math_safe_retry.py alongside this script.
No API use, source edits, or automatic overwrites.
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import ml4t_math_safe_retry as safe
except ImportError as exc:
    raise SystemExit("ERROR: 請把 ml4t_math_safe_batch.py 和 ml4t_math_safe_retry.py 放在同一目錄") from exc


class BatchError(ValueError):
    pass


def get_context(root: Path, source: str, pack_num: int):
    src = (root / source).resolve()
    if not src.is_relative_to(root) or src.suffix != '.ipynb' or src.stem.endswith('_zh') or not src.is_file():
        raise BatchError("請指定專案內有效的英文 Notebook .ipynb")
    work = root / 'translations' / 'work' / src.relative_to(root).with_suffix('')
    manifest = json.loads((work / 'manifest.json').read_text('utf-8'))
    packs = json.loads((work / 'pack_manifest.json').read_text('utf-8'))
    if manifest.get('source') != src.relative_to(root).as_posix() or manifest.get('source_sha256') != safe.sha(src.read_bytes()) or packs.get('source_sha256') != manifest['source_sha256']:
        raise BatchError('來源與 manifest 的 SHA256 不一致，停止')
    pack = next((p for p in packs['packs'] if p['number'] == pack_num), None)
    if pack is None:
        raise BatchError(f'找不到 Pack {pack_num:03d}')
    return work, manifest, pack


def mask_unit(original: str):
    """Use the same tested LaTeX matcher as the single-unit tool."""
    replacements = {}
    def repl(m):
        token = f'[[ML4T_MATH_{len(replacements) + 1:03d}]]'
        if token in original:
            raise BatchError('英文原文已有公式佔位符，停止')
        replacements[token] = m.group(0)
        return token
    masked = safe.MATH.sub(repl, original)
    # Avoid passing dangerous unmasked math commands back to the model.
    if any(cmd in masked for cmd in (r'\frac', r'\sqrt', r'\mathcal', r'\begin{equation}', r'\begin{align}')):
        raise BatchError('發現未被遮蔽的 LaTeX 命令；需先檢查來源，不匯出不安全任務')
    return masked, replacements


def get_missing_units(root, source, pack):
    work = root / 'translations' / 'work' / Path(source).with_suffix('')
    missing = []
    for uid in pack['ids']:
        if not (work / 'responses' / f'{uid}.md').is_file():
            _, original, unit, pack_no = safe.work_data(root, source, uid)
            if pack_no != pack['number']:
                raise BatchError(f'單元 {uid} 所屬 Pack 異常')
            masked, replacements = mask_unit(original)
            missing.append({'uid': uid, 'source_sha256': unit['source_sha256'],
                            'masked': masked, 'replacements': replacements})
    return missing


def group_units(units, max_units, max_chars):
    groups = []
    cur = []
    size = 0
    for unit in units:
        this_len = len(unit['masked'])
        if cur and (len(cur) >= max_units or size + this_len > max_chars):
            groups.append(cur)
            cur, size = [], 0
        cur.append(unit)
        size += this_len
    if cur:
        groups.append(cur)
    return groups


def stem(pack_num, part):
    return f'safe_retry_pack_{pack_num:03d}_part_{part:02d}'


def prepare(root, source, pack_num, max_units, max_chars):
    work, manifest, pack = get_context(root, source, pack_num)
    units = get_missing_units(root, source, pack)
    if not units:
        print('此 Pack 沒有待翻譯單元。')
        return
    groups = group_units(units, max_units, max_chars)
    map_path = work / 'packs' / f'safe_retry_pack_{pack_num:03d}_manifest.json'
    batch_meta = {'source': source, 'source_sha256': manifest['source_sha256'],
                  'pack': pack_num, 'parts': []}
    pending = []
    for n, group in enumerate(groups, 1):
        name = stem(pack_num, n)
        batch_meta['parts'].append({'number': n, 'ids': [u['uid'] for u in group],
                                     'units': [{key: u[key] for key in ('uid', 'source_sha256', 'replacements')} for u in group]})
        task = [
            f'# ML4T 公式遮蔽補翻 | Pack {pack_num:03d} | 第 {n}/{len(groups)} 組',
            '',
            '請只翻譯下列單元的英文文字，使用臺灣繁體中文；不刪減任何資訊。',
            '所有原始 LaTeX 公式已替換為 [[ML4T_MATH_001]] 類型的佔位符。',
            '**嚴禁**還原、改寫或輸出 LaTeX 公式。佔位符各自逐字保留，數量、順序不得改動。',
            '每個單元的 BEGIN/END 標記須各自獨占一行，標記 ID 原樣保留。',
            '只輸出翻譯結果（每個 BEGIN 到 END 之間），不要解說，不要外層程式碼區塊。',
            '保持原本的 Markdown、清單、程式碼和術語。',
            ''
        ]
        for u in group:
            task += [f'## 原始英文單元 {u["uid"]}（公式已遮蔽）', '', '~~~~~~markdown',
                     u['masked'].rstrip('\n'), '~~~~~~', '',
                     f'<<<ML4T-ZH-BEGIN:{u["uid"]}>>>',
                     '（將本行替換成對應的完整中文翻譯，保留全部佔位符）',
                     f'<<<ML4T-ZH-END:{u["uid"]}>>>', '']
        task_path = work / 'packs' / f'{name}.md'
        data = ('\n'.join(task) + '\n').encode('utf-8')
        pending.append((task_path, data))
    meta_data = (json.dumps(batch_meta, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    pending.append((map_path, meta_data))
    for p, data in pending:
        if p.exists() and p.read_bytes() != data:
            raise BatchError(f'已有不同內容的輸出檔，拒絕覆寫：{p}')
    for p, data in pending:
        safe.write_new_or_same(p, data)
    print(f'PASS：{len(units)} 個待補翻單元，分成 {len(groups)} 份小任務')
    for n, group in enumerate(groups, 1):
        name = stem(pack_num, n)
        print(f'  第 {n} 組：{len(group)} 單元、{sum(len(u["replacements"]) for u in group)} 處公式')
        print(f'    任務：{(work / "packs" / f"{name}.md").relative_to(root)}')
        print(f'    回覆：{(work / "inbox" / f"{name}_reply.txt").relative_to(root)}')
    print('請逐組把任務檔交給 GPT，確認標記完整，將回覆存至對應 inbox。')
    print(f'之後執行：python3 translation_tools/ml4t_math_safe_batch.py restore {source} --pack {pack_num} --all --collect')


def extract_parts(raw, ids):
    chunks = {}
    opened = None
    lines = []
    order = []
    for lineno, line in enumerate(raw.splitlines(keepends=True), 1):
        body = line.rstrip('\r\n')
        m = safe.MARKER_LINE.fullmatch(body)
        if m:
            kind, uid = m.groups()
            if kind == 'BEGIN':
                if opened is not None or uid in chunks:
                    raise BatchError(f'第 {lineno} 行：重複或未關閉 BEGIN')
                opened, lines = uid, []
                order.append(uid)
            else:
                if opened != uid:
                    raise BatchError(f'第 {lineno} 行：END 未配對 BEGIN：{uid}')
                text = ''.join(lines).strip()
                if not text:
                    raise BatchError(f'第 {lineno} 行：空翻譯單元：{uid}')
                chunks[uid] = text
                opened, lines = None, []
            continue
        if 'ML4T-ZH-' in body:
            raise BatchError(f'第 {lineno} 行：無法辨識標記')
        if opened is not None:
            lines.append(line)
        elif body.strip() and body.strip() != '\\':
            raise BatchError(f'第 {lineno} 行：標記外出現多餘文字')
    if opened is not None:
        raise BatchError(f'回覆在 {opened} 單元中截斷，請先補齊再匯入')
    if order != ids:
        raise BatchError(f'翻譯 ID/順序不符；預期 {ids}，實際 {order}')
    return chunks


def restore_part(root, source, pack_num, batch, manifest, do_collect):
    part = batch['number']
    name = stem(pack_num, part)
    work = root / 'translations' / 'work' / Path(source).with_suffix('')
    reply = work / 'inbox' / f'{name}_reply.txt'
    if not reply.is_file():
        print(f'略過第 {part} 組：尚未有 GPT 回覆。')
        return False
    src = root / source
    if safe.sha(src.read_bytes()) != manifest['source_sha256']:
        raise BatchError('英文 Notebook 已變動，停止')
    completed = [(work / 'responses' / f'{uid}.md').is_file() for uid in batch['ids']]
    if all(completed):
        print(f'略過第 {part} 組：{len(completed)} 個單元先前已成功匯入。')
        return True
    if any(completed):
        raise BatchError(f'第 {part} 組有部分單元已匯入；為避免不同版本混用，請人工檢查')
    contents = extract_parts(reply.read_text('utf-8-sig'), batch['ids'])
    output = []
    total_math = 0
    for u in batch['units']:
        uid = u['uid']
        _, original, unit, this_pack = safe.work_data(root, source, uid)
        if this_pack != pack_num or u['source_sha256'] != unit['source_sha256']:
            raise BatchError(f'{uid} 來源不一致')
        _masked, replacements = mask_unit(original)
        if replacements != u['replacements']:
            raise BatchError(f'{uid} 數學公式與來源不一致')
        translated = contents[uid]
        seen = safe.TOKEN_PATTERN.findall(translated)
        if seen != list(replacements):
            raise BatchError(f'{uid} 佔位符錯誤：預期 {list(replacements)}；實際 {seen}')
        # Extra hand-written math should never sneak through masking workflow.
        if safe.MATH.search(translated) or any(cmd in translated for cmd in (r'\frac', r'\sqrt', r'\mathcal')):
            raise BatchError(f'{uid} 回覆包含非原文公式，拒絕匯入')
        for token, math in replacements.items():
            translated = translated.replace(token, math)
            total_math += 1
        output += [f'<<<ML4T-ZH-BEGIN:{uid}>>>\n{translated}\n<<<ML4T-ZH-END:{uid}>>>\n']
    outpath = work / 'inbox' / f'{name}_restored.txt'
    safe.write_new_or_same(outpath, ('\n'.join(output)).encode('utf-8'))
    print(f'PASS：第 {part} 組 {len(batch["ids"])} 個單元，{total_math} 處原始公式已逐字還原')
    if do_collect:
        command = [sys.executable, str(root / 'translation_tools/collect_translation.py'), source,
                   '--pack', str(pack_num), '--file', str(outpath.relative_to(root)), '--partial']
        print('執行 A2 匯入：' + ' '.join(command[1:]))
        proc = subprocess.run(command, cwd=root)
        if proc.returncode:
            raise BatchError(f'第 {part} 組匯入失敗（返回碼 {proc.returncode}）')
    else:
        print('請匯入：python3 translation_tools/collect_translation.py ' + source +
              f' --pack {pack_num} --file {outpath.relative_to(root)} --partial')
    return True


def restore(root, source, pack_num, part, all_parts, do_collect):
    work, manifest, pack = get_context(root, source, pack_num)
    map_path = work / 'packs' / f'safe_retry_pack_{pack_num:03d}_manifest.json'
    batch_meta = json.loads(map_path.read_text('utf-8'))
    if batch_meta.get('source') != source or batch_meta.get('pack') != pack_num or batch_meta.get('source_sha256') != manifest['source_sha256']:
        raise BatchError('任務對照資料不匹配')
    batches = batch_meta['parts'] if all_parts else [next((p for p in batch_meta['parts'] if p['number'] == part), None)]
    if any(b is None for b in batches):
        raise BatchError('找不到指定的補翻小組')
    handled = 0
    for batch in batches:
        handled += restore_part(root, source, pack_num, batch, manifest, do_collect)
    if not handled:
        print('沒有找到可還原的回覆，尚未匯入任何單元。')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    prep = sub.add_parser('prepare')
    prep.add_argument('source')
    prep.add_argument('--pack', type=int, required=True)
    prep.add_argument('--max-units', type=int, default=3)
    prep.add_argument('--max-chars', type=int, default=6000)
    restore_parser = sub.add_parser('restore')
    restore_parser.add_argument('source')
    restore_parser.add_argument('--pack', type=int, required=True)
    choose = restore_parser.add_mutually_exclusive_group(required=True)
    choose.add_argument('--part', type=int)
    choose.add_argument('--all', action='store_true')
    restore_parser.add_argument('--collect', action='store_true')
    args = parser.parse_args()
    root = Path.cwd().resolve()
    try:
        if args.action == 'prepare':
            if args.max_units < 1 or args.max_chars < 1:
                raise BatchError('max-units 與 max-chars 必須為正整數')
            prepare(root, args.source, args.pack, args.max_units, args.max_chars)
        else:
            restore(root, args.source, args.pack, args.part, args.all, args.collect)
    except (BatchError, safe.Invalid, OSError, ValueError, KeyError, IndexError) as exc:
        print(f'ERROR：{exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
