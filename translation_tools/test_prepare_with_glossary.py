#!/usr/bin/env python3
"""Offline integration tests for the optional glossary preparation wrapper."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

import nb_zh
import prepare_with_glossary as tool


def run() -> None:
    assert tool.matches_english("Factor returns", "These factor returns fluctuate")
    assert tool.matches_english("Market regime", "Two market regimes emerged")
    assert not tool.matches_english("Factor", "factorization and factor_model")
    assert tool.matches_english("Gaussian mixture model (GMM)", "A GMM estimates clusters")
    assert not tool.matches_english("Alpha", "alphabetical order")

    original_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="ml4t-glossary-test-") as temp:
        root = Path(temp)
        (root / ".git").mkdir()
        (root / "pyproject.toml").write_text("", encoding="utf-8")
        (root / "translations").mkdir()
        (root / "translations" / "glossary_zh_TW.md").write_text(
            "# 詞彙\n\n| 英文 | 建議繁體中文 |\n|---|---|\n"
            "| Market regime | 市場狀態 |\n"
            "| Gaussian mixture model (GMM) | 高斯混合模型 |\n"
            "| Factor returns | 因子報酬率 |\n"
            "| Alpha | 超額報酬 |\n"
            "| Portfolio | 投資組合 |\n", encoding="utf-8")
        chapter = root / "01_process_is_edge"
        chapter.mkdir()
        src = chapter / "sample.ipynb"
        notebook = {
            "nbformat": 4, "nbformat_minor": 5,
            "metadata": {"jupytext": {"formats": "ipynb,py:percent"},
                         "ml4t_provenance": {"executor": "source"}},
            "cells": [
                {"cell_type": "markdown", "metadata": {},
                 "source": "# Gaussian mixture model\n\nMarket regimes relate to factor returns.\n"},
                {"cell_type": "code", "metadata": {}, "source": "print(42)\n",
                 "outputs": [{"output_type": "stream", "name": "stdout", "text": "42\n"}],
                 "execution_count": 1},
                {"cell_type": "markdown", "metadata": {},
                 "source": "This unrelated paragraph describes an axis.\n"},
            ],
        }
        src.write_text(json.dumps(notebook, ensure_ascii=False), encoding="utf-8")
        os.chdir(root)
        try:
            args = argparse.Namespace(source="01_process_is_edge/sample.ipynb",
                                      max_chars=1800, batch_chars=5000, max_terms=25,
                                      glossary="translations/glossary_zh_TW.md")
            tool.prepare_glossary(args)
            work = root / "translations/work/01_process_is_edge/sample"
            task = (work / "tasks/batch_001.md").read_text(encoding="utf-8")
            assert "Gaussian mixture model (GMM) → 高斯混合模型" in task
            assert "Market regime → 市場狀態" in task
            assert "Factor returns → 因子報酬率" in task
            assert "Alpha →" not in task
            assert "Portfolio →" not in task
            assert task.index("## 本批次相關術語") < task.index("## 單元：")
            manifest = nb_zh.read_json(work / "manifest.json")
            assert manifest["glossary_info"]["entries"] == 5
            assert manifest["source"] == "01_process_is_edge/sample.ipynb"
            # Existing translations remain safe: repeated prepare must abort without modifying a task.
            try:
                tool.prepare_glossary(args)
                raise AssertionError("reprepare overwrote existing tasks")
            except nb_zh.PipelineError:
                pass
            assert (work / "tasks/batch_001.md").read_text(encoding="utf-8") == task

            # Original ingest / build / verify still works on glossary-augmented tasks.
            lines = []
            for unit in manifest["units"]:
                uid = unit["id"]
                lines.extend((f"<<<ML4T-ZH-BEGIN:{uid}>>>", "中譯內容。",
                              f"<<<ML4T-ZH-END:{uid}>>>"))
            inbox = work / "inbox/batch_001.txt"
            inbox.write_text("\n".join(lines) + "\n", encoding="utf-8")
            nb_zh.ingest(argparse.Namespace(source=args.source, batch=1,
                                            file=str(inbox), replace=False))
            nb_zh.build(argparse.Namespace(source=args.source, replace=False))
            nb_zh.verify(argparse.Namespace(source=args.source))
            assert "ml4t_translation" in nb_zh.read_json(chapter / "sample_zh.ipynb")["metadata"]
            assert "jupytext" not in nb_zh.read_json(chapter / "sample_zh.ipynb")["metadata"]
        finally:
            os.chdir(original_cwd)
    print("ALL GLOSSARY TESTS PASSED: matching, selection, prepare, safe refusal, ingest, build, verify")


if __name__ == "__main__":
    run()
