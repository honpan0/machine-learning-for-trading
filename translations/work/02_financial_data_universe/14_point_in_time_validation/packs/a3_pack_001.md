# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/14_point_in_time_validation.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Point-in-Time (PIT) Data Validation

**Docker image**: [[ML4T_A3_0001]]

## Purpose
Demonstrate the operational checks needed to keep a backtest free of
lookahead bias on real ETF and macroeconomic data. Three threads run
through the notebook: feature-time vs decision-time alignment, a
correlation-based heuristic for catching obvious feature leakage, and the
bitemporal (vintage) view of macro data via the FRED provider.

## Learning Objectives
- Distinguish *event time* (when something happened) from *knowledge time*
  (when we learned about it), and the bitemporal axis for macro releases.
- Show why a centered moving average leaks future information, and why a
  level-versus-return correlation heuristic misses it.
- Build the corrected scale-invariant heuristic (feature-return against
  future-return) that does fire for [[ML4T_A3_0002]] features.
- Determine, by measurement, what the macro panel's timestamps mean, and
  what a forward-fill over them costs when they are period stamps.
- Query FRED with [[ML4T_A3_0003]] to see how the GDP advance estimate
  differs from the revised value.

## Book reference
Chapter 2, §2.3 (data quality framework — point-in-time correctness and
bitemporal data). The figure below is the §2.3 illustration.

## Prerequisites
- ETF parquet files materialized under [[ML4T_A3_0004]].
- Macro parquet (FRED snapshot) materialized under [[ML4T_A3_0005]] or
  loadable via [[ML4T_A3_0006]].
- [[ML4T_A3_0007]] environment variable for the live vintage query, which is
  the last section so that everything before it runs without a key
  (free key at [[ML4T_A3_0008]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] is the correlation above which the validator in the last-but-one section
calls a feature leaky. It is declared here rather than living on the class so the value the
reader sees and the value the check uses are the same one, and Section 4 prints the measured
correlations it has to separate.

[[ML4T_A3_0002]] and [[ML4T_A3_0003]] are how long after a period ends
its first estimate is published. They are round numbers standing in for a real release
calendar: US payrolls and unemployment land on the first Friday after the reference month,
CPI in the middle of the following month, and the GDP advance estimate about four weeks
after the quarter closes. A production system reads the actual calendar; these two make the
size of the correction visible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Load Real Market Data

Daily bars for one ETF anchor every example below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Lookahead Bias: A Visual Demonstration

A trailing moving average of width [[ML4T_A3_0001]] at time [[ML4T_A3_0002]] averages [[ML4T_A3_0003]], which is what
a live system can compute. A *centered* one is the same window slid forward so that [[ML4T_A3_0004]] sits
near its middle, which puts some of its inputs after [[ML4T_A3_0005]].

Exactly how many depends on the library's centering convention and on whether the width is
odd or even, so the next cell asks rather than assumes: running the centered average over a
ramp makes each output reveal the window that produced it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0010-p000

~~~~~~markdown
The centered average sits closer to the close, by the measured distance printed above, and
it turns where the price turns rather than after it. Both follow from the same thing: half
its inputs are prices that had not printed yet. No live system can produce that line, so a
backtest that uses it reports skill the strategy could not have had.

What the two measured windows show is that the future share does not fall away as the window
widens: it approaches half, wobbling with the parity of the width rather than declining. The
distance leaked does grow, at roughly half the width. So a longer centered average is not a
smaller violation; it is a violation that reaches further ahead.

There is a second tell, and it is the one that shows up first in practice. A centered
average has no value for the most recent rows, because they are still waiting for inputs,
so [[ML4T_A3_0001]] above silently ends the plotted series short of the data. A feature that
cannot be computed for today is a feature no live system can trade on, and that missing
tail is visible long before any correlation test is run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
## 3. Why the Naive Correlation Heuristic Fails

A leakage test that suggests itself is to correlate a feature's *level* with the next
period's *return*. It does not work, and the reason is not subtle once stated: a price
level is dominated by where the series has drifted to over years, and next-day returns are
close to mean-zero noise around that drift. The correlation is between a slow trend and a
fast wiggle, and it comes out near zero whether or not the feature contains tomorrow's
price. The next cell scores three features, one of which is tomorrow's close itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0014-p000

~~~~~~markdown
All three score near zero, including the one that *is* tomorrow's price. The test does not
separate a clean feature from a leaking one, so a feature matrix passing it has learned
nothing about itself.

What the test needs is for both sides to be the same kind of quantity. Turning the feature
into its own period-over-period return does that, and it is what the next section builds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
## 4. A Correct Scale-Invariant Leakage Test

Convert any feature to its own period-over-period return, then correlate that with the next
period's price return. A feature built from [[ML4T_A3_0001]] now exposes itself: for
[[ML4T_A3_0002]] the feature's return at [[ML4T_A3_0003]] *is* the price return [[ML4T_A3_0004]] periods ahead, so the
correlation goes to one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
The same three features now sort: the trailing average stays low, the centered average rises
because part of its window sits in the future, and [[ML4T_A3_0001]] saturates near one
because it is the next day's price.

What separates them is a gap in the middle of the scale, and the validator later in this
notebook puts its threshold there. The gap is what makes a threshold possible at all: a
detector whose clean and leaking cases sat close together would need a cutoff chosen to
produce the answer already known, which is not a detector.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## 5. Signal-to-Trade Lag: Trading Days, Not Calendar Days

A signal computed from the close of [[ML4T_A3_0001]] can be acted on no earlier than the open of [[ML4T_A3_0002]].
The shift has to be by *rows* rather than by calendar days, because the next tradable
moment after a Friday close is a Monday open and no amount of date arithmetic knows which
Mondays are holidays. Shifting the timestamp column by rows inherits the trading calendar
from the data itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
