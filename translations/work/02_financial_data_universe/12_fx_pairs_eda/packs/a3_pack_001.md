# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/12_fx_pairs_eda.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# FX Pairs: Exploratory Data Analysis

**Docker image**: [[ML4T_A3_0001]]

## Purpose
Profile the OANDA 20-pair, 4-hour FX dataset that anchors the FX case study. FX is OTC:
there is no central tape, so quotes and reported volumes are venue-specific, and the trading
day is a convention rather than an event. The notebook surveys coverage, quote conventions,
OHLC integrity, the gap structure of a 24/5 calendar, and the daily aggregation downstream
chapters use.

## Learning Objectives
- Load and inspect the 4-hour OHLC and indicative-volume panel for 20 pairs.
- Distinguish direct (USD-quoted), indirect (USD-base) and cross pairs.
- Read FX volume as an OANDA indicator rather than an authoritative tape.
- Recover the session grid the file is stamped on, and aggregate to daily bars on it.

## Book reference
Chapter 2, §2.2 (asset-class market data, foreign exchange). The FX case study built on this
dataset lives in [[ML4T_A3_0002]].

## Prerequisites
- OANDA 4h FX parquet files materialized under [[ML4T_A3_0003]].
- Loader [[ML4T_A3_0004]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] and [[ML4T_A3_0002]] are the two that carry an argument rather than
a preference. Section 5 shows that this file's bars are stamped on a grid anchored to 5PM in
New York, which is the rollover the interbank market treats as the start of a new value date,
and the daily aggregation is built on that boundary rather than on UTC midnight. Both are
declared here so the whole convention is visible in one place and CI can override it.

[[ML4T_A3_0003]] passes straight to the loader, so a CI run can narrow the universe without any
cell downstream knowing the difference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Load and Inspect
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
### The volume column is not traded volume

FX is an OTC market with no consolidated tape, so nothing in this file can report what a
currency traded. What the column does report is narrower than that and worth naming
exactly: [[ML4T_A3_0001]] records it as **tick volume**, a count of how many times the
venue updated its quote inside the bar. It is a count of updates, not a sum of sizes.

That makes it useless for anything sized in currency and still informative about activity,
because a venue reprices when something moves. Section 2 shows how far the two come apart.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Symbol normalization

The file writes pairs with an underscore ([[ML4T_A3_0001]]). The canonical form used everywhere
downstream is concatenated ([[ML4T_A3_0002]]), so the join keys line up.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 2. Coverage Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### The ranking is a ranking of quote updates

Ranking pairs by average tick volume puts the global majors well down the table, and the
next cell prints exactly where they land rather than leaving that as an impression.

It is tempting to read this as a liquidity ranking and it is not one. The column counts one
venue's quote updates, so the ordering reflects how often that venue repriced each pair,
and a pair can be repriced often for reasons that have nothing to do with how much of it
trades anywhere. What this file supports is the negative claim, which is the useful one: a
ranking built from this column is not a ranking of market size, and the majors sitting mid
table is the proof. Explaining *why* the ordering comes out as it does would need trade
data this file does not carry.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 3. Quote Conventions

FX pairs follow a **BASE/QUOTE** convention: the price is the number of QUOTE units that buy
one unit of BASE. EURUSD is dollars per euro, so it falls when the dollar strengthens. USDJPY
is yen per dollar, so it rises when the dollar strengthens. EURGBP names no dollar at all.

The direction of the dollar therefore depends on where the dollar sits in the symbol, and any
composite built across pairs has to invert one group before averaging. Rather than hand-label
a subset, classify every pair by rule: *Direct* if USD is the quote currency, *Indirect* if
USD is the base, *Cross* if USD does not appear.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## 4. Data Quality

### A percentage cannot show you one bad bar

[[ML4T_A3_0001]] reports the share of rows satisfying each invariant. On a panel this
size a single violation moves that share by less than the display rounds away, so a column
of hundreds is consistent with a clean file and with a handful of broken bars. The count is
printed beside it, because a count of zero is a different statement from a percentage that
rounds to a hundred.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### The gap between bars is the calendar

FX trades continuously from Sunday evening to Friday evening, so the interval between
consecutive bars is not always the bar length. The check runs over every pair rather than a
reference one: a gap is a property of the file, and picking the most liquid pair to test it
on samples the row least likely to show it.

Three cases are separated rather than two. A step of exactly one bar length is the ordinary
case. A Friday-to-Sunday step is the weekend close, which is the calendar working as intended
and not a hole. Everything else is neither, and the next cell shows what those turn out to be.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
The third group is the holiday calendar. Christmas Eve and New Year's Eve dominate it, each
recurring across most years of the sample, and the days around them fill in much of the rest.

The distinction that matters is between a closure and a fault, and the pair count makes it.
Roughly half these dates take the entire universe out at once, and because those are the
recurring ones they carry the large majority of the steps. A download failure would have to
knock out twenty independently quoted instruments simultaneously and pick December 24th to
do it on. The remaining dates hit a subset of pairs and are the residue worth treating as
possible faults, which is a far smaller thing to investigate than every long gap in the file.

This is why "weekends only" is the wrong summary even though it is nearly right by count. The
leftover is small, systematic, and predictable from a calendar, and a pipeline that treats
every long gap as a weekend will read the year-end holidays as missing data every year.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
## 5. The Session Grid, and Daily Aggregation On It

Aggregating to daily bars needs a day boundary, and the obvious one is UTC midnight. Before
taking it, it is worth asking what grid the timestamps are already on, because the file
answers that question directly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>
