# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/16_risk_management.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Drawdown → 回撤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETF risk overlays: what a stop costs when the holding period is a month

A risk overlay is a rule that closes a position before the strategy would have. A stop-loss
closes it when it has lost a fixed amount, a trailing stop when it has given back a fixed amount
of its gain, a time exit when it has been held long enough. Each is uncontroversial as an idea
and each does the same thing to the return distribution: it removes the left tail and, because it
cannot tell which is which, part of the right one too.

**The reason this is a real question here and not a formality is the rebalancing cadence.** This
strategy holds a fund for a month and then re-ranks. A stop that fires on day nine has not
avoided a month of loss; it has ended a position nine days early and left the capital idle until
the rebalance that would have closed the position anyway. Whether that helps depends entirely on
what the fund did over the remaining days, which is the thing nobody knows at the time.

So the overlay grid spans thresholds from very tight to very loose, and the tight end is expected
to fire on ordinary intra-month movement rather than on anything the strategy should react to.
Where the grid turns from harmful to harmless is what this notebook is for.

**Learning objectives**

- Say what a position-level risk rule does to both tails of a return distribution, not only the
  left one.
- Say why a rule's trigger frequency has to be read against the strategy's holding period.
- Calibrate a trailing threshold from the observed adverse-excursion distribution rather than
  from a round number, and say what that changes.
- Read a risk overlay against its own baseline rather than against zero.

**Book reference**: Chapter 19, Sections 19.3 to 19.6.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Prerequisites**: [[[ML4T_A3_0001]]](15_portfolio_management.ipynb), whose allocation
stage supplies the combinations the overlays are applied to.

**What it writes**: one row in [[ML4T_A3_0002]] per combination and risk control, at
[[ML4T_A3_0003]] - and no row for the un-overlaid strategy, which is why
[[[ML4T_A3_0004]]](17_costs.ipynb) pools this stage with [[ML4T_A3_0005]] and [[ML4T_A3_0006]] rather than reading
it alone. [[[ML4T_A3_0007]]](20_strategy_analysis.ipynb) reads the whole pipeline, this
stage included.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
## 1. What the overlays are applied to

The combinations are the allocation-stage leaders. Nothing is re-selected here: the prediction,
the concentration and the allocator are held exactly as registered, and the only thing added is
the rule. That is what makes each overlay's Sharpe comparable with the baseline it came from -
and what lets [[[ML4T_A3_0001]]](17_costs.ipynb), which runs after this stage, decide between an
overlaid and an un-overlaid combination on the measurement rather than on the order of the chain.

**Position rules need a bar-by-bar engine.** A stop-loss has to be evaluated on every bar of the
holding period to know whether it fired, so a case study whose backtests are computed as a
vectorized weight-times-return product cannot express one. This case study runs on the engine, so
both rule families are available; the check below reports which, rather than assuming.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
**The population the baselines are drawn from.** A refit publishes a second generation under the
same population name and leaves the one it replaced in the registry, backtests and all. An
overlay applied to a retired baseline measures a rule against a strategy its own publisher no
longer stands behind, and the comparison reads exactly like a valid one. The same is true of a
baseline no population ever listed: nobody retired it, so only a membership test excludes it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0009-p000

~~~~~~markdown
## 2. The grid, and where the thresholds come from

The declared grid is a set of round numbers - stops at three, five, ten and fifteen percent,
trailing stops from one to twenty, time exits at ten, twenty and forty bars. Round numbers are
what a reader would reach for, which is exactly why they are worth testing: a one percent
trailing stop on a fund whose ordinary daily move is around one percent fires on nothing in
particular.

The calibrated thresholds are the alternative. **Maximum adverse excursion** is how far a
position went against you before it closed, measured over the positions this strategy actually
held. Taking a percentile of that distribution sets a threshold in the units of what this
universe does rather than in round numbers, so a rule at the 25th percentile fires on the quarter
of positions that moved furthest against the signal and leaves the rest to resolve at the
rebalance. The two sit in the same grid so the comparison is direct.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## 3. The sweep

The allocation weights are computed **once per combination** and reused for every risk variant of
it. Weights are a property of the prediction, the concentration and the allocator, none of which
a risk rule changes, and the expensive allocators would otherwise be re-solved once per rule.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## 4. What each rule cost and what it bought

[[ML4T_A3_0001]] is the change against the allocation-stage baseline the overlay was applied to,
which is the only comparison that isolates the rule. Against zero every row would look fine,
because the strategy was already positive before any rule was added.

An overlay is worth adopting when it reduces the drawdown **and** does not spend the Sharpe to do
it. Drawdown reduction on its own is available for free by holding less: the question is whether
the rule found the losses worth avoiding, or merely closed positions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0016-p000

~~~~~~markdown
### Sharpe against drawdown, one point per overlay

The vertical axis is the change in Sharpe against the baseline and the horizontal axis is the
drawdown the overlay produced. A rule in the upper left reduced the drawdown without spending the
Sharpe; one in the lower left bought its drawdown reduction with return; one on the right did
neither. The dashed horizontal line is the baseline: everything below it made the strategy worse
on the measure that matters.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>
