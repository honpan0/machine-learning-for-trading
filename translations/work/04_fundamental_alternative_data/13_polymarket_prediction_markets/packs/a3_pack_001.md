# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/13_polymarket_prediction_markets.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Polymarket Prediction Markets: Crypto-Settled Event Contracts

**Chapter 4: Fundamental and Alternative Data**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 4.4 (Understanding Alternative Data)

## Purpose

The previous notebook read the regulated prediction market. This one reads the other kind.
Polymarket runs on the Polygon blockchain, settles in a dollar stablecoin rather than dollars,
imposes no position limit, and lists whatever its users ask for. It is reported to carry far
more volume than the regulated venue, which Part 5 explains this feed cannot confirm, and it is
not available to US persons.

The pair is worth studying together because the differences between them are the differences
that matter when sourcing any alternative dataset from a venue rather than a vendor: who is
allowed to trade there decides who sets the price, and what the venue lists decides what
questions its data can answer.

## Learning Objectives

After completing this notebook, you will be able to:

- State the structural differences between a regulated and an unregulated prediction market,
  and say which of them affect the data rather than the trading.
- Establish how many markets, bars and dates a snapshot actually contains before computing
  anything from it.
- Recognize a threshold ladder on either venue, and check the monotonicity it has to satisfy.
- Explain why the volume fields of two venues cannot be compared, and what can be compared
  instead.
- Build the same probability features on both venues, and read them against the sample size.

## Prerequisites

[[ML4T_A3_0002]]

## Cross-References
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- **Upstream**: [[ML4T_A3_0001]]
- **Related**: [[[ML4T_A3_0002]]](12_kalshi_prediction_markets.ipynb) (the CFTC-regulated venue)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## 1. The two venues

Both list binary contracts whose price is a probability. Everything else about them differs,
and the differences fall into two groups.

| | Polymarket | Kalshi |
|---|---|---|
| Regulator | None | Commodity Futures Trading Commission |
| Settlement asset | USDC, a dollar stablecoin | US dollars |
| Position limit | None | Twenty-five thousand dollars per contract |
| Available to US persons | No | Yes |
| Listing | User-proposed, broad | Exchange-defined, narrower |

The first four rows are about **who can trade and how much**, and they decide whose views the
price aggregates. A venue closed to US persons prices a US interest-rate decision using the
opinions of everyone except the people closest to it, which is a selection effect, not a
defect, and one to keep in mind before treating either price as the market's view.

The last row is about **what gets listed**, and it decides which questions the data can answer
at all. It is also the row most often overstated, as Part 3 shows.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## 2. What the snapshot contains

The downloader ships a small, reproducible sample rather than a live query, so the first thing
to establish is how small. Every statement later in this notebook is bounded by these three
numbers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0009-p000

~~~~~~markdown
A snapshot in which most markets appear once and none appears more than twice is a smoke test,
not a history. It is enough to read a cross-section of prices and to compare the two venues'
structure; it is not enough to compute a distribution, a volatility, or anything else that needs
a series. The sections below stay inside that limit and say where it binds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
The gap in the middle of that axis is the normal state of a prediction market and it is worth
understanding before building anything on one. A contract only sits near even odds while the
question is genuinely open; most listed questions are either already decided by events or were
never close. A feature built on "the market's probability" is therefore a feature that is
informative on a small and shifting subset of the listed universe, and the rest of the time it
is reporting a settled fact.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
## 3. Both venues price ladders

The obvious way to describe the difference between the two venues is that Kalshi lists a ladder
of rate thresholds and Polymarket lists individual event bets. The snapshot refutes it: several
of these markets ask whether Bitcoin is above each of a series of levels on the same date,
which is the same construction as Kalshi's rate ladder applied to a different underlying.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0013-p000

~~~~~~markdown
Two things have to match before a set of contracts is a ladder rather than a collection.
They must resolve on the **same terms** - a Bitcoin level on 2 May and the same level on
31 May are different questions - and they must be priced on the **same date**, since a
comparison across dates measures the market moving rather than the shape of the distribution.
The ticker carries the resolution term, so both conditions can be enforced rather than assumed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0016-p000

~~~~~~markdown
The curve has the same shape as the Fed ladder in the previous notebook and the same constraint
holds: a higher threshold cannot be priced above a lower one. What differs between the venues is
not the mechanism but the subject. Kalshi's ladders are on the outcomes its regulator has
approved, which in practice means economic releases and policy decisions; Polymarket's are on
whatever its users proposed, which in this snapshot means crypto prices, a space launch and a
central bank appointment.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
## 4. The same event on both venues

Both list contracts on Federal Reserve decisions, which is the one place a direct comparison is
available. The comparison is still not like for like, and the reason is instructive.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
The two panels carry separate scales deliberately. Kalshi's ladder spans the whole probability
range because a ladder always does: some threshold is nearly certain and some is nearly
impossible. Polymarket's policy contracts are all tail events in this snapshot, so a shared axis
would compress them to invisibility and would also suggest a like-for-like comparison that does
not exist. These are different questions about the same institution, not two prices for one
contract.

Where the venues do list the same question, the difference between their prices is the
interesting quantity, and it is a measure of who is allowed to trade rather than of who is
right. That comparison needs both venues to list a genuinely identical contract, which this
snapshot does not contain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
