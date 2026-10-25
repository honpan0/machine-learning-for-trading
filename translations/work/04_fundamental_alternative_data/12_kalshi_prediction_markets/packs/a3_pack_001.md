# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/12_kalshi_prediction_markets.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Kalshi Prediction Markets: Regulated Event Contracts

**Chapter 4: Fundamental and Alternative Data**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 4.4 (Understanding Alternative Data)

## Purpose

A prediction market contract pays one dollar if a stated event happens and nothing if it does
not. Its price is therefore a probability, quoted directly, with no model in between: a contract
on "the federal funds rate is above four and a quarter percent at the April 2027 meeting"
trading at fourteen cents is a fourteen percent chance, priced by people with money at stake.

Kalshi is the first such exchange the Commodity Futures Trading Commission has designated in the
United States, which makes it a legal venue rather than an offshore one and puts its data in
reach of an institutional research pipeline. This notebook reads its Federal Reserve rate
contracts, repairs the ingestion artifacts a thinly traded feed produces, checks the one
arbitrage relation the contracts have to satisfy, and measures whether there is enough trading
behind the prices to build a feature on.

## Learning Objectives

After completing this notebook, you will be able to:

- Read a binary event contract's price as a probability, and decode a ticker into the event it
  settles on.
- Detect the ingestion artifacts a carry-forward feed produces, and repair them without letting
  a repair introduce information from the future.
- Read a family of contracts on the same event at different thresholds as a distribution, and
  check the monotonicity that distribution has to satisfy.
- Measure the trading behind a quoted price, and distinguish a price that moved from a price
  that was carried.
- Build the probability features a rate-sensitive strategy would use, and say what the sample
  supports.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Prerequisites

[[ML4T_A3_0001]]

## Cross-References

- **Upstream**: [[ML4T_A3_0002]]
- **Related**: [[[ML4T_A3_0003]]](13_polymarket_prediction_markets.ipynb) (the unregulated, higher-volume alternative)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## 1. What a contract is

A Kalshi contract settles at one dollar or nothing, so its price sits between the two and is
read as the probability of the event. The tick is a cent, which sets the resolution of that
probability at one percentage point.

**What this feed carries is the bid, not a mid or a trade.** The downloader takes
[[ML4T_A3_0001]] - the highest price anyone is currently offering to pay for the YES side - so every
price below is a lower bound on what the market thinks, short by whatever the spread is. On a
liquid contract that is a cent; on the contracts here, where days pass without a trade, it can
be a great deal more, and nothing in the file says how much.

| Property | Value |
|----------|-------|
| Regulator | Commodity Futures Trading Commission |
| Settlement | US dollars |
| Position limit | Twenty-five thousand dollars per contract |
| Trading hours | Continuous |
| Minimum tick | One cent |

### Reading a ticker

[[ML4T_A3_0002]] names three things: [[ML4T_A3_0003]] is the federal funds rate series, [[ML4T_A3_0004]] is the
April 2027 meeting of the Federal Open Market Committee, and [[ML4T_A3_0005]] is the threshold. The
contract pays if the rate is **above** four and a quarter percent after that meeting, so its
price is the market's probability of that.

The threshold is what makes the series interesting. One contract gives one probability; a
ladder of thresholds on the same meeting gives the whole distribution, which Part 4 draws.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## 2. The data, and how much trading is behind it

The first three numbers to establish are how many bars there are, how many of them recorded a
trade, and how many recorded a change in price. On a market this young those are very different
numbers, and everything after depends on which one a statistic is really counting.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
Five traded bars out of several hundred is the fact that governs the rest of the notebook. The
price on every other bar is a quote carried forward, which is a real number - somebody is
willing to trade there - and is not a transaction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0008-p000

~~~~~~markdown
### The artifacts a carry-forward feed produces

Two problems follow from the thinness, and both have to be dealt with before anything is
computed.

A price field of exactly zero alongside a positive high is an ingestion artifact. A live
contract trades strictly inside zero and one, and one that closes near ninety cents cannot have
printed a true zero the same day. Left in, a single such bar makes a pinned contract look like
the widest-ranging one in the universe.

On a bar with no volume there is also no intraday range: the high and the low are carried from
whenever the contract last traded, so the distance between them measures the age of the quote
rather than the day's uncertainty. The close is the only field worth keeping on such a bar.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0011-p000

~~~~~~markdown
## 3. The contract universe

With the artifacts out, each contract can be summarized by where its probability started and
ended, how often that probability changed at all, and how often it changed because somebody
traded.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
The gap between the last two columns is the whole story of this dataset. Prices move far more
often than trades happen, because the quote is revised whether or not anyone crosses it. That
is not a defect - a revised quote carries information - but it fixes what a statistic computed
on this series is measuring, which is quote revisions and not trading.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
