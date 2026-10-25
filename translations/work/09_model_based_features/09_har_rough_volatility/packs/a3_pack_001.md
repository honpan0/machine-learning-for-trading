# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/09_har_rough_volatility.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# HAR and Rough Volatility

**Chapter 9 | Section 9.3**

**Docker image**: [[ML4T_A3_0001]]

The GARCH model in the previous notebook has one memory: a single decay rate that
governs how long a shock lasts. This notebook covers two things that memory cannot
express. **HAR** replaces the single decay with three horizons at once, on the argument
that the people trading at a daily, weekly and monthly rhythm are different people.
**Roughness** asks a different question entirely: not how long volatility remembers, but
how jagged its path is, and the answer for real markets is far jaggeder than the models
that were standard for thirty years assume.

Both need a measurement of volatility to work on, and getting that measurement right is
the first third of the notebook.

**Learning objectives**

- Compute volatility from within-session data, and use it to check what the estimators
  available from daily bars alone are actually measuring.
- Fit a model of volatility across three horizons, and read its coefficients as a
  statement about which horizon is driving the current level.
- Correct the standard errors of that fit for the overlap its own regressors contain.
- Estimate how jagged a series is over time, apply it to returns and to volatility, and
  read the two answers as the different things they are.

**Book reference**

Chapter 9, Section 9.3 (Volatility Features).

**Prerequisites**

[[ML4T_A3_0002]] for conditional volatility and for what persistence means.
Chapter 8 introduced the range-based estimators this notebook tests.
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
# Part 1: what "volatility" is being measured

Everything in this notebook models a series called realized volatility, and there are
several different things that name refers to. The definition with the strongest claim to
it is computed from within-session data: sum the squared returns of every minute in a
session, and the total estimates that session's variance with an error that falls as the
bars get finer.

[[ML4T_A3_0001]]

It measures the **trading session** and nothing else, and that is the first thing to be
clear about, because a daily estimator's target is the whole day. This section
establishes the relation between the two on a symbol where both are available, and turns
up two data traps on the way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
Two choices in the cell above are worth stating rather than leaving in the code. The
returns are taken from the **last trade price** of each minute rather than from the
minute's volume-weighted average. A volume-weighted average is an average over the
minute, so a series of them is smoother than the price actually was, and squared returns
built from it understate the variance. On this sample the difference is not small.

And the bars cover 09:30 to 16:00 only, so the sum below is the variance of the trading
session. What happens between one session's close and the next one's open is a separate
quantity, measured separately here.

Three details in the cell below are load-bearing. The session's open and close come from
the bars as loaded, not from a frame reduced to the minutes that have a previous close;
an open read from such a frame would be the second minute's price, and the overnight
return would then swallow the opening minute. The opening minute keeps its own
open-to-close return in the variance sum for the same reason: without it the sum covers
one minute less than the session return it is compared against.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0006-p001

~~~~~~markdown

And an overnight return is only an overnight return if the two rows are consecutive
sessions of the exchange. Bar counts cannot establish that, and neither can the number of
calendar days between the dates: a Monday-to-Wednesday pair is three days apart and still
contains all of Tuesday's trading if Tuesday is missing from the data. What settles it is
the exchange calendar, which says which dates are sessions independently of what the data
holds. Each pair is required to be one session apart on that calendar, which keeps
holiday weekends and drops a missing weekday. On a reduced test fixture, which keeps
separated blocks of sessions, an unchecked gap can be weeks long.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p001>>>
<<<ML4T-ZH-END:c0006-p001>>>

### c0008-p000

~~~~~~markdown
## The first trap: these prices are not adjusted

A close-to-close return computed from raw trade prices crosses every corporate action as
though it were a price move. The check below finds any session whose return is too large
to be one, and on this symbol and period it finds exactly one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
One session, and it is the four-for-one share split. The intraday variance of that
session is unaffected, because a split happens between sessions and every minute return
inside the session is a real price move; what is corrupted is anything computed across
the boundary. That asymmetry is worth carrying: the same raw data can be sound for one
statistic and unusable for another, and which is which depends on whether the statistic
crosses a session boundary.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
## The second trap: a session is not a day

A close-to-close return is the overnight move plus the session that follows it, exactly,
because both are logarithms. So the identity below holds term by term with no
approximation:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is the **aggregate** open-to-close return of the session. That is not the
same quantity as the realized variance measured from minute bars: the realized variance
is the sum of squared minute returns and the aggregate is the square of their sum, so
they differ by every cross-product between minutes. Both are reported below, separately,
because they answer different questions and conflating them is how a decomposition comes
out looking exact when it is not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>
