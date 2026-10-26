# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/12_causal_dml.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Machine learning → 機器學習
- Feature → 特徵
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETF momentum: a causal estimate, not a forecast

Every model from [[[ML4T_A3_0001]]](06_linear.ipynb) to
[[[ML4T_A3_0002]]](11e_supervised_autoencoder.ipynb) answers the same question: given
this fund's features today, what is its return going to be. This notebook asks a different one.
Skip-recent momentum - [[ML4T_A3_0003]], the six-month return that skips the most recent month -
is one column of that feature matrix. **If two otherwise identical funds differed only in that
column, how much would their next 21-day returns differ?**

That is not what a predictive model estimates, and the gap matters. Momentum moves with
volatility and with the risk-on/risk-off cycle, and so does the forward return. A regression of
return on momentum absorbs all of that into the momentum coefficient. Double machine learning
separates them: it fits one flexible model for the return given the confounders, another for the
treatment given the same confounders, and estimates the effect from what neither model could
explain. What is left is the part of the momentum-return relationship the confounders cannot
account for.

**The confounders are declared in [[ML4T_A3_0004]], not chosen here**: realized volatility at
21 and 126 days, a regime indicator, and the yield-curve slope. Each one moves both the treatment
and the outcome, which is what makes it a confounder rather than a control.

**Learning objectives**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Say what a causal estimand adds to a specification that a predictive one does not carry.
- Read the analysis population, the temporal geometry and the refutation design out of the
  resolved identity before anything is fitted.
- Read a Driscoll-Kraay standard error against a block-permutation p-value, and say which to
  believe when they disagree.
- Say why a causal row is registered separately from every prediction set and selects nothing.

**Book reference**: Chapter 15, Section 15.6 (cross-dataset causal evidence).

**Prerequisites**: [[[ML4T_A3_0001]]](03_financial_features.ipynb) for the treatment and
the confounders, [[[ML4T_A3_0002]]](04_model_based_features.ipynb) for the rest of the
panel, and [[[ML4T_A3_0003]]](05_evaluation.ipynb) for the holdout boundary this analysis stays
behind.

**What it writes**: one row in [[ML4T_A3_0004]], for the primary label, carrying the estimate, its
Driscoll-Kraay standard error, the naive comparison and the refutation p-value, under a hashed
identity derived from the estimand, the analysis population and the refutation design.
[[[ML4T_A3_0005]]](13_model_analysis.ipynb) reads that row as causal evidence and keeps it out
of the predictive comparison. **It selects nothing**: selection is validation backtest Sharpe in
[[[ML4T_A3_0006]]](14_backtest.ipynb), and a causal estimate is not a candidate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## Identifying assumptions

DML estimates a causal effect under three assumptions, and none of them is tested here:

1. **Conditional ignorability**: every backdoor path between treatment and outcome is blocked by
   the declared confounders. There is no unobserved third thing driving both.
2. **Overlap**: every fund could have carried any level of the treatment, given its confounders.
3. **SUTVA**: one fund's momentum does not change another fund's return.

The refutation test in section 4 is indirect evidence about the estimator, not about these. It
asks whether the estimate stands once the treatment's timing is destroyed, which a spurious
estimate often does not - but standing there is not the same as the assumptions holding.

**Research-design limitations.** This is a stability analysis on the fixed ETF research universe
and the materialized feature panel. [[ML4T_A3_0001]] and [[ML4T_A3_0002]] are finalized FRED values
rather than point-in-time vintages, and their feature timestamps are used as recorded. The
analysis does not claim those macro observations were available at the same close. That narrows
the reading to this retrospective panel, which is what it is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Declaring the request

Nothing about the estimand is written here. The treatment, the confounders and the method come
from [[ML4T_A3_0001]]; the fold count, the placebo count and the seed come from the shared
[[ML4T_A3_0002]] configuration. What this cell declares is which label to estimate the effect on and
under which execution tier.

A nonzero fold, sample, symbol or placebo limit is a **preview**: a reduced run that writes to a
throwaway workspace and is excluded from canonical evidence. A canonical run cannot carry one,
and a preview must declare every one of them - a preview missing [[ML4T_A3_0003]] would otherwise
resolve the full population, which is the opposite of what the tier is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. What resolving the request settles

**Resolving** goes and finds everything the declaration left open: it loads the label and feature
artifacts, checks the treatment and every confounder is present, computes the fold boundaries and
the embargo from the panel's own observed cadence, and works out the exact set of fund-date pairs
the estimate is taken over. It fits nothing, so all of it can be read before any cost is paid.

The three things worth reading in it:

- **The estimand.** Outcome, treatment, confounders, the horizon the outcome runs over, and
  [[ML4T_A3_0001]] - the last decision date whose outcome resolves before the holdout
  begins. Every row after it is dropped. The cutoff is computed **per fund** against that fund's
  own observation count rather than by stepping back a calendar duration, because a 21-day buffer
  is about fifteen sessions on a five-session week and subtracting it as calendar time leaves the
  last few retained rows resolving inside the holdout.
- **The temporal controls.** Cross-fitting groups whole decision timestamps rather than rows, so
  no date is split across a fold boundary and the cross-section stays intact. The embargo is at
  least the outcome horizon, which is what stops a training fold from containing the return a
  validation row is still earning.
- **The refutation design.** The placebo permutes **contiguous blocks within each fund**, not
  rows, so some of the treatment's serial dependence is carried into the null rather than
  destroyed by the shuffle. How much depends on how long the blocks are, which the subsection
  after the table takes up - and it is the difference between a null that means what it reads as
  and one that does not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>
