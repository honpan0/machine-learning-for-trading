# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/06_conformal_prediction.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Training set → 訓練集
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0017-p001

~~~~~~markdown

1. **All assets on a decision date share one [[ML4T_A3_0001]].** We predict
   every ETF on date [[ML4T_A3_0002]] before any of their outcomes exist. Updating alpha
   between assets within a date would let one ETF's realized return set
   another ETF's interval at the same timestamp.
2. **An outcome is only observable 21 sessions after its decision date.**
   The return labeled at date [[ML4T_A3_0003]] is not known until [[ML4T_A3_0004]]. Feeding it
   back any earlier is a look-ahead, however "online" the loop looks.

So the feedback is *delayed*: on decision date [[ML4T_A3_0005]] we build intervals from
the current alpha, then update alpha using only the miss rate of date
[[ML4T_A3_0006]], whose outcomes have just resolved. Each date is one online round,
and the indicator generalizes to that date's cross-sectional miscoverage
rate. The first 21 dates of a fold run at the target alpha because nothing
has resolved yet, and that warm-up is a real property of the method, not an
implementation shortcut.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p001>>>
<<<ML4T-ZH-END:c0017-p001>>>

### c0019-p000

~~~~~~markdown
## Run Conformal Evaluation

We evaluate all three methods (SC, CQR, ACI) across the walk-forward folds.
For each fold, the training set is split 80/20 into model-training and
calibration subsets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
The fitted results are cached so a re-read of the notebook does not refit three
conformal methods across every fold. What the cache is keyed on decides whether
that is a convenience or a hazard. Keyed on the file existing, an edit to any of
the code below would leave the previous run's numbers on the page underneath the
new source, and nothing downstream would notice: the provenance stamp binds this
[[ML4T_A3_0001]] to its [[ML4T_A3_0002]], and after an edit and a re-run both of those are current.
So the cache carries a signature of the notebook's own source, the two input
files, the exact cleaned arrays and the settings that change a fit, and a run
that does not match it refits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0024-p000

~~~~~~markdown
## Calibration Analysis

A well-calibrated conformal predictor should achieve actual coverage close
to the target. We compare the three methods across folds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### Calibration Metrics at the Target Coverage Level
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
**How to read the table.** Four of its columns answer different questions, and
the methods do not rank the same way on all four.

[[ML4T_A3_0001]] is the distance from the target. Under-coverage is the direction
an exchangeability violation predicts: walk-forward evaluation
on non-stationary returns is exactly the assumption the marginal guarantee needs
and does not get.

[[ML4T_A3_0002]] is what the coverage cost. Split conformal fixes one width per
fold, so every observation pays the same premium whether or not its own
uncertainty warrants it. CQR sets the width per observation, which is why it can
buy coverage more cheaply. ACI adjusts one width for the whole cross-section on
each decision date, in response to how the previous dates turned out.

[[ML4T_A3_0003]] is how much a method lets the width move at all, and [[ML4T_A3_0004]] is
how steady its coverage is from one fold to the next. These two are the trade:
a method that holds width constant has nothing to absorb a regime change with,
and its coverage moves instead.

ACI's feedback is 21 sessions stale by construction, because that is when the
label resolves. It can only track drift slower than the label does, and no
choice of step size changes that; the lag is a property of the trading problem,
not of the method.

Read the conditional-coverage table further down before trusting any of these
three marginal numbers. They hide a failure that matters more than the
differences between them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
## Calibration and Rolling Coverage Figure

The figure has two panels: pooled coverage per method against the target level,
and the same three methods' coverage fold by fold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
## Multi-Level Calibration

For the nine target levels in [[ML4T_A3_0001]], evenly spaced across the unit
interval, we plot the requested level against the empirical one. A well-calibrated
method tracks the diagonal.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
Persist the multi-level calibration curve to disk so downstream analyses
can read it without rerunning the walk-forward sweep.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0037-p000

~~~~~~markdown
**What to read off it.** A point above the diagonal is conservative coverage,
intervals wider than the level required; a point below it is under-coverage. The
curve sits below the diagonal here rather than on or above it, and that is the
expected direction: the finite-sample guarantee assumes exchangeability, and
walk-forward evaluation on non-stationary returns breaks it. CQR and ACI are the
response to that violation, and the table above is where their cost shows up.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0038-p000

~~~~~~markdown
## ACI Adaptation Dynamics

The ACI method adjusts [[ML4T_A3_0001]] once per decision date, as the labels of the
date 21 sessions earlier resolve. When those intervals under-covered, [[ML4T_A3_0002]]
**falls**, which raises the residual quantile and widens subsequent intervals.
When they over-covered, [[ML4T_A3_0003]] rises and intervals tighten. The trajectory
below is therefore a response to coverage 21 sessions stale, which is what the
method actually has to work with.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
**What to read off it.** The path only rises while the dates whose labels have
resolved over-covered, and only falls while they missed too often, so it is a
running record of that fold's realized coverage, lagged by the label horizon.
Its level is a different thing from its direction. Alpha settles wherever the
calibration quantile it selects delivers the target miss rate, and that place
need not be the nominal alpha: a path that leaves the target line and stays away
says the pooled calibration scores needed that much adjustment to cover at the
requested rate, not that the intervals are still missing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0041-p000

~~~~~~markdown
## Interval Width Comparison

CQR should produce **adaptive** intervals (wider in volatile periods, narrower
in calm periods), while split-conformal produces constant-width intervals.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
**What to read off it.** Split conformal fixes one width per fold, so its panel is
a small number of spikes and the spread across that panel is fold-to-fold variation
alone. CQR and ACI set the width per observation, so theirs spread continuously.
The three width axes are not shared: compare the shape of each panel, and read the
levels off the width table above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>
