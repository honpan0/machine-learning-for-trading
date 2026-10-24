#!/usr/bin/env python3
"""ML4T A2 chapter preparation regression tests; no network, no live files."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
import unittest
from pathlib import Path

import prepare_chapter as bulk
import prepare_with_glossary as glossary
import nb_zh
import collect_translation as collect


class ChapterTests(unittest.TestCase):
    def setUp(self):
        t = tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.root = Path(t.name).resolve()
        (self.root/'.git').mkdir()
        (self.root/'pyproject.toml').write_text('[project]\nname="sample"\nversion="0.0.1"\n', encoding='utf-8')
        self.chapter = '02_demo'
        (self.root/self.chapter).mkdir()
        glossary_file = self.root/'translations/glossary_zh_TW.md'
        glossary_file.parent.mkdir(parents=True)
        glossary_file.write_text('| 英文 | 繁體中文 |\n| --- | --- |\n| Volatility | 波動率 |\n', encoding='utf-8')
        self.source_bytes = {}
        for i in range(3):
            cells=[]
            for j in range(3):
                cells.append({'cell_type':'markdown','metadata':{},'source':
                    f'## Volatility topic {i}.{j}\n\n' + ('Market volatility is dynamic. ' * 7)})
            cells.append({'cell_type':'code','metadata':{},'source':'x=1\nx','execution_count':1,
                          'outputs':[{'output_type':'execute_result','execution_count':1,'data':{'text/plain':['1']},'metadata':{}}]})
            nb = {'nbformat':4,'nbformat_minor':5,'metadata':{},'cells':cells}
            path = self.root/self.chapter/f'{i+1:02d}_sample.ipynb'
            path.write_text(json.dumps(nb, ensure_ascii=False), encoding='utf-8')
            path.with_suffix('.py').write_text('# placeholder only for pair detection', encoding='utf-8')
            self.source_bytes[path.name] = path.read_bytes()
        cwd=os.getcwd()
        os.chdir(self.root)
        self.addCleanup(os.chdir, cwd)

    def params(self, **kw):
        defaults = {'chapter':self.chapter,'prepare':False,'report_only':False,
                    'limit':None,'max_chars':500,'batch_chars':300,'max_batches':2,
                    'pack_chars':1000,'max_terms':25,'glossary':glossary.DEFAULT_GLOSSARY}
        defaults.update(kw)
        return argparse.Namespace(**defaults)

    def src(self, i):
        return f'{self.chapter}/{i:02d}_sample.ipynb'

    def work(self, i):
        return self.root/f'translations/work/{self.chapter}/{i:02d}_sample'

    def test_dry_run_is_really_readonly_and_predicts_packs(self):
        before = sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob('*'))
        self.assertEqual(0,bulk.run(self.root,self.params()))
        after = sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob('*'))
        self.assertEqual(before,after)
        self.assertEqual(3,len(bulk.sources_for(self.root,self.chapter)))
        predicted=bulk.estimate(self.root,self.src(1),500,300,2,1000)
        self.assertEqual(3,predicted.units)
        self.assertEqual(3,predicted.batches)
        self.assertEqual(2,predicted.packs)

    def test_one_command_creates_all_and_balances_queue(self):
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True)))
        for i in range(1,4):
            self.assertTrue((self.work(i)/'manifest.json').is_file())
            self.assertTrue((self.work(i)/'pack_manifest.json').is_file())
            self.assertEqual(self.source_bytes[f'{i:02d}_sample.ipynb'],
                             (self.root/self.src(i)).read_bytes())
        q=bulk.queue_rows(self.root,bulk.sources_for(self.root,self.chapter))
        self.assertEqual(6,len(q))
        self.assertEqual({'A','B'},set(x['account'] for x in q))
        self.assertTrue(all(x['state']=='待翻譯' for x in q))
        self.assertTrue((self.root/f'translations/reports/{self.chapter}_a2_queue.md').is_file())
        self.assertIn('pack_001.md',(self.root/f'translations/reports/{self.chapter}_a2_queue.md').read_text(encoding='utf-8'))

    def test_idempotent_skips_tasks_not_overwriting(self):
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True)))
        file=self.work(1)/'packs/pack_001.md'
        before=file.read_bytes()
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True)))
        self.assertEqual(before,file.read_bytes())

    def test_prewritten_batch_can_be_packed_without_overwrite(self):
        glossary.prepare_glossary(argparse.Namespace(source=self.src(1),max_chars=500,
                        batch_chars=300,max_terms=25,glossary=glossary.DEFAULT_GLOSSARY))
        task=self.work(1)/'tasks/batch_001.md'
        original=task.read_bytes()
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True,limit=1)))
        self.assertEqual(original, task.read_bytes())
        self.assertTrue((self.work(1)/'pack_manifest.json').is_file())

    def test_reply_waiting_then_completed_and_regenerate_report(self):
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True,limit=1)))
        work=self.work(1)
        info=json.loads((work/'pack_manifest.json').read_text(encoding='utf-8'))
        for p in info['packs']:
            content='\n'.join(f'<<<ML4T-ZH-BEGIN:{uid}>>>\n中文說明\n<<<ML4T-ZH-END:{uid}>>>'
                              for uid in p['ids'])+'\n'
            (work/'inbox'/f'pack_{p["number"]:03d}.txt').write_text(content,encoding='utf-8')
        source_list=[self.src(1)]
        q=bulk.queue_rows(self.root,source_list)
        self.assertTrue(all(r['state']=='回覆待匯入' for r in q))
        for p in info['packs']:
            file=work/'inbox'/f'pack_{p["number"]:03d}.txt'
            _,manifest,_,_=collect.load_packs(self.root,self.src(1))
            collect.collect_one(self.root,self.src(1),work,manifest,info,p['number'],file,False,True)
        self.assertTrue((self.root/self.chapter/'01_sample_zh.ipynb').is_file())
        q=bulk.queue_rows(self.root,source_list)
        self.assertTrue(all(r['state']=='已匯入' for r in q))
        self.assertEqual(0,bulk.run(self.root,self.params(report_only=True,limit=1)))
        self.assertTrue('已匯入' in (self.root/f'translations/reports/{self.chapter}_a2_queue.md').read_text(encoding='utf-8'))
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True,limit=1)))

    def test_source_drift_blocks_further_processing(self):
        self.assertEqual(0,bulk.run(self.root,self.params(prepare=True,limit=1)))
        source=self.root/self.src(1)
        source.write_bytes(source.read_bytes()+b'\n')
        self.assertEqual(1,bulk.run(self.root,self.params(prepare=True,limit=1)))
        self.assertEqual(self.source_bytes['02_sample.ipynb'],(self.root/self.src(2)).read_bytes())

    def test_unexpected_directory_and_unpaired_ignored(self):
        (self.root/self.chapter/'extra.ipynb').write_text('{}',encoding='utf-8')
        self.assertEqual(3,len(bulk.sources_for(self.root,self.chapter)))
        with self.assertRaises(nb_zh.PipelineError):
            bulk.sources_for(self.root,'translations')
        with self.assertRaises(nb_zh.PipelineError):
            bulk.sources_for(self.root,'../')


if __name__=='__main__':
    unittest.main(verbosity=2)
