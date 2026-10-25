# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：06_strategy_definition/01_where_ideas_come_from.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Portfolio → 投資組合
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Where a trading idea meets the data — cross-asset momentum EDA

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: Before we freeze a setup or fit a model, we test whether one concrete
idea — **cross-asset momentum** on the 100-ETF universe — actually leaves a
footprint in the data. This is the exploratory step that sits between a *story*
("what rose recently keeps rising") and a *strategy*. We use the single most
informative EDA tool in this domain: **sort by the signal, then look at forward
returns per bucket.**

## The idea and its mechanism

The idea: assets that went up over the past year tend to keep earning more than the
rest of the universe over the next month, *across* asset classes (equities, sectors, countries, bonds,
commodities). Before any statistics, name the mechanism — *who is on the other
side, and why are they happy to trade with us?* This idea sits in the "behind"
family: we are betting others are slow or a step behind, not that we are paid to
bear a risk.

- **SLOW**: macro information diffuses across siloed markets with a lag; capital
  moves to the trend slowly. That gradual adjustment *is* the return.
- **WRONG**: investors under-react to news and chase performance, extending trends
  past fundamentals.

So this is a SLOW/WRONG blend. That also tells us the failure mode in advance:
momentum reverses sharply at turning points, and — because everyone can read the
same price history — the edge is the kind that **decays**. Keep that hypothesis in
mind; the data will have something to say about it.

## Learning objectives
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Build a monthly cross-sectional panel from the ETF daily data.
- Construct the classic **12-1 month momentum** signal (skip the most recent month).
- Run the **quintile conditional-return sort** and read it for *monotonicity,
  magnitude, and shape*.
- Stress the result by **era** — the difference between a footprint and an artifact.
- Leave with a measured reading that motivates the rest of the chapter: freeze the
  setup, validate walk-forward, and respect costs and effective sample size.

**Book reference**: Chapter 6 §6.1–§6.2 (from idea to evidence; mapping strategies
and sources of edge); Chapter 7 (defining a tradable label and the conditional
feature–label relationship).

**Prerequisites**: [[ML4T_A3_0001]] package on [[ML4T_A3_0002]]; ETF parquet present at
[[ML4T_A3_0003]]. Run [[ML4T_A3_0004]] if missing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
## 1. Build the monthly panel

The signal and the outcome both live at a **monthly** cadence: we rank the
universe once a month and hold for the next month. We take each ETF's last close
of the month. [[ML4T_A3_0001]] from [[ML4T_A3_0002]] is split/dividend-adjusted, so simple
returns are total returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## 2. The signal and the outcome

**Signal — 12-1 momentum**: the cumulative return from 12 months ago to *one month
ago*. Skipping the most recent month is deliberate: it sidesteps the short-term
reversal that contaminates a raw 12-month return (that reversal is a *different*
mechanism — liquidity provision — with the opposite sign).

**Outcome — forward 1-month return**: what we actually earn holding the next month.
Note the two clocks are already distinct: a 12-month **lookback** feeding a 1-month
**holding period**. Keeping them separate is a core discipline of the strategy
research framework (§6.3–§6.5).
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## 3. The simplest test: sort into quintiles, look at forward returns

Each month we rank every eligible ETF by its momentum signal and split them into
five equal buckets (quintile 1 = worst past year, quintile 5 = best), form an
**equal-weight portfolio** of each bucket, and record its return over the *next*
month. If the mechanism has a footprint, the buckets should line up: higher past
momentum → higher forward return.

We report each bucket two ways:

- **Gross** — its raw forward return.
- **Net of the market** — the bucket minus the equal-weight universe that month
  (its *relative* performance). This strips out beta — the return you get just for
  being invested — and leaves the momentum *tilt*. Note this is net of the
  **benchmark**, not net of **trading costs**: we have not subtracted a basis point
  of cost anywhere in this notebook.

We are reading three things:

- **Monotonicity** — does the relationship order correctly across *all* buckets,
  not just top-vs-bottom?
- **Magnitude** — is the top-minus-bottom spread economically material?
- **Shape** — is the effect smooth (premium-like) or concentrated in the tails
  (event-like)?
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0008-p000

~~~~~~markdown
The eligible cross-section keeps the months where both the signal and the outcome are
present and at least [[ML4T_A3_0001]] ETFs qualify. Sorting by `(timestamp, momentum,
symbol)` breaks a tie in the signal by symbol, so the rank is stable from run to run.
The quintile is then cut at the rank quantiles [[ML4T_A3_0002]], which is what pandas'
[[ML4T_A3_0003]] does on a rank: buckets stay balanced and no tie merges two of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
Each bucket becomes an equal-weight portfolio in each month, alongside the equal-weight
universe as a benchmark, and both are averaged across months. The horizon reported is
the one the design uses: the sort ranks once a month and holds for one month, so a
monthly return is the honest unit. Raising a single-month cross-sectional sort to the
twelfth power would assume the edge recurs in every month of the year, and the by-era
split below is the reason not to assume it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0013-p000

~~~~~~markdown
**Read it.** Gross, all five buckets sit close together and close to the dashed
benchmark line: most of what they earn is beta, the return for being invested at all
while the universe drifted up. The right panel takes the universe out and leaves the
*tilt*: the lower buckets net negative, the upper ones net positive, ordering roughly
with past momentum. The printed table above carries the levels; what the figure is for
is the ordering and the size of the gaps against the benchmark. The top-minus-bottom
spread is identical gross or net, because the benchmark cancels, and the long-short
t-statistic is printed beside it - read it before reading the spread. On the full
sample the footprint is there and it is small, and one average over two decades can
hide a lot, so the next section cuts the sample by era.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
