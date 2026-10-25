# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/21_storage_benchmark_database.ipynb；A3 Pack 002；單元 14 個。


## 待翻譯英文單元

### c0003-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] selects the panel size; the production setting is the one §2.4
quotes, and CI overrides it to the small scale through Papermill. Every cell that
reports a number also reports the scale that produced it, so a figure lifted off
this page carries its own provenance.

[[ML4T_A3_0002]] is the fraction of the panel the range query should select.
It is a share rather than a fixed number of days because the panel's calendar span
grows with the scale: a fixed seven-day window selects a fifth of the large panel
and *all* of the small one, which would silently turn the range-query panel of the
chart into a second copy of the full scan.

[[ML4T_A3_0003]] is the spread at which a chart panel switches to a logarithmic
x-axis, measured on the bars actually drawn rather than assumed from a past run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
[[ML4T_A3_0001]] reads the scale from the environment when it is imported,
so the variable has to be set before the import rather than passed to a function
afterwards.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0008-p000

~~~~~~markdown
## Check Available Databases
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Which engines are present

DuckDB ships in both the [[ML4T_A3_0001]] (ARM64) and [[ML4T_A3_0002]] (x86) images, and
SQLite comes with Python, so both are always available and the notebook refuses to
continue without DuckDB rather than quietly dropping it. ArcticDB is x86-only and
lives in [[ML4T_A3_0003]]; where it is absent it is reported as absent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The ArcticDB guard below catches [[ML4T_A3_0001]], not [[ML4T_A3_0002]]. An ArcticDB that is
installed but cannot run raises something else entirely - [[ML4T_A3_0003]]
against an unsupported protobuf, for one - and a guard that catches only
[[ML4T_A3_0004]] lets that end the notebook. An optional engine has to be optional in
every way it can fail to be usable, not only in the one way it can be absent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0017-p000

~~~~~~markdown
### kdb+ via PyKX, in IPC mode

The q binary and the licence are looked for *before* PyKX is imported, and the
order is load-bearing. PyKX must never be imported in unlicensed mode
([[ML4T_A3_0001]]). An unlicensed import leaves the process in a state where
later numpy work segfaults, and the crash lands in [[ML4T_A3_0002]], nowhere
near the import that caused it, so it reads as a data bug. Without a licence there
is nothing to benchmark, so PyKX is not imported at all and kdb+ is skipped.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
[[ML4T_A3_0001]] marks an engine as one the chapter compares. [[ML4T_A3_0002]] says it answered
the availability check on this machine. They are different questions, and conflating
them turns a laptop with no Docker running into a run that reports five failures.
The three counts below, and the coverage report at the end, are read off the status
table rather than written as literals, so adding an engine to that table is most of
what adding an engine takes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
## Generate Test Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
### Measuring the row construction that is written out

PostgreSQL, TimescaleDB and InfluxDB reach their servers through interfaces that
take one Python object per row, so building those objects is part of what writing
through them costs and it stays inside the timed write. Because that construction
is a separate expression, it can also be timed on its own, which the helper below
does. What comes back is a lower bound on each of those three clients' share, not
the whole of it: the client still converts and serializes what it is handed, and
so does every client whose interface takes a frame. Nothing here measures that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## Benchmark Windows

Two derived quantities that every engine below reuses, so that all engines answer
the *same* question and can be validated against the same expected row count:

- **Range query**: the leading sessions of the panel, the slice a backtest walks.
  The window is sized as a share of the panel rather than as a fixed number of
  calendar days, because the panel's span is a function of the scale. Seven
  calendar days is a fifth of the large panel but covers the small panel entirely,
  and a range query that selects every row is a full scan wearing a different
  name: the chart would show two panels measuring one query and the reader would
  have no way to tell. Sizing by share keeps the question the same at every scale,
  and the cell below prints the share it actually achieved.
- **Aggregation**: minute bars resampled to **daily** bars. Every engine buckets
  by day; bucketing minute data by minute would be a near-identity for the engines
  that did it and a real reduction for the ones that did not, which is not a
  comparison.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
---
# Part 1: Embedded Databases
---
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0028-p000

~~~~~~markdown
## SQLite (Embedded RDBMS)

SQLite is an embedded relational database:
- ACID compliant, single-file database
- Good for transactional workloads (OLTP)
- Limited analytical query optimization
- No native ASOF join
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
### SQLite Read and Aggregation
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
### SQLite Range Query

SQLite stores the timestamps as ISO-8601 text, which sorts lexicographically,
so the string bounds below use the covering [[ML4T_A3_0001]] index.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>
