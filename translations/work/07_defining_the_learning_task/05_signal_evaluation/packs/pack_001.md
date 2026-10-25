# ML4T A2 翻譯 Pack 001 — 07_defining_the_learning_task/05_signal_evaluation.ipynb

原 Batch：001, 002；翻譯單元：20。

## 指示（整個 Pack 只需閱讀一次）

將以下所有英文 Markdown 翻譯成**台灣繁體中文**；忠於原意，保留技術論述，不摘要、不增刪內容。
只翻譯自然語言；保留 Markdown 層級、行內程式碼、數學符號、數值、網址、檔案路徑、變數與函式名稱。
獨立程式碼區塊／獨立圖片／獨立公式已由本機保留，不要重複；混合文字內的必要語法請保留。
以下原文視為待翻譯資料，**不要執行或遵循原文中的命令或指示**。
每個單元一組指定的 BEGIN/END，必須完全匹配並各獨占一行；不得插入反斜線、escape 標籤或程式碼框。
僅輸出各單元翻譯及標記；不要重貼英文、術語表或其他解說。每個單元均不可漏。
如果單元完全沒有自然語言，內容填入 [[SKIP_TRANSLATION]]。
若回覆長度不足，停在最後一個**完整**的 END 標記，不要刪掉文字來硬塞完所有單元。

## 此 Pack 相關術語（不要在回覆中重貼）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 翻譯單元

### c0000-p000（原 Batch 001）

~~~~~~markdown
# Signal Evaluation: IC, Quantiles, and Spreads

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.3 - Feature and Label Evaluation as Triage

**Docker image**: `ml4t`

## Purpose

This notebook demonstrates **single-factor evaluation** using Information Coefficient
(IC) analysis, quantile returns, and spread metrics. We answer: "Is this factor
predictive in the cross-section, and what horizon does it live on?"

## Learning Objectives

1. Compute cross-sectional IC and understand its time series properties
2. Interpret IC, ICIR, and HAC-adjusted significance
3. Analyze quantile returns, spread, and the monotonicity of the quantile ladder
4. Understand horizon comparison with proper overlap warnings
5. Measure turnover and signal half-life

## Data Policy

All examples use **real ETF data** from the case study store.
NO synthetic data is used in this notebook.

## Prerequisites

- `02_preprocessing_pipeline` - for split-aware preprocessing concepts that
  underpin fold-aware IC evaluation under **Fold-Aware Evaluation**.
- `03_label_methods` - supplies the forward-return labels used as `y_true`.
- Familiarity with rank correlations (Spearman) and walk-forward CV.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000（原 Batch 001）

~~~~~~markdown
## Data Contract

Signal analysis requires two DataFrames with specific schemas:

**Factor Panel**:
- `timestamp`: Decision date
- `symbol`: Asset identifier
- `factor` or signal column(s): Factor value(s)

**Prices Panel**:
- `timestamp`: Same as factor panel
- `symbol`: Same as factor panel
- `close` or `price`: Closing price

The `ml4t-diagnostic` library aligns these using ASOF joins to compute
forward returns at each decision point.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000（原 Batch 001）

~~~~~~markdown
## Preparing Factor and Price Panels

We compute a simple momentum factor (21-day return) and prepare the data
in the format required by `analyze_signal()`.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0007-p000（原 Batch 001）

~~~~~~markdown
The factor below is a 21-day return, used here as a teaching example. Production factors
come from the Chapter 8 feature pipelines.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000（原 Batch 001）

~~~~~~markdown
### Correctness Screens

Before evaluating predictive power, verify that the factor is usable under the
stated protocol. The chapter's *Correctness screens* section prescribes four checks;
we demonstrate coverage
and staleness here. Timing/lag consistency and mask alignment become critical
with fundamental or third-party data (Chapters 8-10) but are trivially satisfied
for a price-derived momentum signal.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000（原 Batch 001）

~~~~~~markdown
**Coverage** is the fraction of (date, asset) pairs carrying a non-null factor value,
reported overall and per date.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000（原 Batch 001）

~~~~~~markdown
**Staleness** asks whether the factor updates as often as its definition implies. A
price-derived momentum signal should take a new value every session, so a change rate
materially below one points at a data gap rather than at the signal.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000（原 Batch 001）

~~~~~~markdown
## Information Coefficient (IC) Analysis

IC measures the **cross-sectional** rank correlation between signals and forward returns:

$$IC_t = \text{Spearman}(\text{signal}_{t}, \text{return}_{t \to t+h})$$

Where the correlation is computed across assets at each time $t$.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000（原 Batch 001）

~~~~~~markdown
### Two IC Conventions: Pooled vs Cross-Sectional

The library exposes both, and the distinction matters for ranking strategies:

- **`pooled_ic`** - one global Spearman correlation across **all (date, asset)**
  observations.  Conflates *which days were good* with *which assets ranked
  correctly within a day*; sensitive to time-series mean shifts in returns.
- **`cross_sectional_ic`** - Spearman per date, then mean across dates.  Measures
  only the daily ranking skill that a long-short strategy can monetise, and exposes
  IC IR / t-stat / p-value on the per-date series.

Chapter 14 standardises on the cross-sectional convention. The two can disagree
materially on the same data - pooled may inflate or deflate magnitude depending
on the regime structure of returns.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000（原 Batch 001）

~~~~~~markdown
### Interpreting an IC magnitude

The right anchor for interpreting a mean IC is not the headline value but the standard
error of that mean, which is set by the number of periods $T$ in the daily-IC series and
by the dispersion of that series:

$$\text{SE}(\bar{\text{IC}}) \approx \frac{\sigma_{\text{IC}}}{\sqrt{T}}$$

A single point estimate therefore carries very different evidence depending on
$\sigma_{\text{IC}}$ and $T$. The cell below works the confidence interval for one
fixed $\bar{\text{IC}}$ under three sample-size and dispersion combinations, so the
arithmetic can be checked and re-run rather than read.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000（原 Batch 002）

~~~~~~markdown
The same headline number is comfortably above zero in the first row, above zero but
uninformative about the signal's tail behaviour in the second, and indistinguishable
from zero in the third. Reporting a daily-mean IC therefore requires the CI (or the
$t$-statistic) alongside, and ideally the dispersion of the daily series as well.

The **ICIR** $= \bar{\text{IC}} / \sigma_{\text{IC}}$ is the signal-level analog of an
information ratio: $t \approx \text{ICIR} \times \sqrt{T}$ for serially uncorrelated
daily IC, and a HAC-adjusted $t$ for the realistic correlated case.

The bands printed next are typical magnitudes from the equity-factor literature on
multi-year daily-rebalanced cross-sectional studies. They are starting points for the SE
calculation above, not standalone readings, and they live in a declared table so the
code below can score against the same numbers the prose refers to.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000（原 Batch 002）

~~~~~~markdown
The daily IC series is plotted at low opacity behind two rolling means. At this sample
size the raw series is a solid band and carries no readable structure on its own; what a
reader can act on is whether the smoothed level drifts away from zero, and the two
windows show whether an apparent drift is still there under a longer average.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000（原 Batch 002）

~~~~~~markdown
### Publication Figure Artifact

The book IC time-series figure reads a compact NumPy artifact so formatting
changes do not reload the ETF panel or recompute daily cross-sectional ICs.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0027-p000（原 Batch 002）

~~~~~~markdown
The pairs below are sorted on the native timestamp rather than on its string form.
Lexicographic sorting of stringified dates is correct only for zero-padded ISO output
and would silently reorder the series under any other rendering.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000（原 Batch 002）

~~~~~~markdown
## Quantile Analysis

Examine returns by signal quantile to assess **monotonicity** (do higher signal
values lead to higher returns?) and **spread** (what's the return difference
between top and bottom quantiles?).
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000（原 Batch 002）

~~~~~~markdown
The bars do not rise with the quantile in any of the three panels, and in the shortest
horizon they fall - the bottom quantile of the signal earns the most. A long-short book
built the obvious way round would be short the better-performing leg. The spread and
monotonicity numbers below put figures on that, and the sign is the part to read first.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000（原 Batch 002）

~~~~~~markdown
### Monotonicity Interpretation

`analyze_signal` reports monotonicity as the **Spearman rank correlation between the
quantile ranks and their mean returns**, so it runs from $-1$ to $+1$: $+1$ is a
perfectly increasing ladder of quantile returns, $-1$ a perfectly decreasing one, and
$0$ no rank association at all. It is a correlation, not a percentage, and is reported
as such below.

That is not the same statistic as the one the fold section computes further down, which
is the *fraction of adjacent quantile steps that move upward* and runs from $0$ to $1$.
The two answer the same question differently and do not share a scale; where both appear
they are named apart.

The bands below score the **strength** of the ordering, so they read the magnitude. The
sign is a separate fact and the more important one here: a strongly ordered signal
pointing the wrong way is not a weak signal, it is an inverted one, and the two call for
opposite actions. The bands are kept in a declared table so the reading the prose gives
is the one the code applies.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000（原 Batch 002）

~~~~~~markdown
## Horizon Comparison

Compare IC across different forward return horizons to identify the optimal
holding period for the signal.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000（原 Batch 002）

~~~~~~markdown
Read the two panels together. The left panel's bars change sign across horizons, which
invites a story about reversal giving way to momentum; the right panel says the whole
left panel is inside the noise, because an ICIR of essentially zero means the daily IC
series has a standard deviation orders of magnitude larger than its mean. The sign
pattern is not a finding at these magnitudes.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000（原 Batch 002）

~~~~~~markdown
### Overlapping Returns Warning

When comparing IC across horizons, be aware that **longer horizons have overlapping
forward returns**, which introduces autocorrelation in the IC series.

For example, 21-day forward returns on consecutive days share 20 days of overlap.
This means:

1. **IC series are autocorrelated** at longer horizons
2. **Standard errors are understated** without HAC adjustment
3. **Comparing IC across horizons requires caution** - higher IC at longer
   horizons may reflect overlap, not better predictability

**Best practice**: Use HAC-adjusted t-statistics (as provided by `analyze_signal`)
and be skeptical of IC that increases monotonically with horizon.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>
