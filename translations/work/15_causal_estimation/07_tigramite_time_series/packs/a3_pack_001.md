# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/07_tigramite_time_series.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Time Series Causal Discovery with PCMCI

**Chapter 15: Causal Machine Learning**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: See Section 15.6 for PCMCI theory and ADIA Lab insights

## Purpose
This notebook demonstrates **causal discovery** - learning the causal structure
from time series data without specifying a DAG a priori. We compare PCMCI with
traditional Granger causality and show how to discover lead-lag relationships
in multi-asset financial time series.

## Learning Objectives
After completing this notebook, you will be able to:
- LO1: Apply PCMCI algorithm for time series causal discovery
- LO2: Compare Granger causality limitations with PCMCI advantages
- LO3: Interpret discovered causal graphs with time lags
- LO4: Assess edge stability via bootstrap analysis

## Methodology Reference
Runge et al. (2019) "Detecting and quantifying causal associations in large
nonlinear time series datasets" Science Advances

## Key Concepts
1. **Causal discovery**: Infer DAG from data (vs specifying it)
2. **PCMCI algorithm**: PC skeleton + Momentary Conditional Independence
3. **Time lags**: Causal relationships can have delays
4. **Stability analysis**: Bootstrap to assess edge reliability

**Prerequisites**: [[[ML4T_A3_0002]]](01_library_overview.ipynb) for library context;
ETF OHLCV data from Ch2 data pipeline
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Important Methodological Notes

### Multiple Testing Correction

PCMCI separates two statistical decisions. [[ML4T_A3_0001]] regularizes parent
selection in PC1; it is not a multiple-testing correction for the final MCI
tests. This notebook lets Tigramite select [[ML4T_A3_0002]] and applies its explicit
Benjamini-Hochberg false-discovery-rate correction to the MCI p-values.

### Lag Selection

[[ML4T_A3_0003]] defines which delayed causal effects can be discovered. We predeclare
a five-trading-day horizon based on the weekly financial response window. The
ACF is descriptive evidence about serial dependence, not a rule for excluding
cross-variable causal delays.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0002-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0006-p000

~~~~~~markdown
## 1. Load Multi-Asset Time Series
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
Real data only. A load failure is a fatal error here, so neither CI nor a fresh reader
environment without [[ML4T_A3_0001]] can publish synthetic numbers under a real heading.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 2. Inspect Serial Dependence Within the Causal Horizon

The search horizon remains the predeclared five trading days. A rapid decline
in each series' own autocorrelation does not rule out a delayed effect from a
different series, so the ACF does not overwrite [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The chart shows that daily returns have limited own-series persistence. PCMCI
still tests the full weekly horizon because cross-series effects can arrive
after a series' own ACF has decayed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 3. Prepare Data for Tigramite
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## 4. PCMCI with Explicit False-Discovery-Rate Control

[[ML4T_A3_0001]] asks Tigramite to select the PC1 regularization parameter.
[[ML4T_A3_0002]] then adjusts the final MCI p-values across the tested
links. The returned [[ML4T_A3_0003]] therefore contains BH-adjusted p-values.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## 5. Interpret Discovered Causal Graph

We threshold Tigramite's BH-adjusted MCI p-values at [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## 6. Bootstrap Stability Analysis

Discovered edges may be unstable. We use block bootstrap to assess which
edges are consistently found across resamples. This is essential for
robustness in financial applications.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0023-p000

~~~~~~markdown
The stability chart is what turns a single PCMCI fit into a statement about the sample.
Each bar is the share of block-bootstrap resamples that recovered that edge, and the dashed
line is the threshold [[ML4T_A3_0001]] sets. An edge the point estimate found but the
resamples rarely recover is a property of this particular sample; an edge recovered in most
of them survived being asked the question again.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## 7. Balanced Interpretation of Null Results

If no significant lagged links are found, this does NOT prove market efficiency.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## 8. Comparison with Granger Causality

**Granger causality limitations**:
1. Pairwise only - ignores multivariate confounding
2. Assumes linearity
3. Sensitive to lag selection
4. Can find spurious relationships due to common causes

**PCMCI advantages**:
1. Multivariate - conditions on all other variables
2. Conditions on selected observed parents under causal-sufficiency assumptions
3. Tests at multiple lags simultaneously
4. Explicit FDR control for the multivariate MCI tests

PCMCI can reduce bias from observed common drivers included in the panel. It
cannot eliminate hidden confounding, so discovered links remain hypotheses.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
