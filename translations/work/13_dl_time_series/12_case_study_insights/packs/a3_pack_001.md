# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/12_case_study_insights.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Deep learning → 深度學習
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# What the architectures did across the book's case studies

**Docker image**: [[ML4T_A3_0001]]

Every notebook in this chapter demonstrated an architecture on one split of one
panel, and each said in its own words that a single split cannot rank
architectures. This notebook is where the ranking question is actually asked. It
reads the registry - the stored results of walk-forward runs on whichever case
studies carry deep-learning pipelines - and compares LSTM, NLinear, TSMixer,
TCN and PatchTST against each other and against the linear baseline of Chapter 11,
the gradient-boosted models of Chapter 12, and the tabular network TabM.

Nothing here is trained. Every number is read from runs that already happened, which
is why this is the only place in the chapter where a comparison spans datasets, and
why the per-case-study detail lives elsewhere, in
[[ML4T_A3_0002]].

**Two things to hold on to while reading.** Each comparison is restricted to
configurations that covered the same folds and the same number of days, so a model
evaluated on an easier or shorter window cannot win by that alone. And a spread of
per-fold results is a description of the folds, not a confidence interval - the HAC
intervals on daily IC are the uncertainty estimate, and the fold violins are not.

**Learning objectives**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Read an average daily Spearman IC with a HAC 95 % interval and say what the
  interval does and does not cover.
- Trace the architecture-by-case-study coverage map, and notice which cells are
  empty before reading the ones that are full.
- Read per-fold distributions, checkpoint trajectories and conformal coverage as
  diagnostics of a run rather than as scores.
- Compare deep learning against the strongest tabular family on shared timestamps,
  and say why a point-estimate difference is not a test.
- Place each architecture in its class - recurrent, MLP-style, convolutional,
  attention - and ask whether the class explains more than the individual model.

**Book reference**: Section 13.7 (A practical framework) and Section 13.9
(Case study insights).

**Prerequisites**: each case study's per-architecture training notebooks
([[ML4T_A3_0001]], [[ML4T_A3_0002]], [[ML4T_A3_0003]], [[ML4T_A3_0004]], [[ML4T_A3_0005]])
have populated that study's [[ML4T_A3_0006]] for the [[ML4T_A3_0007]] family. The
linear, GBM, and TabM baselines come from Ch11-Ch12 pipelines.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
One warning is silenced, by message and module rather than by a blanket filter.
polars cannot verify that a frame is sorted once [[ML4T_A3_0001]] groups are given, and says so
on every grouped [[ML4T_A3_0002]]. [[ML4T_A3_0003]] sorts by entity and
step itself immediately before each of those joins, which is exactly the
precondition the warning is about, so the warning reports a check polars could not
perform rather than a problem. Every other warning, from that module or anywhere
else, still reaches the output.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0007-p000

~~~~~~markdown
**Architecture helper**: maps registry [[ML4T_A3_0001]] values to the display
names used across every downstream table and figure so the four LSTM
variants collapse to a single [[ML4T_A3_0002]] row and the per-architecture grids
stay consistent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
Architectural classes support the aggregate comparison, while the complete
grid loader keeps missing architectures explicit.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
Every comparison below ranks only configurations that covered the same folds and the
same number of days, so a model evaluated on a shorter or easier window cannot come
out ahead on that account.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
## 1. Scope and Coverage

The DL grid varies across the case studies - not every architecture trains
on every panel, and US Firm Characteristics (monthly cross-section) carries
no DL family at all. The headline metric is the average daily Spearman IC
with HAC 95 % confidence interval on each case study's primary label
([[ML4T_A3_0001]], [[ML4T_A3_0002]], [[ML4T_A3_0003]], [[ML4T_A3_0004]]).
The linear (Ch11), GBM (Ch12), and TabM ([[ML4T_A3_0005]], Ch12) baselines are
loaded so the §5 delta is computable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0015-p000

~~~~~~markdown
Architecture coverage is computed from full-day, exact-fold candidates. A
missing family stays missing rather than being filled with a shorter-span or
stale candidate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 2. Cross-CS Forest of Highest-IC DL Configurations

For each DL-covered case study, the architecture and configuration with
the highest average daily IC on the primary label is plotted with its HAC
95 % CI. Filled markers indicate [[ML4T_A3_0001]] (CI excludes zero); open
markers indicate the CI overlaps zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0022-p000

~~~~~~markdown
## 3. Within-Family Comparison

Three subsections trace the architecture grid: the highest IC by architecture
inside each case study (3a), the aggregate count of which architecture
achieves the highest IC (3b), and the per-checkpoint IC trajectory of the
highest-IC configuration on each case study (3c).
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
### 3a. Architecture × case-study heatmap

Within each case study, the highest IC achieved by each architecture is shown as a
heatmap cell. A blank cell means no eligible run, which covers two situations: the
architecture was never trained on that case study, or it was but its runs did not
cover the same folds and the same number of days as the rest of the row. Both are
coverage facts and neither is a low score, so they stay blank rather than being
filled in.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0026-p000

~~~~~~markdown
### 3b. Aggregate: which architecture achieves the highest IC most often

Counting across DL-covered case studies, how often does each architecture
achieve the highest IC at the primary label? The bar is annotated with the
mean IC of the case studies where the architecture achieves the highest IC
(the table above also reports the min/max across those case studies) -
magnitudes matter as much as counts.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0030-p000

~~~~~~markdown
### 3c. Checkpoint dynamics

For each case study's highest-IC DL configuration, the per-checkpoint
(epoch) IC trajectory is plotted with the IQR band across folds. Peaked
curves identify clear early-stopping value; flat curves indicate the
optimization landscape is benign across the budget.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0034-p000

~~~~~~markdown
## 4. Stability and Uncertainty

Average daily IC with HAC CI is the headline metric. Per-fold IC is the
stability diagnostic; conformal coverage is the calibration diagnostic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>
