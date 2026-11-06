# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/11_causal_dml.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Feature → 特徵
- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# A different question from the one every other model here asks

Every notebook from [[[ML4T_A3_0001]]](06_linear.ipynb) through [[[ML4T_A3_0002]]](10_dl_tcn.ipynb) asks
the same question in different ways: **given what I can see now, what is the best guess for the
next 8-hour return?** A model that answers it well is useful whether or not any of its features
cause anything. Collinear features, proxies, coincidences - all fine, as long as the association
holds out of sample.

This notebook asks something else: **if the premium's z-score were higher, holding the other
declared drivers fixed, would the subsequent return be different?** That is a question about an
intervention, and no amount of predictive accuracy answers it. The two live in the same case
study and must not be reported as though they were the same finding, which is why the causal
result is registered under its own identity and never enters the population that
[[[ML4T_A3_0003]]](13_backtest.ipynb) selects from.

## The estimand, stated before anything is fitted

- **Treatment:** [[ML4T_A3_0004]], the premium's standing relative to its own recent range.
  Continuous, not binary - so the estimate is a slope, the change in expected return per unit of
  treatment, not a difference between two groups.
- **Outcome:** [[ML4T_A3_0005]], the return over the settlement interval after the decision time.
- **Confounders:** [[ML4T_A3_0006]], [[ML4T_A3_0007]], [[ML4T_A3_0008]]. These are the
  variables declared to drive both the treatment and the outcome, and adjusting for them is the
  entire identification claim.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

That list is short, and its shortness is the honest part of the exercise. **Double machine
learning removes confounding by variables you name.** It does nothing about one you did not, and
nothing about the possibility that the relationship runs the other way. Naming three confounders
is a claim that those three are the relevant ones; the estimate is only as good as that claim.

## What double machine learning actually does

The naive approach - regress the outcome on the treatment and the confounders together - biases
the treatment coefficient whenever the confounders enter nonlinearly, because whatever the linear
term fails to absorb leaks into the treatment. DML avoids that by splitting the problem in two:

1. Predict the **outcome** from the confounders alone, and take the residual.
2. Predict the **treatment** from the confounders alone, and take the residual.
3. Regress residual on residual. What remains is the part of the treatment the confounders do not
  explain, against the part of the outcome they do not explain.

The two nuisance predictions can be any flexible learner, because the residual-on-residual step
is what carries the causal interpretation. **Cross-fitting** is what keeps that step honest: each
observation's residual is computed by a model that did not see it, so an overfitted nuisance
model cannot manufacture a residual correlation. Here the folds are chronological with an
embargo, so the nuisance models are also never fitted on data that comes after what they predict.

## Why the placebo is the part to read carefully
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

A causal estimate on financial data will produce a number whether or not there is anything there,
so the refutation matters more than the point estimate. The placebo permutes the treatment and
re-estimates, and the estimate should collapse. What makes it a real test rather than a formality
is the **block size**, discussed at the table below: permuting one bar at a time destroys exactly
the serial dependence that makes the original estimate hard to get right, and a placebo that
destroys the difficulty is a test the estimate passes for free.

**Learning objectives.** By the end of this notebook you will be able to:

- State an estimand - treatment, outcome, confounders, horizon - precisely enough that someone
  else could disagree with it.
- Explain what cross-fitting protects against, and why chronological folds with an embargo are
  the right shape for it on overlapping financial labels.
- Say why a block-permutation placebo needs a block long enough to preserve serial dependence,
  and how the block size is derived here rather than chosen.
- Keep a causal estimate and a predictive result in separate reports, and say in one sentence
  why combining them would misdescribe both.

**Book reference:** Chapter 15, causal inference for trading research.

**Prerequisites:** [[[ML4T_A3_0001]]](03_financial_features.ipynb),
[[[ML4T_A3_0002]]](02_labels.ipynb) and [[[ML4T_A3_0003]]](05_evaluation.ipynb) - the features, the
return labels and the purged walk-forward folds.

**What it writes:** one causal result under its own identity in [[ML4T_A3_0004]]. It is read
by [[[ML4T_A3_0005]]](12_model_analysis.ipynb), which reports it **beside** the predictive
results rather than among them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0003-p000

~~~~~~markdown
## 1. Resolve the estimand and the refutation contract

Nothing is fitted below. The request resolves to a specification and an identity, and the table
prints the fields that decide what the estimate means: what is being intervened on, what is being
measured, over what horizon, how the nuisance folds are cut, and how the placebo will be built.
Reading them before the fit is the only point at which disagreeing with the estimand is cheap.

[[ML4T_A3_0001]] is the analysis population - the rows that survive having a treatment, an
outcome and every confounder present. Quote that, not the panel height, when describing what the
estimate rests on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
[[ML4T_A3_0001]] is the parameter the refutation lives or dies on, so it is on the
table rather than buried in the spec. The placebo permutes contiguous blocks
within each symbol; a block of one bar is an iid shuffle, which destroys the
serial dependence the placebo is meant to keep and makes the test trivially
easy to pass. Two things create that dependence and the block spans the longer
of them: the overlapping labels span the outcome horizon, and the treatment
spans its own construction window. Here the horizon is a single 8-hour bar
while [[ML4T_A3_0002]] is a 42-bar rolling statistic, so the treatment
window sets the block and [[ML4T_A3_0003]] says so.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>
