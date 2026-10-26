# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/14_panel_features.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Trading signal → 交易訊號
- Feature → 特徵
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Panel Features

**Chapter 9 | Section 9.6**

**Docker image**: [[ML4T_A3_0001]]

Every feature so far has been computed from one series. This notebook computes features that
need two or more, and they come in two shapes that have almost nothing to do with each other
beyond both requiring a panel.

A **pairwise** feature reads two price series and asks whether a combination of them is
stationary when neither is. That is the cointegration question, and its output is a spread, a
hedge ratio, and a speed of reversion.

A **cross-sectional** feature reads one quantity across many assets on the same date and
replaces its level with its position among them. An annualized volatility of a quarter means
one thing for a Treasury fund and another for an energy fund, and a rank says which of the
two a reader is looking at without needing to know.

**Learning objectives**

- Test a pair for cointegration two ways and read what it means when the two disagree.
- Estimate a hedge ratio that changes over time with a Kalman filter, and see where it
  differs from the single number a full-sample regression gives.
- Estimate a mean-reversion half-life on a first block and use it to size the window a
  trading signal is computed over, so the window length is not chosen with future data.
- Convert a temporal feature into a cross-sectional rank and a benchmark-relative value, and
  say which of the two a downstream model wants.
- Aggregate a per-asset regime measure across a universe without ranking each asset against
  its own future.

**Book reference**

Chapter 9, Section 9.6 (Cross-sectional and panel features).

**Prerequisites**

[[ML4T_A3_0002]] for the recursion the hedge ratio uses. [[ML4T_A3_0003]] for the regime
measures the last section aggregates.
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
## The universe

The ETF universe, because a pair needs two series whose relationship has a reason behind it
and exchange-traded funds come with the reason written on them. The pair used through the
first half is an energy sector fund against a crude oil fund, and the fallback pair for a
reduced fixture is two broad equity funds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## Two tests for one question

Two price series are **cointegrated** when some fixed combination of them is stationary even
though neither of them is. That is a stronger statement than correlation and a different one:
two series can move together every day and drift apart without limit over years, and it is
the drift that decides whether a spread between them comes back.

The two standard tests reach the question differently. **Engle-Granger** regresses one series
on the other and tests the residual for a unit root, so it takes one of the two as the
dependent variable and gives a different answer if the roles are swapped. **Johansen** treats
the pair as a system and tests how many stationary combinations exist, which is symmetric in
the two series and extends past two of them.

Both are run on the whole sample here, and that is the correct thing for what they are being
used for. Whether a pair is worth trading is a question asked before any trading, out of the
history available at that point; the answer is not a feature and does not enter a design
matrix. What must not use the whole sample is anything the signal below reads.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
This pair is the lesson rather than the demonstration. An energy sector fund and a crude oil
fund are related by something a reader can state in a sentence, and neither test calls them
cointegrated over this sample. The reason is visible in the funds: one holds equity in companies
whose earnings depend on the oil price, the other holds futures and pays to roll them, and a
roll cost accumulates as a drift that no fixed combination removes.

The implied hedge ratio printed above is a good place to see what a rejected test means. It is
far from the regression's, and on a pair where no stationary combination is found the leading
eigenvector is not estimating one: it is the least badly behaved direction in a system that has
no well behaved one, and its ratio is not a number to hold a position on.

The mechanics below are worth working through anyway, because every step still computes and
every step's output says something about a pair that fails.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
## Two hedge ratios

The spread needs a ratio: how many units of one series to hold against one unit of the other.
A regression over the whole sample gives one number and a filter gives a series, and the
difference between them is not a matter of preference.

The regression is fitted on everything, which makes its ratio unavailable at every date
except the last. It is reported because it is the number the cointegration test used, and its
spread is what the stationarity test below is run on.

The **Kalman filter** treats the intercept and the ratio as a two-dimensional state following
a random walk and updates it one session at a time. Its estimate at session [[ML4T_A3_0001]] has seen
sessions up to [[ML4T_A3_0002]] and no more, which is what a hedge ratio has to be if a position is taken
on it. The two parameters that decide its behavior are the measurement noise and the process
noise, and their ratio is the whole tuning: a larger process noise lets the ratio move faster
and tracks a genuine structural change sooner, at the cost of chasing noise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## How fast the spread comes back

Fit an autoregression of order one to the spread and the coefficient says what fraction of a
deviation is still there one session later. Written as a change,

[[ML4T_A3_0001]]

a negative [[ML4T_A3_0002]] means the spread is pulled back toward its level, and the **half-life** is
the number of sessions over which half of a deviation is expected to have gone:
[[ML4T_A3_0003]]. A non-negative [[ML4T_A3_0004]] says the spread is not being pulled anywhere
and there is no half-life to report.

The half-life is used below to choose the window the trading signal's mean and standard
deviation are computed over, which is why it is estimated on the first [[ML4T_A3_0005]] of the
sample only. A window length chosen from the whole sample is a small leak and an easy one to
miss, because a length does not look like a parameter.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
The two half-lives differ, and the gap between them is how far the window length would have
moved. Neither is more correct as an estimate. The first is the only one available at the
moment the window has to be chosen.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
