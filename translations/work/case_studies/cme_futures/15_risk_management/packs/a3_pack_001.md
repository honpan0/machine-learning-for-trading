# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/15_risk_management.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Drawdown → 回撤
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Risk Overlays

For each return horizon, this notebook selects the highest validation Sharpe from the immutable
union of signal and allocation results, then applies every position-level risk rule declared in
the case-study configuration. Stop-loss, trailing-stop, and time-exit parameters are fixed before
the validation backtest. They are not calibrated from the same validation price path they assess.

Risk rules execute inside the existing futures engine after product-keyed target decisions cross
the typed boundary. Every declared rule must finish, and the resulting per-label candidate sets
remain eligible for final validation selection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What a risk overlay is, and why it is a separate stage

The stages before this one decided *what to hold*: a signal ranked the products, an allocation
rule decided how much of each. A risk overlay decides *when to stop holding it* - it sits on
top of an existing set of positions and closes them on a condition the signal never
considered.

The three rules here are the standard family. A **stop-loss** exits when a position has lost
more than a set amount from entry. A **trailing stop** exits when it has given back a set
amount from its best level, so it protects an unrealized gain rather than only the entry
price. A **time exit** closes after a fixed holding period whatever the position is doing, on
the reasoning that a signal with a horizon has nothing to say beyond it.

### The asymmetry these introduce, which is the point and the danger

A signal is symmetric about its own prediction: it is as willing to be wrong in one direction
as the other. A stop is not. It truncates the loss side of the distribution and leaves the
gain side alone, and that is why it appeals.

What it also does is convert an unrealized loss into a realized one at the worst available
moment, and give up any recovery that would have followed. For a mean-reverting signal - which
describes carry, the signal this case study trades - that is a direct conflict: the position
is exited precisely when the thing the signal is betting on has become most attractive. A stop
on a mean-reverting strategy is not a free reduction in risk. It is a change to the strategy,
and it can easily be a change for the worse.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

That is the whole reason this is measured rather than assumed. Risk management is the part of
a strategy where intuition is least reliable and where "obviously prudent" is applied without
testing more often than anywhere else in the pipeline.

### Why the parameters are fixed before the backtest, and not after

The stop distances and holding periods come from [[ML4T_A3_0001]] and are fixed before the
validation backtest runs. They are deliberately **not** calibrated on the price path they are
then assessed against.

The reason is that this stage is unusually easy to cheat at without noticing. Choosing a stop
level by trying several and keeping the one with the best validation Sharpe would find the
level that best avoided the particular drawdowns that particular history happened to contain,
and would report the result as a risk improvement. Nothing about it would generalize, and
nothing in the output frame would show what happened - the returns would simply look better.
Fixing the parameters in configuration is what makes the comparison between overlay and no
overlay a real one.

### Why every declared rule must finish

A rule that failed and was skipped would leave a candidate set that silently means "the rules
that happened to work", and the selection downstream would then choose from it as though it
were the declared set. Failing the notebook is the only outcome that keeps the population
equal to the configuration.

### These candidates stay eligible
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

Unlike the cost sweep, risk-overlay results are part of the final selection pool.
[[ML4T_A3_0001]] selects over the union of signal, allocation and risk-overlay
backtests, so an overlay that genuinely improves validation Sharpe can be what the case study
ships - and one that does not is visible as such next to the configuration it was applied to.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>

### c0004-p000

~~~~~~markdown
## Fixed per-label inputs and risk rules

No candidate cap or runtime-dependent skip is allowed. The configured list is the population.

**What the overlay is applied to.** An overlay needs an existing strategy to sit on, and there
is one per label: the highest validation Sharpe from the immutable union of the signal and
allocation stages. Taking the best of the two stages rather than the signal alone matters,
because an overlay applied to a weaker parent would be measuring the overlay against a
strategy the case study would not have shipped anyway.

**Why per label rather than one overall.** Each return horizon is a different prediction
problem and its best configuration is chosen within its own horizon. Picking one parent across
all labels would let the strongest horizon's configuration stand in for horizons it was never
fitted for, and the overlay comparison would then be confounded by which label the parent came
from. Every configured rule runs against every label's own parent, so the comparison within a
label is like for like.

**Why the configured list is the population, with no cap.** A runtime cap would make the set
depend on how long the run took, which means a re-run could select from a different set and
nothing would record that it had. The rules are declared in configuration precisely so the
population is a property of the configuration rather than of the execution.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## Execute and freeze risk candidates

Each request carries the fitted prediction checkpoint, product decisions, fold-transition policy,
contract and roll inputs, and one risk rule. Missing members fail before the candidate set exists.

One request is one rule applied to one parent, so a rule's effect is read against its own
parent rather than against the field. Two rules that both improve Sharpe are not therefore
combinable: they may exit on the same moves, and their joint effect is not the sum of their
separate ones. Nothing here estimates that, and a reader stacking rules on the strength of
this table would be assuming an additivity it does not measure.

The results are frozen as a named population, and [[ML4T_A3_0001]] in the
parameter cell is how a re-run names the generation it retires. A retired snapshot stays in
the registry rather than being deleted, so a Sharpe quoted from an earlier generation remains
traceable to the population it was computed over.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>
