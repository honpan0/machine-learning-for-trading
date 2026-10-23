#!/usr/bin/env python3
"""Self-contained regression test; creates a temporary fake ML4T repository."""
import argparse
import contextlib
import io
import json
import os
import tempfile
from pathlib import Path

import nb_zh
import progress_dashboard as dash


def write_notebook(root: Path, source: str) -> Path:
    target = root / source
    target.parent.mkdir(parents=True, exist_ok=True)
    nb = {"nbformat": 4, "nbformat_minor": 5, "metadata": {"jupytext": {"formats": "ipynb,py:percent"}},
          "cells": [
              {"cell_type": "markdown", "metadata": {}, "source": ["# Introduction\n", "\n", "This is a paragraph about markets.\n"]},
              {"cell_type": "code", "metadata": {}, "source": ["print(1)\n"], "execution_count": 5,
               "outputs": [{"output_type": "stream", "name": "stdout", "text": ["1\n"]}]},
          ]}
    target.write_text(json.dumps(nb, ensure_ascii=False), encoding="utf-8")
    target.with_suffix(".py").write_text("# %% [markdown]\n# Introduction\n# %%\nprint(1)\n", encoding="utf-8")
    return target


def main():
    previous = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="ml4t-dashboard-test-") as folder:
        root = Path(folder)
        (root / ".git").mkdir()
        (root / "pyproject.toml").write_text("", encoding="utf-8")
        completed = write_notebook(root, "01_chapter/example.ipynb")
        ready = write_notebook(root, "case_studies/study1/ready.ipynb")
        partial = write_notebook(root, "data/example_data.ipynb")
        untouched = write_notebook(root, "02_other/untouched.ipynb")
        for source in [completed, ready, partial]:
            os.chdir(root)
            with contextlib.redirect_stdout(io.StringIO()):
                nb_zh.prepare(argparse.Namespace(source=source.relative_to(root).as_posix(), max_chars=200, batch_chars=250))
        os.chdir(root)
        # finish two, leave one partial
        for source in [completed, ready, partial]:
            rel = source.relative_to(root).as_posix()
            work = root / "translations" / "work" / source.relative_to(root).with_suffix("")
            manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
            for i, unit in enumerate(manifest["units"]):
                if source == partial and i == len(manifest["units"]) - 1:
                    continue
                (work / "responses" / f"{unit['id']}.md").write_text("中文翻譯。\n", encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            nb_zh.build(argparse.Namespace(source="01_chapter/example.ipynb", replace=False))
        records = {r.source: r for r in [dash.inspect(root, p) for p in dash.find_sources(root)]}
        assert len(records) == 4
        assert records["01_chapter/example.ipynb"].state == "verified"
        assert records["case_studies/study1/ready.ipynb"].state == "ready"
        assert records["data/example_data.ipynb"].state == "in_progress"
        assert records["02_other/untouched.ipynb"].state == "not_started"
        # Changing the English source must flag drift, and never erase translations.
        ready.write_text(ready.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        assert dash.inspect(root, ready.relative_to(root)).state == "stale"
        ready.write_text(ready.read_text(encoding="utf-8").rstrip("\n"), encoding="utf-8")
        # Tampering with code in bilingual notebook must be flagged.
        result = completed.with_name("example_zh.ipynb")
        rendered = json.loads(result.read_text(encoding="utf-8"))
        rendered["cells"][1]["source"] = ["print(999)\n"]
        result.write_text(json.dumps(rendered), encoding="utf-8")
        assert dash.inspect(root, completed.relative_to(root)).state == "broken"
        # Report serialization works without touching the source notebooks.
        dash.markdown_report(list(records.values()))
        assert "4 份" in dash.summary(list(records.values()))
        os.chdir(previous)
    print("ALL DASHBOARD TESTS PASSED: discover, completed, ready, partial, untouched, drift, tamper, report")


if __name__ == "__main__":
    main()
