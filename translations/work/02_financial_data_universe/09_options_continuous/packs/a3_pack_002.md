# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/09_options_continuous.ipynb；A3 Pack 002；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Backtesting → 回測
- Transaction costs → 交易成本
- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0022-p000

~~~~~~markdown
The teeth of the sawtooth are much finer than the description usually attached to one. Days
to expiration never sweeps the width of the selection window and resets: the longest run on
one contract is a handful of days and the average is under two, so what the panel shows is a
rapid zigzag inside a narrow band rather than a slow decay with occasional jumps.

The direction is still mostly downward, which is decay doing its work, and the upward steps
are the expiration changes identified above. But the scale matters for what follows. A series
that resets every few days is not a lightly contaminated version of a real instrument with a
few bad days in it; the contamination is the majority of its observations, and any adjustment
applied to those days touches most of the sample.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
## 3. Same-Contract Holding Returns

The correct return for a straddle trade is: enter a specific contract at mid on
day [[ML4T_A3_0001]], exit the **same contract** at mid on day [[ML4T_A3_0002]]. This requires
looking up that specific contract in the raw option chain [[ML4T_A3_0003]] days later.

[[ML4T_A3_0004]]

where [[ML4T_A3_0005]] identifies the specific strike and expiration.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0024-p000

~~~~~~markdown
### An exit-price lookup from the raw chain
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0027-p000

~~~~~~markdown
### Computing same-contract returns

For each day's constant-maturity straddle, find the same contract's price
[[ML4T_A3_0001]] trading days later in the raw chain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0030-p000

~~~~~~markdown
### Naive against same-contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0031-p000

~~~~~~markdown
The naive return is the one a [[ML4T_A3_0001]] on the constant-maturity series produces. For the
comparison to isolate the construction, both sides must cover the same window: the
same-contract return runs from the selection day to [[ML4T_A3_0002]] days later, so the naive
one has to as well. Entering a day later, as a label-shifted version would, means the two
series differ partly because they cover different days and partly because of the roll, and
the comparison could not separate them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
The correlation is the number to read, and it is low. Squaring it gives the share of variance
the naive series shares with the return an actual trade would have earned, and that share is
small: most of what the naive series moves on is not the trade.

The two are computed over the same days, on the same instrument, for the same holding period.
The only difference between them is that one follows the contract it entered and the other
follows whatever the selection rule picked up along the way. A label built from the second is
mostly a record of the selection rule.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
## 4. Building a Continuous Series for Backtesting

For backtesting we need a price series whose daily returns are actual P&L, with no phantom
jumps at rolls. Futures roll quarterly and suit Panama adjustment; straddles reselect on most
days, so the adjustment has to be return-based:

1. On a non-roll day, the daily return is the held contract's own move. Uncontroversial.
2. On a roll day, the naive-looking answer is to set the return to zero, on the grounds that a
   roll is a transaction rather than a return.
3. Reconstruct prices from whichever returns you chose: [[ML4T_A3_0001]].

**Step 2 is wrong, and the section measures how wrong.** On a roll day you did hold a
position: yesterday's contract, from yesterday's close to today's. It moved with the market,
and that move is real P&L. Zeroing it does not remove the phantom jump alone - it removes the
day's genuine return along with it.

The correct return for a roll day is the *held* contract's return: yesterday's strike and
expiration, priced yesterday and today. Section 3 already built the raw-chain lookup that
makes this available, so it costs nothing but the lookup.

Both are computed below and the difference is reported. Roll costs, the bid-ask actually paid
to switch, are a separate matter and are modelled as transaction costs in Chapter 18.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0038-p000

~~~~~~markdown
The held contract is recoverable on every roll day, so there is no data reason to discard the
day. And the return being discarded is not noise around zero: on average the position held
into a roll made money, so zeroing those days does not remove a bias, it introduces one.

This is also where the question Section 2 left open can be answered. Splitting the roll days
by what changed showed strike-only days averaging close to the days where nothing changed,
which says the two groups have similar means and nothing more. The construction error is a
per-day quantity - what the series recorded minus what the contract held would have earned -
and it can be large on individual days while averaging to little.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
Strike-only days are not clean. Their mean error is several percentage points, and the error
is defined as the raw series minus the held contract, so the sign says which way each group
is wrong on average: expiration days come out positive, meaning the raw series records more
than the position earned, and strike-only days come out negative, meaning it records less.
The two biases point in opposite directions and neither is small.

The mean absolute error exceeds the absolute mean in both groups, which says the individual
days are not all wrong in their group's direction - the average is a net of errors both
ways, and the worst single day in each group is tens of percentage points. A bias that
happens to be modest in the average can still be large on the day a label is taken.

So the two group means in Section 2 agreed for a reason that has nothing to do with the
series being right on those days. A day on which the strike moved records a return that
belongs partly to a contract nobody held, and the resemblance between that group's average
and the do-nothing group's average is a coincidence of aggregation. Comparing averages of a
quantity cannot establish that the quantity is correct case by case; only the case-by-case
comparison can, and here it fails.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>
