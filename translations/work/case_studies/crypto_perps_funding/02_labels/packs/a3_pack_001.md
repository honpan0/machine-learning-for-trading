# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/02_labels.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Cross-validation → 交叉驗證
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto Perpetuals: Label Engineering

Every model in this case study is trained to predict the label defined here, so an error in
it is silent where it is made and reaches every metric and every backtest after it. This
notebook fixes the execution convention, proves each labelled row has a complete forward
window, measures how much independent information those rows carry, establishes what the
simplest signal already earns against the label, and writes the label files the rest of the
case study trains against.

## Learning objectives

- Move a provider's bar-open timestamps onto the clock at which each bar is actually known,
  and express a forward return from that boundary
- Measure a forward window on the price series the return is taken from, so that a gap in a
  predictor cannot decide whether a label exists
- Assert, rather than describe, that every labelled row has a gap-free window inside one
  symbol, and account for every row that carries no label
- Restrict a diagnostic to the rows whose outcome is already known when the holdout begins,
  which is not the same as the rows observed before it
- Measure how much independent information overlapping forward windows carry, both as a
  decay curve and as an effective row count
- Measure what the simplest declared signal earns against the label, under a standard error
  that accounts for dependence between consecutive measurements

## Book reference, prerequisites and artifacts
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

Chapter 7, Section 7.2. Reads the Binance eight-hourly perpetual bars through
[[ML4T_A3_0001]], whose coverage
[[[ML4T_A3_0002]]](01_feasibility_analysis.ipynb) establishes, and
[[ML4T_A3_0003]], which declares the label set, the horizons and the holdout boundary.
Writes [[ML4T_A3_0004]], [[ML4T_A3_0005]], [[ML4T_A3_0006]]
and [[ML4T_A3_0007]].

[[ML4T_A3_0008]] reads the primary label file directly; [[ML4T_A3_0009]] and
the modelling notebooks read it through [[ML4T_A3_0010]]. The
walk-forward folds every one of them trains on are derived from the timeline of that same
file by [[ML4T_A3_0011]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0002-p000

~~~~~~markdown
Both parameters are unset by default, and both are read below. [[ML4T_A3_0001]] trims the history
to a later start; [[ML4T_A3_0002]] keeps only the first symbols in alphabetical order. Either one
shortens a run, at the cost of a thinner cross-section for the rank correlation in Section G.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## Configuration

Everything that defines a label is declared in [[ML4T_A3_0001]] and bound here. A horizon
or a boundary typed into a cell is a second copy of a value the rest of the pipeline reads
from the file, and the two drift apart the first time either is edited.

[[ML4T_A3_0002]] prefers an explicit [[ML4T_A3_0003]] entry and falls back to the
cross-validation buffer. The two fields are separate, because the gap that keeps folds
independent need not equal the horizon an outcome resolves over; here they coincide, and both
are declared in hours. Dividing by the length of a bar turns each into a number of settlement
periods, which is the unit a shift counts in. A day is three settlement periods on this grid,
and Section G's two smoothing windows are counted in days for the same reason: expressed that
way they stay right if the exchange ever changes how often it settles.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## A. The learning task

A perpetual future is a derivative contract with no expiry date. Nothing forces its price
back to the spot market the way a delivery date does, so the exchange makes one side pay the
other at fixed intervals instead: every eight hours, holders of the crowded side of the
contract pay holders of the other. That payment is called funding, and its size tracks the
*premium index*, the gap between what the perpetual trades at and what the underlying trades
at.

The hypothesis is that this premium is a crowding measure that mean reverts. When the premium
index sits far above its own recent level, longs are paying to hold the contract, and the
perpetual price is expected to give ground relative to the rest of the universe. The label is
therefore a forward price return on the perpetual itself, ranked across symbols rather than
judged in isolation.

The decision cadence comes from the market's own settlement rhythm. Binance settles funding
every eight hours, the premium index is published on that grid, and a decision can be acted
on at each settlement, which fixes the primary horizon at one period. The variant asks
whether the same relationship pays over three periods. That is a question about how long the
crowding takes to unwind, and about how often a strategy would have to trade, rather than a
second hypothesis.

One thing the label is not: the funding payment. The premium index predicts funding without
being it, because the realized rate adds an interest component and exchange clamps. A
strategy that collects funding is a separate construction on the funding-rate series, and
this label cannot measure it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>
