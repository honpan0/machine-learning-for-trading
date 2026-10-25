# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/16_provider_comparison.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Portfolio → 投資組合
- Sharpe ratio → 夏普比率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Provider Comparison: Multi-Source Data Acquisition

**Docker image**: [[ML4T_A3_0001]]

## Purpose
Demonstrate the [[ML4T_A3_0002]] unified [[ML4T_A3_0003]] interface
across YahooFinance, WikiPrices and FRED, then build a fallback strategy
and a price-level provider-comparison report. The notebook seeds the
ETF rotation universe used by the ETFs case study downstream.

## Learning Objectives
- Fetch OHLCV from multiple providers with one call signature.
- Build a priority-ordered fallback fetcher for production resilience.
- Quantify provider disagreement (row counts, price-difference stats)
  so multi-source stitching is auditable.
- Use FRED (vintage-aware) to pull macro series for risk overlays.

## Book reference
Chapter 2, §2.3 (multi-source stitching). The ETF universe materialised
here feeds the [[ML4T_A3_0004]] pipeline.

## Prerequisites
- Network access for live YahooFinance + FRED calls (the notebook is a
  provider-acquisition demo — these are the only places in the
  publication pass where live API calls are intentional).
- WikiPrices parquet under [[ML4T_A3_0005]]
  for the historical leg.
- [[ML4T_A3_0006]] set (free signup) for §8.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] fixes the right-hand end of every window so the outputs are stable between
book editions rather than moving with the wall clock. Bump it when the book is revised.

[[ML4T_A3_0002]] is subtracted in the Sharpe ratio in Section 7. It is a parameter rather
than a constant in the arithmetic because it is a choice, and a wrong one changes the
ordering of the table it feeds.

The FRED key is required only by Section 8, which is the last section, so the rest of the
notebook runs without it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
---

## Section 1: Understanding the Provider Architecture

ml4t-data provides a **unified interface** for fetching data from multiple sources. All providers inherit from [[ML4T_A3_0001]] and implement the same [[ML4T_A3_0002]] method.

### Key Benefits:
1. **Consistency**: Same API regardless of data source
2. **Validation**: Automatic OHLC invariant checks
3. **Polars Output**: [[ML4T_A3_0003]] measures what that is worth here
4. **Rate Limiting**: Built-in throttling to avoid API bans
5. **Circuit Breaker**: Automatic failure detection and recovery
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
The table below lists the provider landscape. This notebook exercises Yahoo, WikiPrices and
FRED; the rest need API keys of their own and appear in the asset-class notebooks that use
them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
---

## Section 2: Fetching Data with Yahoo Finance

Yahoo Finance is the easiest starting point - no API key required. Let's fetch our ETF universe for the momentum strategy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0013-p000

~~~~~~markdown
---

## Section 3: Historical Data with WikiPrices

For long-term backtests (30+ years), Yahoo Finance has limitations. WikiPrices provides
long-horizon U.S. equity history (including many delisted names) from roughly 1962 to 2018.

**Key Advantage**: Includes delisted companies, but you still need explicit survivorship
checks and delisting return handling (see [[ML4T_A3_0001]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### WikiPrices Schema Adapter

When WikiPrices data has been canonicalized to [[ML4T_A3_0001]]/[[ML4T_A3_0002]] columns,
this adapter provides the same [[ML4T_A3_0003]] interface as the library provider.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### Load WikiPrices Provider

Try multiple paths to find WikiPrices data (local install, Docker, CI fixtures).
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0021-p000

~~~~~~markdown
---

## Section 4: Multi-Provider Fallback Strategy

For production systems, we need a robust strategy that handles:
1. API failures
2. Rate limits
3. Data gaps
4. Historical coverage

The **fallback pattern** tries providers in order until one succeeds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
### Fallback Fetch

Try multiple providers in priority order; return the first successful result.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0026-p000

~~~~~~markdown
---

## Section 5: Combining Historical and Recent Data

For 30+ year backtests, we combine:
1. **WikiPrices** (1962-2018) - includes delisted names
2. **Yahoo Finance** (2018-present) - current data

One covers a span the other does not, in both directions, so a panel that reaches from the
1960s to today has to come from both and the seam has to be somewhere.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0029-p000

~~~~~~markdown
---

## Section 6: Provider Data Comparison

Yahoo Finance and WikiPrices both expose a close price, but they apply different
adjustment conventions and cover different date ranges, so the two series can
diverge sharply. This section demonstrates how to:

1. Align data from multiple providers by date
2. Quantify differences (row counts, price discrepancies)
3. Identify systematic vs random variations
4. Diagnose the causes (splits, dividends, timing)

**Why this matters**: Multi-source strategies must understand when providers disagree.
Small discrepancies compound over backtests; large ones signal data errors.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0033-p000

~~~~~~markdown
### Reading the comparison

The two providers quote the same exchange, so their raw prints agree. What they do not
share is an adjustment basis, and the printed statistics above show that difference
dominating everything else: the exact-match count is zero and every overlapping day
differs by roughly the same large percentage.

A constant offset across a whole year is the signature to recognise. A rounding difference
would be tiny and vary day to day; a mis-dated split would be a step, agreeing before the
date and disagreeing after. A uniform ratio means the two series are the same prices under
different retroactive adjustments, and here the reason is datable: Yahoo's adjusted close
reflects Apple's 2020 split, and the WikiPrices feed stopped in 2018 and could not.

So the number to check first in any provider diff is not the mean difference but the
*shape* of the difference over time. Align the adjustment basis before comparing, or the
comparison measures the adjustment rather than the data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
---

## Section 7: ETF Universe Performance

We visualize the 7 core ETFs defined at the start of this notebook. These represent
distinct asset classes for the rotation strategy:

| Symbol | Asset Class | Role in Portfolio |
|--------|-------------|-------------------|
| SPY | US Large Cap | Risk-on equity |
| QQQ | US Tech | High-beta growth |
| IWM | US Small Cap | Cyclical exposure |
| EFA | Intl Developed | Geographic diversification |
| EEM | Emerging Markets | Growth/risk allocation |
| TLT | Long Treasury | Flight-to-quality |
| GLD | Gold | Inflation/crisis hedge |

A rotation strategy switches between these based on momentum signals (Chapter 7).
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>
