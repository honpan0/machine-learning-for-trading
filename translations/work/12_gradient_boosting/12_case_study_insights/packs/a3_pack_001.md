# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/12_case_study_insights.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Case Study Insights: Gradient Boosting

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: assemble the cross-case-study view of LightGBM and contrast it
with the linear baseline (Ch11) and the tabular deep-learning variant (TabM).
Per-case-study deep dives live in [[ML4T_A3_0002]];
this notebook is the comparative view across all nine case studies.

**Learning objectives**

- For each case study, read the highest-IC GBM configuration's average daily
  Spearman IC with HAC interval on the primary label
- Compare GBM design choices - loss function, tree depth, optimal iteration
  count - and locate the operating regime that achieves the highest IC
- Inspect per-fold IC distributions and the validation to holdout decay where
  the holdout retrain has been run
- Compare full-coverage GBM and linear daily-IC point estimates without
  treating fold summaries as an uncertainty estimator, faceted across labels
- Extend the comparison across labels (horizon view) and across the
  classification ↔ regression metric symmetry
- Inspect feature-importance rank shift versus the linear baseline, per-fold rank
  stability, and the TabM-vs-GBM-vs-linear three-way picture

**Book reference**: Section 12.6 - Case study insights.

**Prerequisites**: each case study's [[ML4T_A3_0003]] pipeline has populated
[[ML4T_A3_0004]] for the GBM family. Where present, [[ML4T_A3_0005]]
adds TabM rows. Teaching notebooks NB01-NB11 cover the underlying techniques.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Scope and Coverage

The GBM grid spans four tree-depth profiles
(7 / 15 / 31 / 63 leaves) × 3 regression loss functions (MSE / MAE /
Huber), evaluated at 10 boosting checkpoints per configuration. Direction
labels add a binary-logistic variant. The headline metric is average daily
cross-sectional Spearman IC with a HAC confidence interval on the primary label
([[ML4T_A3_0001]], [[ML4T_A3_0002]], [[ML4T_A3_0003]], [[ML4T_A3_0004]]).
The linear family (Ch11) and TabM ([[ML4T_A3_0005]]) are loaded as baselines.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Cross-CS Forest of Highest-IC GBM Configurations

For each case study, the GBM configuration with the highest average daily IC
on the primary label is plotted with its HAC interval. Filled markers
indicate [[ML4T_A3_0001]] (CI excludes zero); open markers indicate the CI
overlaps zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
The next cell derives the cross-case conclusion from the selected rows, naming
no case study or value that it has not just computed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## 3. Within-Family Comparison

How much does each design knob change the IC at the primary label? Three
subsections trace the structured grid: loss function (3a), tree depth (3b),
and checkpoint dynamics (3c). Each is presented with HAC intervals so the
resolution between operating points stays explicit.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### 3a. Loss function (MSE / MAE / Huber)

For each case study, the highest-IC configuration is selected within each
regression loss family, then the three (case study, loss) IC values are plotted
side by side with HAC interval bars.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0016-p000

~~~~~~markdown
The helper adds bars and intervals without rendering an unfinished figure
between notebook cells.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
Shared labels and a zero line make the grouped confidence intervals comparable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0022-p000

~~~~~~markdown
### 3b. Tree depth heatmap

Within each case study, the highest IC achieved by each leaf profile -
7 / 15 / 31 / 63 leaves - is shown as a heatmap cell. Panels with a
clean diagonal favor a specific depth; panels that are nearly flat across
leaves indicate the depth knob has no resolution at this signal-to-noise
ratio.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0025-p000

~~~~~~markdown
### 3c. Checkpoint dynamics

Where in the boosting trajectory does the highest-IC checkpoint sit? For
each case study we plot the highest-validation-IC GBM configuration's mean
cross-sectional IC against the boosting checkpoint (number of trees,
50–500). The trajectory is read from [[ML4T_A3_0001]] written by
the boosting runner during training; the final early-stopped checkpoint is
the IC that propagates to the selected row in [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0028-p000

~~~~~~markdown
Small multiples keep each trajectory on its own axis while sharing the tree budget.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0032-p000

~~~~~~markdown
## 4. Stability and Uncertainty

Average daily IC with HAC CI is the headline metric. Per-fold IC is the
stability diagnostic, and the validation→holdout decay is the
generalization diagnostic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
### 4a. Per-fold IC distribution

For each case study's highest-IC GBM configuration, the per-fold IC
distribution is shown as a box-plus-scatter. The reference comparison is
Ch11 §4 - the linear panels frame the GBM panels' fold-stability picture.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0037-p000

~~~~~~markdown
### 4b. Validation → holdout decay dumbbell

Where the holdout retrain has been run, the validation-fold IC and the
nested-holdout IC are linked by a dumbbell. The case studies without GBM
holdout rows in the registry are excluded - the gap is explicit, not
silent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>
