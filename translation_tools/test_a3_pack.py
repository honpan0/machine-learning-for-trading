#!/usr/bin/env python3
"""Offline integration tests for A3 using real A2/Notebook pipeline."""
from __future__ import annotations
import argparse
import json
import os
import tempfile
import unittest
from pathlib import Path

import a3_pack as a3
import nb_zh
import pack_translation as a2


class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / ".git").mkdir()
        (self.root / "pyproject.toml").write_text('[project]\nname="a3-test"\nversion="0.1.0"\n')
        (self.root / "02_demo").mkdir()
        (self.root / "translations").mkdir()
        (self.root / "translations" / "glossary_zh_TW.md").write_text("| 英文 | 中文 |\n| --- | --- |\n| Gamma | 伽瑪 |\n", encoding="utf-8")
        self.source = "02_demo/greeks.ipynb"
        self.src = self.root / self.source
        cells = [
            {"cell_type":"markdown","metadata":{},"source":[
                "### Gamma ($\\Gamma$)\n\n", "Gamma measures change: $$\\Gamma = \\frac{N'(d_1)}{S \\sigma \\sqrt{T}}$$\n"]},
            {"cell_type":"code","metadata":{},"execution_count":1,
             "source":["print(1 + 1)"],"outputs":[{"output_type":"stream","name":"stdout","text":"2\\n"}]},
            {"cell_type":"markdown","metadata":{},"source":[
                "Vega sensitivity `vega`, $\\mathcal{V}$ and price $100.\n\n",
                "```python\nformula = r'\\frac{a}{b}'\n```\n\nRead [docs](https://example.org).\n"]},
            {"cell_type":"markdown","metadata":{},"source": "Theta loss \\(\\Theta = -\\frac{1}{2}\\) and option time.\n"},
        ]
        self.src.write_text(json.dumps({"nbformat":4,"nbformat_minor":5,"metadata":{},"cells":cells}), encoding="utf-8")
        self.cwd = Path.cwd()
        os.chdir(self.root)
        nb_zh.prepare(argparse.Namespace(source=self.source,max_chars=1000,batch_chars=1400))
        a2.pack_all(self.root, self.source, 2, 4000, 25, False, False)
        self.work = self.root / "translations/work/02_demo/greeks"

    def tearDown(self):
        os.chdir(self.cwd)
        self.tmp.cleanup()

    def originals(self):
        _, _, _, units, nb, _ = a3.work_context(self.root, self.source)
        return {uid: a3.mask_text(a2.english(nb, unit))[0] for uid, unit in units.items()}

    def reply(self, entry, wanted=None, bad=None, truncated=None, escape=False):
        originals = self.originals()
        lines = []
        for u in entry["units"]:
            uid = u["id"]
            if wanted is not None and uid not in wanted:
                continue
            if truncated == uid:
                lines.extend([f"<<<ML4T-ZH-BEGIN:{uid}>>>", "$$\\frac", ""])
                break
            start = f"<<<ML4T-ZH-BEGIN:{uid}>>>"
            end = f"<<<ML4T-ZH-END:{uid}>>>"
            if escape:
                start = start.replace("<<<", "<<\\<")
                end = end.replace("<<<", "<<\\<")
            text = originals[uid]
            if uid == bad:
                text = text.replace("[[ML4T_A3_", "[[BAD_A3_")
            lines.extend([start,"翻譯：" + text,end,""])
        return "\n".join(lines)

    def test_math_and_code_never_seen_by_model_and_build(self):
        n = a3.do_prepare(self.root, self.source, 6500, 14)
        self.assertEqual(n, 1)
        data = json.loads(a3.map_file(self.work).read_text("utf-8"))
        entry = data["packs"][0]
        task = (self.work / "packs" / entry["file"]).read_text("utf-8")
        self.assertNotIn(r"\\frac{N'(d_1)}", task)
        self.assertNotIn("formula =", task)
        self.assertIn("[[ML4T_A3_0001]]", task)
        reply = self.work / "inbox/a3_pack_001.txt"
        reply.write_text(self.reply(entry, escape=True), encoding="utf-8")
        self.assertTrue(a3.do_collect(self.root, self.source))
        nb_zh.verify(argparse.Namespace(source=self.source))
        self.assertEqual(a3.do_prepare(self.root, self.source, 6500, 14), 0)
        src_nb = json.loads(self.src.read_text("utf-8"))
        out_nb = json.loads(self.src.with_name("greeks_zh.ipynb").read_text("utf-8"))
        self.assertEqual(src_nb["cells"][1],out_nb["cells"][1])
        self.assertIn(r"\\Gamma = \\frac", json.dumps(out_nb))
        self.assertNotIn("[[ML4T_A3_",json.dumps(out_nb))

    def test_incomplete_tail_auto_retry_without_resending_completed(self):
        a3.do_prepare(self.root, self.source, 6500, 14)
        data = json.loads(a3.map_file(self.work).read_text("utf-8"))
        original = data["packs"][0]
        ids = [u["id"] for u in original["units"]]
        self.assertGreaterEqual(len(ids), 3)
        reply = self.work / "inbox/a3_pack_001.txt"
        reply.write_text(self.reply(original,wanted=ids[:2],truncated=ids[1]),encoding="utf-8")
        self.assertTrue(a3.do_collect(self.root, self.source))
        self.assertTrue((self.work / "responses" / f"{ids[0]}.md").exists())
        self.assertFalse((self.work / "responses" / f"{ids[1]}.md").exists())
        # Collect generated retry task automatically.
        self.assertEqual(a3.do_prepare(self.root,self.source,6500,14),0)
        data = json.loads(a3.map_file(self.work).read_text("utf-8"))
        retry = data["packs"][1]
        self.assertNotIn(ids[0],[u["id"] for u in retry["units"]])
        (self.work / "inbox/a3_pack_002.txt").write_text(self.reply(retry),encoding="utf-8")
        self.assertTrue(a3.do_collect(self.root,self.source))
        nb_zh.verify(argparse.Namespace(source=self.source))
        self.assertEqual(a3.do_prepare(self.root,self.source,6500,14),0)

    def test_invalid_token_only_retries_bad_unit(self):
        a3.do_prepare(self.root, self.source, 6500, 14)
        original = json.loads(a3.map_file(self.work).read_text("utf-8"))["packs"][0]
        ids = [u["id"] for u in original["units"]]
        (self.work / "inbox/a3_pack_001.txt").write_text(self.reply(original,bad=ids[0]),encoding="utf-8")
        self.assertTrue(a3.do_collect(self.root,self.source))
        self.assertFalse((self.work/"responses"/f"{ids[0]}.md").exists())
        self.assertTrue((self.work/"responses"/f"{ids[1]}.md").exists())
        self.assertEqual(a3.do_prepare(self.root,self.source,6500,14),0)
        retry = json.loads(a3.map_file(self.work).read_text("utf-8"))["packs"][1]
        self.assertEqual([u["id"] for u in retry["units"]],[ids[0]])

    def test_idempotence_and_collision(self):
        a3.do_prepare(self.root,self.source,6500,14)
        self.assertEqual(a3.do_prepare(self.root,self.source,6500,14),0)
        task = self.work / "packs/a3_pack_001.md"
        task.write_text(task.read_text('utf-8')+'tamper\n',encoding='utf-8')
        with self.assertRaises(a3.A3Error):
            a3.do_prepare(self.root,self.source,6500,14)


    def test_price_math_and_repeated_protected_spans(self):
        original = ("The price is $10 and the cost is $20. "
                    "Compute $2 + 3$ and $2 x$, with $\\Gamma$ and "
                    "`\\frac{a}{b}` repeated repeated repeated.")
        masked, tokens, parts = a3.mask_text(original, with_sources=True)
        self.assertIn(" and the cost is ", masked)
        self.assertIn("Compute ", masked)
        self.assertNotIn(r"\\frac{a}{b}", masked)
        restored = masked
        for key, value in parts.items():
            restored = restored.replace(key, value)
        self.assertEqual(restored, original)

    def test_chapter_bootstrap_and_balanced_queue(self):
        extra = self.root / "02_demo/other.ipynb"
        extra.write_bytes(self.src.read_bytes())
        extra.with_suffix(".py").write_text("# paired notebook\n",encoding="utf-8")
        rc = a3.main(["prepare","02_demo"])
        self.assertEqual(rc,0)
        self.assertTrue((self.root/"translations/work/02_demo/other/pack_manifest.json").is_file())
        queue = self.root/"translations/reports/02_demo_a3_queue.csv"
        self.assertTrue(queue.is_file())
        text = queue.read_text("utf-8")
        self.assertIn("account,source,pack",text)
        self.assertIn("a3_pack_001.txt",text)
        self.assertIn("02_demo/other.ipynb",text)

    def test_fail_closed_math_missing_delimiter(self):
        with self.assertRaises(a3.A3Error):
            a3.mask_text("Theta = $$\\frac{S}{T} cannot close")
        source = "Repeated words repeated words $\\frac{a}{b}$ and \\(x+y\\)"
        mask,tokens,originals = a3.mask_text(source,True)
        restored = mask
        for key,value in originals.items():
            restored = restored.replace(key,value)
        self.assertEqual(source,restored)


if __name__ == "__main__":
    unittest.main(verbosity=2)
