# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/07_itch_stylized_facts.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構
- Momentum → 動能
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Microstructure Stylized Facts: Bid-Ask Bounce and Liquidity

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Demonstrate two of §3.3's stylized facts using NASDAQ ITCH-derived trade
data: (i) bid-ask bounce as negative first-order autocorrelation in
tick-level returns, and (ii) the liquidity spectrum that motivates Chapter
19's price-impact model.

## Learning Objectives

After completing this notebook, you will be able to:
- Compute lag-1 autocorrelation of tick-level trade returns and explain why
  it is negative for typical equities (bid-ask bounce).
- Compare liquidity metrics (volume, dollar value, average trade size,
  intraday volatility) across high-, medium-, and low-liquidity tickers.
- Recognize when trade-price returns must be replaced with mid-price
  returns to avoid microstructure noise.

## Book reference

Section §3.3, *From Raw Messages to the Limit Order Book* — stylized-facts
subsection on bid-ask bounce.

## Prerequisites

- The canonical enriched-trade parquet at
  [[ML4T_A3_0002]] and the matching
  [[ML4T_A3_0003]] (used for ticker selection and the liquidity-spectrum
  section); both are produced by [[ML4T_A3_0004]].
- For the order-arrival panel, parsed ITCH [[ML4T_A3_0005]]/[[ML4T_A3_0006]]/[[ML4T_A3_0007]] parquets at the
  canonical [[ML4T_A3_0008]]
  path (output of [[ML4T_A3_0009]]).

---
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0003-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] is the floor a ticker must clear to stand for one of the three liquidity
tiers compared in the last section. It is declared here and explained where the tiers
are drawn.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Load Trade Data

Load outputs from [[ML4T_A3_0001]]:
- [[ML4T_A3_0002]]: Aggregated stats by ticker (for symbol selection)
- [[ML4T_A3_0003]]: Canonical tick-level trades (for analysis)

Using the canonical trades file ensures we include enriched E/C data
(executions attributed to a ticker by [[ML4T_A3_0004]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Intraday Resampling
Resample tick-level trades to fixed-frequency bars for intraday pattern analysis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 3. Order Arrivals and Order Sizes

We use the **Add** messages ([[ML4T_A3_0001]]/[[ML4T_A3_0002]]) to characterize order arrivals over the
session and the distribution of submitted order sizes, and we report the volume
removed by **partial-cancel** ([[ML4T_A3_0003]]) messages as a share of submitted volume.
That share is small by construction rather than by finding: an [[ML4T_A3_0004]] reduces an order's
size, and most orders leave the book whole, through a [[ML4T_A3_0005]] delete.
[[ML4T_A3_0006]] measures how often each happens; this notebook
reports only the partial-cancel share and does not re-derive that rate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Analyze Order Flow for a Ticker
Compute order submission, cancellation, and size statistics for a given stock.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Print Order Flow Summary
Display order flow statistics including counts, cancel rates, and size distribution.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Plot Order Flow
Visualize hourly order arrivals and print top order sizes for a ticker.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0020-p000

~~~~~~markdown
## 4. The Bid-Ask Bounce

A fundamental microstructure phenomenon: trade prices bounce between bid and ask,
creating **negative autocorrelation** in tick-level returns. This is why:
- Mid-price returns are preferred over trade-price returns
- Tick-level "momentum" signals fail
- The Roll (1984) spread estimator works

**Implication for Chapter 8**: Always compute returns from mid-prices, not trade prices.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0023-p000

~~~~~~markdown
## 5. The Liquidity Spectrum: From Blue Chips to Small Caps

One of the most important microstructure insights: **liquidity varies enormously**
across stocks. A 1000-share order has near-zero impact on AAPL but can move
an illiquid stock by 50+ basis points.

This comparison foreshadows the price impact discussion in Chapter 19.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
The comparison is drawn from names active enough to form one-minute bars. The session's
long tail runs to thousands of tickers with a handful of prints each, and a ticker that
printed twice has no intraday shape to compare: its volatility estimate would be a
statement about two moments rather than about the stock.

Above the [[ML4T_A3_0001]] floor, five names are taken at even positions in the ranking by
traded value: the top, the three quartiles, and the bottom. Five spans the range while
staying readable on a bar chart, and taking them by position rather than by name means
the comparison follows the data rather than a list someone wrote down. Where fewer than
five clear the floor, whatever cleared it is compared instead, and where nothing clears
it there is no spectrum to draw: a truncated parse is the case that reaches this, and
widening the selection to every ticker in the session would answer a different question
from the one the section asks.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>
