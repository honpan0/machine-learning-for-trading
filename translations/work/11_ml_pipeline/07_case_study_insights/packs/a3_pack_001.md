# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/07_case_study_insights.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Deep learning → 深度學習
- Feature → 特徵
- Label → 標籤
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Case Study Insights: Linear Models

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: assemble the cross-case-study view of the linear family
(OLS, Ridge, Lasso, ElasticNet). Per-case-study deep dives live in
[[ML4T_A3_0002]]; this notebook is the
comparative view across all nine case studies.

**Learning objectives**

- For each case study, read the highest-IC complete linear configuration's
  mean daily cross-sectional Spearman IC with its HAC interval on the primary label
- Compare regularization families (OLS, Ridge, Lasso, ElasticNet) at
  each case study's primary label
- Inspect per-fold IC distributions and the ICIR diagnostic for
  stability
- Extend the comparison across labels (horizon view) and across the
  classification ↔ regression metric symmetry
- Inspect coefficient sign consistency, Lasso sparsity, and the overlap
  of selected features across case studies

**Book reference**: Section 11.6 - Case study insights.

**Prerequisites**: each case study's [[ML4T_A3_0003]] pipeline has populated
[[ML4T_A3_0004]] for the linear family. Teaching notebooks NB01-NB06
cover the underlying techniques.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Complete-result guard

A model result is eligible for comparison only when no fold has an undefined
IC and its validation-day coverage equals the maximum for that label. The
local loader excludes predictions with any null fold IC and rejects shorter,
partially populated results before ranking.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
The loader preserves exact training and prediction identities so every later
statistic and coefficient view can be traced to one registry-selected artifact.

It also drops the generations a refit has retired. A case study that refits under
a corrected input artifact publishes new prediction identities and a snapshot that
supersedes the previous one; the retired rows stay in the registry, because the
record of what was superseded is evidence rather than litter. That record lives in
[[ML4T_A3_0001]], one layer above the tables joined below, so a query that
stops at [[ML4T_A3_0002]] sees two rows where the study has one. It cannot
separate them on the numbers either: a refit that changes only a declared input
leaves the computation, and therefore every metric, bit-identical, so a [[ML4T_A3_0003]] or an
[[ML4T_A3_0004]] would pick one arbitrarily and look like it had worked.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### Resolving a tie for rank one

Two rows can tie on mean daily IC for two different reasons, and only one of them is
an ambiguity. [[ML4T_A3_0001]] alone does not identify a configuration: a name can be
reused across generations while the parameters behind it move, so collapsing two such
rows would pick one by hash order. A refit that only re-declared an input, on the other
hand, leaves the row bit-identical apart from its two hashes. Requiring agreement on
every column except those two hashes separates the duplicate from the genuine
ambiguity without reading the training spec here.

There is a third case, and it is the one this chapter is about. Ridge at a shrinkage
small enough to be numerically inert reproduces OLS, and the registry then holds two
or three rows whose every recorded statistic agrees to the last digit and whose only
difference is the name of the configuration. [[ML4T_A3_0002]] at [[ML4T_A3_0003]]
carries exactly that: [[ML4T_A3_0004]], [[ML4T_A3_0005]] and [[ML4T_A3_0006]] at one IC, one standard
error and one day count. Nothing is ambiguous about the measurement, so the rows
collapse to the first name alphabetically and the others are carried in
[[ML4T_A3_0007]] and printed, rather than the notebook refusing to draw the section. A
tie that differs on any measured column is still a real ambiguity and still raises.

The excluded set is written as "everything except the two identities a refit moves"
rather than as a list of fields to compare, because a list is a second copy of
[[ML4T_A3_0008]] to keep in step: the first draft of one omitted [[ML4T_A3_0009]] and
[[ML4T_A3_0010]] while claiming to cover every recorded statistic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The primary-label collector applies the same completeness rule independently
to every case study before selecting the highest mean daily IC.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
HAC inference is rebuilt from the exact selected prediction artifact. Daily
correlations are sorted before the Bartlett Newey-West calculation, avoiding
the fold-order dependence in several stored registry intervals.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0015-p000

~~~~~~markdown
Recomputed inference replaces only the selected rows, preserving their exact
training and prediction identities for later coefficient and fold diagnostics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
Every grouped comparison fails closed when two artifacts tie for the highest daily
IC, so row order never decides which configuration a section reports.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
Fold diagnostics use the exact complete configurations selected above, rather
than independently ranking a second time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
Multi-label comparisons repeat the complete-coverage selection within every
case-study and label pair.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
## 1. Scope and Coverage

The linear family is the baseline against which Ch12 (gradient boosting),
Ch13 (deep learning for time series), and Ch14 (latent factors) are
compared. Each case study's primary label is fixed in
[[ML4T_A3_0001]]; the primary metric is mean daily cross-sectional Spearman IC.
Selection uses registry coverage and IC fields, while HAC inference is recomputed
from each selected prediction artifact after sorting daily IC chronologically.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## 2. Cross-CS Forest of Highest-IC Linear Configurations

For each case study, the linear configuration with the highest
mean daily IC on the primary label is plotted with its HAC interval.
Filled markers indicate [[ML4T_A3_0001]] (CI excludes zero); open
markers indicate the CI overlaps zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0029-p000

~~~~~~markdown
## 3. Regularization Comparison

How much does the choice of regularization family change the IC at
the primary label? For each case study we take the highest-IC OLS,
Ridge, Lasso, and ElasticNet configurations and compare their daily-
mean daily IC with HAC intervals, then trace the Ridge regularization path
with its HAC band. The axes carry the confidence level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
### Figure: Regularization Family Comparison

Missing families remain gaps rather than zeros in the grouped chart.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>
