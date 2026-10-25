# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/20_storage_benchmark_file.ipynb；A3 Pack 001；單元 13 個。


## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# File-Format Storage Benchmark

**Environment**: the locked environment ([[ML4T_A3_0001]]) — see Prerequisites below.

**Purpose**: Compare CSV, Parquet, Feather (Arrow IPC), and HDF5 on the same
1 M-row OHLCV panel along three axes — write time, read time (with forced
materialization), and on-disk size — so the trade-offs in §2.4 are
reproducible end to end.

**Learning objectives**:
1. Generate a deterministic OHLCV benchmark panel at the L scale that
   chapter §2.4 cites (100 symbols × 10,000 one-minute bars = 1,000,000 rows).
2. Time write and read for each format under one stated timing policy.
3. Force materialization on Feather / HDF5 reads so memory-mapped or lazy
   reads don't masquerade as instant.
4. Quantify the columnar-projection win (read 2 columns vs 9).
5. Render a 3-panel comparison (read time / write time / file size).

**Book reference**: §2.4 — file-based storage benchmarks.

**Prerequisites**: PyTables (the HDF5 backend) ships in the locked
environment, so [[ML4T_A3_0002]]
from the repo root is all this notebook needs — no database services, unlike
[[ML4T_A3_0003]].

> **Which environment produced the numbers**: the locked environment
> ([[ML4T_A3_0004]], i.e. [[ML4T_A3_0005]]), which is what §2.4 reports. The [[ML4T_A3_0006]]
> Docker image currently resolves a *newer* pandas than [[ML4T_A3_0007]] pins, and
> pandas' newer string dtype makes PyTables store the low-cardinality
> [[ML4T_A3_0008]] column about 8 bytes/row wider — enough to move the HDF5 file
> from ~71 MB to ~79 MB for the identical panel. CSV, Parquet, and Feather
> are unaffected. Run this notebook under [[ML4T_A3_0009]] to reproduce §2.4.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0003-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] selects the panel size. The production setting is the one §2.4 quotes,
and CI overrides it to the small scale through Papermill; [[ML4T_A3_0002]] and the printed
row count below say which one produced the numbers on the page.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
[[ML4T_A3_0001]] reads the scale from the environment when it is imported, so
the variable has to be set before the import rather than passed to a function afterwards.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Timing Policy

Every number below follows one policy, applied identically to all four
formats. A comparison that mixes policies across the things it compares is
not a comparison, so this is stated up front rather than left in the call
sites:

- **Writes** ([[ML4T_A3_0001]]) — a single shot, no warm-up run. Writing the
  panel is a once-per-dataset operation, so that is what we time.
- **Reads** ([[ML4T_A3_0002]]) — the mean of [[ML4T_A3_0003]] runs after one untimed
  warm-up run. **These are warm-cache numbers.** The file has just been
  written and re-read repeatedly, so it sits in the OS page cache.

Warm-cache reads are the honest description of the *repeated-access* pattern
a research loop actually has, but they flatter memory-mapped formats: Feather
maps pages that are already resident, so its read number below is close to a
best case. A first read of a cold file off disk narrows the gap to Parquet,
and on a network or object store the compressed format usually wins outright
because it moves fewer bytes. Rankings here are for warm, local, repeated
reads — the caveat that §2.4 attaches to these figures.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0008-p000

~~~~~~markdown
## 1. Generate the Benchmark Panel

[[ML4T_A3_0001]] returns a deterministic OHLCV panel: per-symbol random
walks under a fixed seed so format comparisons aren't muddled by data drift
across runs. At L scale that's 100 symbols × 10,000 one-minute bars =
1 M total rows, laid out over 26 regular trading sessions (390 bars each), so
the panel carries the overnight and weekend gaps real minute data has. All
symbols share the session grid, as they do in any synchronized bar panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0011-p000

~~~~~~markdown
## 2. CSV — Universal Baseline

CSV is the row-oriented baseline: human-readable, no compression, no schema.
Every other format is judged against it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## 3. Parquet — Compressed Columnar Standard

Parquet's row-group layout, dictionary encoding, and Snappy compression make
it the default for analytical workloads. Column projection reads only the
row-group chunks for the requested columns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
## 4. Feather (Arrow IPC) — Zero-Copy Interchange

Feather opens the file by memory-mapping it; the bare [[ML4T_A3_0001]] call returns
almost instantly because no bytes have been read yet. We capture both the
raw open time and the time to actually materialize the columns into memory.
Only the materialized number is comparable across formats.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 5. HDF5 — Legacy Scientific Container

HDF5 keeps a foothold in research codebases that predate Parquet. The
[[ML4T_A3_0001]] format used by [[ML4T_A3_0002]] doesn't support column projection,
so we record the columnar read as the same as the full read for fairness.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 6. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0025-p000

~~~~~~markdown
Memory-mapped reads still need to be materialized before they're useful;
the raw [[ML4T_A3_0001]] handle time below is excluded from the comparison and
listed only so the gap to the materialized Feather read is visible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## 7. Visualisation
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
