# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/04_maximum_favorable_adverse_excursion.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Maximum Favorable/Adverse Excursion (MFE/MAE) Analysis

**Docker image**: [[ML4T_A3_0001]]

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.2 - Label Engineering

## Purpose

This notebook provides **empirical justification** for triple-barrier parameter
choices. Rather than picking arbitrary barrier widths, we analyze actual price
excursions to determine appropriate thresholds.

## Key Questions Answered

1. How far do prices typically move in our favor before reversing?
2. How far do prices move against us before recovering?
3. How do these distributions differ by asset class and volatility regime?
4. What barrier widths capture meaningful price moves without excessive stops?

## MFE/MAE Definitions

Maximum Favorable Excursion (MFE) and Maximum Adverse Excursion (MAE) were
introduced by John Sweeney in *Campaign Trading* (1996) to analyze trade
management. For a **long** entry at time [[ML4T_A3_0002]] with holding period [[ML4T_A3_0003]]:

[[ML4T_A3_0004]]

[[ML4T_A3_0005]]

**Note**: Both MFE and MAE are non-negative by definition. For **short** positions,
the definitions reverse: MFE uses lows (favorable moves down) and MAE uses highs
(adverse moves up).

The window opens at [[ML4T_A3_0006]]. The entry fills at bar [[ML4T_A3_0007]]'s close, so bar [[ML4T_A3_0008]]'s own
high and low have already happened: counting them measures movement the position
was never exposed to, and stretches an [[ML4T_A3_0009]]-bar holding period over [[ML4T_A3_0010]] bars.
Both excursions are inflated, and unevenly, since where the close sits inside bar
[[ML4T_A3_0011]]'s range decides which side gains more.

## Data Coverage
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- **ETF Universe** (daily): SPY as representative equity exposure
- **Crypto Premium** (hourly): BTC for high-volatility comparison
- **CME Futures** (daily): ES for institutional context

## Prerequisites

- [[ML4T_A3_0001]] - defines the triple-barrier label whose parameters
  this notebook empirically justifies.
- Familiarity with OHLCV bar data and ATR (true range with Wilder smoothing).
- Polars [[ML4T_A3_0002]] / [[ML4T_A3_0003]] and forward-shifted columns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## Vectorized MFE/MAE Computation

We use Polars' [[ML4T_A3_0001]] and [[ML4T_A3_0002]] functions to compute
forward-looking extremes without Python loops. This approach builds [[ML4T_A3_0003]] shifted
columns - shifts [[ML4T_A3_0004]] through [[ML4T_A3_0005]], so the entry bar is excluded - resulting in
[[ML4T_A3_0006]] work and memory. While vectorized (no Python loops), memory scales
with horizon. For very large horizons the equivalent reverse-rolling form is
[[ML4T_A3_0007]]; note the [[ML4T_A3_0008]], without
which the window reopens at bar [[ML4T_A3_0009]] and reintroduces the pre-entry extremes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## ATR Computation

**True Range** (accounts for gaps) with Wilder's smoothing:

[[ML4T_A3_0001]]

[[ML4T_A3_0002]]

The Wilder smoothing is equivalent to an EMA with [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
### Library ATR: ml4t-engineer

The manual [[ML4T_A3_0001]] above teaches Wilder's smoothing. [[ML4T_A3_0002]]
provides the same algorithm with edge-case handling and panel data support -
a modern Python alternative to TA-Lib's [[ML4T_A3_0003]] function.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0010-p000

~~~~~~markdown
## ETF Analysis (Daily)

We start with SPY as the representative low-volatility daily asset.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### MFE/MAE computation over the ETF horizon
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### ATR comparison: manual vs library

The conventional "TP=2xATR, SL=1xATR" is printed below **for comparison only** and is
deliberately not a recommendation. Read it against what the recommendations table
derives from the measured excursions, where the stop this panel supports is over three
times ATR rather than one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### ETF MFE/MAE Distribution
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
The two panels share their x and y ranges. The point of the figure is a comparison
between them, and panels on independent axes cannot support one: plotly's default fits
each histogram to its own extent, so the narrower distribution is drawn as wide as the
broader one. The shared limit is the [[ML4T_A3_0001]] quantile of whichever series runs
further, which keeps the bulk legible without letting a handful of crisis observations
set the scale.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
The two shapes differ in a way the medians only half describe. The typical favorable
move is the larger one: SPY's median MFE runs above its median MAE, printed above. But
the adverse panel is the more concentrated near zero *and* carries the heavier tail, so
the ordering reverses further out - the p90 adverse excursion exceeds the p90 favorable
one. A take-profit set from the MFE distribution and a stop set from the MAE
distribution therefore do not keep a fixed ratio as the percentile moves, which is why
the recommendations table reports both at more than one quantile rather than a single
reward-to-risk number.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
## Crypto Analysis (Hourly)

Crypto exhibits higher volatility, requiring wider barriers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
### Crypto MFE/MAE Distribution
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
Each panel gets a reference line at its own 75th percentile. That line used to sit at a
flat two percent "from typical crypto settings" - a round number asserted as typical, in
the notebook whose argument is that barrier widths should be measured rather than
assumed.
The measured p75 is what the rest of the notebook calibrates against, and drawing each
panel's own value is what makes the symmetry between them checkable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>
