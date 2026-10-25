# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/19_incremental_updates.ipynb；A3 Pack 001；單元 14 個。


## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Incremental Updates: Keeping Market Data Fresh

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: Walk through the update lifecycle — initial load, daily delta,
gap detection, and a small health dashboard — so the same flow that runs
in [[ML4T_A3_0002]] is visible end-to-end.

**Learning objectives**:
1. Compare full-refresh and incremental update costs.
2. Drive a daily delta with [[ML4T_A3_0003]] and
   understand why the [[ML4T_A3_0004]] default is unsafe for OHLCV data.
3. Verify completeness with [[ML4T_A3_0005]].
4. Render a 3-panel health dashboard (volume, freshness, issues).

**Book reference**: §2.4 (storing data) — operational counterpart to the
storage benchmarks in notebooks 20 and 21.

**Prerequisites**: ml4t-data installed; live network access for Yahoo Finance.

**Why incremental updates**: a full refresh re-fetches every row a symbol has ever had,
and an incremental run fetches the sessions since the last one. On a universe of a few
hundred symbols with a decade of history, the first is millions of rows and the second is
hundreds, every day. Section 1 measures the ratio on the demo universe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0003-p000

~~~~~~markdown
### Declared parameters

The freshness thresholds are the two that carry a judgment. A daily equity feed that has
not moved in more than a weekend is behind, and one that has not moved in more than a week
is broken; those are the two lines the dashboard draws and colours against.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
---

## 1. Full Refresh vs Incremental Update

Let's demonstrate the difference with a concrete example.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0006-p000

~~~~~~markdown
### Step 1: Initial Load (Full History)
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Step 2: Incremental Update (Only New Data)

An update reads the last timestamp in storage, refetches a small overlap
([[ML4T_A3_0001]]) so a bar the vendor revised replaces the stored one, and
merges everything since.

**Where it stops matters more than where it starts.** Yahoo returns the
current exchange date as a row with accumulating volume and no
open/high/low/close. A bar with no prices is not a bar, and the provider says
so:

[[ML4T_A3_0002]]

[[ML4T_A3_0003]] fetches to [[ML4T_A3_0004]], so it asks for that row on
every trading day and raises. [[ML4T_A3_0005]] performs the
same delta and **finds** the end of its window rather than computing one. It
starts a day before the current exchange date — in exchange time, not UTC,
since at 22:00 in New York the UTC date is already tomorrow — and steps back a
day at a time while the provider refuses the window.

The retreat is what a date cannot do. The placeholder row usually resolves a
few hours after the close, and sometimes it does not: Yahoo's 2026-09-03 daily
bar for AAPL was still [[ML4T_A3_0006]] eight and a half hours
later, while the same window ending 2026-09-02 was clean on every column. Both
look identical from the calendar, so the vendor has to be asked.

When a window is refused, ml4t-data logs it at error level. If you see
[[ML4T_A3_0007]] below and
then a row count on the next line, that is the retreat working: the first
window asked for a bar the vendor has not published, and the second one landed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0008-p001

~~~~~~markdown

The other reason not to call [[ML4T_A3_0001]] blind is its [[ML4T_A3_0002]] default:
a calendar-unaware gap detector that treats every weekend and US holiday as a
missing trading day and forward-fills it, inflating each symbol's row count by
hundreds of phantom bars. For OHLCV data the right behavior is to leave
non-trading days absent and rely on a calendar-aware completeness check
downstream — which is what section 3 does with [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p001>>>
<<<ML4T-ZH-END:c0008-p001>>>

### c0010-p000

~~~~~~markdown
Each symbol started with 502 rows (2023-01 through 2024-12). The update
fetches the 7-day overlap plus every session through the last complete bar and
merges; the resulting row count equals the original 502 plus exactly the new
trading sessions — no synthetic weekend/holiday rows, and no half-formed bar
for the session that is still running.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
---

## 2. Update Strategies

ml4t-data supports four strategies for different scenarios:
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
The [[ML4T_A3_0001]] class provides low-level control over these strategies.
For most use cases, [[ML4T_A3_0002]] (which uses [[ML4T_A3_0003]]) is sufficient.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
---

## 3. Gap Detection

Before running a backtest, verify that your data is complete.
Gaps can occur from failed downloads, provider outages, or holiday handling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
[[ML4T_A3_0001]] filters Saturdays and Sundays. US market holidays
(MLK Day, Good Friday, Thanksgiving, etc.) still register as one-day gaps
because the detector has no exchange calendar — fine for routine update
health checks, but pair with a calendar-aware completeness check before
trusting the result for backtest panels.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
---

## 4. Data Health Dashboard

In production, monitor data health across your entire universe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0021-p000

~~~~~~markdown
---

## 5. The Book's Update Workflow

The book's [[ML4T_A3_0001]] script implements exactly this pattern
for all asset classes. Run it with [[ML4T_A3_0002]] to extend datasets to the present:

[[ML4T_A3_0003]]

Under the hood, [[ML4T_A3_0004]] uses:
- [[ML4T_A3_0005]] → [[ML4T_A3_0006]]
- [[ML4T_A3_0007]] → [[ML4T_A3_0008]]
- [[ML4T_A3_0009]] → [[ML4T_A3_0010]]
- [[ML4T_A3_0011]] → [[ML4T_A3_0012]]

Each manager reads its YAML config for symbols, date ranges, and provider settings,
then updates only what's new.

### Config-Driven Downloads

The ETF config at [[ML4T_A3_0013]] defines:
[[ML4T_A3_0014]]

When you run [[ML4T_A3_0015]] in 2026+, it extends data beyond the configured end date
to the present — no config changes needed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>
