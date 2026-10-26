# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/03_econml_dml.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Machine learning → 機器學習
- Feature → 特徵
- Label → 標籤
- Cross-validation → 交叉驗證
- Time series → 時間序列
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Double Machine Learning for Momentum Causal Effect

**Chapter 15: Causal Estimation**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: See Section 15.4 for DML theory and the ETF factor application

## Purpose
**Double machine learning** (DML) estimates the effect of a momentum signal on forward
returns while adjusting for volatility and regime, on a panel of ETFs. The estimate is one
of two things this notebook is about. The other is that a panel breaks every correction
that has a notion of "nearby": the standard error, the cross-validation folds, the
permutation blocks and the temporal subsets all count in rows unless they are told not to,
and on a stacked panel a row is a different ETF rather than the next day.

## Learning Objectives
- LO1: Explain what confounding does to a factor regression, and what adjustment can and
  cannot recover
- LO2: Fit a DML estimator with EconML for a continuous treatment
- LO3: Compare the raw and adjusted estimates and read the direction of the bias
- LO4: Build folds, standard errors and permutations that count in decision times
- LO5: Read a refutation test, including one that cannot refute anything

## Cross-References
- **Upstream**: Chapter 8 (ETF momentum features)
- **Downstream**: Chapter 16 (strategy simulation), Chapter 19 (risk management)
- **Related**: [[[ML4T_A3_0002]]](02_dowhy_causal_graph.ipynb) (graphical approach), [[[ML4T_A3_0003]]](04_dml_crypto_regime.ipynb) (regime effects)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Methodological Notes
Following Chernozhukov et al. (2017) and de Prado (2018):
- **WalkForwardCV** from ml4t-diagnostics, with purging and embargo, built over the
  panel's decision times
- **Driscoll-Kraay standard errors**, which aggregate by decision time before applying the
  Newey-West kernel
- **Block permutation within entity**, so the placebo treatment keeps its persistence

**Prerequisites**: [[[ML4T_A3_0001]]](02_dowhy_causal_graph.ipynb) for the DoWhy
workflow, and an ETF modeling dataset built by the features pipeline

## Causal Design Contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

| Element                   | This notebook                                                                                |
|---------------------------|----------------------------------------------------------------------------------------------|
| Unit                      | ETF-date row from the ETF modeling panel                                                     |
| Treatment                 | [[ML4T_A3_0001]] - 6/1 momentum factor (continuous)                                          |
| Outcome                   | [[ML4T_A3_0002]] - 21-day forward return                                                         |
| Controls (W in EconML)    | [[ML4T_A3_0003]], [[ML4T_A3_0004]], [[ML4T_A3_0005]], [[ML4T_A3_0006]] - all backward-looking, pre-treatment    |
| Effect modifiers (X)      | None in this notebook; constant ATE target. See [[ML4T_A3_0007]] for the X-slot example |
| Identification assumption | Selection on observables given the four controls; sufficient pre-treatment information       |
| Main failure mode         | Unobserved confounding (sentiment / macro shocks), nuisance-model misspecification, panel-time leakage if CV is not date-grouped |
| Estimand                  | Marginal effect of a one-unit change in 6/1 momentum on 21-day forward return after adjustment |
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0003-p000

~~~~~~markdown
## Configuration
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0006-p000

~~~~~~markdown
## 1. Load ETF Features from Modeling Pipeline

We use [[ML4T_A3_0001]] to load pre-computed features (Ch8),
temporal features (Ch9), and labels, joined and ready for analysis.
Real-data only - no synthetic fallback. If the modeling dataset is missing,
the notebook fails loudly with a clear error rather than silently switching
to a synthetic substitute that would publish indistinguishable numbers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### The Panel Keys, and Why Everything Below Needs Them

A row here is an ETF *and* a date, and the frame is sorted by date, so consecutive rows
are usually different ETFs on the same day rather than the same ETF on consecutive days.
Every correction in this notebook that has a notion of "nearby" - the standard error, the
cross-validation folds, the permutation blocks, the temporal subsets - has to count in
decision times, not in rows. Counting in rows on this frame measures a slice of one day's
cross-section and calls it three weeks.

The two arrays below carry that information, and each of those four places takes them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 2. The Unadjusted Slope

An OLS regression of forward returns on momentum, with nothing else in it. It is the
benchmark the adjusted estimates are read against, and it is confounded by construction:
volatility and the yield-curve regime both move the momentum signal and move forward
returns, so its slope carries their contribution as well as momentum's. Which way that
pushes the slope is an empirical question the comparison below answers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
### Which Robust Standard Error a Panel Takes

Overlapping 21-day returns make consecutive observations of one ETF correlated, and the
usual answer is a Newey-West standard error with the bandwidth set to the label horizon.
On this frame that answer is applied to the wrong axis. [[ML4T_A3_0001]] runs its kernel
down the rows, and 21 rows here are a fifth of one day's cross-section, so the correction
treats different ETFs on the same day as if they were successive days.

**Driscoll-Kraay** is the version that fits a panel. It aggregates the regression score by
decision time first and applies the Newey-West kernel to that time series, which makes it
robust both to the serial correlation the overlap creates and to whatever the ETFs share
on a given day. statsmodels reaches it through [[ML4T_A3_0002]] with a [[ML4T_A3_0003]]
argument, which is the same call [[ML4T_A3_0004]] makes for every case study.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>
