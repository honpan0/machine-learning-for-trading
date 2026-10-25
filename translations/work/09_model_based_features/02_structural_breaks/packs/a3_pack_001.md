# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/02_structural_breaks.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Structural Break Detection

**Chapter 9 | Section 9.1**

**Docker image**: [[ML4T_A3_0001]]

A **structural break** is a date after which the process generating a series is not the
one that generated it before: the average level moves, the size of a typical move
changes, or the way one observation depends on the last changes. Every model fitted on
the earlier period is describing something that has stopped happening, which is why
locating breaks is worth doing before fitting anything and worth monitoring afterwards.

This notebook covers three ways of getting at them, in increasing generality: a test
that allows exactly one break, a segmentation that finds several, and a classifier that
learns what a break looks like from a set of statistics comparing the period before a
candidate date with the period after it.

**Learning objectives**

- Test for a break in a price series with a test that estimates the break date rather
  than requiring you to name it in advance.
- Split a long series into segments whose average level is stable inside each segment,
  and read the dates the split produces.
- Turn a detected break into a column a model can read on a given date without using
  anything that happened after it.
- Monitor for a break as new observations arrive, using a statistic that accumulates
  evidence and one that looks only at a recent window, and say what each is good for.
- Build the statistics that compare two adjacent windows - their averages, their
  spreads, their whole distributions, and their dependence - and combine them into a
  single detector.

**Book reference**

Chapter 9, Section 9.1 (Diagnostics and stationarity features).

**Prerequisites**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

[[ML4T_A3_0001]] for stationarity testing and the ADF test. Familiarity with
hypothesis testing and with reading a p-value.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## The series

SPY, the exchange-traded fund tracking the S&P 500, is the working example: two decades
of daily closes containing two episodes nobody disputes were breaks, the 2008 credit
crisis and the March 2020 shutdown, and a great deal of ordinary market that was not.
A detector worth having separates those.

[[ML4T_A3_0001]] and [[ML4T_A3_0002]] bound the sessions every method here may read. The ETF
panel's SPY history opens in 2006, so the requested start binds nothing and the sample
is what the panel holds.

Returns are **log returns**, the difference of the logged close, scaled to percent.
Logs make the return over several days the sum of the daily returns, which is the
property the cumulative statistics later in the notebook rely on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
# Part 1: finding breaks in a price series
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0008-p000

~~~~~~markdown
## One break, with its date estimated: Zivot-Andrews

The ADF test asks whether a series has a unit root under the assumption that one
process generated the whole sample. If the sample contains a break, that assumption is
wrong in a specific direction: a stationary series whose mean jumps once looks, to a
test that cannot see the jump, exactly like a series that wanders. The ADF test then
fails to reject a unit root that is not there.

The **Zivot-Andrews** test removes the assumption. It fits the ADF regression once for
every candidate break date, allowing the intercept and the trend to change at that
date, and reports the date whose fit is most hostile to the unit root. Its null
hypothesis is a unit root with no break; rejecting it says the series is stationary
around a level and trend that shift once.

Three settings decide what the test can find. [[ML4T_A3_0001]] allows both the level and
the slope to shift at the break, which is the general case for a price series.
[[ML4T_A3_0002]] refuses candidate dates in the first and last fraction of the sample it is
given, here fifteen percent at each end, because a break estimated from a handful of
observations is not estimated at all. [[ML4T_A3_0003]] is the number of lagged differences in the regression: enough to
absorb short-run dynamics at daily frequency without spending the sample on them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
The test carries the same caution as any single-break test. Failing to reject leaves
two possibilities open that it cannot distinguish: the series has a unit root, or it
has more than one break and no single shift describes it. The next section allows
several.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
## Several breaks: segmenting the series

**Segmentation** takes a different route. Rather than testing a hypothesis it partitions
the series into consecutive segments, choosing the split points that minimise the total
within-segment cost. With a squared-error cost the fitted value inside each segment is
its mean, so the algorithm is looking for the places where the average level moves.

Two algorithms in [[ML4T_A3_0001]] implement this, and the difference between them is what
you have to supply:

- **PELT** is given a penalty per additional break and returns however many breaks pay
  for themselves. The penalty here is the log of the sample size times the variance of
  the series, which is the shape of the Bayesian information criterion: the variance
  puts the penalty in the units of the cost being minimised, and the log makes the
  price of a break grow slowly with the sample.
- **Binary segmentation** is given the number of breaks and splits recursively, taking
  the split that reduces the cost most, then splitting each part the same way.

[[ML4T_A3_0002]] refuses a segment shorter than about a quarter, which stops both
algorithms from spending breaks on individual selloffs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>
