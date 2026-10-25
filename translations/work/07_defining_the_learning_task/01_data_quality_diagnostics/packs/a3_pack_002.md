# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/01_data_quality_diagnostics.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0033-p000

~~~~~~markdown
The smallest flagged return is positive, which is the whole story in one number:
not a single row was flagged for falling. The filter catches most reverse splits
and essentially none of the forward splits, even though forward splits are the far
more common event here by roughly eight to one.

So "extreme returns signal corporate actions" is the wrong direction of inference.
Most flagged rows are *not* splits, and the great majority of splits are *not*
flagged. The lesson is the general one: **when a dataset records an event
directly, detect it from that column rather than inferring it from a threshold on
something else** - and check the bounds of the quantity you are thresholding before
assuming a two-sided rule is two-sided.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
US Equities is the dataset that most needs active cleaning. Penny stocks should be
filtered so microstructure noise does not dominate cross-sectional models, and the
rows the return threshold flags need investigating rather than deleting: the section
above shows they are not the corporate actions they look like. See
[[ML4T_A3_0001]] for the full cleaning pipeline.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
### Coverage Heatmap: US Equities

Visualize data availability across time and assets. Shaded cells mark months with
data; white marks their absence. **Assets are ordered left to right by the month
they first appear**, which is what makes the pattern legible: in alphabetical order
the same panel is a ragged skyline with no visible structure, because a ticker's
spelling says nothing about when it listed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
Two things to read off it. The **staircase rising to the right** is the listing
history: each column begins at the month its asset first traded, and because the
columns are ordered by that month the start dates form a step rather than
scattering. The **broken top edge** is delisting - a column that stops short of the
present is an asset that left the panel, and it is still in the data. That is what
survivorship-free means, and it is the reason a universe must be rebuilt as of each
decision date rather than taken from today's index membership.

What is *not* here is equally informative, but only one of the two absences is
something this figure can report. There are **no full-width white rows**: the month
axis is a continuous range built from the panel's own bounds, so a month in which
nothing traded would be drawn as a blank row, and none is - no vendor outage or
exchange closure is written into this panel.

The columns cannot answer the matching question. The symbol axis is assembled from
the assets that *appear in the data*, so an asset missing throughout would not be a
white column - it would not be a column at all. "No asset is entirely absent" is
therefore not a finding this figure can produce, and checking it needs an
independently defined expected universe to compare against, which this notebook
does not have. The cell below counts only what is countable here.

Interior gaps, where an asset goes quiet and comes back, do exist but are rare.
Missingness is overwhelmingly a question of when each asset entered and left, which
makes the Section 7.1 strategy a universe-construction problem rather than an
imputation one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
### Crypto Perpetuals

24/7 trading with 8-hour funding settlement cycles. Bars should
align exactly to 00:00, 08:00, 16:00 UTC.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
### Crypto Premium Index

Premium index for funding arbitrage strategies. Same 8-hour frequency
as perpetuals; values represent the basis between spot and futures.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0044-p000

~~~~~~markdown
Both crypto datasets pass integrity checks. The 24/7 schedule means no
weekend gaps to worry about, but delisting events mid-panel (coins removed
from the exchange) can create sudden coverage drops.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0045-p000

~~~~~~markdown
### CME Futures

Session-aligned daily bars with roll continuity across contract months.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0047-p000

~~~~~~markdown
### FX Pairs

4-hour bars with expected weekend gaps: the market closes Friday 17:00 EST and reopens
Sunday 17:00 EST. That reopen lands between 21:00 and 22:00 UTC depending on daylight
saving, so a Sunday bar at or after the reopen hour is ordinary market data rather than
an anomaly. Saturday bars, and Sunday bars earlier in the day, fall outside the trading
week and are the ones worth filtering.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
FX trades continuously from the Sunday 17:00 EST reopen to the Friday close, so
Sunday bars at or after 21:00 UTC are expected market data. Saturday bars and
Sunday-daytime bars fall outside the trading week and are the genuine anomalies
to filter.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0050-p000

~~~~~~markdown
### Firm Characteristics

Chen-Pelger-Zhu academic monthly panel with 46 pre-computed characteristics
(plus [[ML4T_A3_0001]], [[ML4T_A3_0002]], and a [[ML4T_A3_0003]] indicator). Coverage is engineered
upstream: rows that fail the source paper's data-availability rules are
dropped before the panel is published, so the columns themselves arrive
dense - but the *firm-month* footprint shrinks substantially relative to a
raw CRSP–Compustat join.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0052-p000

~~~~~~markdown
The sampled characteristics show complete column-level coverage, because the upstream
filter only retains firm-months with valid characteristic vectors. The cost of that
filter is in the row count: many small-cap firm-months are excluded entirely, which is
the right framing for Section 7.1's discussion of "missing due to observed coverage
rules". Downstream notebooks should not attempt to reconstruct dropped rows; treat the
panel as the authors' own coverage rule applied at source.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0053-p000

~~~~~~markdown
## Summary Dashboard

Comparative view across all datasets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0056-p000

~~~~~~markdown
All datasets pass index integrity. Coverage is high for market data (ETFs,
crypto, futures, FX). Firm characteristics show full coverage for the sampled
columns, though sparsity increases for less common characteristics.
US Equities has outlier flags (price spikes) that [[ML4T_A3_0001]]
addresses with domain filters and spike detection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>
