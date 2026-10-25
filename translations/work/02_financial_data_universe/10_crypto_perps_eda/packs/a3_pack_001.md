# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/10_crypto_perps_eda.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Cross-sectional → 橫斷面
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto Perps: Exploratory Data Analysis

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Profile the Binance Futures hourly OHLCV dataset for 19 perpetual contracts
alongside the 8-hourly Premium Index that captures the perpetual–spot
basis. The notebook anchors data shape, units, coverage, and OHLC integrity
before the strategy work begins in Chapter 6.

## Learning Objectives

- Load hourly OHLCV and 8-hourly premium index data via the canonical loaders.
- Document premium-index units (decimal, multiply by 100 for percent).
- Quantify cross-frequency join coverage between OHLCV and premium data.
- Run OHLC invariant checks and inspect for time-stamp gaps.

## Book Reference

§2.2, "The asset-class market data landscape" - the digital-asset part of it.

## Prerequisites

- Familiarity with daily OHLCV equity data ([[ML4T_A3_0002]]).
- The Binance Futures parquet at [[ML4T_A3_0003]] (OHLCV + premium).
- Methodology continues in [[ML4T_A3_0004]]; the case-study
  pipeline lives under [[ML4T_A3_0005]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] of zero loads every symbol. CI overrides it to reduce the notebook, so it has
to be passed to the loaders rather than sit beside them unused.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Load and Inspect OHLCV

Hourly OHLCV data from Binance Futures for 19 cryptocurrencies.
Trading is 24/7 (8,760 hours/year vs 252 days for equities).
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## 2. Coverage Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0011-p000

~~~~~~markdown
### Contracts list at different dates

The universe is not fixed: BTC and a handful of majors are present from 2020,
and newer contracts (SUI lists in 2023) switch on later. Counting distinct
symbols per month makes the staggered onboarding explicit, and it is coverage that any
cross-sectional signal has to account for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## 3. Premium Index Data

The premium index measures how far the perpetual is trading from the underlying index. It is
often described as the simple relative difference between the two prices, and that
description is close enough to build intuition on but wrong in a way that matters later:
Binance computes it from the *impact bid and ask* against the price index, with a term that
is zero whenever the index sits between them. The exact definition and its consequence are in
the data-quality section below.

- Positive premium: the perpetual's executable bid sits above the index
- Negative premium: its executable ask sits below the index

Which side pays does not follow from that sign. Funding is the premium passed through a
clamp against a positive interest rate, and the clamp pins a whole band of premiums -
including zero and mildly negative ones - to the interest rate itself, which longs pay.
[[ML4T_A3_0001]] derives the formula and measures how often each case occurs.

### Units

Premium values are stored as **decimals**, not percentages: a value of one thousandth means
a tenth of one percent. Multiply by a hundred before displaying. Nothing in the column name
records the convention, so the printed range below is what settles it - the magnitudes are
only plausible under one reading.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0016-p000

~~~~~~markdown
### The basis is small, until it is not

The premium sits within a fraction of a percent almost all the time, and the printed range
above shows how far the extremes reach. The distribution is not symmetric around that central
mass, and the asymmetry is what the funding strategy in the case study is built on, so it is
worth drawing rather than tabulating.

The axis is clipped so the central mass is legible at all. Unclipped, a single dislocation
sets the range and the observations the strategy actually trades collapse into one bar. The
clip half-width is declared as a parameter rather than typed into the figure, and the
annotation carries the number the clipping hides, so the choice conceals nothing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## 4. Data Quality

These are raw exchange bars, not an adjusted panel, so the OHLC relations here are exact
rather than approximate: the high is a maximum of prices that were printed and the low a
minimum of the same. Nothing has been multiplied by an adjustment ratio, so there is no
arithmetic that could leave a high and a close a bit apart when they are the same price.

[[ML4T_A3_0001]] compares against a relative tolerance, which is what an adjusted
panel needs and what [[ML4T_A3_0002]] shows the reason for. On this file that tolerance has
nothing to forgive, so the cell converts the percentage back into a count of bars: any
breach at all, of any size, would be a defect in the capture rather than a rounding
artifact, and a count of zero says that more plainly than a percentage that rounds to a
hundred.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
### A point mass, and how to tell what makes one

Neither file has a null in it. That is worth exactly as much as the encoding behind it,
because absence recorded as a null is visible to a null check and absence recorded as a
valid-looking number is not. So it is worth looking for the second kind.

The premium index has an obvious candidate. It is a continuous quantity stored to eight
decimal places with a standard deviation around a thousandth, and yet a large share of its
closes are exactly zero - a value that a continuous distribution at that resolution should
essentially never produce.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
One observation in seven sits on a value the rest of the distribution never visits. The
tempting reading is that these are missing values written as zero - a placeholder the schema
accepts, which is why the null count sees nothing.

**That reading is wrong, and the way it goes wrong is the point of this section.** Before
treating a point mass as a data defect, read the definition of the quantity. Binance computes
the premium index as

[[ML4T_A3_0001]]

Both numerator terms are zero whenever the price index lies between the impact bid and the
impact ask. The formula has a **dead zone** exactly the width of the impact spread, and
inside it the output is not approximately zero but exactly zero. A point mass there is
what the definition predicts, and it means "no premium is owed", which is a measurement
rather than the absence of one.

### Distinguishing a dead zone from missing data

Both produce a point mass, so the count cannot separate them. What separates them is what the
rate correlates with. Non-publication is an operational failure and has no reason to sort
itself by market structure. A dead zone whose width is the impact spread has every reason to:
the spread is wide where liquidity is thin, so the zone is easier to sit inside.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>
