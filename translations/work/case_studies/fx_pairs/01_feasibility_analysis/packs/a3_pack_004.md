# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/01_feasibility_analysis.ipynb；A3 Pack 004；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0027-p000

~~~~~~markdown
## C. Design decisions

The sections above are evidence. This section is where that evidence meets the choices recorded
in [[ML4T_A3_0001]], and says what each one rests on.

### C.1 How often to rebalance

[[ML4T_A3_0002]] sorts the pairs at the daily snapshot and trades on the next bar's
open. Section B.3 supports that interval over the faster alternative: a four-hour move clears its
round trip about as often as not, where a one-day move clears it far more often, so the shorter
interval spends the same cost on a smaller move. Section B.2 supports it from the other side,
because the four-hour grid drops pairs that the daily snapshot keeps, and an ordering computed on
a bar that part of the universe did not print at ranks only the part that did.

### C.2 What would send this design back

A feasibility study is only useful if some result would have stopped it. Three would, and each is
measured where its evidence exists rather than here.

The one this notebook could have produced is a cost failure: if a typical move were smaller than
the round trip needed to capture it, the ordering would pay more to trade than the move it is
trying to catch. Section B.5 is that measurement, and Chapter 18 repeats it against the trades a
backtest actually places rather than against raw moves.

The other two are outcomes of the strategy rather than properties of the data. Chapter 7 asks
whether the ordering has any relationship at all to the returns that follow it, at any horizon.
And an ordering whose result comes entirely from being long or short the US dollar across the
board is a directional bet on one currency wearing twenty tickers rather than a cross-sectional
strategy; [[ML4T_A3_0003]] measures how much of what a model reads is that single exposure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0027-p001

~~~~~~markdown

### C.3 What the strategy does with the ordering

[[ML4T_A3_0001]] holds both sides: it buys the pairs at the top of the ordering and
sells the ones at the bottom. Section A gave the reason this is cheap here where it is expensive
in equities - a pair is already a relative price, so the sold side needs no borrow and costs what
the bought side costs. Holding both sides also puts a position on every pair the ordering covers,
which is what spends the whole of the breadth Section B.2 measures.

Each position gets an equal share of the money. A weighting optimised for risk would fold an
estimate of how the pairs move together into the result, and the ordering's own contribution
could no longer be separated from that estimate's. Chapter 17 compares the alternatives with the
ordering held fixed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p001>>>
<<<ML4T-ZH-END:c0027-p001>>>

### c0028-p000

~~~~~~markdown
## D. Walk-forward structure

### D.1 How much an evaluation has to spend

A panel of four-hour bars looks large, but a strategy that changes its positions once a day does
not get to treat every row as an independent opportunity. What it spends is decision dates. The
calendar says how many trading days the development period holds, and comparing that against the
days actually observed, and against the number of pair-days a complete panel would carry, says
whether anything is missing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
### D.2 The folds

A model is fitted on one stretch of history and evaluated on the stretch that follows it, then
the pair moves forward and the process repeats. Each fit-then-evaluate pair is a **fold**, and
evaluating this way is called **walk-forward**, because the split always runs in the direction
time does.

One detail decides whether the evaluation is honest. The return being predicted lands one day
ahead, so a training row dated on the last day of its block is labelled with a price from after
the block ends. Validating on the day immediately after training would score the model on data it
had partly seen already. The fix is to leave a gap between the two, at least as wide as the
horizon, and that gap is called **purging**. Its width comes from [[ML4T_A3_0001]] in [[ML4T_A3_0002]].
The two longer variants declare wider gaps of their own in [[ML4T_A3_0003]] - five days
for [[ML4T_A3_0004]], twenty-one for [[ML4T_A3_0005]] - and every stage that generates folds resolves the
gap for the label it is about to train on, so the timeline below is the primary label's design
rather than one design shared by all three.

The splitter is given the whole sample, holdout included, and applies the holdout boundary itself
from [[ML4T_A3_0006]], which is what every later stage does too. It is handed trading
days and no prices, so nothing the holdout contains reaches a number computed above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0030-p001

~~~~~~markdown

[[ML4T_A3_0001]] numbers folds chronologically, so fold 0 is the earliest and the highest
number is the last one before the holdout. The figure draws them earliest-first and labels each
with that number, so the labels count up alongside the dates; every later stage prints the same
ones. The three assertions below establish what the figure cannot: the gap is one trading
day against training blocks measured in years, far too narrow to see, so only counting it off the
timeline can confirm it matches the label horizon. The other two check that the number of folds is
the number [[ML4T_A3_0002]] declares, and that no validation window reaches into the holdout. The
figure then draws the boundaries the splitter returned rather than recomputing them, so the
picture and the folds cannot disagree.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p001>>>
<<<ML4T-ZH-END:c0030-p001>>>

### c0032-p000

~~~~~~markdown
## E. What this notebook hands on

Nothing. The universe is fixed and declared in [[ML4T_A3_0001]], which is where
this notebook reads it and where a later stage that needs the list reads it too. Section B.1
established that every declared pair quotes on every trading day of the sample, so there is no
eligibility table for a later notebook to filter on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
## F. What the evidence says about each setting

One row per setting: the evidence behind it, and the condition under which a reader working on
their own data would choose differently.

| Setting | Evidence | Choose differently when |
|---|---|---|
| [[ML4T_A3_0001]] | B.2, pairs quoting on each decision date and the independent bets they carry | a pair stops quoting at the daily snapshot, or the independent bets fall further |
| [[ML4T_A3_0002]] | B.2 pairs quoting by snapshot, B.3 move sizes against cost | a shorter interval starts clearing its round trip on a grid that carries the whole universe |
| [[ML4T_A3_0003]] | B.3, the declared range charged at its wide end for each of the two groups | spreads estimated from quotes sit outside the declared range |
| [[ML4T_A3_0004]] | D.1 trading days available, D.2 fold boundaries | the folds no longer fit the development period |
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>
