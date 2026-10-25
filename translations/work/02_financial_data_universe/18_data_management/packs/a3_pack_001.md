# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/18_data_management.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Backtesting → 回測
- Feature → 特徵
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Data Management: From Download to Production Pipeline

**Docker image**: [[ML4T_A3_0001]]

**Chapter 2: The Financial Data Universe**

Previous notebooks fetched and validated data. This notebook shows how to
**manage** it at scale using ml4t-data's production features:

- **DataManager**: Unified entry point for fetching, storing, and updating
- **Universe**: Predefined symbol lists (S&P 500, NASDAQ 100, etc.)
- **HiveStorage**: Partitioned Parquet for fast queries and incremental writes
- **Incremental Updates**: Keep data fresh without re-downloading history
- **CLI**: Command-line interface for scripted workflows

## Learning Objectives

By completing this notebook, you will:
1. Use [[ML4T_A3_0002]] as a single entry point for all data operations
2. Load predefined universes with the [[ML4T_A3_0003]] class
3. Store and query data with Hive-partitioned Parquet
4. Perform incremental updates and detect gaps
5. Use the [[ML4T_A3_0004]] CLI for scripted workflows

## Why This Matters

A one-time download is fine for a tutorial. A trading system needs:
- **Daily updates** that only fetch new data (10x faster than full refresh)
- **Partitioned storage** that supports fast date-range queries
- **Gap detection** to ensure completeness before backtesting
- **Metadata tracking** so you know what you have and when it was updated

> **ml4t-data docs**: See the [Incremental Updates Guide]([[ML4T_A3_0005]])
> and [Storage Guide]([[ML4T_A3_0006]]) for full reference.

**Prerequisites**: ml4t-data installed; live network access for Yahoo Finance.
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

The demo universe, its window and the batch worker count are the three things a CI run
would want to narrow, so they are declared rather than written into the call that uses
them. [[ML4T_A3_0001]] is the value each series is rebased to in the figure below, and it
appears in the axis label as well as the arithmetic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
---

## 1. DataManager: The Unified Entry Point

[[ML4T_A3_0001]] puts provider selection, storage and updates behind one interface. Compare:

[[ML4T_A3_0002]]

The real power shows with batch operations, storage integration, and updates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0006-p000

~~~~~~markdown
### Fetch: Single Symbol
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Batch Fetch: Multiple Symbols

[[ML4T_A3_0001]] fetches multiple symbols in parallel and returns a single
stacked DataFrame — the standard multi-asset format used throughout the book.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
A row count says the call returned something; it does not say what. Rebasing each series to
a common level at the first session makes the frame legible, and colouring by asset class
rather than by ticker makes the point of a multi-asset loader visible: the three equity
lines travel together and the bond and gold lines do not, which is the dispersion a batch
spanning three asset classes exists to capture and a single-asset loader cannot show.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
---

## 2. Universe: Predefined Symbol Lists

Instead of maintaining symbol lists in YAML or hardcoding them, ml4t-data
ships curated universes that stay current with index rebalances.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0015-p000

~~~~~~markdown
A universe feeds straight into [[ML4T_A3_0001]]. The full list is the whole index, which is
more fetching than a demonstration needs, so this takes a slice of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
---

## 3. HiveStorage: Partitioned Parquet

For data you'll query repeatedly, Hive-partitioned Parquet is the storage
layer used throughout ml4t-data. The HiveStorage backend encodes a logical key such as
[[ML4T_A3_0001]] as a filesystem-safe directory name and nests Hive-style year and
month partitions underneath:

[[ML4T_A3_0002]]

**Benefits over flat files**:
- **Partition pruning**: Query "last 30 days" reads 1 file, not all of history
- **Incremental writes**: New data appends without rewriting existing partitions
- **Metadata tracking**: Know when each symbol was last updated
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
### DataManager with Storage
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
### Load and Store

[[ML4T_A3_0001]] fetches from the provider and writes to Hive
partitions in one call. The storage key encodes the asset class, frequency,
and symbol.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
### Query Stored Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0024-p000

~~~~~~markdown
[[ML4T_A3_0001]] walks the on-disk layout rather than reading a manifest, so it
reports what is actually there even if a metadata file is missing or stale.

The read below carries a date range, and only the partitions overlapping that range are
opened. Reading one year out of a two-year archive touches about half the files.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>
