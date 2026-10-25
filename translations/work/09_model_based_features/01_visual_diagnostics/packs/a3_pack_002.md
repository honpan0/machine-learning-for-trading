# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/01_visual_diagnostics.ipynb；A3 Pack 002；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Clustering → 分群
- Volatility → 波動率
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0014-p000

~~~~~~markdown
The consensus label counts votes: [[ML4T_A3_0001]] when all three tests agree, [[ML4T_A3_0002]] when
two of the three do, and [[ML4T_A3_0003]] when the votes split evenly. The agreement
score is the share of tests voting with the majority, so with three tests it is one
when they are unanimous and two-thirds when one dissents; it cannot fall below
two-thirds, because a majority of three is always at least two.

Where the two tables disagree about a series, they are counting the same votes
differently rather than measuring different things. The joint matrix keeps a
disagreement as a disagreement and hands it back for diagnosis; the consensus label
has no such case and reports whichever way the majority went. The label is the more
convenient of the two and the less informative, so read it alongside the per-test
statistics in the [[ML4T_A3_0004]] table above rather than in place of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
## Autocorrelation: what the past says about the future

The **autocorrelation function** (ACF) at lag [[ML4T_A3_0001]] is the correlation between the series
and itself shifted [[ML4T_A3_0002]] periods back. It answers "if I know the value [[ML4T_A3_0003]] days ago, how
much does that narrow down today's value?" The **partial** autocorrelation function
(PACF) asks the same question with the intervening lags held fixed, which separates a
direct dependence on lag [[ML4T_A3_0004]] from one inherited through lags [[ML4T_A3_0005]] to [[ML4T_A3_0006]].

Three patterns do most of the work when reading a **correlogram**, the pair of plots
together:

- autocorrelations that decay slowly and stay positive for many lags point to a level
  that wanders, which is the unit root the ADF test looks for
- a PACF that drops to zero abruptly after lag [[ML4T_A3_0007]] points to an autoregressive process
  of order [[ML4T_A3_0008]]: the value depends on its own last [[ML4T_A3_0009]] values
- an ACF that drops to zero abruptly after lag [[ML4T_A3_0010]] points to a moving-average process
  of order [[ML4T_A3_0011]]: the value depends on the last [[ML4T_A3_0012]] shocks

The shaded band on each plot is the region within which an autocorrelation is
indistinguishable from zero at the five percent level, so bars inside it carry no
evidence of dependence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
The rolling mean panel says the level of returns does not wander: it stays near zero
throughout, which is what a stationary series looks like. The quantile plot bends away
from the reference line at both ends, meaning the largest observed moves in each
direction are far larger than a normal distribution with this standard deviation would
produce. The ACF and PACF bars sit close to zero at every lag, so no single lag carries
much information about the next return; whether the small values are collectively
distinguishable from zero is what the Ljung-Box test below decides.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0018-p000

~~~~~~markdown
### Order suggestion from the library

[[ML4T_A3_0001]] reads the same ACF and PACF pattern and proposes the ARIMA
order the correlogram implies, which is the starting point [[ML4T_A3_0002]] fits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## Ljung-Box: are the autocorrelations jointly zero?

Reading individual ACF bars against a confidence band tests one lag at a time, and with
forty lags some will cross the band by chance. The **Ljung-Box** test pools the first
[[ML4T_A3_0001]] autocorrelations into a single statistic and tests them jointly, so it answers the
question the correlogram raises without paying for forty separate looks.

Four horizons are tested, chosen to span the intervals a daily strategy would care
about: one week, two weeks, one month and two months of sessions.

The test is then repeated on **squared** returns. Squaring discards the sign and keeps
the magnitude, so autocorrelation in squared returns means large moves are followed by
large moves regardless of direction. That is volatility clustering, and it is the
condition the GARCH models in [[ML4T_A3_0002]] are built to describe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
The two results answer different questions and are worth keeping apart. Rejection on
raw returns says the sign of the next move is not quite independent of the last few;
it says nothing about how large the dependence is, and over a sample this long a
very small autocorrelation is enough to reject. Rejection on squared returns says the
*size* of the next move is predictable from recent sizes, and that dependence is what
a volatility model is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
## Turning the tests into features

Stationarity is not a fixed property of a series, and treating a single test over the
whole sample as settled throws that away. Refitting the same two tests on a window
that moves forward turns each one into a column: a series that passes for years and
then stops is exactly the event a model wants to know about, and the same construction
detects a cointegrating relationship weakening before the spread stops mean-reverting.

[[ML4T_A3_0001]] sets how many sessions each test reads. At 252 it is about one trading
year, which is long enough for both tests to have power and short enough that a
regime lasting a few quarters is visible rather than averaged away. [[ML4T_A3_0002]] sets
how often the tests are refitted: at 5 sessions that is once a trading week, which is
how often a weekly-rebalanced model would refresh the feature.

Each window ends at the session before the timestamp it is recorded under, so the value
stamped on a date is computable from data available on the previous close and can be
used as a feature for that date without look-ahead. The critical values are taken from
each test's own output rather than typed in, because both depend on the sample size and
ADF's also depends on the lag order [[ML4T_A3_0003]] chose.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0026-p000

~~~~~~markdown
## Distribution: what shape are the returns

Stationarity and autocorrelation describe how a series moves through time. The shape of
its distribution at a point in time is a separate question, and it decides different
things: how far into the tail a risk measure has to reach, whether a directional bet is
symmetric, and whether a model that assumes normal errors will understate extremes.

[[ML4T_A3_0001]] reports the first four moments with the **Jarque-Bera** test,
which combines skewness and kurtosis into one test of normality. Note the convention:
**excess** kurtosis is measured against the normal distribution, so a normal has excess
kurtosis of zero and a positive value means more probability in the tails than a normal
with the same standard deviation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
