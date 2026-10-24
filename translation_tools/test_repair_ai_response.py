#!/usr/bin/env python3
"""Regression tests for safe marker-only repair; no external packages needed."""
from __future__ import annotations

import tempfile
import unittest
import shutil
import subprocess
import sys
from pathlib import Path

from repair_ai_response import RepairError, apply, inspect, normalize, validate

U0 = "c0000-p000"
U1 = "c0001-p000"
BEG0 = f"<<<ML4T-ZH-BEGIN:{U0}>>>"
END0 = f"<<<ML4T-ZH-END:{U0}>>>"
BEG1 = f"<<<ML4T-ZH-BEGIN:{U1}>>>"
END1 = f"<<<ML4T-ZH-END:{U1}>>>"


class MarkerRepairTests(unittest.TestCase):
    def test_bad_prefixes_and_glued_markers(self):
        original = (
            f"<<\\<ML4T-ZH-BEGIN:{U0}>>>\n"
            "中文第一段，保留 `factor_regimes` 與 $x^2$。\n"
            f"<escape><<<ML4T-ZH-END:{U0}>>><<<ML4T-ZH-BEGIN:{U1}>>>\n"
            "中文第二段。\n"
            f"<escape><<<ML4T-ZH-END:{U1}>>>\n"
        )
        fixed, changed, joins = normalize(original)
        self.assertEqual(changed, 3)
        self.assertEqual(joins, 1)
        self.assertEqual(validate(fixed, [U0, U1]), 2)
        self.assertIn("中文第一段，保留 `factor_regimes` 與 $x^2$。", fixed)
        self.assertIn(f"{END0}\n{BEG1}", fixed)
        self.assertEqual(normalize(fixed)[0], fixed)

    def test_preserves_crlf_in_markers(self):
        raw = f"<<\\<ML4T-ZH-BEGIN:{U0}>>>\r\n翻譯\r\n{END0}\r\n"
        fixed, count, joins = normalize(raw)
        self.assertEqual((count, joins), (1, 0))
        self.assertEqual(fixed, f"{BEG0}\r\n翻譯\r\n{END0}\r\n")

    def test_reject_unmatched_or_unknown_markers(self):
        cases = [
            f"{BEG0}\n譯文\n",
            f"{BEG0}\n譯文\n{END1}\n",
            f"{BEG0}\n譯文\n{END0}\n{BEG0}\n重複\n{END0}\n",
            f"{BEG0}\n譯文\n{END0}\n這是額外前言\n",
            f"<bad>{BEG0}\n譯文\n{END0}\n",
            f"{BEG0}\n（在此填寫 {U0} 的完整繁體中文 Markdown 翻譯）\n{END0}\n",
        ]
        for content in cases:
            with self.subTest(content=content):
                with self.assertRaises(RepairError):
                    validate(content, [U0])

    def test_inspect_only_and_backup(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            task = work / "batch_001.md"
            reply = work / "batch_001.txt"
            task.write_text(f"## 單元：{U0}\n原文...\n", encoding="utf-8")
            original = f"<<\\<ML4T-ZH-BEGIN:{U0}>>>\n這是完整譯文。\n{END0}\n".encode()
            reply.write_bytes(original)
            data = inspect(reply, task)
            self.assertTrue(data.changed)
            self.assertEqual(reply.read_bytes(), original)
            backup = apply(data)
            self.assertEqual(backup.read_bytes(), original)
            self.assertEqual(validate(reply.read_text(), [U0]), 1)
            self.assertFalse(inspect(reply, task).changed)
            self.assertIsNone(apply(inspect(reply, task)))

    def test_cli_all_batches_refuses_partial_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tools = root / "translation_tools"
            tools.mkdir()
            shutil.copy2(Path(__file__).with_name("repair_ai_response.py"), tools / "repair_ai_response.py")
            work = root / "translations/work/01_process_is_edge/example"
            (work / "tasks").mkdir(parents=True)
            (work / "inbox").mkdir(parents=True)
            (work / "tasks/batch_001.md").write_text(f"## 單元：{U0}\n", encoding="utf-8")
            (work / "tasks/batch_002.md").write_text(f"## 單元：{U1}\n", encoding="utf-8")
            one = work / "inbox/batch_001.txt"
            two = work / "inbox/batch_002.txt"
            raw = f"<<\\<ML4T-ZH-BEGIN:{U0}>>>\n翻譯一\n{END0}\n".encode()
            one.write_bytes(raw)
            # Incomplete second batch should block all changes
            two.write_text(f"{BEG1}\n翻譯二\n", encoding="utf-8")
            command = [sys.executable, str(tools / "repair_ai_response.py"), "01_process_is_edge/example.ipynb"]
            result = subprocess.run(command + ["--fix"], text=True, capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(one.read_bytes(), raw)
            self.assertFalse((work / "inbox/batch_001.txt.bak").exists())
            two.write_text(f"{BEG1}\n翻譯二\n{END1}\n", encoding="utf-8")
            checked = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(checked.returncode, 1)
            self.assertEqual(one.read_bytes(), raw)
            result = subprocess.run(command + ["--fix"], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(one.read_text(), f"{BEG0}\n翻譯一\n{END0}\n")
            self.assertTrue((work / "inbox/batch_001.txt.bak").is_file())
            self.assertFalse((work / "inbox/batch_002.txt.bak").exists())
            checked = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(checked.returncode, 0, checked.stderr)

    def test_reject_without_touching_invalid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            task = work / "batch_001.md"
            reply = work / "batch_001.txt"
            task.write_text(f"## 單元：{U0}\n## 單元：{U1}\n", encoding="utf-8")
            raw = f"<<\\<ML4T-ZH-BEGIN:{U0}>>>\n只有一單元\n{END0}\n".encode()
            reply.write_bytes(raw)
            with self.assertRaises(RepairError):
                inspect(reply, task)
            self.assertEqual(reply.read_bytes(), raw)
            self.assertFalse((work / "batch_001.txt.bak").exists())


    def test_real_world_escaped_html_suffix_and_orphan_slash(self):
        # Reproduces the pattern from the 04_cme_futures_eda Pack 001 reply.
        raw = (
            r"\<escape><<\<ML4T-ZH-BEGIN:c0000-p000>>>" + "\n"
            + "保留原始內文中的 `\\` 和 $x^2$。\n"
            + r"<<\<ML4T-ZH-END:c0000-p000>>>" + "\\" + "\n"
            + "\\\n"  # An orphan backslash outside all translation units
            + r"\<escape><<\<ML4T-ZH-BEGIN:c0001-p000>>>" + "\n"
            + "第二段完整翻譯。\n"
            + r"<<\<ML4T-ZH-END:c0001-p000>>>" + "\n"
        )
        normalized, changes, joins = normalize(raw)
        self.assertEqual(normalized, (
            f"{BEG0}\n保留原始內文中的 `\\` 和 $x^2$。\n{END0}\n"
            f"{BEG1}\n第二段完整翻譯。\n{END1}\n"
        ))
        self.assertEqual((changes, joins), (5, 0))
        self.assertEqual(validate(normalized, [U0, U1]), 2)
        self.assertEqual(normalize(normalized), (normalized, 0, 0))

    def test_mixed_escaped_glued_markers_with_trailing_slash(self):
        raw = (
            f"{BEG0}\r\n第一單元。\r\n"
            + r"<<\<ML4T-ZH-END:c0000-p000>>>\\<escape><<\<ML4T-ZH-BEGIN:c0001-p000>>>" + "\r\n"
            + "第二單元。\r\n"
            + r"<<\<ML4T-ZH-END:c0001-p000>>>" + "\\" + "\r\n"
        )
        fixed, count, joins = normalize(raw)
        self.assertEqual(fixed, f"{BEG0}\r\n第一單元。\r\n{END0}\r\n{BEG1}\r\n第二單元。\r\n{END1}\r\n")
        self.assertEqual((count, joins), (3, 1))
        self.assertEqual(validate(fixed, [U0, U1]), 2)

    def test_standalone_backslash_inside_translation_preserved(self):
        raw = f"{BEG0}\n\\\n\n內文含獨立反斜線。\n{END0}\n"
        fixed, changes, joins = normalize(raw)
        self.assertEqual(fixed, raw)
        self.assertEqual((changes, joins), (0, 0))
        self.assertEqual(validate(fixed, [U0]), 1)

    def test_malformed_marker_or_extra_prose_still_rejected(self):
        bad = [
            r"\<escape><<\<ML4T-ZH-BEGIN:c0000-p000>>" + "\n譯文\n" + END0,
            r"<<<ML4T-ZH-BEGIN:c0000-p000>>>\ other" + "\n譯文\n" + END0,
            "不可隨意刪除的前言\n" + BEG0 + "\n譯文\n" + END0,
            BEG0 + "\n譯文\n" + r"<<\<ML4T-ZH-END:c0001-p000>>>" + "\n",
        ]
        for raw in bad:
            with self.subTest(raw=raw):
                normalized, _, _ = normalize(raw)
                with self.assertRaises(RepairError):
                    validate(normalized, [U0])

    def test_repair_failure_does_not_write_backup_or_change_translation(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            task = work / "batch_001.md"
            reply = work / "batch_001.txt"
            task.write_text(f"## 單元：{U0}\n", encoding="utf-8")
            bad = (r"\<escape><<\<ML4T-ZH-BEGIN:c0000-p000>>>" +
                   "\n原譯文\n" +
                   r"<<\<ML4T-ZH-END:c0001-p000>>>" + "\n").encode("utf-8")
            reply.write_bytes(bad)
            with self.assertRaises(RepairError):
                inspect(reply, task)
            self.assertEqual(reply.read_bytes(), bad)
            self.assertFalse((work / "batch_001.txt.bak").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
