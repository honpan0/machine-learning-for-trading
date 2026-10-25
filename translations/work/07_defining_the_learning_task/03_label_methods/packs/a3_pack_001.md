# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/03_label_methods.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Label → 標籤
- Data leakage → 資料洩漏
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
**Docker image**: [[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
# Label Engineering Methods

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.2 - Label Engineering

## Purpose

This notebook demonstrates **all major labeling methods** for ML-based trading
strategies, with practical examples on real ETF data. It serves as the canonical
reference for choosing and configuring labels across all modeling chapters.

## Learning Objectives

1. Understand fixed-horizon vs path-dependent labels
2. Compare time-series vs **cross-sectional** percentile approaches
3. Implement triple-barrier with fixed and ATR-based thresholds
4. Visualize barrier mechanics with price path examples
5. Understand anchor alignment (close-to-close vs next-open)

## Prerequisites

- [[ML4T_A3_0001]] - establishes the ETF coverage assumptions used here.
- Familiarity with leakage-aware splitting (Chapter 6, *Data leakage and estimation bias*)
  and forward-return semantics.
- Polars DataFrame manipulation; basic statistics (t-statistics, percentiles).

## Data Contract

- **Input**: Real ETF OHLCV from data loaders (SPY for single-asset, full universe for cross-sectional)
- **Output**: Example labels for teaching. Each case study builds its production labels in its
  own [[ML4T_A3_0002]] notebook, reading the horizon from that case study's [[ML4T_A3_0003]]
  through [[ML4T_A3_0004]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## Helper Functions

Robust label column discovery to avoid brittle hardcoded column names.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Load Sample Data

We use the ETF universe for demonstrations. SPY serves as the single-asset
example; the full universe enables cross-sectional analysis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## Fixed Time Horizon Labels

The simplest approach: compute forward returns over a fixed window.
This is the workhorse of factor-based ML strategies.

### Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| [[ML4T_A3_0001]] | Raw percentage return | Regression targets |
| [[ML4T_A3_0002]] | +1 if return > 0, else -1 | Classification |
| [[ML4T_A3_0003]] | Log return | Regression with better properties |
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Return vs binary comparison

Both methods use the same forward window but produce different target types:
continuous returns for regression, binary direction for classification.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## Anchor Alignment

**Critical concept**: The anchor point determines when returns are measured.
Different anchors produce different labels even with the same horizon.

- **Close-to-close**: Decision at close, measure return from close to H-day close
- **Next-open-to-open**: Decision at close, execute at next open, measure from there

This is one of the most common sources of subtle lookahead bias.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0017-p000

~~~~~~markdown
The two anchors agree on average and disagree on every individual trade. The mean
difference printed above is indistinguishable from zero, while its standard deviation
is of the same order as a typical daily move - so the choice of anchor is invisible in
a summary statistic and decisive for any single label. A model trained on close-to-close
labels is being scored on a price its strategy could not have transacted at.

For an end-of-day signal executed at the next open, anchor the label at the next open.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0018-p000

~~~~~~markdown
## Time-Series Percentile Labels

Labels are relative to recent history for a **single instrument**,
making them adaptive to volatility regimes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
The cell below correlates the threshold the labeler actually produced - not a
re-derivation of it - against two quantities measured strictly backwards from each date,
so nothing in the comparison sees the future the threshold is trying to anticipate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
The threshold is not a fixed return; it is whatever the top quartile of the last year
looked like. It moves mostly with trailing volatility, which is the property the method
is usually sold on, but the correlation above is well short of one because it also moves
with trailing drift: a year of steady gains raises the bar for "top quartile" without
any change in dispersion. Both effects raise the threshold, and a reader cannot tell
them apart from the line alone.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0024-p000

~~~~~~markdown
## Cross-Sectional Percentile Labels

**The most natural use of percentile labels**: rank assets within the universe
at each decision time, then label top/bottom quantiles.

This is the standard approach for equity and ETF rotation strategies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
Cross-sectional percentile labels rank assets at each decision time [[ML4T_A3_0001]].
This is inherently point-in-time: the ranking at [[ML4T_A3_0002]] uses only returns
realized at [[ML4T_A3_0003]], so no future information leaks into label construction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
Counts per class move with the size of the universe on each date; proportions do not,
because the cut is a rank. Converting to proportions before plotting is what makes the
construction visible rather than the coverage.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>
