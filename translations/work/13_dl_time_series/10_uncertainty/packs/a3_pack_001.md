# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/10_uncertainty.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# From a point forecast to an interval: MC Dropout, deep ensembles, conformal

**Docker image**: [[ML4T_A3_0001]]

Every model in this chapter has returned one number per fund per day, and every
comparison has ranked those numbers. But a position size is not set by a forecast
alone: two funds with the same expected return and different confidence do not
deserve the same exposure. This notebook asks what a network can say about how sure
it is, and then whether that answer means anything.

It takes three steps, and the third is the one that matters.

**MC Dropout** (Gal and Ghahramani, 2016) keeps dropout switched on at inference and
runs the same input through the network many times, treating the spread of those
passes as uncertainty. It costs nothing extra to train.

**Deep ensembles** (Lakshminarayanan et al., 2017) train several networks that
differ only in initialisation and data order, and treat their disagreement as
uncertainty. It costs a full training run per member.

Both produce a number with the units of a return. Neither produces a number with a
coverage property, and the empirical coverage table below is where that becomes
visible. **Split-conformal calibration** is the step that converts a spread into an
interval with a coverage claim - under an exchangeability assumption this setup
does not fully satisfy, which is stated where it bites rather than in a footnote.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Learning objectives**:
- Implement both methods and say precisely what quantity each one's spread is the
  spread *of*.
- Read an empirical coverage table and say what an under-covered interval means for
  a position-sizing rule built on it.
- Apply split-conformal calibration in both its plain and normalized forms, and say
  which of the two actually uses the model's uncertainty estimate.
- Name the exchangeability assumption conformal needs and the two places this
  notebook violates it.

**Book Reference**: Chapter 13, Section 13.8 (Quantifying prediction uncertainty)

**Prerequisites**: ETF features ([[ML4T_A3_0001]])
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## Data Loading

Both methods share identical data: ETF features and forward return labels from
the case study pipeline. Loading once eliminates the duplication that separate
notebooks would require.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## Sequence Creation and Temporal Split

Two housekeeping steps before the split, both of which affect what the models see.

NaN and infinite feature values are replaced with zero. The features are already
standardized returns and a NaN here means a missing observation at a series
boundary, so zero is the standardized mean rather than an invented value.
Forward-filling within a symbol would be the other option and would not leak - it
only ever reads earlier observations - but it would present a stale value as a
current one, which for a trailing-return feature says the return was unchanged
rather than unknown. The count is printed so a large number cannot pass unnoticed.

The rows are then put in one canonical order, by date and then symbol. The sequence
builder pools assets in whatever order the frame yields them, and that order is not
fixed between runs - which changes which examples land in which mini-batch, and with
it every number below, seeds notwithstanding.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Splitting by date, with a gap for the label horizon

The split is by date, at fixed fractions of the trading days, and an example belongs
to the partition the date it carries falls in. The label is a [[ML4T_A3_0001]]-session
forward return, so an example dated within that many sessions of a boundary has an
outcome resolved by days on the far side; those examples are dropped.

The gap matters more here than in the notebooks before it. The validation split is
not only where training stops early - it is also the calibration set for the
conformal intervals further down, and a conformal guarantee needs the calibration
residuals to be exchangeable with the test residuals. Validation examples whose
outcomes land inside the test period are not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
**Cross-sectional IC helper**: every method below scores predictions with the same
daily Spearman correlation between forecast and forward return, averaged over the
test window. Defining it once keeps the comparison consistent.

A date's IC is undefined when a model predicts the same value for every fund on it:
the predicted ranks are all tied and there is nothing to correlate. The library
returns [[ML4T_A3_0001]] for such a date, and polars treats [[ML4T_A3_0002]] and null as different values,
so [[ML4T_A3_0003]] alone leaves it in place and one of them makes the whole mean [[ML4T_A3_0004]].
Both are filtered here, and the count of dates the mean was taken over is returned
alongside it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## Ridge Baseline

Both uncertainty methods need a point-prediction baseline for comparison.
We train Ridge once and reuse it throughout.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
---
## Part A: Monte Carlo Dropout

MC Dropout treats dropout as approximate Bayesian inference. By keeping dropout
**active at test time** and running multiple forward passes, we get a distribution
of predictions whose spread estimates model uncertainty.

The key insight from Gal and Ghahramani (2016): a neural network with dropout
applied before every weight layer is mathematically equivalent to an approximation
of a deep Gaussian process.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
### LSTM with MC Dropout

This model has dropout in two places:
1. Between LSTM layers (via the [[ML4T_A3_0001]] parameter)
2. Before the output head (explicit [[ML4T_A3_0002]])

At inference time, we call [[ML4T_A3_0003]] to keep both dropout layers active,
then run [[ML4T_A3_0004]] forward passes to generate a prediction distribution.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### Training
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
### MC Inference

The critical step: switch to [[ML4T_A3_0001]] to keep dropout active, then
run [[ML4T_A3_0002]] stochastic forward passes. Each pass samples a different
subset of neurons, approximating a draw from the posterior over model weights.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
**Interpretation**: averaging [[ML4T_A3_0001]] stochastic forward passes gives the MC
Dropout point estimate above. Two LSTM layers at a dropout rate of [[ML4T_A3_0002]] produce
highly correlated passes, so the spread of the resulting distribution is small in
absolute terms - compare the printed mean standard deviation against the label's own
standard deviation printed with the data. Which of the MC mean and the ridge
baseline scores higher moves between runs on this panel; the size of the
dropout spread relative to the return scale does not. The second observation is what
the calibration check below turns on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>
