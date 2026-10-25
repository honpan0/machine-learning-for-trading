# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/05_feature_selection.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Sharpe ratio → 夏普比率
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Cluster → 群集
- Clustering → 分群
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Feature Selection and Deduplication

**Chapter 8: Feature Engineering**
**Section Reference**: 8.6, Combining Features and Controlling Search

**Docker image**: [[ML4T_A3_0001]]

## Purpose

A feature engineering pipeline produces many candidates: different lookbacks,
transforms, and interaction variants. This notebook demonstrates how to reduce
that set to a focused, production-ready collection using systematic selection
and deduplication.

## Learning Objectives

1. Compute cross-sectional IC and rank features by predictive power
2. Apply correlation filtering to remove redundant features
3. Cluster near-duplicate features and select representatives
4. Use Benjamini–Hochberg FDR to control false discovery across multiple tests
5. Assess feature stability via bootstrap IC
6. Compare IC-based and ML-based (LightGBM) importance rankings

## Prerequisites

- Run [[[ML4T_A3_0002]]](../case_studies/etfs/03_financial_features.ipynb)
  to produce [[ML4T_A3_0003]]
- Requires [[ML4T_A3_0004]] and [[ML4T_A3_0005]] libraries

## References

- Harvey, Liu, and Zhu (2016), on multiple testing in factor research
- Meinshausen and Bühlmann (2010), on stability selection

**Output**: Selected feature list for downstream Chapter 9 use
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
## Load Features from ETF Case Study

The ETF case study produced features in [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
Feature selection is a development decision, so it must not see the holdout. The
boundary comes from the case study's own [[ML4T_A3_0001]] under [[ML4T_A3_0002]],
and the rule it follows is set out in [[ML4T_A3_0003]].
Everything below reads pre-holdout rows only: the IC ranking, the multiple-testing
correction, the stability selection and the model importances alike. The forward-return
labels are computed from the already-filtered prices, so no label reaches across the
boundary either.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
Non-finite feature values, such as the 0/0 a short-window Sharpe ratio can produce, are
replaced with nulls. Left as NaN they pass straight through [[ML4T_A3_0001]], which removes
only nulls, and then propagate through [[ML4T_A3_0002]] into the panel correlation matrix,
which both corrupts those features' correlations and misgroups them in the clustering.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## Compute Information Coefficient (IC)

IC measures the Spearman rank correlation between features and forward returns.
We compute IC **cross-sectionally** (per date, then average). Pooled IC
conflates time-series drift with cross-sectional predictive power.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
Cross-sectional IC is computed per date, then sorted by timestamp. The sort matters:
[[ML4T_A3_0001]] does not preserve order, and the Newey-West t-statistic below regresses each
feature's daily IC series on a constant with an autocovariance correction, which means
something only on a chronologically ordered series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
The daily IC series is serially correlated, through overlapping information sets and
slow-moving common factors, so the cell below reports both the i.i.d. t-statistic and a
Newey-West one from regressing the IC series on a constant. The Newey-West figure is the
one the multiple-testing correction consumes.

[[ML4T_A3_0001]] returns a float NaN rather than a null on any date where a feature is constant
across symbols, so each daily IC series is filtered on finiteness rather than on nulls. A
feature whose cross-sectional IC is undefined on most dates, or whose defined ICs have no
variance, is a date-level series carrying no cross-sectional signal; it is dropped from
the ranking and from every step that follows.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
## Correlation Filtering

Highly correlated features provide overlapping information. We compute
correlation on the full panel (all dates by symbols), then remove features whose
absolute correlation exceeds [[ML4T_A3_0001]], keeping the one with the higher IC in
each redundant pair. The threshold is declared in the parameters cell, and the printed
header repeats whatever it is set to.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
### Remove Redundant Features
Greedily drop the weaker member of each highly correlated pair.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0024-p000

~~~~~~markdown
## Clustering and Deduplication

Even after removing pairs above that threshold, many features remain near-duplicates.
Hierarchical clustering groups similar features so we can pick one
representative per cluster, which preserves diversity across families while
removing redundancy within them.

**Linkage choice**: We use **complete linkage** (not Ward) because Ward
assumes Euclidean distance, which correlation-based distances do not satisfy.
Complete linkage also avoids the chaining that average linkage produces on
this panel, where many features share moderate correlations; it yields compact
clusters whose members are mutually near-duplicate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
Only features carrying a cross-sectional IC are clustered; the date-level series dropped
above have no cross-sectional correlation structure to group on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0028-p000

~~~~~~markdown
The block structure reveals which features are essentially measuring the
same thing. Within each block, correlations are high, confirming that one
representative per cluster captures the shared signal. Between blocks,
correlations are lower, marking genuine diversification.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
## Multiple Testing Correction (BH-FDR)

With many features tested, some appear significant by chance.
Benjamini–Hochberg FDR controls the expected false discovery rate.

**Inference**: the p-values fed into BH-FDR come from the **Newey-West HAC**
t-statistic on each feature's daily IC series (matching the table above and
the headline measure in [[ML4T_A3_0001]]). The i.i.d. t-stat
would overstate significance because daily ICs share slow-moving common
factors and overlapping information sets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>
