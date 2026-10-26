# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/05_tcn.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Test set → 測試集
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Temporal Convolutional Network

**Docker image**: [[ML4T_A3_0001]]

[[ML4T_A3_0002]] measured the cost of walking a window one day at a time, and
[[ML4T_A3_0003]] answered it with attention. This notebook takes the third route:
convolution, which reads the whole window in parallel like the fully connected
network but, unlike it, respects the ordering of the days.

A plain convolution has two problems for forecasting. Its filter reads in both
directions from each position, so the output at day [[ML4T_A3_0004]] mixes in days after [[ML4T_A3_0005]]; and
its reach is the width of that filter, so covering sixty days would take a very wide
filter or very many layers. A **temporal convolutional network** answers both. Its
convolution is *causal* - the output at day [[ML4T_A3_0006]] is a function of days up to [[ML4T_A3_0007]] and
no later - which is what makes every position a legitimate forecast for its own date.
And it multiplies the gap between the positions each filter reads by two at every
layer - a *dilation* - so the reach grows geometrically with depth rather than
linearly.

**Learning objectives**:
- Build a causal convolution and check which inputs each output can actually see,
  rather than trusting the word "causal" in the class name.
- Stack dilated blocks so the receptive field - the span of input one output depends
  on - covers the whole window, and compute that span rather than assuming it.
- Explain what a residual connection is doing in a stack this deep, and why the block
  normalises weights rather than activations.
- Score the result against a penalised linear map on the same window, which is the
  comparison that decides whether the convolutional structure earned anything.

**Book Reference**: Chapter 13, Section 13.6 (Alternative architectures and foundation
models).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Prerequisites**: [[ML4T_A3_0001]]; ETF features from [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## The data

The same ETF case-study panel [[ML4T_A3_0001]] used: eight trailing-return features
per fund per date, and a 21-day forward return as the label. Keeping the data fixed
across the chapter's architecture notebooks is what lets their results be read
against each other at all, and it is why [[ML4T_A3_0002]] can aggregate them.

The panel's breadth is worth printing before anything is fitted, because the scoring
metric is computed across whatever funds exist on each date, and that count moves as
funds launch.
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

Mean cross-sectional Spearman IC by date - TCN evaluation is on cross-asset
ranking, not pooled point error, so the same date/entity-aware metric used in
[[ML4T_A3_0001]] and [[ML4T_A3_0002]] is the right comparison anchor.

A date's IC is undefined when a model predicts the same number for every fund on
it: the predicted ranks are all tied and there is nothing to correlate. The library
returns [[ML4T_A3_0003]] for such a date, and polars treats [[ML4T_A3_0004]] and null as different values,
so [[ML4T_A3_0005]] alone leaves it in place and one of them makes the whole mean [[ML4T_A3_0006]].
Both are filtered here, and the count of dates the mean was actually taken over is
printed beside it, so a model that ties often is visible rather than averaged over
whichever dates happened to survive.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
> **Note**: This fixed 60/20/20 split is a pedagogical simplification. Its
> 21-day purge keeps forward-label windows disjoint, but production deployment
> still requires the expanding walk-forward protocol from Chapter 6.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0013-p000

~~~~~~markdown
## TCN Architecture

The TCN consists of stacked causal convolution blocks with exponentially
increasing dilation factors. Each block uses:

1. **Causal padding**: pad both ends by [[ML4T_A3_0001]] and drop the right-hand
   overhang, which is identical to padding only on the left - the output at [[ML4T_A3_0002]]
   depends on inputs up to [[ML4T_A3_0003]] and no later, and the sequence keeps its length
2. **Dilated convolutions**: Dilation factors of 1, 2, 4, 8 give an
   exponentially growing receptive field
3. **Residual connections**: Enable training deeper networks
4. **Weight normalization and channel dropout**: Match the reference TCN
   residual block without mixing information across batch members

The receptive field grows as:

[[ML4T_A3_0004]]

where [[ML4T_A3_0005]] is kernel size, [[ML4T_A3_0006]] is the dilation at layer [[ML4T_A3_0007]], and
[[ML4T_A3_0008]] is the number of layers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### TCN Block

Each block follows Bai, Kolter, and Koltun (2018): two weight-normalized
causal convolutions, ReLU activations, channel-wise dropout, and a residual
connection. A 1x1 convolution aligns channel dimensions when necessary.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### Full TCN Regressor

Stacking blocks with dilations [1, 2, 4, 8] followed by a linear head on
the final causal state. The final state can use the full receptive field;
averaging across intermediate states would mix shorter effective histories.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
## Train the TCN
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0023-p000

~~~~~~markdown
## Evaluate on Test Set
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## Ridge Baseline Comparison
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## The convolutional network against the linear baseline

Two questions, two panels. The left asks whether the model ordered the funds usefully
on each date; the right asks whether its predicted return levels were closer than
predicting zero. A model can do better on one and worse on the other, and both are
reported because acting on a forecast uses the ordering while fitting one minimises
the squared error.

The ridge regression is the comparison that decides anything. It sees the same window
flattened into one vector and fits a penalised linear map - no causality constraint,
no dilation, no notion that the columns are ordered in time. Whatever the dilated
causal structure is worth has to appear as a difference from that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
