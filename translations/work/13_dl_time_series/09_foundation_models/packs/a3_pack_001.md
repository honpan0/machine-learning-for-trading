# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/09_foundation_models.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Walk-forward validation → 滾動向前驗證
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Time series foundation models, applied to a panel they never saw

**Docker image**: [[ML4T_A3_0001]]

Every model so far in this section was fitted on this ETF panel. A **time series
foundation model** is pretrained on a large, mostly non-financial corpus and asked
to forecast a new series with no fitting at all - the transfer story that reshaped
language and vision, applied to sequences of numbers.

Two are run here in that zero-shot mode: **Chronos** (Amazon), which quantises a
series into tokens and runs a T5 encoder-decoder over them, and **TinyTimeMixer**
(IBM Granite), a small mixing architecture in the family [[ML4T_A3_0002]] builds. They
are scored against two models fitted on this panel: an LSTM and a penalised linear
map. All four read the same thing - one feature column, [[ML4T_A3_0003]] days of it
- so the input is held fixed and what differs is whether the model was fitted here
and what it was asked to produce.

**What the comparison actually asks.** The zero-shot models forecast the context
series itself for [[ML4T_A3_0004]] steps, and the mean of that path is used as a
score for ranking funds. The label is a [[ML4T_A3_0005]]-session forward return, and
the two horizons are not tied together. So this is a probe of whether a zero-shot
forecast ranks assets usefully, not a calibrated forecast of the label - which is
why the results table below leaves MSE blank for those rows and reports only rank
IC.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Learning objectives**:
- Run a pretrained forecaster with no fitting step and say exactly what it was given
  and what it returned.
- State what a rank-IC comparison between a forecast of one quantity and a label of
  another can and cannot establish.
- Name the design choices that bound this result - one feature, first-generation
  models, a fixed horizon, zero-shot only - and separate them from the published
  findings the notebook cites.

**Key references**:
- Rahimikia et al. (2025): zero-shot TSFMs on financial series
- DELPHYNE (Ding et al., 2025): negative transfer from financial pretraining data
- Rasul et al. (2024), Lag-Llama: probabilistic forecasting

**Book Reference**: Chapter 13, Section 13.6 (Alternative architectures and foundation models)

**Prerequisites**: ETF features ([[ML4T_A3_0001]])
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0002-p000

~~~~~~markdown
Three of the settings below decide what the comparison is, rather than tuning it.

[[ML4T_A3_0001]] is the horizon the zero-shot models forecast over. It is held
fixed and deliberately not tied to the label's horizon, because these models are
being used as a ranking signal rather than as a forecast of the label; the design
note further down says what that costs.

[[ML4T_A3_0002]] is how many trading sessions pass between a decision date and the
day its label resolves. The ETF case study's primary label is a close-to-close
return over that many sessions, and the split drops every example within one horizon
of a boundary.

[[ML4T_A3_0003]] decides what happens when Chronos or TTM fails at
*runtime*: True raises, False leaves a null row in the results table. It does not
govern missing installs - both libraries are imported at module load, so they have
to be present either way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0005-p000

~~~~~~markdown
## Data Loading

ETF features and labels from the case study pipeline. Every model in this notebook
reads the same univariate context - one feature column, [[ML4T_A3_0001]] days long.
The eight columns selected here are used to decide which rows are complete, not as
model inputs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Prepare Univariate Contexts

Foundation models expect univariate time series contexts. We extract
the first feature column (typically close returns) per symbol and build
sliding windows of length [[ML4T_A3_0001]]. Each window is paired with
the forward return label at the next timestep.

**Design note on horizon and target alignment.** The zero-shot baseline
below forecasts the *first feature column* for [[ML4T_A3_0002]] steps
and uses the mean of that forecast path as a directional score, which is
then compared cross-sectionally to the label [[ML4T_A3_0003]]. The forecast
horizon ([[ML4T_A3_0004]]) is held fixed across models and does
not necessarily match the label horizon - for the ETF case study used
here, the label is a multi-day forward return. The experiment is therefore
a *directional-signal probe*, not a calibrated forecast of the label
itself: it tests whether a zero-shot foundation model's mean forecast on
raw historical values produces a useful ranking of assets at the next
rebalance, against the same ranking from a task-specific baseline. Tying
[[ML4T_A3_0005]] to the label horizon and explicitly aggregating the
forecasted path into the same target definition would let foundation
models be evaluated on the label directly; that variation is left as an
exercise and would change the numerical comparisons that follow.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
## Temporal Train/Test Split

A 60/20/20 split by date, the same shape the rest of this section uses, rather than
walk-forward validation: foundation model inference is expensive and the comparison
here is zero-shot against trained, not a claim about stability over time.

The split has to be indexed by date and not by row. These samples are pooled across
assets, so a positional slice would cut through a cross-section and put the same day
on both sides of a boundary.

It also needs a gap. The label is a close-to-close return over [[ML4T_A3_0001]]
trading sessions, so an example dated within that many sessions of a boundary has an
outcome resolved by days on the far side. Without the gap the LSTM would be fitted
on targets that resolve inside the validation stretch, and selected on targets that
resolve inside the test stretch. Those examples are dropped.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The three sample caps below are for local iteration only and the shipped run leaves
them at [[ML4T_A3_0001]]. They are worth understanding before using: they keep the *last* rows
of an index that is ordered by symbol and pooled across assets, so a non-[[ML4T_A3_0002]] cap
returns an arbitrary subset of symbols and a possibly partial cross-section, which
makes the per-date IC depend on symbol ordering. [[ML4T_A3_0003]] and
[[ML4T_A3_0004]] show the alternative: trim to the most recent complete dates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>
