# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/04_fundamentals_macro_calendar.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Feature engineering → 特徵工程

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Slow Features and Context: Fundamentals, Macro, Calendar

**Chapter 8: Feature Engineering**
**Section Reference**: 8.4 - Contextual and Slow-Moving Features
**Docker image**: [[ML4T_A3_0001]]

## Purpose

This notebook covers **slow-moving features** that provide context for faster signals:

1. **Fundamentals**: Value, quality, growth factors from financial statements
2. **Macro**: Economic indicators, yield curves, credit spreads, risk regimes
3. **Calendar**: Cyclical encodings for seasonal patterns

## Key Principle

Slow features update infrequently (quarterly, monthly, or by schedule) but
condition daily decisions. The binding constraint is **data integrity**:
ensuring each observation reflects only what was knowable at decision time.

## Data Policy

All examples use **real data** (SEC XBRL, FRED macro).

## References

- Fama and French (1992, 1993): Value, size, profitability factors
- Cochrane (2011): "Presidential Address: Discount Rates", on the factor zoo
- Harvey, Liu, and Zhu (2016): "...and the Cross-Section of Expected Returns"

## Case Study Mapping

| Case Study | Relevant Features |
|------------|-------------------|
| ETFs ([[ML4T_A3_0002]]) | Calendar encodings, macro regimes |
| US Firm Characteristics ([[ML4T_A3_0003]]) | All fundamental factors |
| S&P 500 Equity+Options ([[ML4T_A3_0004]]) | Macro + VIX regime |
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
---

# Part 1: Fundamental Factors

Fundamental factors update quarterly but inform daily trading decisions.

**Key challenges**:
- Point-in-time accuracy (use announcement date, not period end)
- Forward-filling to daily frequency
- Factor staleness between announcements
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0004-p000

~~~~~~markdown
## Load Fundamental Data

### Scope: scaffolding for the construction mechanics, not a real-data value pipeline

[[ML4T_A3_0001]] reads SEC XBRL filings. XBRL publishes accounting numbers
(book equity, earnings, operating cash flow, capex) but does **not** publish
market capitalization, which comes from market prices on the announcement
date. To keep the value-factor cells below executable on the XBRL output
alone, this notebook approximates [[ML4T_A3_0002]]. This is a
**scaffolding** value: it lets the downstream [[ML4T_A3_0003]] cell
show the mechanics of book-to-market, earnings yield, and cash-flow yield,
but the resulting numbers are **not** the real-data factor values.

The lookahead-safe, real-data version (XBRL fundamentals joined to daily
adjusted prices on the announcement date, with point-in-time discipline) is
demonstrated in the [[ML4T_A3_0004]] case study and uses the
[[ML4T_A3_0005]] loader from [[ML4T_A3_0006]]. See
Chapter 11's case study pipeline ([[ML4T_A3_0007]])
and the Chen-Pelger-Zhu (2020) panel for the production version.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The XBRL loader exposes one column per us-gaap concept, lowercased. The map below gives
them the shorter names the rest of this notebook uses.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## Value Factors

Value factors identify stocks trading at discounts relative to fundamentals.

> **Reminder**: every factor below has [[ML4T_A3_0001]] in the denominator and
> [[ML4T_A3_0002]] is the [[ML4T_A3_0003]] scaffolding from §1.1. The cell
> demonstrates the *construction* of book-to-market, earnings yield, and
> cash-flow yield; the *values* are not the real-data factor values. See
> the [[ML4T_A3_0004]] case study for the production version.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
**Interpretation**: read the distinct-value counts printed above before reading anything
into the ratios. Book-to-market takes a single value across every row, because this
scaffolding derives [[ML4T_A3_0001]] from [[ML4T_A3_0002]] by a fixed multiple rather than
reading a market price. The cell demonstrates the formula; it does not show a
cross-section, and no ranking can be built from a column that is constant.

On real data the ratio would vary, and a low book-to-market would say the market prices
the firm well above its book value, which is usually read as a premium for intangibles
or expected growth. Earnings yield is earnings over market cap, the inverse of the P/E
ratio, so higher is more value-oriented. It does vary here, because earnings move across
quarters even while the book-to-market is pinned, which is why its distinct-value count
is the larger of the two.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
## Quality Factors

Quality factors identify financially healthy companies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## Daily Alignment with Correct ASOF Join

**Critical**: Both DataFrames must be sorted by the join keys.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
The ASOF join makes point-in-time discipline visible: the daily ROE is a step
function that changes **only** on an announcement date and holds the last
reported value until the next filing. Plotting one symbol shows the staircase;
the amber dashed lines mark the quarterly announcement dates that create each
step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
[[ML4T_A3_0001]] does not promise a stable order, and a few symbols carry all-null ROE on this
slice because their XBRL earnings are missing. The selection below is therefore
deterministic: the symbol whose daily ROE has the fewest gaps, which gives the figure an
unbroken staircase to draw.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### Inflated Sample-Size Warning

Forward-filling quarterly data to daily frequency inflates the apparent
sample size. Each fundamental observation is repeated across every trading
day until the next announcement - roughly a quarter's worth of days - so the
daily panel carries the same information many times over. The cell below
reports the empirical inflation factor for this demo.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
---

# Part 2: Macro Features

Macro data comes at mixed frequencies (daily, weekly, monthly, quarterly).

**Key considerations**:
- **Publication lag**: Monthly data has 2-4 week delay
- **Revisions**: Initial estimates are often revised
- **Forward-fill carefully**: Limit to avoid stale data
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
## Load Macro Data

> **Publication Lag Warning**: Macro data has significant publication delays.
> Conservative approach: Lag monthly data by 30+ days.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
## Trend Features with Publication Lag

> **Conservative Lagging**: For monthly data, add 30-day lag to ensure
> the data was actually available at the trading date.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>
