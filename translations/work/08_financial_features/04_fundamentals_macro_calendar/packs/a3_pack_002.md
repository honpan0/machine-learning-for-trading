# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/04_fundamentals_macro_calendar.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0025-p000

~~~~~~markdown
**Interpretation**: Z-scored macro data measures whether the current indicator
level is unusual relative to its recent history. A VIX z-score of +2 means
fear is elevated relative to the last 21 or 63 days, which conditions how
momentum and carry signals perform.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0026-p000

~~~~~~markdown
## Monthly Features with Correct Forward-Fill

**Fix**: Use forward-filled version for YoY/3m changes, not raw monthly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## Relative Value Features

**Naming fix**: Rolling median ≠ percentile rank. Be precise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
## Yield-Curve Slope Feature

The yield-curve slope, the ten-year minus two-year spread, arrives as [[ML4T_A3_0001]]. Two
transforms follow, with their windows declared as constants in the next cell: an
exponential moving average to smooth the daily series, and a rolling z-score so the
level is read against its own recent range rather than in absolute basis points.

Both windows count **calendar** days, which is the thing to check before copying a
window length from a notebook that works on price bars. This macro panel carries a row
for every date, weekends and holidays included, because FRED series are forward-filled
onto a daily grid. A window of 250 rows on price bars is a trading year; the same 250
rows here reach back about eight months. The cell below asserts the grid spacing rather
than trusting it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
The two panels below trace the whole history. The top panel shows the raw ten-year minus
two-year spread with its smoothed version; the shaded band marks inversions, where the
spread sits below zero, which is the classic recession precursor. The bottom panel shows
the z-score, which restates the same slope relative to its own recent regime, so a
reading far from zero means the curve is unusual for this period rather than unusual in
absolute terms.

The count of shaded episodes printed with the figure includes several that lasted a
single day. Those bands are drawn, and at this width they are narrower than a pixel:
twenty-five years across a nine-hundred-pixel figure leaves each day about a tenth of
one. Read the count rather than trying to find them, and note that an inversion lasting
one day is a fact about the series that a chart of this span cannot show, which is a
reason to keep the count beside the chart rather than to redraw it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
**Interpretation**: The z-score centers the slope relative to its recent history.
Values above +2 indicate an unusually steep curve (risk-on, growth expectations);
below -2 indicates inversion (recession signal). The EMA removes daily noise
without introducing significant lag.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0035-p000

~~~~~~markdown
## Risk Regime Features
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
---

# Part 3: Calendar and Seasonal Encodings

Calendar features encode **predictable clocks**: sessions, day-of-week,
month-of-year, and scheduled events. The key principle is to encode
**phase and proximity**, not outcomes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0038-p000

~~~~~~markdown
## Cyclical Encoding

Encoding month as an integer (1-12) implies an ordinal relationship
(December > January). Cyclical sin/cos encoding removes this artifact:

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
The value of the encoding is easiest to see on the unit circle. Mapping each
month to [[ML4T_A3_0001]] places the twelve months evenly around a
ring, so December (12) sits right next to January (1) - the "wrap-around" that
an integer 1-12 encoding breaks. Distance on the ring equals distance in the
calendar.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
**Usage**: Calendar features are primarily **state variables** for conditioning.
For example, momentum signals may behave differently in January (tax-loss selling
reversal) versus other months. Time-to-event encodings (e.g., days to next
earnings, days to FOMC) follow the same pattern.

**Note**: Volatility state features (vol ratio, percentile, decile) and
price-derived regime indicators (variance ratio, fractal efficiency) are
covered in [[ML4T_A3_0001]] since they derive from price data.
Signal × state interactions and feasibility overlays are in
[[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
## Time-to-Event Encoding

Time-to-event measures proximity to a known future event (earnings, FOMC,
rebalance). The text specifies:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is the next event date and [[ML4T_A3_0003]] caps the
feature to avoid extreme values far from events.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
The earnings calendar below is synthetic, placed a fixed number of days after each
quarter end. A real system reads filing dates from SEC EDGAR; the point here is the
encoding, not the dates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0048-p000

~~~~~~markdown
The feature is a sawtooth: it counts down to zero as an earnings date
approaches, resets to the [[ML4T_A3_0001]] cap the day after (when the next event is
more than 63 days out; copper dashed line), then counts down again toward the
following quarter's announcement. The plot shows one symbol across two years.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>
