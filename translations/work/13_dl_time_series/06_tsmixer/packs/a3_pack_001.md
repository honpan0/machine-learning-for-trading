# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/06_tsmixer.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Test set → 測試集
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# TSMixer: mixing one axis at a time

**Docker image**: [[ML4T_A3_0001]]

[[ML4T_A3_0002]] let one position in the window depend on another through
attention, and [[ML4T_A3_0003]] did the same through dilated convolution. Both are devices
for relating positions. A fully connected layer already relates every input to every
other, so the question TSMixer (Chen et al., 2023) asks is not whether to use one but
along which axis to apply it.

Its answer is to alternate, and never to mix both axes in a single layer. A
**time-mixing** layer applies one shared linear map across the [[ML4T_A3_0004]] days, the
same map for every feature. A **feature-mixing** layer applies a small MLP across the
features, separately at each day. Stacking the two lets a representation depend on
both axes at a cost of [[ML4T_A3_0005]] mixing weights along time and [[ML4T_A3_0006]] across features,
where a single dense layer over the flattened window would cost [[ML4T_A3_0007]]. The model
prints its parameter count below, so the arithmetic is checkable.

**Learning objectives**:
- Read a tensor's axes well enough to say what a permutation before a [[ML4T_A3_0008]] layer
  changes about which numbers get combined.
- Build the two mixing layers and say what each one can and cannot represent: the
  time-mixing map is the same for every feature, and the feature-mixing MLP is the
  same at every day.
- Say what the residual connection and the pre-normalisation are for in a stack that
  has no recurrence and no convolution to stabilise.
- Score the result against a penalised linear map on the same flattened window,
  which is the comparison that decides whether the mixing structure earned
  anything.

**Book Reference**: Chapter 13, Section 13.6 (Alternative architectures and foundation models)

**Prerequisites**: ETF features ([[ML4T_A3_0009]])
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## Data Loading

We use eight fixed momentum horizons from the ETF case-study pipeline.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## Sequence Creation and Temporal Split
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Splitting by date, with a gap for the label horizon

The split is by date, at fixed fractions of the trading days, and an example belongs
to the partition the date it carries falls in. The label is a [[ML4T_A3_0001]]-day
forward return, so an example dated within that many days of a boundary has an
outcome resolved by days on the far side; those examples are dropped. Input windows
may still reach back over a boundary, which is right - at decision time the model has
every past observation available.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Cross-sectional IC helper

Mean cross-sectional Spearman IC by date - the same metric used in
[[ML4T_A3_0001]], [[ML4T_A3_0002]] and [[ML4T_A3_0003]], so the comparison anchors
on one per-date rank correlation across the section's architectures.

A date's IC is undefined when a model predicts the same number for every fund on it:
the predicted ranks are all tied and there is nothing to correlate. The library
returns [[ML4T_A3_0004]] for such a date, and polars treats [[ML4T_A3_0005]] and null as different values,
so [[ML4T_A3_0006]] alone leaves it in place and one of them makes the whole mean [[ML4T_A3_0007]].
Both are filtered here, and the count of dates the mean was taken over is printed
beside it, so a model that ties often is visible rather than averaged over whichever
dates happened to survive.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## TSMixer Architecture

TSMixer alternates between two types of MLP blocks:

1. **Time-mixing**: Transposes to [[ML4T_A3_0001]] and applies the
   same temporal projection to every feature channel
2. **Feature-mixing**: Applies an MLP along the feature axis -- each timestep
   learns cross-variate interactions

Both use pre-normalization and residual connections. This is conceptually
similar to the MLP-Mixer vision architecture, adapted for time series. The
block below follows the authors' basic TSMixer implementation: one temporal
projection followed by a two-layer feature MLP.

The mixing operations can be written as:

[[ML4T_A3_0002]]

for time-mixing, and similarly without the transpose for feature-mixing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Feature-Mixing MLP

Operates directly on the feature dimension at each timestep, learning
cross-variate interactions without transposing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Mixer Block

Pairs one time-mixing step with one feature-mixing step, forming the
fundamental building block of TSMixer.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### TSMixer Regressor

Stacks multiple mixer blocks and applies the paper's temporal forecast
projection with output length one. A small feature adapter then maps those
per-feature forecasts to the single cross-sectional return label.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
## Train TSMixer
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0024-p000

~~~~~~markdown
## Evaluate on Test Set
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## Ridge Baseline Comparison

Flattening the 3D input to 2D and fitting Ridge regression provides a
simple linear baseline to gauge whether TSMixer's learned mixing adds value.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## The mixer against the linear baseline

Two questions, two panels. The left asks whether the model ordered the funds usefully
on each date; the right asks whether its predicted return levels were closer than
predicting zero. A model can do better on one and worse on the other, and both are
reported because acting on a forecast uses the ordering while fitting one minimises
the squared error.

The ridge regression is the comparison that decides anything. It sees the same window
flattened into one vector and fits a penalised linear map straight to the label: [[ML4T_A3_0001]]
coefficients, no hidden representation, and no notion that one axis is time and the
other is features. Whatever the alternating structure is worth has to appear as a
difference from that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
The left panel measures cross-sectional ranking, while the right panel asks
whether either fitted model improves squared error over predicting zero. These
are distinct questions. This purged single split demonstrates the architecture;
it does not establish a stable model ranking. Section 13.9 supplies the
walk-forward comparison across datasets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>
