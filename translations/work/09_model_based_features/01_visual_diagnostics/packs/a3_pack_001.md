# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/01_visual_diagnostics.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Visual Diagnostics and Stationarity Testing

**Chapter 9 | Section 9.1**

**Docker image**: [[ML4T_A3_0001]]

Before a series can be modelled it has to be characterised. This notebook works
through the diagnostics that decide what kind of temporal object a price series is:
eyeballing it, testing whether its statistical properties hold still, measuring how
much of today it can predict about tomorrow, and turning those tests into features
that are recomputed as the sample rolls forward.

**Learning objectives**

- Read a four-panel diagnostic view of a price series and say what each panel rules in
  or out: a trend, clustered volatility, or tails heavier than a normal distribution.
- Decide whether a series can be modelled as-is by running two tests whose null
  hypotheses point in opposite directions, and reading them together.
- Measure whether the past of a series predicts its own future, and whether the past
  of its *squared* values predicts the size of future moves.
- Recompute those tests on a moving window so that "is this series well behaved" becomes
  a column that changes over time rather than one answer for the whole sample.

**Book reference**

Chapter 9, Section 9.1 (Diagnostics and stationarity features).

**Prerequisites**

None. This is the starting point for Chapter 9. The transforms that follow from these
diagnostics are in [[ML4T_A3_0002]] and [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## The two series, and why these two

The diagnostics need a series that trends and a series that does not, so that the tests
have something to distinguish. SPY, the exchange-traded fund tracking the S&P 500,
supplies the first: its price drifts upward over two decades, so its average level in
one year says little about its average level in the next. The CBOE volatility index
(VIX) supplies the second: it measures the option market's expectation of near-term
volatility, spikes in a crisis, and comes back to a level in the teens afterwards, so
its long-run average is a number a model can use.

[[ML4T_A3_0001]] and [[ML4T_A3_0002]] bound the sessions every test in this notebook may read.
The ETF panel's SPY history opens in 2006, so the requested start binds only the VIX
series and the two are tested on different samples. The table below gives each series
its own span, and each test result carries the observation count it was computed from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## Four panels before any test

Every formal test below answers a question that these four panels have already raised.
The price panel shows whether the level wanders; the return panel shows whether large
moves arrive in bursts rather than independently; the VIX panel shows a series that
repeatedly returns to the same neighbourhood; the histogram shows how far the return
distribution departs from the bell curve drawn by a normal distribution with the same
mean and standard deviation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## Stationarity: two tests, opposite nulls

A series is **stationary** when its statistical properties do not depend on where in
the sample you look: the mean, the variance and the autocorrelations are the same in
the first half as in the second. A model fitted on one period only carries over to
another if this holds, which is why it is the first thing to test.

The specific failure to look for in a price series is a **unit root**: today's value is
yesterday's value plus a shock that never decays, so the level has no long-run average
to return to and shocks accumulate forever. A random walk is the canonical example.

Two tests are used together because each has a different null hypothesis, and a test
only ever gives evidence against its null:

| Test | Null hypothesis | Rejecting it means |
|:--|:--|:--|
| Augmented Dickey-Fuller (ADF) | the series has a unit root | there is no unit root |
| Kwiatkowski-Phillips-Schmidt-Shin (KPSS) | the series is stationary around a constant level | the level is not constant |

Reading them jointly resolves the cases that either one alone leaves open:

| ADF | KPSS | Reading |
|:--|:--|:--|
| rejects | does not reject | stationary; both tests agree |
| does not reject | rejects | a unit root; both tests agree |
| rejects | rejects | the two disagree; diagnose before transforming |
| does not reject | does not reject | the sample does not settle it |

Both tests are read at the conventional five percent level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0009-p001

~~~~~~markdown

The third row is the one that needs care. Both tests here are run with a constant and
no trend term, so a double rejection is not by itself evidence of a trend; it says the
two tests are pointing in opposite directions, and three things produce that. The
series may be stationary around a deterministic trend that neither specification
includes, in which case refitting both with a trend term settles it. It may contain a
structural break, which shifts the level without any trend and which [[ML4T_A3_0001]]
locates. Or the sample may simply be one where both tests are inaccurate at their
nominal size, which happens when the series is strongly persistent without having a
unit root. Diagnose which before transforming anything.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p001>>>
<<<ML4T-ZH-END:c0009-p001>>>

### c0011-p000

~~~~~~markdown
Two things about this table are properties of the tests rather than of these series,
and both matter every time you read one.

The KPSS p-value is interpolated from a published table whose ends are one percent and
ten percent, so a statistic beyond either end returns the boundary value. A KPSS
p-value printed as exactly one percent means "at most one percent" and one printed as
exactly ten percent means "at least ten percent"; neither is a measurement of how far
past the boundary the statistic went.

[[ML4T_A3_0001]] is not the length of the series. ADF regresses the differenced series on its own
lags, and [[ML4T_A3_0002]] picks how many, so each lag costs one observation and the
count reported is what the regression had left.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
### The same decision from the library

Doing this by hand once is worth it: the decision matrix above is the whole content of
the test, and reading it off a table is how you learn what the two tests each rule out.
From here on, [[ML4T_A3_0001]] does the same job in one call. It adds the
Phillips-Perron test, which shares the ADF null of a unit root but corrects for
autocorrelation and heteroscedasticity in the residuals differently, and it summarises
the three as a consensus label with an agreement score.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>
