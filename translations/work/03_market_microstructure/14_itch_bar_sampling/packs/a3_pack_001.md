# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/14_itch_bar_sampling.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Information-Driven Bars: Beyond Time Sampling

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Build the four bar families §3.4 walks through (time, tick, volume, dollar
plus imbalance/run information bars) from a single AAPL ITCH trading day,
compare their statistical properties (normality, autocorrelation), and
generate the sampling-comparison panel.

## Learning Objectives

After completing this notebook, you will be able to:
- Construct tick, volume, dollar, and imbalance bars from raw trades using
  [[ML4T_A3_0002]] (vectorized polars + numba).
- Quantify the gain in normality (lower JB stat, lower kurtosis) when moving
  from time bars to volume/dollar bars.
- Apply Lee-Ready aggressor-side classification on ITCH (which lacks the
  aggressor field) and contrast tick-test vs midpoint-based imbalance bars.

## Book reference

Section §3.4, *The Art of Sampling: From Ticks to Bars* — this notebook builds
the sampling comparison that section discusses from a single AAPL ITCH day.

## Prerequisites

- Parsed ITCH [[ML4T_A3_0003]]/[[ML4T_A3_0004]]/[[ML4T_A3_0005]]/[[ML4T_A3_0006]]/[[ML4T_A3_0007]]/[[ML4T_A3_0008]]/[[ML4T_A3_0009]]/[[ML4T_A3_0010]] parquets at the canonical
  loader path (output of [[ML4T_A3_0011]]). The Lee-Ready section
  reconstructs the LOB on the fly from these messages.

---
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0006-p000

~~~~~~markdown
## 1. Load Trade Data from ITCH

We use trade messages (type 'P') from ITCH data. These represent actual
executions on the exchange, providing the raw tick stream for bar construction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
**Note**: [[ML4T_A3_0001]] is imported from the chapter-local
[[ML4T_A3_0002]] module, which shares the LOB reconstruction logic used in
[[ML4T_A3_0003]] — consistent order-pool tracking and proper
handling of Replace (U) chains.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
### Load trades and classify aggressor side

We initialise the bar variables to [[ML4T_A3_0001]] so downstream cells degrade
gracefully if the ITCH data is unavailable, then load the tick-test-classified
trade stream for [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
Bars are cut over regular trading hours only. ITCH timestamps are nanoseconds since
midnight on the exchange's own clock and carry no timezone, so the window below is
already in exchange-local time and needs no conversion - which also means these
timestamps must not be treated as UTC anywhere downstream.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## 2. Create All Bar Types Using ml4t.engineer

The [[ML4T_A3_0001]] module provides vectorized bar construction:
- **TickBarSampler**: Fixed number of trades per bar
- **VolumeBarSampler**: Fixed total volume per bar
- **DollarBarSampler**: Fixed dollar volume per bar
- **FixedTickImbalanceBarSampler**: Bars close when the signed tick imbalance
  exceeds a fixed threshold (stable; avoids the adaptive feedback loop)
- **TickRunBarSampler**: Bars close when a "run" of same-side trades exceeds expected length

The imbalance and run families are signed: they need a buyer/seller label per
trade. Here that label is the **tick test** computed at load time (§1); §7
rebuilds the imbalance family with the more accurate Lee-Ready quote-midpoint
classifier and contrasts the two.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Imbalance bars close on a fixed signed-tick threshold

A tick-imbalance bar closes when the cumulative signed order flow crosses a
threshold:

[[ML4T_A3_0001]]

We use a **fixed** threshold [[ML4T_A3_0002]] rather than the adaptive
[[ML4T_A3_0003]] target. The adaptive form
feeds back on its own bar lengths and threshold-spirals on persistently
one-sided flow — the instability §3.4 warns about — so the library recommends
the fixed sampler for production. Signed bars also need genuine two-sided flow:
an all-one-side stream (the raw ITCH [[ML4T_A3_0004]] before tick-test
classification) makes [[ML4T_A3_0005]] monotonic and degenerates the bars into tick
bars, so we require both directions to be present.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### Run bars close when one side sustains a directional run

A tick-run bar tracks the longer of the cumulative buy/sell run,
[[ML4T_A3_0001]], and closes when it
exceeds the expected run length. Bars form when one side dominates, flagging
sustained directional flow. A small EWMA decay keeps the adaptive expected-run
threshold stable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 3. Compare Statistical Properties

We compare key properties that affect ML model performance:
- **Return distribution**: Closer to normal is better
- **Autocorrelation**: Lower is better (more IID)
- **Heteroskedasticity**: More stable variance is better
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
The reference table above carries the full set of moments; the headline is
**excess kurtosis** (0 for a normal distribution — higher means fatter tails).
The chart below reads it directly.

| Metric | Meaning | Better value |
|--------|---------|--------------|
| JB stat | Distance from normality | Lower |
| Autocorr (lag 1) | Serial dependence | Closer to 0 |
| Kurtosis | Excess kurtosis, fat tails (0 = normal) | Lower |
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
### Volume and dollar bars trim the fat tails that time bars leave in

Sampling on activity rather than the clock pulls return kurtosis toward the
Gaussian benchmark. The bar below sorts each family by excess kurtosis; the
dashed line marks the normal reference of 0.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## 4. Visualize Return Distributions
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## 5. Bar Duration Analysis

Information-driven bars have variable duration - they are faster during
high activity periods and slower during quiet periods.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
