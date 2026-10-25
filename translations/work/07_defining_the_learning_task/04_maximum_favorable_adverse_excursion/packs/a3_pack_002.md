# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/04_maximum_favorable_adverse_excursion.ipynb；A3 Pack 002；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market regime → 市場狀態
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0026-p000

~~~~~~markdown
The two BTC panels are close to interchangeable: the median favorable and adverse
excursions printed above agree to the second decimal, and so do the 75th percentiles.
Over an eight-hour window a perpetual future goes as far one way as the other, which is
what a symmetric barrier pair assumes and what the daily equity panels above do not
deliver. Note that this is a statement about this horizon, not about crypto: the
asymmetry in the SPY and ES panels is built over twenty-one sessions, and drift needs
time to accumulate against dispersion.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0027-p000

~~~~~~markdown
## Futures Analysis (Daily)

Futures have institutional flow and roll considerations.

[[ML4T_A3_0001]] returns one row per session *and tenor*, three rows per session
across tenors 0, 1 and 2. [[ML4T_A3_0002]] walks a forward window with [[ML4T_A3_0003]] over
whatever row order it is handed, so on the unfiltered frame the excursion window
steps across three different contracts instead of forward in time on one, and every
excursion statistic comes out inflated. Those statistics are exported to
[[ML4T_A3_0004]] as the source for the chapter's barrier-width references, so the
filter below runs before the sort rather than after it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## MFE/MAE Scatter Plot

A scatter plot reveals the joint distribution and helps identify
candidate barrier rectangles.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
The cloud has no diagonal in it, which is the figure's point. Entries are not sorted
into "good" trades that ran up without drawing down and "bad" ones that did the reverse:
most bars that travel far in one direction also travel some way in the other, and the
joint distribution offers no barrier rectangle that keeps the favorable excursions while
excluding the adverse ones. Barrier choice is a decision about which of the two to cut
off first, not a partition of the sample into trades that only rose and trades that
only fell.

The spacing of the reference lines carries the other half. The favorable percentiles sit
close together while the adverse ones spread out, so moving a stop from the median to
the 90th percentile buys far more room than moving a take-profit by the same quantile
step. That is the shape behind the recommendations table below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
## Regime-Conditional Analysis

Barrier effectiveness varies by market regime. High volatility periods
require wider barriers to avoid premature stops.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
## Barrier Validation via Hit-Type Analysis

MFE/MAE alone doesn't tell us which barrier hits first.
We validate by running triple-barrier and inspecting hit distributions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
The barrier widths below are taken from the measured excursion percentiles rather than
from round numbers, which is the notebook's stated purpose: *rather than picking
arbitrary barrier widths, we analyze actual price excursions*. Take-profit comes from
the MFE distribution and stop-loss from the MAE distribution, at the same percentile, so
each label names the quantity it is derived from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
## Recommendations Summary

Each instrument's barriers come from its own excursion distribution, at the same
percentile, so the take-profit is read off the MFE and the stop off the MAE. The
table below is built from the measured quantiles rather than typed, which is the
whole point of the exercise: a barrier width is a claim about how far price
travels, and this notebook measured how far it travels.

For the two daily instruments the table also reports the ATR multiple a
volatility-scaled stop would use. That multiple is the 75th percentile of the
per-entry ratio [[ML4T_A3_0001]], **not** the p75 excursion divided by the mean
ATR. The two are different numbers and only the first answers the question an
ATR-scaled stop asks. A stop placed at [[ML4T_A3_0002]] is re-sized every day, so
what has to hold at the 75th percentile is the *ratio*; dividing one aggregate by
another gives the ratio of typical values, which ignores that ATR and the
excursion it scales move together. It is a *consequence* of the measured
distribution rather than an input to it, which is why the multiple differs by
instrument instead of being a round number chosen in advance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
**What the table says.** BTC's excursions over one funding cycle are an order of
magnitude smaller than the daily instruments' over a trading month, which is horizon
rather than asset:
a fixed percentage barrier is workable there because the funding cycle fixes the
holding period. For SPY and ES the stop that the p75 adverse excursion implies is
*wider* than one ATR, so an implementation that reaches for a round [[ML4T_A3_0001]] stop
will be stopped out by ordinary movement.

Note the ES-versus-SPY comparison printed above, which holds only while the two
instruments carry the same horizon - the print says so when they do not. At the shipped
horizons ES adverse excursions are wider than SPY's at both quantiles, so the intuition
that an index future deserves a *tighter* stop than the matching ETF is contradicted by
the measurement. This is
the same trap as the take-profit/stop-loss ordering under **Barrier Validation via
Hit-Type Analysis**: a plausible-sounding
asymmetry, asserted rather than measured, pointing the wrong way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0041-p000

~~~~~~markdown
**Key findings:**

1. A barrier width is a property of one instrument at one horizon, not of an asset
   class - the printed table is the calibration, recomputed whenever the data is.
2. Regime conditioning matters more than the choice of instrument: the
   regime-conditional table shows the high-volatility tercile carrying roughly twice
   the excursion of the low one, a ratio larger than any gap between SPY and ES.
3. ATR-scaled barriers adapt to that regime shift; fixed percentage barriers are
   defensible only where the holding period is short and externally fixed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
## Export Statistics for Documentation

Save summary statistics for chapter reference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0046-p000

~~~~~~markdown
## Multi-Horizon Excursion Analysis

The manual implementation above analyzes one horizon at a time.
[[ML4T_A3_0001]] provides [[ML4T_A3_0002]] for multi-horizon analysis
in a single call - useful for comparing barrier widths across holding periods.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>
