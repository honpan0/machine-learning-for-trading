# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/08_causal_sanity_checks.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Mechanism Plausibility Checks for Feature Triage

**Docker image**: [[ML4T_A3_0001]]

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.5 - From Correlation to Causality

## Purpose

This notebook implements **lightweight falsification tests** for feature evaluation.
These tests complement the correlation-based IC analysis from Section 7.3 by checking
whether a feature-outcome association is *consistent* with a proposed mechanism.

**Important**: These checks do not identify causal effects. They are robustness
diagnostics guided by mechanism reasoning, testing one feature-outcome pair at
a time. They cannot detect multivariate confounding. Formal causal
identification is deferred to Chapter 15.

We begin with a **feature × horizon scan** that expands on the ETF results from
[[[ML4T_A3_0002]]](07_multiple_testing.ipynb), where no feature survived BH-FDR at a 5-day horizon.
Widening the search to 10 features × 3 horizons and correcting across all 30 tests,
the long-lookback momentum terms (252d and 12-1) are the only ones that survive, and
they survive at the 5-day horizon. Their largest ICs are at 21 days but do not clear
the corrected threshold there - a weaker result than the textbook finding
(Jegadeesh and Titman 1993, Asness et al. 2013) would lead you to expect from 92 ETFs
over 14 years, and the honest one. We then apply the three diagnostic checks to two
features selected from the scan:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- **12-1 Momentum** (12-month return skipping the most recent month): clears triage
  with actionable caveats - it carries genuine cross-sectional information
  (strongest at lag 0), does not predict Treasury returns, but concentrates in
  low-volatility regimes.
- **Short-term reversal** (negated 1-day return): fails triage - no significant
  IC at the 21-day horizon, and its one significant cell does not survive the
  shifted-label check in Section 4.1.

## Learning Objectives

1. Run a multi-feature, multi-horizon IC scan to identify where signal exists
2. State a proposed mechanism using DAG vocabulary (confounder, mediator, collider)
3. Implement timing placebos (shift features, examine IC half-life)
4. Run shared-driver checks (unrelated outcomes should show no effect)
5. Assess regime heterogeneity (IC stability across VIX regime partitions)
6. Interpret results as triage decisions (proceed / revise / stop)

## Book Reference

Section 7.5 applies the three core checks to two features on the [[ML4T_A3_0001]] universe
with a 21-day forward return label. This notebook produces the feature scan
heatmap and dual-feature diagnostics referenced in the worked example.

**Prerequisites**: Notebooks [[[ML4T_A3_0002]]](05_signal_evaluation.ipynb) and [[[ML4T_A3_0003]]](06_ic_inference.ipynb)
introduce IC analysis; [[[ML4T_A3_0004]]](07_multiple_testing.ipynb) motivates the horizon expansion.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## Motivation: Why Expand the Search?

The multiple-testing scan in [[[ML4T_A3_0001]]](07_multiple_testing.ipynb) found that 0 out of 13
short-lookback features survived BH-FDR correction at a 5-day horizon on ETFs.
Two explanations are possible: the features are genuinely uninformative, or the
5-day horizon is too short for cross-sectional predictability in a 100-asset
universe. Cross-asset momentum is well-established at monthly+ horizons
(Asness, Moskowitz, and Pedersen 2013) but largely absent at weekly frequencies.

We resolve this by scanning 10 features across three horizons (5d, 21d, 63d).
This empirical scan determines which feature–horizon combinations carry signal,
and two are selected for the mechanism plausibility checks that follow.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## Load Data

We use the full ETF universe (~92 non-bond assets) and load VIX from FRED macro
data for regime conditioning. Treasury ETFs are excluded from the analysis
universe but IEF is retained for the shared-driver control.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0009-p000

~~~~~~markdown
### Compute features and labels

The shared-driver control is joined with inner semantics, so an absent Treasury series
does not weaken the analysis - it empties it, and every statistic downstream is then
computed on nothing. The load below therefore fails loudly rather than letting a later
cell fail on whichever column happens to be missing first.

We compute 10 features spanning four families (momentum, reversal, trend,
volatility) and forward returns at three horizons (5d, 21d, 63d). All features
use data available at time [[ML4T_A3_0001]] (no lookahead). The 12-1 momentum follows the
academic convention of skipping the most recent month to avoid short-term
reversal contamination.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0013-p000

~~~~~~markdown
The permutation helper below pre-computes and standardizes both sides' ranks once per
date. Ranks are invariant to relabeling, and a permutation changes neither a vector's
mean nor its standard deviation, so the Spearman IC of a permuted pair is the dot
product of the two standardized rank vectors divided by the count. That is identical to
the general correlation routine to floating-point noise and well over an order of
magnitude faster, which matters because the loop runs once per permutation per date.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
## Cross-Sectional IC Function

We compute Spearman rank correlation between each feature and forward returns at
each date, producing a time series of ICs. This is the same IC framework from
Section 7.3.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Feature × Horizon Scan

We scan 10 features across three forward-return horizons (5d, 21d, 63d) using
HAC-adjusted inference. The heatmap reveals a clear pattern: long-lookback
momentum features (126d+) carry significant cross-sectional information,
while short-term features remain noise regardless of horizon.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
### Correcting the scan for multiple testing

The scan above is not one test, it is one per cell of the grid. At a conventional
significance level a grid this size produces one or two false positives from noise
alone - the count is printed below - so reading [[ML4T_A3_0001]] off every cell is the error
[[[ML4T_A3_0002]]](07_multiple_testing.ipynb) exists to prevent. We control
the false discovery rate across the whole grid with Benjamini-Hochberg, and mark
significance with the corrected decision rather than the raw threshold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
