# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/11_crypto_premium_analysis.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Time series → 時間序列
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto Premium Index: Funding Rate Arbitrage Data

**Docker image**: [[ML4T_A3_0001]]

## Purpose
Explore the Binance perpetual-futures premium index — the per-period deviation between
perpetual and spot prices that determines the funding rate paid every 8 hours. The
notebook profiles 19 USDT-margined perpetuals from 2020-01 to 2025-12 and turns the
raw premium series into estimated funding APY for the funding-arbitrage case study.

## Learning Objectives
- Load the 8-hour premium-index panel and read its schema.
- Characterize the distribution and time-series behavior of BTC premium.
- Compare premium volatility across majors and altcoins.
- Translate premium into Binance's clamped funding rate and an annualized return.

## Book reference
Chapter 2, §2.2 (asset-class market data — crypto datasets). The funding-arbitrage
case study built on this dataset lives in [[ML4T_A3_0002]].

## Prerequisites
- Crypto perpetual + premium parquet files materialized under [[ML4T_A3_0003]]
  ([[ML4T_A3_0004]]).
- Binance's published funding settlements, which Section 5 scores the formula against.
  The perpetual downloader does not fetch them; `case_studies/crypto_perps_funding/
  funding_data.py` does.
- Loaders [[ML4T_A3_0005]] and
  [[ML4T_A3_0006]].

---
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

The funding constants are Binance's, not ours: the interest rate and the clamp half-width are
published contract terms, and the settlement cadence follows from them. They are declared
rather than written into the arithmetic so a reader can see the whole contract in one place
and CI can override any of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
---

## Section 1: Understanding the Premium Index

### What is the Premium Index?

The **premium index** measures how far the perpetual trades from the underlying index. The
one-line version is the relative difference between perpetual and spot, and it is worth
starting there, but the exchange's definition is not that:

[[ML4T_A3_0001]]

The impact bid and ask are the prices at which a fixed notional would fill on each side, so
the numerator asks how far the perpetual's *executable* quote sits outside the index. Both
terms are zero whenever the index falls between them, which means the index has a **dead
zone** the width of the impact spread and returns exactly zero inside it.

That is not a technicality. It is why a large share of this column is exactly zero, why the
share is far larger for illiquid contracts than for BTC, and why treating those zeros as
missing data would be a mistake - [[ML4T_A3_0002]] measures all three.

### Key properties

1. **Positive premium**: the impact bid sits above the index - the perpetual's executable
   quote is rich
2. **Negative premium**: the impact ask sits below the index - the executable quote is
   cheap
3. **Exactly zero**: the index falls inside the impact spread
4. **Funding rate**: derived from the premium index, settled every 8 hours on Binance

### Who pays whom
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0004-p001

~~~~~~markdown

The premium's sign does not answer this, and the difference is not a corner case. Funding
is [[ML4T_A3_0001]] with a positive interest rate [[ML4T_A3_0002]], so the premium
has to fall below [[ML4T_A3_0003]] before funding turns negative at all - a zero premium still
leaves longs paying shorts at exactly the interest rate. Section 5 derives this and
measures how often each case occurs.

Payment direction follows the funding rate:

- **Funding positive**: longs pay shorts. **Long Spot** + **Short Perpetual** collects it,
  market-neutral.
- **Funding negative**: shorts pay longs. **Short Spot** + **Long Perpetual** collects it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p001>>>
<<<ML4T-ZH-END:c0004-p001>>>

### c0008-p000

~~~~~~markdown
---

## Section 2: Premium Index Distribution

Understanding the distribution of premium values is crucial for:
1. Setting entry/exit thresholds for arbitrage
2. Risk management (tail events)
3. Comparing opportunities across assets
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0011-p000

~~~~~~markdown
The four panels below drop the outermost half percent from each tail before binning. Limiting
the axis alone is not enough: bin width is set by the full range, so a contract carrying
thousand-basis-point dislocations would resolve its whole body into two bins. The guard on an
empty array is for reduced CI panels, where a symbol may be absent and a percentile of
nothing raises.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
---

## Section 3: Time Series Analysis

Premium index varies over time based on market sentiment. Let's analyze:
1. Long-term trends
2. Regime changes (bull vs bear markets)
3. Correlation with price movements
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
The rolling window is expressed in days and converted to observations here, because the
series is on an eight-hour cadence and a window given in rows would mean a different span if
the cadence ever changed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0019-p000

~~~~~~markdown
---

## Section 4: Cross-Asset Premium Comparison

Different cryptocurrencies have different premium dynamics:
- **BTC/ETH**: Lower volatility, tighter premiums
- **Altcoins**: Higher volatility, wider premium swings

This affects arbitrage opportunity selection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
The colour scale on the heatmap below is clipped. A handful of contract-months reach far
enough that, unclipped, they set the range and flatten every other cell to the same shade.
The clipped extremes are listed after the figure rather than hidden by it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>
