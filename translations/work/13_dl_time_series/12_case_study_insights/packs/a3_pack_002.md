# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/12_case_study_insights.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Standard deviation → 標準差

## 待翻譯英文單元

### c0035-p000

~~~~~~markdown
### 4a. Per-fold IC distribution

For each DL-covered case study, the per-fold IC distribution of the highest-
IC configuration is shown as a box-plus-scatter, sorted left-to-right by
headline IC.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0038-p000

~~~~~~markdown
Fold summaries diagnose stability only. Inference remains attached to the
chronological daily IC series, not to the small collection of fold summaries.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
### 4b. Cross-fitted OOF fold calibration at the 90 % nominal level

The width measured here is the one the [[ML4T_A3_0001]] allocator sizes
positions with: calibrated per symbol on every residual known at [[ML4T_A3_0002]],
where [[ML4T_A3_0003]] is the sizing lag in data steps - [[ML4T_A3_0004]], one step
even where the horizon is zero, because the position was chosen before the row
that records its outcome - falling back to a quantile
pooled over every symbol where one has too few residuals of its own. A
decision is covered when its absolute residual falls inside that half-width.
A well-calibrated DL signal sits near the diagonal (empirical coverage =
nominal level); points below indicate the interval is too narrow, points
above that it is too wide. Per-CS interval width is reported in units of the
standard deviation of the outcomes it was measured against, so case studies
trading different return magnitudes stay comparable.

Read it as a diagnostic of residual dispersion, not a guarantee. Split
conformal's finite-sample coverage needs the calibration and evaluation
residuals to be exchangeable and return residuals are not, each OOF fold can
come from a different fitted model, and nothing in the allocation path reads
an interval or a coverage level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0043-p000

~~~~~~markdown
The complete calibration chart is assembled in one rendering cell. The
horizontal reference marks the nominal target, not a performance threshold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0047-p000

~~~~~~markdown
## 5. DL versus Tabular Baselines

The DL family enters a contested space - for every case study it is
compared to the highest-IC tabular configuration across linear, GBM, and
TabM. The selected models are rescored over the exact intersection of their
evaluation timestamps. The notebook does not infer uncertainty from a small set of
fold summaries.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
Apply the same complete-coverage selector to each tabular family before
choosing the strongest point estimate within a case study.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0052-p000

~~~~~~markdown
The comparison selects complete-coverage rows from each family, then
computes both point estimates from their shared evaluation timestamps. The
table does not estimate uncertainty for the difference between models.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
### 5a. DL versus highest-IC tabular baseline - scatter

The scatter plots the highest-IC tabular baseline on the x-axis and the
highest-IC DL configuration on the y-axis, one point per case study.
Points above the diagonal indicate DL exceeds the highest-IC tabular
baseline; points below indicate the tabular baseline tops the DL signal.
Marker shape identifies the selected tabular family; color shows only the
direction of the point-estimate difference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0056-p000

~~~~~~markdown
A common scale and equality line make the point-estimate comparison
interpretable without implying paired uncertainty.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0058-p000

~~~~~~markdown
Shape identifies the selected tabular family; fill identifies only the
direction of the observed difference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0060-p000

~~~~~~markdown
The figure is created only after all drawing helpers are defined.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0063-p000

~~~~~~markdown
### 5b. When does DL help? Diagnostic table

The same delta cross-referenced with panel-level features: data frequency,
universe size (entities), and the highest-IC tabular family. The rows are
sorted by the DL-minus-tabular point-estimate delta, largest first.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0066-p000

~~~~~~markdown
## 6. Multi-Label Horizon View

Only case studies with at least two complete registered regression labels
enter the horizon figure. Single-point series are excluded rather than
padded.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0068-p000

~~~~~~markdown
Only complete registered labels enter the horizon census and figure, and "complete"
is measured against the case study's own fold grid rather than against what the run
declared. [[ML4T_A3_0001]] sets [[ML4T_A3_0002]] and scores four of
that case study's sixteen modelling folds on a Friday-resampled panel, so its
[[ML4T_A3_0003]] point is a weekly IC over a quarter of the grid. Drawn on this figure it
would join the daily [[ML4T_A3_0004]] point on a shared "average daily IC" axis and read
as one quantity moving with horizon. A cell whose grid could not be derived is kept,
because "not measured" is not "measured and short", and the cell below prints how many
of the retained cells that covers.

The grid fails to derive for two different reasons, and the printed count does not
separate them. On this worktree it is the two intraday case studies, whose fold
boundaries carry a time of day that [[ML4T_A3_0005]] refuses. The second reason
reaches a reader rather than us: [[ML4T_A3_0006]] is gitignored and the release
bundle ships [[ML4T_A3_0007]] alone, so running this chapter from a downloaded bundle derives
no grid for any case study. That prints "not derivable" for every retained cell and
excludes nothing - including the [[ML4T_A3_0008]] weekly point this filter exists to
exclude. A census reading "17 of 17" means the label surfaces are absent, not that
seventeen grids were checked and found underivable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>
