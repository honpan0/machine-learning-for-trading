# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/17_costs.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Sharpe ratio → 夏普比率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETF costs: where the edge runs out

Every Sharpe ratio so far was earned at one cost level - the one [[ML4T_A3_0001]] declares.
That single number hides the question a reader actually needs answered, which is not "what did it
make" but **"how much friction would it take to make nothing"**. A strategy whose Sharpe is
unchanged at four times the declared cost is a different proposition from one that breaks even
just above it, even when the two report the same number today.

This notebook walks a cost grid over the leading allocation-stage combinations and registers a
backtest at each level, so the decay curve is a set of registered results rather than an
extrapolation from one point.

**Two cost regimes are swept, and they are not two views of one thing.** The case study's
declared model is per-share commission plus a half-spread in cents, which is how an ETF actually
trades: the cost of a share does not scale with its price. The basis-point grid is the convention
most of the literature uses and most other case studies here declare, and it is run alongside as
a comparator. The two disagree by construction - a one-cent half-spread is about one basis point
on a [[ML4T_A3_0002]] fund and about five on a [[ML4T_A3_0003]] one - so the panels are read for their slopes and their
breakevens, not point against point.

**Learning objectives**

- Read a cost decay curve and locate the level at which a strategy stops paying.
- Say why a per-share cost model and a basis-point cost model give different answers on the same
  universe, and which one this universe is priced under.
- Say what a uniform cost sweep does and does not tell you about a strategy priced under a
  per-asset spread map.

**Book reference**: Chapter 18, Sections 18.2 to 18.5.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Prerequisites**: [[[ML4T_A3_0001]]](16_risk_management.ipynb), and through it
[[[ML4T_A3_0002]]](15_portfolio_management.ipynb) and [[[ML4T_A3_0003]]](14_backtest.ipynb).
This is the last stage that selects, so it runs after all three and draws from all of them.

**What it writes**: one row in [[ML4T_A3_0004]] per combination and cost level, at
[[ML4T_A3_0005]], under both regimes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
## 1. What is being re-priced, and under what

The combinations are the highest-Sharpe validation runs across every stage a selected
configuration can come from - the equal-weight baseline, the allocation sweep and the risk
overlay - not the allocation stage alone. Each later stage is an alternative to the one before it
rather than an improvement on it by construction: where every allocator lands below the
equal-weight parent it was built from, an allocation-only rule would carry forward a strategy the
earlier notebook measured as worse than doing nothing, and where every risk control hurts, an
overlay-only rule would charge costs against an overlay the sweep just found unhelpful. Which
stage wins is decided by measurement here and printed below, not by which stages this query
happens to name.

They are re-priced rather than re-selected: the prediction, the concentration and the allocator
are held exactly as registered, and the only thing that moves is the cost model. That is what
makes the curve below a statement about cost sensitivity and not about which strategy happens to
do best under friction.

The per-share commission is read from [[ML4T_A3_0001]] with no default. Elsewhere in the fleet that
key is exploratory and a missing value can fall back; here it is the headline regime, so a
missing key has to fail loudly rather than quietly re-price the whole sweep at somebody's
default.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
**The population the leaders are drawn from.** A refit publishes a second generation under the
same population name and leaves the one it replaced in the registry, backtests and all. Reading
the leaders without asking the population lineage lets a retired identity - or one no population
ever listed - be re-priced here and carried onward as though it were what the model notebook
publishes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0010-p000

~~~~~~markdown
## 2. Sweeping both grids

**The sweep applies one flat rate to every fund, which the production backtests do not.** The
signal, allocation and risk stages price each fund from the tiered per-asset half-spread map in
[[ML4T_A3_0001]] - a half cent on the largest funds, a cent on the sector funds, two cents by
default. What follows is therefore one-axis sensitivity to a universe-wide cost level, not a
re-pricing of the live cost structure. Read the slope and the crossing point; do not read a
single point as what the strategy would have earned.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0014-p000

~~~~~~markdown
## 3. The decay curves

Read back from the registry rather than from the sweep, so a resumed run and a fresh one show the
same thing. Each row's cost level and allocator come out of its own registered specification,
which is what the backtest hash was taken over.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Where each regime crosses zero

The breakeven is the cost level at which the mean Sharpe crosses zero, interpolated between the
two grid points that bracket it. A curve that never crosses within the grid has no breakeven to
report, and saying so is the answer: the grid did not reach far enough to find one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>
