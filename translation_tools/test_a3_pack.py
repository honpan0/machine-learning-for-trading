#!/usr/bin/env python3
"""Offline integration tests for A3 using real A2/Notebook pipeline."""
from __future__ import annotations
import argparse
import json
import os
import tempfile
import unittest
from unittest import mock
from pathlib import Path

import a3_pack as a3
import nb_zh
import pack_translation as a2


# Verbatim boundary regression from notebook 13, c0014-p000.
BOUNDARY_CASE = r"""- **MAD** flags a return when $|r - \mathrm{median}|$ exceeds $\tau \cdot \mathrm{MAD} /
  c$, where MAD is the median absolute deviation from the median and $c$, declared as
  `MAD_NORMAL_SCALE`, is the MAD of a standard normal.
- **Z-score** flags it when $|r - \mathrm{mean}|$ exceeds $\tau \cdot \sigma$.
- **IQR** flags it when $r$ falls outside $[Q_1 - \tau \cdot \mathrm{IQR},\ Q_3 + \tau \cdot
  \mathrm{IQR}]$."""


class MaskVersionTests(unittest.TestCase):
    def test_multiline_math_keeps_explanation_visible_and_restores_exactly(self):
        masked, tokens, parts = a3.mask_text(BOUNDARY_CASE, True)
        self.assertEqual(len(tokens), 8)
        self.assertIn("where MAD is the median absolute deviation from the median and", masked)
        self.assertIn("is the MAD of a standard normal", masked)
        self.assertNotIn("where MAD", "".join(parts.values()))
        self.assertNotIn(r"\tau", masked)
        self.assertNotIn("$", masked)
        self.assertEqual(list(parts.values()), [
            r"$|r - \mathrm{median}|$", "$\\tau \\cdot \\mathrm{MAD} /\n  c$",
            "$c$", "`MAD_NORMAL_SCALE`", r"$|r - \mathrm{mean}|$",
            r"$\tau \cdot \sigma$", "$r$",
            "$[Q_1 - \\tau \\cdot \\mathrm{IQR},\\ Q_3 + \\tau \\cdot\n  \\mathrm{IQR}]$",
        ])
        for key, value in parts.items():
            masked = masked.replace(key, value)
        self.assertEqual(masked, BOUNDARY_CASE)

    def test_unversioned_entry_uses_legacy_boundaries_and_rejects_tampering(self):
        masked, tokens = a3.mask_text(BOUNDARY_CASE, mask_version=1)
        self.assertEqual(len(tokens), 6)
        unit = {"id": "c0014-p000", "source_sha256": a3.sha(BOUNDARY_CASE.encode()),
                "masked_sha256": a3.sha(masked.encode()), "tokens": tokens}
        reply = (f"<<<ML4T-ZH-BEGIN:{unit['id']}>>>\n{masked}\n"
                 f"<<<ML4T-ZH-END:{unit['id']}>>>\n").encode()
        with mock.patch.object(a3.packing, "english", return_value=BOUNDARY_CASE):
            restored, rejected, _, _, _ = a3.restore_one(
                Path(), "", Path(), {}, {unit['id']: unit}, {}, {"units": [unit]}, reply)
            self.assertFalse(rejected)
            self.assertEqual(restored[unit['id']], BOUNDARY_CASE)
            unit['masked_sha256'] = 'tampered'
            with self.assertRaises(a3.A3Error):
                a3.restore_one(Path(), "", Path(), {}, {unit['id']: unit}, {},
                               {"units": [unit]}, reply)

    def test_fail_closed_unbalanced_and_paragraph_crossing_math(self):
        for text in ("Compute $x + y", "$x\n\nEnglish explanation$", "Compute $x$ then $y"):
            with self.subTest(text=text), self.assertRaises(a3.A3Error):
                a3.mask_text(text)
        with self.assertRaises(a3.A3Error):
            a3.mask_text("$x$", mask_version=99)

    def test_v2_collect_restores_multiline_math_and_rejects_extra_formula(self):
        # Explicitly exercise the issued v2 Pack protocol, not current v3 defaults.
        masked, tokens = a3.mask_text(BOUNDARY_CASE, mask_version=2)
        unit = {"id": "c0014-p000", "mask_version": 2,
                "source_sha256": a3.sha(BOUNDARY_CASE.encode()),
                "masked_sha256": a3.sha(masked.encode()), "tokens": tokens}
        phrase = 'where MAD is the median absolute deviation from the median and'
        translated = masked.replace(phrase, '其中 MAD 是相對於中位數的絕對偏差中位數，而')
        with mock.patch.object(a3.packing, 'english', return_value=BOUNDARY_CASE):
            for extra in ('', ' $x$'):
                reply = (f"<<<ML4T-ZH-BEGIN:{unit['id']}>>>\n{translated}{extra}\n"
                         f"<<<ML4T-ZH-END:{unit['id']}>>>\n").encode()
                out, rejected, _, _, _ = a3.restore_one(
                    Path(), '', Path(), {}, {unit['id']: unit}, {}, {'units': [unit]}, reply)
                if extra:
                    self.assertEqual(rejected, [unit['id']])
                    self.assertFalse(out)
                else:
                    self.assertEqual(out[unit['id']], BOUNDARY_CASE.replace(
                        phrase, '其中 MAD 是相對於中位數的絕對偏差中位數，而'))


class MaskV3Tests(unittest.TestCase):
    def test_price_prose_never_swallowed_in_currency_pairs(self):
        examples = [
            ("The price is $50.00; next is $60.00.",
             ["$50.00", "$60.00"], "; next is "),
            ("Cost $10; alpha is $x$ and beta is $y$.",
             ["$10", "$x$", "$y$"], "; alpha is "),
            ("Currency $100 and `inline` with math $\\beta$.",
             ["$100", "`inline`", "$\\beta$"], " with math "),
            ("Costs $5 + $10 today.", ["$5", "$10"], " + "),
            ("Amounts $1,000 per year and $2,500 per year.",
             ["$1,000", "$2,500"], " per year and "),
        ]
        for source, expected, prose in examples:
            with self.subTest(source=source):
                masked, tokens, pieces = a3.mask_text(source, True)
                self.assertEqual(list(pieces.values()), expected)
                self.assertIn(prose, masked)
                self.assertEqual(len(tokens), len(expected))
                restored = masked
                for key, value in pieces.items():
                    restored = restored.replace(key, value)
                self.assertEqual(restored, source)

    def test_numeric_math_and_multiline_latex(self):
        source = ("Examples $2 + 3$, $2 x$, $100$, "
                  "and $\\tau \\cdot \\mathrm{MAD} /\n  c$. "
                  "Display $$\\frac{a}{b}$$ ends here.")
        masked, tokens, pieces = a3.mask_text(source, True)
        self.assertEqual([t['kind'] for t in tokens], ["math"] * 5)
        self.assertNotIn("\\frac", masked)
        self.assertNotIn("$", masked)
        result = masked
        for k, v in pieces.items():
            result = result.replace(k, v)
        self.assertEqual(result, source)

    def test_dollar_does_not_pair_over_protected_inline_code(self):
        source = "Cost $10 and `code $x$` then price $20, formula $y$."
        masked, _, pieces = a3.mask_text(source, True)
        self.assertEqual(list(pieces.values()),
                         ["$10", "`code $x$`", "$20", "$y$"])
        self.assertIn(" and ", masked)
        self.assertIn(" then price ", masked)

    def test_ambiguous_math_fails_closed(self):
        examples = ["$x\n\nEnglish explanation$", "Compute $x + y",
                    "$some English phrase$", "Cost $5 but math $x",
                    "$$\\frac{a}{b} missing end"]
        for source in examples:
            with self.subTest(source=source), self.assertRaises(a3.A3Error):
                a3.mask_text(source)

    def test_v3_restore_preserves_prose_and_rejects_added_dollars(self):
        source = "The price is $50.00; next is $60.00. Compute $x + 1$."
        masked, tokens = a3.mask_text(source)
        u = {"id": "c0001-p000", "mask_version": 3,
             "source_sha256": a3.sha(source.encode()),
             "masked_sha256": a3.sha(masked.encode()), "tokens": tokens}
        for extra in ("", " $new$"):
            translated = masked.replace("next is", "接著為") + extra
            reply = (f"<<<ML4T-ZH-BEGIN:{u['id']}>>>\n{translated}\n"
                     f"<<<ML4T-ZH-END:{u['id']}>>>\n").encode()
            with mock.patch.object(a3.packing, "english", return_value=source):
                outputs, rejected, _, _, _ = a3.restore_one(
                    Path(), "", Path(), {}, {u['id']: u}, {},
                    {"units": [u]}, reply)
            if extra:
                self.assertEqual(rejected, [u['id']])
                self.assertFalse(outputs)
            else:
                self.assertFalse(rejected)
                self.assertEqual(outputs[u['id']], source.replace("next is", "接著為"))

    def test_audit_is_read_only_and_reports_old_span_risk(self):
        source = "The price is $50.00; next is $60.00."
        old, tokens = a3.mask_text(source, mask_version=2)
        u = {"id": "c0001-p000", "mask_version": 2,
             "source_sha256": a3.sha(source.encode()),
             "masked_sha256": a3.sha(old.encode()), "tokens": tokens}
        data = {"packs": [{"processed_sha256": None, "units": [u]}]}
        root = Path("/unreal")
        with mock.patch.object(a3, "work_context", return_value=(
                root, {}, {}, {u['id']: u}, {}, {})), \
             mock.patch.object(a3, "load_a3", return_value=data), \
             mock.patch.object(a3.packing, "is_complete", return_value=False), \
             mock.patch.object(a3.packing, "english", return_value=source):
            checked, changed, blocked = a3.do_audit(root, "demo.ipynb")
        self.assertEqual((checked, changed, blocked), (1, 1, 0))


class MaskV4UnitPricesTests(unittest.TestCase):
    def test_databento_dollar_price_with_per_symbol_per_month(self):
        source = "ITCH (Free) | DataBento (~$10/symbol/mo), with notes."
        masked, tokens, originals = a3.mask_text(source, True)
        self.assertEqual([t['kind'] for t in tokens], ['price'])
        self.assertEqual(list(originals.values()), ['$10/symbol/mo'])
        self.assertIn('DataBento (~', masked)
        self.assertIn('), with notes.', masked)
        restored = masked
        for key, value in originals.items():
            restored = restored.replace(key, value)
        self.assertEqual(restored, source)

    def test_multiple_currency_units_are_distinct_from_latex(self):
        source = 'Price $2/GB/day and $20/month; mathematical value $x$.'
        masked, tokens, originals = a3.mask_text(source, True)
        self.assertEqual(list(originals.values()), ['$2/GB/day', '$20/month', '$x$'])
        self.assertEqual([t['kind'] for t in tokens], ['price', 'price', 'math'])
        self.assertIn(' and ', masked)
        self.assertIn('; mathematical value ', masked)

    def test_numeric_math_not_misread_as_unit_price(self):
        for source in ('$10/x$', '$10/GB$', '$10/x + y$', '$10/x = 5$'):
            with self.subTest(source=source):
                _, tokens, originals = a3.mask_text(source, True)
                self.assertEqual([t['kind'] for t in tokens], ['math'])
                self.assertEqual(list(originals.values()), [source])

    def test_v3_behavior_is_preserved_for_issued_packs(self):
        source = 'DataBento costs ~$10/symbol/mo.'
        with self.assertRaises(a3.A3Error):
            a3.mask_text(source, mask_version=3)
        masked, tokens, originals = a3.mask_text(source, True, mask_version=4)
        self.assertEqual(list(originals.values()), ['$10/symbol/mo'])
        self.assertEqual(tokens[0]['kind'], 'price')
        self.assertNotIn('$', masked)


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

    def test_explicit_remask_appends_without_changing_legacy_pack(self):
        # Install the real defective source into this isolated test project.
        cells = json.loads(self.src.read_text())
        cells['cells'][0]['source'] = BOUNDARY_CASE
        self.src.write_text(json.dumps(cells))
        # Recreate only this test's scratch preparation, before any A3 tasks exist.
        import shutil
        shutil.rmtree(self.work)
        nb_zh.prepare(argparse.Namespace(source=self.source, max_chars=4000, batch_chars=5000))
        a2.pack_all(self.root, self.source, 2, 6000, 25, False, False)
        current_mask = a3.mask_text
        current_prepare = a3.prepared_unit
        def legacy_unit(*args):
            result = current_prepare(*args)
            result.pop('mask_version')
            return result
        with mock.patch.object(a3, 'mask_text', side_effect=lambda raw, **kw:
                               current_mask(raw, mask_version=1, **kw)), \
             mock.patch.object(a3, 'prepared_unit', side_effect=legacy_unit):
            a3.do_prepare(self.root, self.source, 6500, 14)
        old = json.loads(a3.map_file(self.work).read_text())['packs']
        old_files = {e['file']: (self.work/'packs'/e['file']).read_bytes() for e in old}
        self.assertEqual(a3.do_prepare(self.root, self.source, 6500, 14), 0)
        self.assertEqual(a3.do_prepare(self.root, self.source, 6500, 14, remask_legacy=True), 1)
        entries = json.loads(a3.map_file(self.work).read_text())['packs']
        self.assertEqual(entries[:-1], old)
        self.assertEqual(len(entries[-1]['units']), 1)
        self.assertEqual(entries[-1]['units'][0]['mask_version'], a3.MASK_VERSION)
        for file, raw in old_files.items():
            self.assertEqual((self.work/'packs'/file).read_bytes(), raw)
        self.assertEqual(a3.do_prepare(self.root, self.source, 6500, 14, remask_legacy=True), 0)


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
