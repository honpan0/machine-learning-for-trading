# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/10_uncertainty_features.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Sharpe ratio → 夏普比率
- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Uncertainty Features

**Chapter 9 | Section 9.4**

**Docker image**: [[ML4T_A3_0001]]

Every model in this chapter has produced an estimate. A model that also produces a
statement about how sure it is of that estimate is producing two features, and the second
one is often the more useful: a signal the model is confident about and a signal it is
guessing at should not be traded the same size, and only the second feature can tell them
apart.

**Learning objectives**

- Fit a volatility model that returns a distribution over its estimate rather than a
  single number, and extract the width of that distribution as a column.
- Refit it forward through a sample so that no posterior reads its own future, and say
  what the cost of doing so is when each fit takes minutes.
- Check that the sampler that produced the posterior actually converged, rather than
  assuming it, and know which two numbers say so.
- Turn a forecast interval into a feature, and recognize when the interval is telling you
  about the data and when it is telling you about the model.

**Book reference**

Chapter 9, Section 9.4 (Uncertainty features).

**Prerequisites**

[[ML4T_A3_0002]] for a point-estimate volatility model and for the filter-forward
construction this notebook's cost forces it to approximate. [[ML4T_A3_0003]] for
the Garman-Klass estimator used as the target here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## The data

SPY daily bars, with returns in percent and a Garman-Klass volatility as the target for
the forecasting half. [[ML4T_A3_0001]] is where that estimator is compared
against the alternatives; it is used here because it reads the whole daily bar rather
than only the close.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## What an uncertainty feature is

Take any statistic a model produces. Estimated by maximum likelihood it is one number;
estimated by sampling from a posterior it is a distribution, and the width of that
distribution is a second quantity that varies over time for reasons the point estimate
does not. A Sharpe ratio computed from a hundred sessions and one computed from a
thousand can be the same number and mean entirely different things.

The example below is the smallest version of that: the Sharpe ratio of this sample as a
single number, with nothing attached saying how far it could be from the truth. Chapter
17 develops the Bayesian version in full. This notebook applies the same idea to
volatility, where the payoff is larger because the quantity being estimated moves.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## A volatility model that returns a distribution

The **stochastic volatility** model treats log-volatility as an unobserved series that
follows its own autoregression, and the returns as draws whose scale is that hidden
series:

[[ML4T_A3_0001]]

It differs from GARCH in what it treats as unknown. GARCH says the variance is a
deterministic function of past returns, so given the parameters there is one variance
path and no uncertainty about it. Stochastic volatility says the variance has its own
noise, so even with the parameters known the path is uncertain, and fitting it produces
a distribution at every session rather than a number.

Three parameters carry the model. [[ML4T_A3_0002]] is how persistent volatility is, [[ML4T_A3_0003]]
is how much the volatility process itself moves, and the observation distribution is
Student-t rather than normal, whose degrees of freedom [[ML4T_A3_0004]] is estimated: a small [[ML4T_A3_0005]]
says the returns have tails a normal cannot produce, and a large one says a normal would
have done.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Refitting forward, and what it costs

Each fit takes minutes, which decides the shape of everything below. The model is refit
quarterly on the preceding year of returns, and from each fit two kinds of feature come
out.

The **parameters** are one number per fit by construction: how persistent volatility is
and how much the volatility process moves are properties of a window, not of a session,
so a column holding them is genuinely constant between refits and nothing is lost.

The **level** is not. What is extracted here is the posterior at the last session of the
training window, which is a filtered quantity conditioned only on data up to that point
and therefore causal. Carried forward for a quarter it stops being a volatility estimate:
by the end of the quarter it describes a session three months old. Use it as written for
the parameter columns and read [[ML4T_A3_0001]] for the level, where a cheap
recursion filters forward between refits at no cost. Making the same thing work here
needs a particle filter, which is the standard answer and is outside this notebook.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0014-p000

~~~~~~markdown
## Did the sampler converge

A posterior is only worth reading if the sampler explored it, and three numbers say
whether it did. **Divergences** are steps the sampler could not take and are counted
above; any at all are a warning. [[ML4T_A3_0001]] compares the variance between chains against
the variance within them and should be at or very near one. The **effective sample size**
is how many independent draws the correlated ones are worth, and a few hundred is the
usual floor for a stable posterior mean.

This model is a hard one for the sampler, and the reason is structural rather than a
matter of tuning: the persistence, the volatility of volatility and the hidden path are
not separately identified by the data, so the posterior has a narrow curved region the
sampler has to follow. Expect the two parameters to have lower effective sample sizes
than the ones the returns pin down directly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Whether the sampler noise is large enough to matter

Two of these parameters are features, so a failed diagnostic is not an academic point
about the fit; it decides whether the column carries anything. Two quantities bound the
question. The **Monte Carlo standard error** is how far one fit's posterior mean could be
from the mean the sampler was estimating, purely because it took finitely many draws; it is
reported per refit above because it differs between them. The **spread across refits** is
how much the feature moves from quarter to quarter, which is the variation a model would
read.

Putting the largest error next to that spread says whether sampling error is large enough
to matter. It does not divide the spread into signal and noise: each fit's error is a
separate quantity, and a fit whose diagnostics failed makes its own error estimate
unreliable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>
