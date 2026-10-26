# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/02_nbeats_interpretable.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Time series → 時間序列
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Interpretable Forecasting with N-BEATS

**Docker image**: [[ML4T_A3_0001]]

[[ML4T_A3_0002]] ended on a cost: a network that walks a window one step at a
time pays for the walk and, on that data, bought nothing with it. N-BEATS is the
first of the chapter's answers. It never walks the window. It reads the whole thing
at once through stacked fully connected blocks, and it constrains what each block is
allowed to say, so that the forecast comes out already separated into a slow trend
and a repeating cycle rather than as one opaque number.

The notebook builds the architecture from parts, fits it to SPY closing prices, and
then does two things the architecture invites. It reads the trend and the cycle off
the fitted model separately, which is the payoff for constraining the blocks. And it
scores the forecast against the crudest rule available - repeat today's price - which
is the comparison a flexible architecture has to win before its structure has earned
anything.

**Learning objectives**:
- Build an N-BEATS block: a fully connected stack that emits two vectors, one
  reconstructing its input and one predicting ahead, and understand why subtracting
  the first from the input is what makes a stack of them work.
- Constrain a block's output to a polynomial or to a sum of sine waves, and read the
  resulting forecast as a trend part and a cyclical part you can plot separately.
- Fit the constrained and the unconstrained variants on the same data and say what
  the constraint costs and what it buys.
- Score both against repeating the last price, and measure how far outside its
  training range a trending price series puts the days you are asking about.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Book Reference**: Chapter 13, Section 13.2 (N-BEATS and explicit decomposition).
Based on Oreshkin et al. (2020), *N-BEATS: Neural Basis Expansion Analysis
for Interpretable Time Series Forecasting*.

**Prerequisites**: [[ML4T_A3_0001]]; ETF price data via the [[ML4T_A3_0002]]
canonical loader.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
**Reproducibility.** The fixed seed controls stochastic initialization and
mini-batch order. Strict PyTorch kernels and a fixed cuBLAS workspace make
this training path reproducible on the pinned environment; other PyTorch,
CUDA, or hardware versions can still shift the final decimals.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## Data preparation

N-BEATS forecasts one series at a time, so the notebook uses one: the closing price
of SPY, the exchange-traded fund tracking the S&P 500. Prices rather than returns,
because a trend and a seasonal cycle are properties of a level and mostly vanish when
a series is differenced - and a trend is half of what the interpretable configuration
is built to expose.

That choice has a cost, and the notebook measures it rather than assuming it away.
A network's weights are fitted to inputs on a particular numerical scale, so the
prices are standardised - shifted and divided so the training window has mean zero
and standard deviation one. The shift and the scale are computed on the training
window alone, so the scaling the network sees is a function of data available when
training starts. Statistics taken over the whole series would encode how high prices
eventually went into every input the network reads, including the held-back ones.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### Where the three partitions sit on the standardized scale

The figure below is the one to look at before any result in this notebook. It draws
the standardized price with the three partitions shaded, and marks the highest value
the training window ever reached.

A stationary series would wander across that line in every partition. This one does
not: SPY trends, so the later partitions sit above the earlier one on a scale fitted
to the earlier one. The printed summary gives the ranges. What it says is that the
network is asked to forecast from inputs it has no example of - not unusual inputs,
but values outside the interval it saw at all - and a fully connected network given
an input beyond its training range extrapolates whatever its last layer's slope
happens to be.

This is not a flaw in N-BEATS and it does not go away with a bigger network. It is a
property of standardising a trending level with one shift and one scale for the whole
series. Two standard remedies exist and both appear elsewhere in this chapter:
normalise inside each window instead of globally, which is exactly what N-Linear does
in [[ML4T_A3_0001]], or difference the series into returns, which is what every
other notebook in the chapter forecasts. Keep it in mind when reading the errors
below - and it is the reason the benchmark to beat is a rule that carries the level
forward rather than one that predicts it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
## Building the training examples

One example pairs a [[ML4T_A3_0001]]-day window of standardized prices with the
[[ML4T_A3_0002]] days that follow it. Unlike [[ML4T_A3_0003]], where the target was a
single day, the target here is the whole path: N-BEATS emits [[ML4T_A3_0004]] numbers at
once rather than being applied repeatedly, which is what lets a polynomial or a sine
wave describe the forecast as a shape.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## N-BEATS Block

Each block takes a lookback window as input and produces two outputs:
- **Backcast**: reconstruction of the input (for residual connections)
- **Forecast**: prediction of the future horizon

The interpretable version uses constrained basis functions:
- **Trend stack**: polynomial basis (degree 2-3)
- **Seasonality stack**: Fourier basis

### Basis Expansion Formula

The forecast is generated via basis expansion (Section 13.2):

[[ML4T_A3_0001]]

In the code below:
- [[ML4T_A3_0002]] (from [[ML4T_A3_0003]]) = learned expansion coefficients
- [[ML4T_A3_0004]] / [[ML4T_A3_0005]] = pre-computed basis matrices ([[ML4T_A3_0006]] vectors)
- [[ML4T_A3_0007]] = the weighted sum above

For trend, [[ML4T_A3_0008]] (polynomial); for seasonality,
[[ML4T_A3_0009]] (Fourier harmonics).
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## N-BEATS Model

The full model stacks multiple blocks with **doubly-residual** connections:
each block processes the residual from previous blocks (input minus backcast).
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Training
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>
