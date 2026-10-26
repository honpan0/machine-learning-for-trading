# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/01_library_overview.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Causal Inference Library Decision Guide

**Chapter 15: Causal Estimation with ML**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: See Section 15.1 (Table 15.1) for the method selection guide

## Purpose
Chapter 15 uses five Python libraries, and they do not compete with one another.
This notebook maps a causal question to the library that answers it, and shows the
API each one expects: what it takes as treatment, outcome, controls and graph.

## Why the estimates below are not a benchmark

The same synthetic sample runs through several libraries, which invites a ranking.
Four differences prevent one:

1. **Different problems.** Effect estimation (EconML, DoWhy, CausalML) starts from a
   causal structure and quantifies an effect. Structure discovery (Tigramite,
   causal-learn) starts from data and proposes a structure.
2. **Different treatment types.** EconML and DoWhy handle a continuous treatment
   directly; CausalML is built for binary and discrete interventions.
3. **Different estimands.** The **estimand** is the quantity the analysis targets.
   Binarizing a continuous treatment to suit CausalML changes the estimand from a
   marginal effect to a contrast between a high and a low group.
4. **Different assumptions.** Each library asks for a different account of how the
   data were generated and what confounding remains.

## Learning Objectives
After completing this notebook, you will be able to:
- LO1: Match a causal question to the library that answers it
- LO2: Apply the selection guide in Table 15.1 to your own problem
- LO3: Read the API each library expects, and which argument carries the controls
- LO4: Separate effect estimation from structure discovery
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Cross-References
- **Upstream**: None (synthetic data with a known data-generating process)
- **Downstream**: Each library has a notebook of its own
  - EconML: [[[ML4T_A3_0001]]](03_econml_dml.ipynb), [[[ML4T_A3_0002]]](04_dml_crypto_regime.ipynb)
  - DoWhy: [[[ML4T_A3_0003]]](02_dowhy_causal_graph.ipynb)
  - BSTS: [[[ML4T_A3_0004]]](06_fed_announcement_bsts.ipynb)
  - Tigramite: [[[ML4T_A3_0005]]](07_tigramite_time_series.ipynb)
  - causal-learn: [[[ML4T_A3_0006]]](08_neural_causal_discovery.ipynb)

## Libraries Covered
**Effect estimation**, given a causal structure:
1. **EconML** (Microsoft) - double machine learning (DML) and metalearners for a
   continuous or binary treatment
2. **DoWhy** (Microsoft/Amazon) - explicit graph, identification, refutation tests

**Structure discovery**, to propose a causal graph:
3. **Tigramite** - PCMCI for time series
4. **causal-learn** (CMU) - PC, FCI, GES, LiNGAM and Granger, for contemporaneous
   and lagged structure

**Also referenced**: CausalML (binary treatment, not used in this chapter),
tfp-causalimpact (Bayesian structural time series for event studies, used in
[[ML4T_A3_0007]])

**Prerequisites**: None

## Causal Design Contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

| Element                   | This notebook                                                                          |
|---------------------------|----------------------------------------------------------------------------------------|
| Unit                      | Synthetic observation (1 of 1,000 i.i.d. rows generated from a known DGP)               |
| Treatment                 | [[ML4T_A3_0001]] (continuous), partly driven by [[ML4T_A3_0002]] and [[ML4T_A3_0003]]                    |
| Outcome                   | [[ML4T_A3_0004]] (continuous), driven by treatment and confounders; the true average treatment effect (ATE) is bound to [[ML4T_A3_0005]] below |
| Controls (W in EconML)    | [[ML4T_A3_0006]], [[ML4T_A3_0007]] - both confound the treatment-outcome path                      |
| Effect modifiers (X)      | None; the target here is a constant ATE, and [[ML4T_A3_0008]] uses X for regime heterogeneity |
| Identification assumption | The synthetic DGP is fully observed, so there is no unobserved confounding by design    |
| Main failure mode         | None in identification; this is an API smoke test, not an empirical finding             |
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## Check Library Availability

A library counts as available when it imports. The version comes from the installed
distribution metadata rather than from the package itself, because three of these five
packages expose no version attribute.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Generate Common Demonstration Data

One synthetic dataset runs through every library so the API calls sit side by side.
[[ML4T_A3_0001]] and [[ML4T_A3_0002]] drive both the treatment and the outcome, which makes them
confounders: an unadjusted regression of [[ML4T_A3_0003]] on [[ML4T_A3_0004]] picks up their effect
as well as the treatment's.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The treatment carries very little independent variation: once [[ML4T_A3_0001]] and [[ML4T_A3_0002]]
are partialled out, what is left of [[ML4T_A3_0003]] is its own noise term. That, not the size
of the effect, is what sets how precisely any of these estimators can measure the ATE,
which is why each estimate below is reported with an interval.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0010-p000

~~~~~~markdown
## 1. EconML (Microsoft)

EconML fits **double machine learning** (DML): one model predicts the outcome from the
controls, another predicts the treatment from the controls, and the treatment effect is
estimated from what is left over in both. It takes a continuous or a binary treatment and
can model heterogeneous effects, so it is the tool when the question is how large an
effect is and how it varies.

Use it when the adjustment set is known but a graph is not written down.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
Confounders enter EconML's DML interface as [[ML4T_A3_0001]], the controls used for residualization,
not as [[ML4T_A3_0002]], the effect modifiers that model treatment-effect heterogeneity. For a single
adjusted ATE the distinction does not change the answer, but it does as soon as the
question is whether the effect differs across regimes; [[ML4T_A3_0003]] uses the
[[ML4T_A3_0004]] role.

[[ML4T_A3_0005]] splits the sample at random, which is valid here because the rows are i.i.d. by
construction. A time series needs splits that respect the ordering, or the outcome model
learns from the future; [[ML4T_A3_0006]] walks forward instead.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>
