# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/16_costs.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Transaction costs → 交易成本
- Slippage → 滑價
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Transaction-Cost Sensitivity - FX Pairs

This notebook selects one validation strategy per label from the equal-weight, allocation and
risk-overlay populations, then changes only its percentage transaction costs. The sensitivity
grid does not participate in later model or strategy selection.

Costs are swept last because a cost curve is only informative about the strategy that would
actually be traded, and that strategy is not settled until the risk controls have been measured.
Sweeping before the overlay charges the grid against a configuration the next notebook may
discard.

This is a perturbation analysis, not a choice. It asks what happens to a settled strategy if the
cost model is wrong, which is a different question from which strategy to trade. The two must
stay separate for a mechanical reason: a strategy allowed to compete on its own cost assumption
would win by having costs assumed away, and the ranking would report the most optimistic
assumption rather than the best strategy.

**Why basis points here.** FX spreads are quoted in pips, a fraction of the rate itself, so a
proportional charge is how the friction is actually expressed - there is no share or contract
to bill per unit. Case studies where nominal prices are stable, or where spreads are measured
from quote data, use per-share instead; applying a flat per-unit charge to a rate would assume
spread scales with the level, which it does not. The configured grid runs from 0 to 50 basis
points per traded leg, against a real quoted band of roughly 1 to 3 for major pairs and 3 to 8
for crosses, so most of the grid sits deliberately past anything plausible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

[[ML4T_A3_0001]] names the cost components as spread and swap points. That list is a
taxonomy, read by the Chapter 18 teaching notebooks to describe what the friction consists of;
the backtest charges a single aggregate rate per traded leg. So this curve perturbs the
aggregate, and the overnight financing cost of carrying a position is described rather than
separately priced.

**Learning objectives**

- Select from an immutable validation candidate set by backtest Sharpe.
- Preserve model, checkpoint, signal, allocation, and execution identities across a cost curve.
- Keep cost sensitivity outside the official selection cohort.
- Read a cost curve as a statement about turnover.

**Book reference**: Chapter 18

**Prerequisite**: [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
## Select one strategy for each label

Production selection considers the signal, allocation and risk-overlay populations together -
the same three stages the canonical validation rank-1 is selected over in
[[ML4T_A3_0001]]. All three are
candidates because each stage is an alternative to the one before it rather than an improvement
on it by construction. Naming only the overlays would charge the cost grid against a risk
control even where every control measured worse than leaving the position rule alone; naming
only signal and allocation would sweep a strategy the risk notebook has already improved on.
Which stage the parent came from is printed below rather than assumed, and the gap between the
best overlay and the best un-overlaid configuration is printed with it: a negative gap is the
measurement that the controls did not help on this label.

Cost variants are descendants of that choice and cannot improve their own chance of selection.
Preview mode uses a deterministic allocation request from the reduced catalog and remains
outside candidate sets.

Getting the parent wrong has a quiet failure mode. The cost curve would be computed correctly,
the population would freeze and validate, and every number would be right - about a strategy
the chapter does not report. Nothing raises, because a cost sweep over the wrong parent is a
perfectly valid sweep. That is why the stage the parent came from is printed rather than
assumed, and why the selection here is made over the same three stages, in the same way, as
[[ML4T_A3_0002]] selects the strategy the chapter goes on to describe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## Plan and freeze exact cost siblings

The configured cost grid is expressed as total basis points per traded leg. Commission and
slippage each receive half. The identity audit removes only the cost fields and the chapter label;
every remaining field must match the selected validation strategy. Production freezes the full
sensitivity set before the first backtest is written.

The even split between commission and slippage is a modelling convention, not a measurement.
Nothing in the data says the two halves of the friction are equal; the split exists so that a
single configured rate can populate two fields the backtest engine charges separately. Read the
total, not the halves.

What the curve measures, once it exists, is turnover. Cost enters the return series through
[[ML4T_A3_0001]] at each rebalance, so a strategy's sensitivity to the assumed rate is set by how
much of the book it moves and how often, not by how good its predictions are. Two strategies
with the same gross Sharpe can have breakevens that differ by an order of magnitude, and the
whole reason to plot a curve rather than report one number is that the difference is invisible
at any single rate. The quantity to read off is where the curve crosses zero and how far that
sits from the quoted band above - a strategy that survives to 40 basis points on pairs that
trade at 3 has room; one that dies at 4 is reporting an edge that is really a spread.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>
