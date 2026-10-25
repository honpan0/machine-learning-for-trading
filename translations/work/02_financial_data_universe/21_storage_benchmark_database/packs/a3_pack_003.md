# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/21_storage_benchmark_database.ipynb；A3 Pack 003；單元 14 個。


## 待翻譯英文單元

### c0034-p000

~~~~~~markdown
### SQLite OHLCV Aggregation

[[ML4T_A3_0001]] is the first price of the session and [[ML4T_A3_0002]] the last, ordered by
time — not [[ML4T_A3_0003]] / [[ML4T_A3_0004]], which are a different (and wrong)
statistic. SQLite has no [[ML4T_A3_0005]]/[[ML4T_A3_0006]] aggregate, so the OHLCV reduction
needs window functions. That costs SQLite time relative to the engines with
native [[ML4T_A3_0007]]/[[ML4T_A3_0008]], and that cost is the honest answer to "what does this
aggregation take on SQLite?"
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
## DuckDB (Embedded Analytics)

DuckDB is designed for analytical workloads (OLAP):
- Columnar storage, vectorized execution
- Native ASOF join support (v1.1+)
- Zero-copy reads from Parquet
- Out-of-core processing for data larger than RAM
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0040-p000

~~~~~~markdown
## ArcticDB (Versioned DataFrames)

ArcticDB is designed for versioned time-series storage:
- "Git for DataFrames" - version history, time travel
- Optimized for financial time-series
- LMDB backend (local), S3/Azure (cloud)

ArcticDB answers the read and the aggregation but not the range query. Its
server-side [[ML4T_A3_0001]] filter keys off a datetime *index*, and this panel carries
[[ML4T_A3_0002]] as a column, which is the canonical schema; pushing the filter down
would need a different write layout from the one timed above. So ArcticDB is absent
from the range-query panel rather than being timed on a client-side filter no other
engine pays.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
---
# Part 2: Server Databases (Docker Required)
---
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
## ClickHouse (OLAP Analytics)

ClickHouse excels at:
- Massive aggregations (billions of rows/second)
- Columnar compression (10-15x)
- Native ASOF JOIN
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0049-p000

~~~~~~markdown
## QuestDB (High-Throughput Time-Series)

QuestDB is optimized for:
- Ultra-high ingestion (1M+ rows/second via ILP)
- Time-series specific SQL extensions (SAMPLE BY)
- Native ASOF JOIN
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0050-p000

~~~~~~markdown
QuestDB ingests over ILP, which acknowledges before the rows are queryable. The WAL
commit is therefore polled *inside* the timed region, so QuestDB's write ends where
PostgreSQL's does: when the data can be read back. A fixed sleep outside the timed
call charges QuestDB nothing for durability.

The panel is handed to [[ML4T_A3_0001]] as a block, so QuestDB pays no per-row
Python cost and does not appear in the client-side table.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0053-p000

~~~~~~markdown
## TimescaleDB (PostgreSQL + Time-Series)

TimescaleDB combines PostgreSQL with time-series optimizations:
- Hypertables (automatic partitioning)
- time_bucket() for aggregations
- Full SQL + relational integrity
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0055-p000

~~~~~~markdown
### TimescaleDB write

[[ML4T_A3_0001]] takes a sequence of Python tuples, so the panel has to be turned
into one tuple per row before any of it reaches the server. That construction uses
[[ML4T_A3_0002]], not [[ML4T_A3_0003]]: [[ML4T_A3_0004]] boxes each row as a Series first, which
costs an order of magnitude more to produce tuples that compare equal. The
difference is pandas rather than the database, and it was being charged to this
engine's write bar. The cell below prints what the construction cost on this run.

On size, [[ML4T_A3_0005]] rather than [[ML4T_A3_0006]]: a hypertable's
rows live in child chunks, so the parent relation is empty and
[[ML4T_A3_0007]] reports about 16 kB of catalog overhead instead of data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0059-p000

~~~~~~markdown
## PostgreSQL (Vanilla RDBMS Baseline)

Vanilla PostgreSQL serves as the relational baseline: same SQL surface as
TimescaleDB but without hypertables, compression, or time-series functions.
The comparison isolates what TimescaleDB's time-series extensions buy you
on the same engine.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0061-p000

~~~~~~markdown
### PostgreSQL write

The same [[ML4T_A3_0001]] interface as TimescaleDB, so the same per-row Python
construction, built the same way and measured separately for the same reason.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0066-p000

~~~~~~markdown
## InfluxDB (Time-Series Database)

InfluxDB is a purpose-built time-series database with a tag-based data model
and the Flux query language. We benchmark line-protocol writes via the Python
client, full-bucket Flux reads, and per-minute aggregation via
[[ML4T_A3_0001]] joined back with [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0068-p000

~~~~~~markdown
### InfluxDB write

The line-protocol client takes one [[ML4T_A3_0001]] per row, so InfluxDB pays a per-row
Python cost like PostgreSQL and TimescaleDB, and like theirs it is inside the timed
write and measured separately. The poll to first-queryable is inside the timed
region too, so this write ends at the same event as every other one: the rows are
readable. A fixed sleep outside the timed call would charge InfluxDB nothing for
the acknowledge-early behaviour that makes it fast.
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0072-p000

~~~~~~markdown
Every InfluxDB handle is dropped as soon as it is done with, rather than left to the
interpreter. The client signs out from its destructor, and by the time the
interpreter tears down, the module globals that sign-out needs are already gone: any
surviving handle then becomes a traceback on stderr after the last cell has run.

The aggregation buckets to daily bars with the OHLCV-correct reduction per field
(first, max, min, last, sum), which is what TimescaleDB, QuestDB and PostgreSQL
compute. A single-pass [[ML4T_A3_0001]] across all fields would be both semantically wrong
for open, high, low and volume, and artificially fast against the engines doing the
mixed aggregation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0072-p000>>>
<<<ML4T-ZH-END:c0072-p000>>>
