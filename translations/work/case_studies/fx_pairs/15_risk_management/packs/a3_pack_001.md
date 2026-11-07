# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/15_risk_management.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Drawdown → 回撤
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Position Risk Controls - FX Pairs

The two stages before this one decided what to hold and how much. A position risk rule decides
when to stop holding it. That makes this the first stage whose effect depends on the price path
inside a holding period rather than on its endpoints: a position that ends the period down four
percent and one that dipped nine percent on the way to ending down four are indistinguishable
to every earlier stage, and a stop separates them.

The rules compared here are declared in [[ML4T_A3_0001]], not invented in the notebook: four
fixed stop-loss levels and five trailing stops. Portfolio-level controls - a drawdown cap or a
daily loss limit applied to the book as a whole - are absent for this case study, so nothing in
this stage restrains the aggregate. Each position is governed on its own.

This notebook selects one validation strategy per label from the equal-weight and allocation
populations, then changes only its predeclared position-risk rule. Cost-sensitivity results are
excluded from selection, and the reason is a selection defect rather than tidiness: a cost sweep
re-prices one strategy under several assumptions, so a ranking that included those rows would
advance whichever strategy had been measured under the kindest cost model. The comparison would
read as a difference between strategies and be a difference between assumptions.

**Learning objectives**

- Select one parent strategy from an immutable validation cohort.
- Compare declared position controls while preserving upstream identity.
- Freeze the complete risk population before final strategy selection.
- See why the count of variants tried belongs beside any improvement they produce.

**Book reference**: Chapter 19

**Prerequisite**: [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Select the parent strategy

Production uses the same signal-plus-allocation candidate cohort as the cost notebook. Preview
mode resolves one deterministic allocation result from the reduced prediction catalog.

One parent per label, chosen by best validation backtest Sharpe from the sealed pre-risk cohort.
Sharing the cohort with the cost notebook is deliberate: both stages branch from the same
strategy, so their results are siblings of one parent and can be read against each other. If
each stage picked its own parent, a cost result and a risk result for the same label would
describe two different strategies and the comparison between them would mean nothing.

The cohort is sealed before it is ranked, which is what makes "best" a statement about a fixed
set. A cohort that could still gain members after the selection would let a later run change
which strategy this notebook chose, retroactively, with no record that it had changed.

The [[ML4T_A3_0001]] filter below carries the same trap [[ML4T_A3_0002]] documents:
it names the schema version a row was written under, not whether its producer still publishes
it. A refit leaves the replaced generation in the registry, complete and current, so the filter
alone would let a retired prediction set into the cohort - and nothing would fail, because a
retired prediction still produces a correct backtest. [[ML4T_A3_0003]] reads the lineage,
which is where the retirement is recorded.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## Plan and freeze exact risk siblings

Every position rule is declared in [[ML4T_A3_0001]]. Portfolio-level controls are absent for
this case study. The identity audit removes only the risk block and chapter label; the prediction,
signal, allocation, configured costs, and execution contract must remain unchanged. Production
freezes every expected risk identity before the first backtest is written.

The audit is what makes each result a sibling rather than another strategy. Two backtests that
differ in their stop and in nothing else can be subtracted; two that differ in their stop and
their cost model cannot, and no field in the output would say which case you are looking at.
Removing exactly the risk block and the chapter label, then requiring the remainder to match,
is how that is established rather than assumed.

How a stop is evaluated is worth knowing before reading its results. [[ML4T_A3_0002]] and
[[ML4T_A3_0003]] in [[ML4T_A3_0004]] trigger on the bar's low or high where the price frame
supplies a range, and fall back to the close where it does not, so the same threshold is a
different rule depending on what the bars carry. The fill is a separate configured choice:
filling at the stop price, at the bar's extreme, or at the close give materially different
answers for one triggered stop, and the gap between them widens exactly in the volatile periods
a stop is meant to handle. A stop's measured benefit is therefore partly a statement about the
fill model, and that is a declared assumption rather than a property of the market.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Execute the frozen risk grid, and validate what was frozen

The population is validated in the cell that fills it: the expected set was written down before
the first member ran, and [[ML4T_A3_0001]] is what turns that declaration into a published
result.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>
