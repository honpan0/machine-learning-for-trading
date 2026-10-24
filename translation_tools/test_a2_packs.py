#!/usr/bin/env python3
"""Offline regression tests for ML4T A2 packaging and collection (no API/network)."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
import unittest
from pathlib import Path

import nb_zh
import pack_translation as packer
import collect_translation as collect


class A2Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / ".git").mkdir()
        (self.root / "pyproject.toml").write_text('[project]\nname = "sandbox"\nversion = "0.1"\n', encoding="utf-8")
        (self.root / "01_test").mkdir()
        glossary = self.root / "translations/glossary_zh_TW.md"
        glossary.parent.mkdir(parents=True)
        glossary.write_text("| 英文 | 繁體中文 |\n| --- | --- |\n| Regime | 市場狀態 |\n| Volatility | 波動率 |\n", encoding="utf-8")
        cells = []
        for i in range(6):
            cells.append({"cell_type": "markdown", "metadata": {}, "source":
                          f"## Unit {i} — Volatility and Regime\n\n" +
                          f"Learning the financial market regime and volatility behaviour in example {i}. " +
                          "The explanatory section should retain its technical detail.\n"})
        cells.insert(3, {"cell_type":"code", "metadata":{}, "source": "x = 3\nx", "execution_count": 5,
                         "outputs":[{"output_type":"execute_result", "data":{"text/plain":["3"]}, "metadata":{}, "execution_count":5}]})
        notebook = {"nbformat":4,"nbformat_minor":5,"metadata":{"jupytext":{"formats":"ipynb,py:percent"}}, "cells":cells}
        self.src_rel = "01_test/sample.ipynb"
        self.src = self.root / self.src_rel
        self.src.write_text(json.dumps(notebook,ensure_ascii=False), encoding="utf-8")
        self.old_cwd = os.getcwd()
        os.chdir(self.root)
        self.addCleanup(os.chdir, self.old_cwd)
        nb_zh.prepare(argparse.Namespace(source=self.src_rel,max_chars=1000,batch_chars=200))
        self.work = self.root / "translations/work/01_test/sample"
        self.original_source = self.src.read_bytes()
        self.manifest = json.loads((self.work / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(6,len(self.manifest["batches"]))

    def make_packs(self):
        packer.pack_all(self.root,self.src_rel,2,10000,25,False,False)
        return json.loads((self.work / "pack_manifest.json").read_text(encoding="utf-8"))

    def reply(self, p, kind="canonical"):
        sections = []
        for uid in p["ids"]:
            begin = f"<<<ML4T-ZH-BEGIN:{uid}>>>"
            end = f"<<<ML4T-ZH-END:{uid}>>>"
            if kind == "broken":
                begin = begin.replace("<<<", "<<\\<")
                end = "<escape>" + end
            sections.append(begin + "\n" + f"市場狀態與波動率的完整解說（{uid}）。" + "\n" + end)
        return "\n".join(sections)+"\n"

    def test_preview_readonly_and_packing(self):
        before = sorted(p.as_posix() for p in self.work.rglob("*"))
        packs = packer.pack_all(self.root,self.src_rel,2,10000,25,True,False)
        self.assertEqual(3, len(packs))
        self.assertEqual(before, sorted(p.as_posix() for p in self.work.rglob("*")))
        data = self.make_packs()
        self.assertEqual(3, len(data["packs"]))
        self.assertEqual([2,2,2],[len(p["batches"]) for p in data["packs"]])
        first = (self.work/"packs/pack_001.md").read_text(encoding="utf-8")
        self.assertEqual(1, first.count("## 指示（整個 Pack 只需閱讀一次）"))
        self.assertIn("Volatility → 波動率", first)
        self.assertIn("Regime → 市場狀態", first)
        self.assertEqual(self.original_source, self.src.read_bytes())

    def test_strict_reject_incomplete_and_preserve_files(self):
        data=self.make_packs()
        pack=data["packs"][0]
        raw="<<<ML4T-ZH-BEGIN:"+pack["ids"][0]+">>>\n譯文\n<<<ML4T-ZH-END:"+pack["ids"][0]+">>>\n"
        p=self.work / "inbox/pack_001.txt"
        p.write_text(raw,encoding="utf-8")
        with self.assertRaisesRegex(collect.CollectError,"缺少"):
            collect.collect_one(self.root,self.src_rel,self.work,self.manifest,data,1,p,False,False)
        self.assertFalse((self.work/"responses"/f"{pack['ids'][0]}.md").exists())
        self.assertFalse(list((self.work/"inbox").glob("pack_001_*.txt")))

    def test_repair_split_ingest_resume_and_build(self):
        data=self.make_packs()
        for p in data["packs"]:
            number=p["number"]
            file=self.work/"inbox"/f"pack_{number:03d}.txt"
            file.write_text(self.reply(p,"broken"),encoding="utf-8")
            n=collect.collect_one(self.root,self.src_rel,self.work,self.manifest,data,number,file,False,True)
            self.assertEqual(len(p["ids"]),n)
            self.assertEqual(self.reply(p,"broken"),file.read_text(encoding="utf-8"))
            self.assertEqual(0,collect.collect_one(self.root,self.src_rel,self.work,self.manifest,data,number,file,False,False))
        output=self.src.with_name("sample_zh.ipynb")
        self.assertTrue(output.is_file())
        nb_zh.verify(argparse.Namespace(source=self.src_rel))
        self.assertEqual(self.original_source,self.src.read_bytes())
        with self.assertRaisesRegex(nb_zh.PipelineError,"已存在"):
            packer.pack_all(self.root,self.src_rel,2,10000,25,False,False)
        preview=packer.pack_all(self.root,self.src_rel,2,10000,25,True,True)
        self.assertEqual(3,len(preview))
        nothing=packer.plan(self.work,self.manifest,{u['id']:u for u in self.manifest['units']},2,10000,False)
        self.assertEqual([],nothing)

    def test_conflict_and_unknown_id_rejected(self):
        data=self.make_packs()
        p=data["packs"][0]
        f=self.work/"inbox/pack_001.txt"
        f.write_text(self.reply(p).replace(p["ids"][0],"c9999-p999"),encoding="utf-8")
        with self.assertRaises((collect.CollectError,nb_zh.PipelineError)):
            collect.collect_one(self.root,self.src_rel,self.work,self.manifest,data,1,f,False,False)
        self.assertEqual([],list((self.work/"responses").glob("*.md")))
        f.write_text(self.reply(p),encoding="utf-8")
        (self.work/"responses"/f"{p['ids'][0]}.md").write_text("不同的人工譯文\n",encoding="utf-8")
        with self.assertRaisesRegex(collect.CollectError,"不同翻譯"):
            collect.collect_one(self.root,self.src_rel,self.work,self.manifest,data,1,f,False,False)
        self.assertEqual(1,len(list((self.work/"responses").glob("*.md"))))

    def test_partial_explicit_rescue_and_retry_only_missing(self):
        data=self.make_packs()
        p=data["packs"][0]
        first=p["ids"][0]
        f=self.work/"inbox/pack_001.txt"
        f.write_text(f"<<<ML4T-ZH-BEGIN:{first}>>>\n譯文\n<<<ML4T-ZH-END:{first}>>>\n"+
                     f"<<<ML4T-ZH-BEGIN:{p['ids'][1]}>>>\n被截斷",encoding="utf-8")
        added=collect.collect_one(self.root,self.src_rel,self.work,self.manifest,data,1,f,True,False)
        self.assertEqual(1,added)
        self.assertFalse((self.work/"responses"/f"{p['ids'][1]}.md").exists())
        tasks=list((self.work/"packs").glob("retry_pack_001_*.md"))
        self.assertEqual(1,len(tasks))
        content=tasks[0].read_text(encoding="utf-8")
        self.assertNotIn(f"<<<ML4T-ZH-BEGIN:{first}>>>",content)
        self.assertIn(f"<<<ML4T-ZH-BEGIN:{p['ids'][1]}>>>",content)

    def test_source_drift_and_tampered_pack(self):
        data=self.make_packs()
        task=self.work/"packs/pack_001.md"
        task.write_text(task.read_text(encoding="utf-8")+"malicious",encoding="utf-8")
        with self.assertRaisesRegex(collect.CollectError,"被修改"):
            collect.load_packs(self.root,self.src_rel)
        task.write_text(task.read_text(encoding="utf-8").replace("malicious",""),encoding="utf-8")
        self.src.write_bytes(self.src.read_bytes()+b"\n")
        with self.assertRaisesRegex(nb_zh.PipelineError,"已變更"):
            collect.load_packs(self.root,self.src_rel)


if __name__ == "__main__":
    unittest.main(verbosity=2)
