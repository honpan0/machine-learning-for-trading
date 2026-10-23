#!/usr/bin/env python3
"""Offline smoke test for nb_zh.py. Uses an isolated temporary fake repository."""
import argparse
import json
import os
import tempfile
from pathlib import Path

import nb_zh as tool


def main():
    original_dir = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="ml4t-translation-test-") as tmp:
        root = Path(tmp)
        (root / ".git").mkdir()
        (root / "pyproject.toml").write_text("", encoding="utf-8")
        folder = root / "01_process_is_edge"
        folder.mkdir()
        src = folder / "factor_regimes.ipynb"
        prose = "# A model\n\n" + "\n\n".join(
            f"Paragraph {i}: this sentence explains financial returns and asset risk."
            for i in range(20)
        )
        source = {
            "nbformat": 4, "nbformat_minor": 5,
            "metadata": {"jupytext": {"formats": "ipynb,py:percent"},
                         "ml4t_provenance": {"executor": "source"},
                         "kernelspec": {"name": "python3", "display_name": "Python 3"}},
            "cells": [
                {"cell_type": "markdown", "metadata": {}, "source": prose},
                {"cell_type": "code", "metadata": {"tags": ["important"]},
                 "source": ["print(42)\n"], "execution_count": 8,
                 "outputs": [{"output_type": "stream", "name": "stdout", "text": ["42\n"]}]},
                {"cell_type": "markdown", "metadata": {},
                 "source": "A related formula follows.\n\n$$x=1$$\n\n```python\nprint(7)\n```"},
            ],
        }
        src.write_text(json.dumps(source, ensure_ascii=False), encoding="utf-8")
        os.chdir(root)
        relative = "01_process_is_edge/factor_regimes.ipynb"
        tool.prepare(argparse.Namespace(source=relative, max_chars=200, batch_chars=320))
        _, _, work, out = tool.paths(root, relative)
        manifest = tool.read_json(work / "manifest.json")
        assert len(manifest["units"]) > 2
        assert len(manifest["batches"]) > 2
        # Simulate receiving batches from two accounts in reverse order.
        for i in reversed(range(1, len(manifest["batches"]) + 1)):
            lines = []
            for uid in manifest["batches"][i - 1]:
                lines += [f"<<<ML4T-ZH-BEGIN:{uid}>>>",
                          "這是對照翻譯。" if uid != manifest["units"][-1]["id"] else tool.SKIP,
                          f"<<<ML4T-ZH-END:{uid}>>>"]
            reply = work / "inbox" / f"batch_{i:03d}.txt"
            reply.write_text("\n".join(lines) + "\n", encoding="utf-8")
            tool.ingest(argparse.Namespace(source=relative, batch=i, file=str(reply), replace=False))
        tool.build(argparse.Namespace(source=relative, replace=False))
        tool.verify(argparse.Namespace(source=relative))
        expected = tool.read_json(src)
        generated = tool.read_json(out)
        assert generated["cells"][1] == expected["cells"][1], "code/output drift"
        assert tool.MARKER.sub("", tool.text_of(generated["cells"][0])) == prose
        assert "jupytext" not in generated["metadata"]
        assert "ml4t_provenance" not in generated["metadata"]
        try:
            tool.build(argparse.Namespace(source=relative, replace=False))
            raise AssertionError("build accidentally overwrote an existing derivative")
        except tool.PipelineError:
            pass
        generated["cells"][1]["source"] = ["print('tampered')"]
        out.write_text(json.dumps(generated, ensure_ascii=False), encoding="utf-8")
        try:
            tool.verify(argparse.Namespace(source=relative))
            raise AssertionError("tampered code was not detected")
        except tool.PipelineError:
            pass
        src.write_text(src.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        try:
            tool.status(argparse.Namespace(source=relative))
            raise AssertionError("upstream source drift was not detected")
        except tool.PipelineError:
            pass
    os.chdir(original_dir)
    print("ALL TESTS PASSED: split, out-of-order import, resume, SKIP, build, verify, tamper, source drift, overwrite protection")


if __name__ == "__main__":
    main()
