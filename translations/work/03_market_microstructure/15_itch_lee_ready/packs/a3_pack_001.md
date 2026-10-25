# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/15_itch_lee_ready.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Lee-Ready Trade Classification Validation

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Quantify how well the Lee-Ready algorithm recovers the aggressor side of
trades, using DataBento XNAS-ITCH MBO data (which carries the ground-truth
aggressor flag) as the benchmark.

## Learning Objectives

After completing this notebook, you will be able to:
- Reconstruct the LOB from DataBento MBO messages and align trades to the
  contemporaneous quote midpoint.
- Apply the Lee-Ready quote-test + tick-test cascade and compare its
  accuracy against the tick test alone.
- Read the per-day breakdown (NVDA, 5 trading days) and reproduce the ~16pp
  gap §3.4 reports between tick-only and Lee-Ready classification.

## Book reference

Section §3.4, *The Art of Sampling* — Lee-Ready subsection (Table 3.3).

## Prerequisites

- DataBento XNAS-ITCH MBO parquets at
  [[ML4T_A3_0002]]
  (downloaded via [[ML4T_A3_0003]]).

## Decision Time vs Exchange Time

This validation uses **exchange timestamps** for trade-quote alignment, which
matches the ground truth's timestamping. In live trading, observation delay
means the quote you could actually have seen at decision time lags the
exchange state — apply a conservative lag (~1ms co-located, ~10ms retail)
in any backtest that relies on this kind of classification.

---
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## 1. Load DataBento MBO Data

DataBento MBO format:
- [[ML4T_A3_0001]]: A(Add), C(Cancel), F(Fill), M(Modify), T(Trade), R(Clear)
- [[ML4T_A3_0002]]: B(Bid/Buy), A(Ask/Sell), N(None)
- [[ML4T_A3_0003]]: Integer fixed-point (nanodollars, divide by 1e9)
- [[ML4T_A3_0004]]: Order/trade size
- [[ML4T_A3_0005]]: Unique order reference
- [[ML4T_A3_0006]]: Exchange timestamp
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0008-p000

~~~~~~markdown
## 2. Lee-Ready Classification with LOB Reconstruction

Lee-Ready algorithm (1991):
1. **Quote test**: Compare trade price to midpoint
   - Above midpoint → buy-initiated
   - Below midpoint → sell-initiated
2. **Tick test** (fallback when at midpoint):
   - Higher than previous trade → buy
   - Lower than previous trade → sell

Key implementation detail: We must maintain LOB state as we process trades
to get the correct midpoint at each trade time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Apply Lee-Ready Classification
Quote test with tick test fallback for trade direction inference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Classify Trades via Lee-Ready
Walk through MBO messages, maintain book state, and classify each trade.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 3. Run Validation
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## 4. Multi-Day Validation

Run validation across multiple days to get robust statistics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
## 5. Compare to Tick Test Only

Compare Lee-Ready (quote + tick test) vs tick test alone.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
## 6. Multi-Day Classification Accuracy (Table 3.3)

Accuracy is aggregated over the same multi-day window the book's Table 3.3 reports.

The tick test is scored two ways, because it faces a choice the quote test does not.
Many trades print at the same price as the one before them, and the rule has nothing
to read. The **continuous** cohort carries the last non-zero direction forward, so it
classifies every trade; the **non-zero** cohort declines to classify those trades at
all, so it is scored only on the ones whose price moved. Comparing the two separates
how good the rule is from how often it has anything to go on.

The summary is written to parquet so the book's table script can rebuild Table 3.3
without re-running this notebook.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0025-p000

~~~~~~markdown
### Table 3.3 as a chart

Read the two numbers on each bar together. The bar length is accuracy on the trades a
method classified; the label to its right is what share of trades that was. A method
that only answers when the answer is easy scores well on a small denominator, and the
non-zero tick test is exactly that case - which is why coverage is printed beside
accuracy rather than left out of the comparison.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## Key Takeaways

### What the comparison establishes

Three things are being compared and it is worth being precise about what each is. The
venue's own aggressor label is the record of which side crossed, and it is the standard
the other two are scored against rather than a method with an accuracy of its own.
Lee-Ready reads the trade price against the quote midpoint and falls back on the tick
test where that is uninformative. The tick test alone reads only the direction of the
last price change.

The figure above carries the numbers. What they show is how much of the classification
comes from the quote: the tick test is the part of Lee-Ready that runs when the quote
says nothing, and scoring it alone measures what the quote was contributing.

### Why Lee-Ready Works

The quote test (comparing trade price to midpoint) captures the fundamental
market microstructure: buyer-initiated trades tend to occur at or above the ask
(above midpoint), while seller-initiated trades occur at or below the bid.

### Implementation Notes

1. **LOB state matters**: Must maintain accurate book state at each trade
2. **Tick test fallback**: Only used when trade exactly at midpoint
3. **Zero-tick handling**: Preserve last direction on unchanged price

---

**Reference**: Lee & Ready (1991), "Inferring Trade Direction from Intraday Data"
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
