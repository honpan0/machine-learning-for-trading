# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/09_options_continuous.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Backtesting → 回測
- Label → 標籤
- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Constructing Continuous Options Series

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Demonstrate why a "constant-maturity" option series chains together different
contracts, produces phantom price jumps at every roll, and contaminates label
construction. Implement two clean alternatives: same-contract holding returns
(correct labels) and a roll-zeroed continuous reconstruction (backtestable
mark-to-market).

## Learning Objectives

- Detect contract rolls in a 30-day ATM straddle time series and quantify the
  resulting bias against non-roll-day returns.
- Compute same-contract holding returns by looking up the entry contract's
  exit price in the raw option chain.
- Build a continuous price series suitable for backtesting, and measure what the choice of
  roll-day return does to it.
- Tell apart the construction a label needs from the one a mark-to-market series needs.

## Book Reference

§2.2, "The asset-class market data landscape" - the derivatives part of it. The futures
analogue is [[ML4T_A3_0002]]; the case-study scale-up is
[[ML4T_A3_0003]].

## Prerequisites

- [[ML4T_A3_0004]] for option-chain structure.
- [[ML4T_A3_0005]] for theta and time decay.
- The AlgoSeek S&P 500 options EDA parquet at [[ML4T_A3_0006]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## 1. The Constant-Maturity Construction

A 30-day ATM straddle is a common volatility instrument: you buy (or sell) both
an ATM call and an ATM put with ~30 days to expiration. To build a daily time
series, we select the "best" straddle each day — the one closest to 30 DTE and
50-delta.

The problem: this selection is **independent** each day. The contract identity
(strike, expiration) changes whenever a new weekly/monthly option enters the
25–35 DTE window or the underlying moves enough to shift which strike is ATM.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0004-p000

~~~~~~markdown
### Loading the raw chains for one symbol
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
### Selecting a constant-maturity straddle

For each trading day, select the ATM straddle closest to 30 DTE.
This replicates the logic in [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0007-p000

~~~~~~markdown
### Straddle Selection Logic

For each trading day, select the ATM straddle closest to 30 DTE.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
## 2. The Roll Problem

How often does the underlying contract change?
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Roll days against non-roll days

If the constant-maturity series were a genuine instrument, days when the contract changed and
days when it did not would have similar return characteristics. They do not.

**But "the contract changed" is two different events.** The selection can move to a different
strike at the same expiration, because spot drifted and a neighbouring strike is now closer
to the money. Or it can move to a different expiration, because a new listing entered the
day-count window. Only the second resets time value, so only the second should produce the
phantom step - and treating them as one category would average a large effect with a small
one and report something in between that describes neither.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
The split is the result, and only one of the three groups is positive. Expiration changes
carry a large positive mean. Days when only the strike moved and days when nothing changed
are close to each other and both negative, which is ordinary time decay showing through.

The expiration result is what the mechanism predicts. Moving to a later expiration buys back
the time value decay had removed, and the series records the difference as a return no
position earned.

The strike result invites a conclusion it does not support. Moving to a neighbouring strike
at the same expiration exchanges one contract for a similar one with no time value to reset,
and the group mean duly lands beside the group mean for days when nothing changed. That is a
statement about two averages. It is not a statement about the individual days, which is
where a return series is used, and Section 5 measures those directly once the held contract's
own price is available. The answer there is not the one this table suggests.

Lumping all the changes into a single "roll day" average blends one large positive effect
with two indistinguishable negative ones and reports a figure describing none of the three.

What this table does not establish is that strike changes are harmless. Two group means can
agree while the individual days behind them are wrong in both directions, and the quantity
that matters is per-day: the gap between the return the series records and the return the
contract actually held would have earned. That gap needs the held contract's own price,
which Section 5 recovers; the comparison is made there, on the days themselves.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0014-p001

~~~~~~markdown

The futures analogue is roll yield, and the difference is one of degree that becomes a
difference in kind. A quarterly futures roll contributes a small adjustment four times a
year. This series reselects on most days, so the phantom component is not an occasional
correction to an otherwise sound return stream - it is a large part of the stream.

**A note on sign, because everything below depends on it.** Every return in this notebook is
the return of the *instrument*: today's price over yesterday's, minus one. Positive means the
straddle got more expensive.

That is the long convention, and it is used here for every series without exception, because
a price series and its returns should mean the same thing in every section. The case study
this feeds sells straddles rather than buying them. A seller's P&L over a *single* period,
before costs and for a fixed quantity, is the negation of the long return printed below.

That does not extend to a cumulative return, and the difference is not small. Negating each
period's return and compounding is a different series from negating the compounded result:
a long series of [[ML4T_A3_0001]] then [[ML4T_A3_0002]] compounds to [[ML4T_A3_0003]], and so does its per-period
negation. A cumulative short return is only defined once the position's sizing is - whether
the quantity is fixed for the whole period or reset against equity each day - so this
notebook prints the long series and states the convention where a short figure is needed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p001>>>
<<<ML4T-ZH-END:c0014-p001>>>

### c0015-p000

~~~~~~markdown
### The sawtooth
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
Both panels are built in one cell so the inline backend does not flush the figure
mid-construction and publish a half-drawn copy above the finished one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
Run lengths below come from the contract identity itself. Encoding runs of an "unchanged"
flag instead drops the first observation of every contract - identities A, B, B, B give two
unchanged flags although B is held for three days - and understates every holding period by
exactly one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
