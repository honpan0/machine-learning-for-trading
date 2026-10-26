# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/08_cnn_image_encoding.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Test set → 測試集
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Turning a window into a picture: GAF and MTF encodings

**Docker image**: [[ML4T_A3_0001]]

Every architecture in this section so far has kept the window as a sequence and
argued about how to relate its positions - attention, dilated convolution, mixing,
a recurrent state. This notebook takes a different route: it turns each window into
a two-channel image and hands it to an ordinary image CNN, so that the whole
apparatus built for pictures applies unchanged.

The encodings are the point. A **Gramian angular field** rescales the window to
[[ML4T_A3_0002]], reads each value as an angle, and fills cell [[ML4T_A3_0003]] with a function of
the two angles - so the image is a table of every pair of positions, and a
convolution over it reads relations between pairs rather than between values. A
**Markov transition field** bins the window into quantiles and fills cell [[ML4T_A3_0004]]
with how often the series moved between the bins those two positions fall in.

What the transformation discards is as important as what it builds, and both
encodings below discard the same thing: they normalise inside each window, so the
level and the range of the returns are gone before the CNN sees anything. Two
windows of the same shape and different volatility become the same picture.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Learning objectives**:
- Build both encodings from the definition and say what each cell of the resulting
  matrix means.
- Say what the per-window normalisation throws away, and why that matters for a
  label whose scale is a return.
- Read the resampling step: a [[ML4T_A3_0001]]-day window becomes an
  [[ML4T_A3_0002]]-by-[[ML4T_A3_0003]] image, so check whether that interpolates up or
  summarises down before treating pixels as data.
- Score the CNN against a penalised linear map on the same flattened pixels, so the
  comparison isolates the CNN and not the encoding.

**Book Reference**: Chapter 13, Section 13.6 (Alternative architectures and foundation models)

**Prerequisites**: ETF features ([[ML4T_A3_0004]])
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## Data Loading

We use the five-day ETF return from the case-study pipeline. Both models see
exactly the same one-feature windows.
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
### Pedagogical subsampling

The GAF/MTF encoding loop produces one (image_size x image_size x 2) tensor
per sample, so the full ETF panel takes considerable wall-clock to encode.
We cap each split at a few tens of thousands of sequences for tractable
runtime. Critically we subsample by **complete dates**, not row count: the
sequence array can begin or end partway through a date, so a raw row slice
would leave a partial cross-section. Keeping the most recent complete dates
instead gives a stable, full cross-section that reproduces across runs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Cross-sectional IC helper

Mean cross-sectional Spearman IC by date - the same metric used across this section,
so the image CNN is scored the way the sequence models were.

A date's IC is undefined when a model predicts the same value for every fund on it:
the predicted ranks are all tied and there is nothing to correlate. The library
returns [[ML4T_A3_0001]] for such a date, and polars treats [[ML4T_A3_0002]] and null as different values,
so [[ML4T_A3_0003]] alone leaves it in place and one of them makes the whole mean [[ML4T_A3_0004]].
Both are filtered here, and the count of dates the mean was taken over is printed
beside it - which matters here, because the subsampling above leaves far fewer dates
than the notebooks that score on the full panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Gramian Angular Summation Field (GASF)

The GASF encodes a time series as a matrix of trigonometric sums. Given a
normalized series [[ML4T_A3_0001]], we compute angles
[[ML4T_A3_0002]] and form:

[[ML4T_A3_0003]]

This preserves temporal ordering. The diagonal evaluates to
[[ML4T_A3_0004]] - a deterministic function of the
normalized value, not the value itself - while off-diagonal entries capture
pairwise angular relationships between time steps [[ML4T_A3_0005]] and [[ML4T_A3_0006]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Markov Transition Field (MTF)

The MTF discretizes a time series into [[ML4T_A3_0001]] quantile bins and builds a
transition matrix [[ML4T_A3_0002]] where [[ML4T_A3_0003]] is the probability of
transitioning from bin [[ML4T_A3_0004]] to bin [[ML4T_A3_0005]]. The full MTF matrix is:

[[ML4T_A3_0006]]

where [[ML4T_A3_0007]] is the quantile bin of the [[ML4T_A3_0008]]-th timestep. This captures the
dynamic transition structure of the series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## Create Multi-Channel Image Dataset

For each one-feature sequence, we encode the return history as a GASF and an MTF,
then stack them as a 2-channel image. This gives the CNN both angular
structure (GASF) and transition dynamics (MTF) as complementary views.

> **Simplification**: This demo encodes only the five-day return history. A production
> system would encode all features, stacking GASF+MTF per feature to produce a
> [[ML4T_A3_0001]]-channel image. We use one
> feature here to keep encoding time manageable and focus on the method itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## Encode Training, Validation, and Test Sets
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## Visualize Sample Encodings

Inspecting the GASF and MTF channels for a few training samples to verify
the encoding produces visually distinct patterns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## CNN Architecture

Three convolutional blocks (Conv2d [[ML4T_A3_0001]] BatchNorm [[ML4T_A3_0002]] ReLU [[ML4T_A3_0003]] MaxPool)
followed by adaptive average pooling and a linear regression head.
The architecture is intentionally simple to isolate the contribution of
the image encoding from the model complexity.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### Full Image CNN

Three CNN blocks downsample the spatial dimensions by [[ML4T_A3_0001]] each,
followed by adaptive average pooling to a fixed-size vector regardless
of the input image size. Dropout before the final linear layer provides
regularization.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
