# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/06_ic_inference.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# IC Inference: HAC Adjustment and Block Bootstrap

**Docker image**: [[ML4T_A3_0001]]

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.3 - Feature and Label Evaluation as Triage

## Purpose

This notebook addresses **statistical inference for IC**: how confident should we
be that a signal's IC is not just noise? We cover HAC adjustment for autocorrelated
IC series and block bootstrap for robust confidence intervals.

## Learning Objectives

1. Understand why naive t-statistics fail for IC inference
2. Apply HAC (Newey-West) adjustment for proper standard errors
3. Implement block bootstrap for distribution-free confidence intervals
4. Distinguish practical vs statistical significance
5. Plan track records using HAC-adjusted effective sample size

## Data Policy

Examples use **real ETF data** from the case study store.

## Prerequisites

- [[ML4T_A3_0002]] - produces the IC time series whose inference we
  formalize here.
- Familiarity with autocorrelation, the Newey-West HAC estimator, and
  block bootstrap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## The Autocorrelation Problem

IC time series exhibit **autocorrelation** due to:

1. **Overlapping forward returns** at longer horizons
2. **Persistent signal values** (momentum doesn't flip daily)
3. **Regime persistence** (markets stay in trends/ranges)

Naive t-statistics assume iid observations and **underestimate standard errors**,
leading to inflated significance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
### Autocorrelation in IC Series

Let's examine the autocorrelation structure directly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
The decline is smooth and reaches the white-noise band near the label horizon, which is
consistent with overlap driving it: two IC values computed [[ML4T_A3_0001]] days apart share [[ML4T_A3_0002]]
days of return, so the shared window shrinks as [[ML4T_A3_0003]] grows. It is consistent with
persistent signal ranks as well, and the two are not separated here. Nor can this figure
say what happens *past* the horizon - it stops at [[ML4T_A3_0004]], and a series of rank
correlations can stay dependent beyond the overlap through regimes or a slow-moving
signal. What the figure does establish is enough for the section's purpose: a naive
t-statistic treats these values as independent draws, and they are not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
### Library Autocorrelation Analysis

The library version includes PACF and the **Ljung-Box portmanteau test**,
which tests the joint null that all autocorrelations up to lag [[ML4T_A3_0001]] are zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## HAC (Newey-West) Adjustment

HAC (Heteroskedasticity and Autocorrelation Consistent) standard errors account
for serial correlation in the IC series.

The Newey-West estimator uses a weighted sum of autocovariances:

[[ML4T_A3_0001]]

Where [[ML4T_A3_0002]] (Bartlett kernel) and [[ML4T_A3_0003]] is the lag truncation.

**[[ML4T_A3_0004]] should not be left to the sample size here.** The usual automatic rule
[[ML4T_A3_0005]] reads only [[ML4T_A3_0006]], and on this series it
returns 9. The labels are [[ML4T_A3_0007]]-day *overlapping* forward returns, so date [[ML4T_A3_0008]] and
date [[ML4T_A3_0009]] share part of their outcome window for every [[ML4T_A3_0010]] - and the signal
is 21-day momentum, whose cross-sectional ranks change slowly. Overlapping
outcomes measured against persistent ranks give ICs that move together over
roughly the label horizon.

**Both halves of that sentence are doing work, and the overlap alone is not
enough.** The IC is a rank correlation, not a return: if the signal ranks were
redrawn independently every day, the ICs could be serially uncorrelated no matter
how much the return windows overlap. So [[ML4T_A3_0011]] is not a theorem about overlapping
labels - it is a **conservative horizon-aware bandwidth for a persistent signal**,
and the evidence that it is the right order of magnitude is the measured ACF in
the figure above, which stays outside the white-noise band until about lag 16.

What is not defensible is [[ML4T_A3_0012]], chosen by a rule that never looked at the
labels or the signal. Passing [[ML4T_A3_0013]] makes the library take
[[ML4T_A3_0014]]; the ACF is what justifies that choice, and the
next section measures what it is worth.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
### What the Bandwidth Is Worth

Worth measuring rather than asserting, so the cell below runs the estimator
both ways on the same IC series. The block bootstrap below resamples contiguous blocks
of length [[ML4T_A3_0001]], so it already respects the overlap. If HAC is given a bandwidth that does
not, the two will not agree - and the gap is then a property of the bandwidth, not of the
estimator families, which is what the side-by-side is there to establish. The bootstrap
section shows the two agreeing once both are horizon-aware.

Calling the estimator without [[ML4T_A3_0002]] raises a [[ML4T_A3_0003]] saying the automatic
bandwidth may be anti-conservative for overlapping labels. That warning is the library
doing its job, and the call below triggers it on purpose; it is silenced for that one
call so it does not read as a defect in the run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Effective Sample Size

The HAC SE inflation factor tells us how much the autocorrelation reduces our
effective sample size:

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Block Bootstrap for Robust CI

When IC series has autocorrelation, **iid bootstrap is invalid**. We use
**block bootstrap** which preserves the dependence structure by resampling
contiguous blocks of observations.

Two common approaches:
1. **Moving Block Bootstrap (MBB)**: Fixed block length
2. **Stationary Bootstrap**: Random block lengths (geometric distribution)

We use the [[ML4T_A3_0001]] library's [[ML4T_A3_0002]] for robust inference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
### Library vs Manual Bootstrap: When to Use Each

The [[ML4T_A3_0001]] library provides [[ML4T_A3_0002]] for
**cross-sectional** bootstrap: given arrays of predictions and returns for a
single date, it resamples asset pairs and recomputes Spearman IC. This is useful
when you want a confidence interval for a single cross-section's IC.

For **time-series** inference on the IC series itself - "is the mean IC over
many dates significantly different from zero?" - the correct tool is the block bootstrap
used above, which preserves temporal dependence.

[[ML4T_A3_0003]]

Throughout this notebook we use the manual block bootstrap because we are
testing whether the *time-averaged* IC is significantly positive.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
