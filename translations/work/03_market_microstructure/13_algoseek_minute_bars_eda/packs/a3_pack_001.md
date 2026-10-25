# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/13_algoseek_minute_bars_eda.ipynb；A3 Pack 001；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構
- Feature → 特徵
- Feature engineering → 特徵工程

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# NASDAQ-100 Minute Bars - Exploratory Data Analysis

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

This notebook provides a comprehensive exploration of the AlgoSeek TAQ minute bar dataset.
Unlike simple OHLCV data, TAQ bars contain 61 pre-computed columns that capture the
full microstructure of each trading minute: quote dynamics, trade execution, aggressor
behavior, and liquidity conditions.

## Learning Objectives

After completing this notebook, you will be able to:
- Load and validate TAQ minute bars using the canonical loader
- Understand the schema: quote-derived vs trade-derived columns
- Interpret null patterns (bars with no trades are normal, not errors)
- Analyze trade bucket fields to measure aggressor behavior
- Interpret pressure and tick direction indicators
- Distinguish exchange volume from off-exchange (FINRA) activity
- Connect spread dynamics to liquidity conditions

## Dataset Overview

| Attribute | Value |
|-----------|-------|
| **Source** | AlgoSeek TAQ Minute Bars |
| **Coverage** | NASDAQ-100 constituents |
| **Period** | 2020-2021 |
| **Frequency** | 1-minute bars (continuous, 04:00-20:00 ET) |
| **Columns** | 61 pre-computed microstructure fields |

## Book reference

Section §3.2, *The Anatomy of Modern Market Data Feeds* — AlgoSeek
minute-bars bullet (61 pre-computed microstructure columns serving as
input for Chapter 7 feature engineering).

## Prerequisites

- AlgoSeek TAQ minute bars under
  [[ML4T_A3_0002]] (Hive
  partitioned). Loaded via [[ML4T_A3_0003]].
- Companion: [[ML4T_A3_0004]] for the underlying tick-level stream
  these bars summarize.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Load and Inspect

The NASDAQ-100 minute bars are stored in Hive-partitioned Parquet files:
[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
The load is bounded to one year of a handful of symbols. The full dataset is two years
of a hundred names at minute frequency with sixty-one columns, which is tens of
millions of rows and more than a laptop holds; the point of this notebook is the
schema and the shape of each field, and neither needs the whole panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### Schema Overview

TAQ minute bars contain 61 columns organized into distinct families based on
the underlying market mechanism they measure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Column Families

The 61 columns can be grouped into 7 families based on what they measure:

| Family | Columns | What They Measure |
|--------|---------|-------------------|
| **Identifiers** | date, symbol, time, timestamp | Row keys |
| **Quote OHLC** | open/high/low/close_bid/ask_price/size/time | NBBO dynamics |
| **Trade OHLC** | first/high/low/last_trade_price/size/time | Actual executions |
| **Spread** | min_spread, max_spread | Bid-ask spread range |
| **Volume** | volume, finra_volume, total_trades | Exchange vs off-exchange |
| **Trade Buckets** | trade_at_bid/mid/ask, trade_at_cross | Aggressor direction |
| **Pressure** | trade_to_mid_vol_weight, uptick/downtick_volume | Directional intensity |
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0014-p000

~~~~~~markdown
## 2. Coverage Summary

TAQ minute bars are **continuous**: a row exists for every minute from 04:00 ET
to 20:00 ET, even when no trades occur. This is different from tick data where
rows only exist when events happen.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
These bars cover extended hours, not just the regular session: pre-market from 04:00,
regular trading from 09:30 to 16:00, and post-market to 20:00, all Eastern. The three
behave differently enough that any statistic computed across all of them is a blend of
three regimes, so the first thing to look at is how the bars divide between them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 3. Null Patterns: Semantic, Not Errors

TAQ minute bars have two types of columns with different null semantics:

| Column Type | When Null | Meaning |
|-------------|-----------|---------|
| **Quote fields** | Rarely | No quote activity (very rare) |
| **Trade fields** | Frequently | No trades in this minute bar |

Null trade fields are NOT missing data - they correctly indicate "no trading
activity in this minute." This is common in extended hours and for illiquid names.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
The share of bars with no trade is a session fingerprint: extended-hours bars are
mostly empty, while regular-hours bars almost always trade.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## 4. Data Quality: OHLC Invariants

Trade OHLC must satisfy invariants: High ≥ Low, High ≥ Open/Close, Low ≤ Open/Close.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 5. Quote OHLC: NBBO Dynamics

Quote fields capture the National Best Bid and Offer (NBBO) at key moments:

| Field Pattern | Meaning |
|--------------|---------|
| [[ML4T_A3_0001]] | NBBO at bar start (carried forward if no change) |
| [[ML4T_A3_0002]] | Highest bid/ask during the bar |
| [[ML4T_A3_0003]] | Lowest bid/ask during the bar |
| [[ML4T_A3_0004]] | NBBO at bar end |

Quote fields are **never null** because NBBO is always defined (carried forward).
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0029-p000

~~~~~~markdown
The spread distribution is heavy-tailed, so an ECDF reads better than a histogram:
most bars sit at a few basis points, with a long tail from illiquid extended-hours bars.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
## 6. Trade OHLC: Actual Executions

Trade fields capture actual executed trades, which may differ from quotes:

| Field | Meaning |
|-------|---------|
| [[ML4T_A3_0001]] | First trade of the minute |
| [[ML4T_A3_0002]] | Trade at highest price |
| [[ML4T_A3_0003]] | Trade at lowest price |
| [[ML4T_A3_0004]] | Final trade of the minute |

Trade fields are **null when no trades occur** in the bar (common in extended hours).
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>
