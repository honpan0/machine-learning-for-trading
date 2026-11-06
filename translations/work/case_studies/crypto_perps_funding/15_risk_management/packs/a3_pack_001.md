# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/15_risk_management.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Slippage → 滑價
- Drawdown → 回撤
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto perpetuals: fourteen ways to leave a position early

The two stages before this one decided which contracts to hold and how much of each. Neither
decided when to stop holding one. Every position so far ran until the entry rule stopped
selecting it, which on an 8-hourly rebalance is at most one funding interval but can be many.
This notebook adds one rule at a time that closes a position before the entry rule would.

Three kinds are declared in [[ML4T_A3_0001]]. A **stop loss** exits when the position is down
by a fixed fraction of its entry price. A **trailing stop** exits when it is down by a fixed
fraction of the highest price it has seen, so the exit level rises with the position and never
falls. A **time exit** closes after a fixed number of bars whatever the price has done.

**What an overlay can and cannot do.** It never adds a position, so it cannot improve a ranking.
All it can do is cut the left tail of positions the ranking already chose, and it pays for that
in two ways: an exit is a trade, so it costs commission and slippage, and a position closed
early stops earning - or paying - funding. On perpetual futures the second is not a rounding
error, because funding is the reason a carry strategy holds anything at all.

**Learning objectives.** By the end of this notebook you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Tell a position-level control from a portfolio-level one, and say which of them a
  single-strategy book can even express.
- Run an overlay so that it differs from its own no-overlay result in one field, and read the
  paired difference.
- Say why a threshold calibrated on the split it is then selected on is not eligible, even when
  the calibration looks like a property of the data rather than of the returns.
- Recognise the two distinct costs an early exit pays on a funding-bearing instrument.

**Book reference**: Chapter 19 (Risk Management).

**Prerequisites**: [[[ML4T_A3_0001]]](14_portfolio_management.ipynb) has frozen a
candidate set per label.

**What it writes**: one [[ML4T_A3_0002]] backtest per label and declared control, and one
candidate set per label spanning all three stages, which
[[[ML4T_A3_0003]]](19_strategy_analysis.ipynb) selects the final configuration from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## 1. What the overlay is applied to

The funnel gives this stage the top one, per [[ML4T_A3_0001]].
One is narrow on purpose: an overlay is a second search over the same validation folds, and
fourteen controls applied to ten configurations would be a hundred and forty readings of one
year of data. The question is whether a control improves the configuration the case study
already arrived at, not which control looks best somewhere in the grid.

This is the stage that reads the allocation set. [[[ML4T_A3_0002]]](16_costs.ipynb) is downstream of
it rather than beside it: cost sensitivity prices the configuration that survives the whole
funnel, so it reads the set frozen at the end of this notebook, not the one read here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
One row per label: the configuration each overlay is measured against, and the no-overlay
numbers the paired difference is taken from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 2. The declared controls

Fourteen position-level rules: four stop losses, seven trailing stops and three time exits. A
**position-level** control reads one position's own price path and decides about that position.
A **portfolio-level** control reads the whole book - its drawdown, its realized volatility, a
regime estimate - and scales or halts everything at once. [[ML4T_A3_0001]] declares no
portfolio-level controls for this case study, and the cell below reports that rather than
assuming it: a single long-short book of nineteen contracts rebalanced every eight hours has no
regime state distinct from the positions themselves, so a portfolio control here would be a
second copy of the position controls with a slower trigger.

### Why no calibrated threshold is in the grid

A tempting fifteenth kind is a threshold read off the data - the tenth percentile of maximum
adverse excursion, say, so the stop sits where prices actually turn. It is not here, and the
reason is worth being precise about, because the calibration looks innocent.

The thresholds would be fitted on the validation prices, and the overlay is then selected on
validation Sharpe. That makes the threshold part of the search rather than an input to it, and
the resulting Sharpe is not a measurement of the control - it is a measurement of how well the
control was fitted to the same year it is scored on. The declared grid is fixed in
[[ML4T_A3_0002]] precisely so the width of the search is a stated property of the case study
rather than something a notebook can widen while running.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 3. Running the grid

For each label, the chosen configuration's own strategy is read back from its registered
specification and re-run once per control, with the [[ML4T_A3_0001]] field added and nothing else
changed. The prices carry the same warmup the allocator was given at the allocation stage, so a
moment-based allocator weights from the same history it did there.

The control is nested under [[ML4T_A3_0002]], which is the key the engine reads. A control
passed as the flat mapping [[ML4T_A3_0003]] declares would install no rule and run the unprotected
book, and it would do so without failing: the mapping still lands in [[ML4T_A3_0004]], so the
specification hashes differently and registers as a distinct result under the control's name.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0013-p000

~~~~~~markdown
## 4. What came out

Read back from the registry, with the control recovered from each registered specification.
[[ML4T_A3_0001]] is derived the same way [[[ML4T_A3_0002]]](14_portfolio_management.ipynb)
derives it, from the registered return series rather than from the control's name, because a
control that closes everything and never re-enters would otherwise look like a comparable
result with a better Sharpe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
