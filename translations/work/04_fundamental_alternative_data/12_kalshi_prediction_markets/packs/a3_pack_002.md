# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/12_kalshi_prediction_markets.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵

## 待翻譯英文單元

### c0014-p000

~~~~~~markdown
## 4. A threshold ladder is a distribution

All the contracts here are on the federal funds rate, and several share a meeting at different
thresholds. Since each pays if the rate is *above* its threshold, reading a meeting's contracts
in threshold order gives the market's implied survival function for the rate: the probability of
exceeding each level.

That structure carries an ordering. A higher threshold is harder to exceed, so the market's
probability for it cannot exceed a lower threshold's.

Checking that ordering on these prices is a **diagnostic and not an arbitrage test**, because
the prices are bids. Two contracts with different spreads can show a higher threshold's bid
above a lower one while their midpoints are correctly ordered, and nothing is tradeable: an
arbitrage needs the higher threshold's bid against the lower threshold's ask, net of fees.

So a violation here says the bid ordering is broken and does not say why. Two spreads of
different widths and two quotes of different ages both produce it, and separating them needs
the ask side, which this feed does not carry. It is still worth running, because a feed that
never violates the ordering is one whose quotes move together, and that is a property to know
about before either price is used.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
The downloader is configured for six Kalshi series and only the rate series uses the
meeting-and-threshold ticker shape, so the ladder is built from the contracts whose ticker
matches that shape rather than from everything loaded. A contract from another series reaches
the notebook as an unparsed row rather than as a crash or, worse, as a threshold read off the
wrong part of its name.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
The curve falls fastest between the thresholds the market thinks are live, which is where the
distribution has its mass. The difference between two adjacent points is roughly the
probability the rate lands between those two levels - roughly, because each point is a bid and
the difference of two bids carries both spreads.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## 5. How the probabilities moved

Over time, each contract's price traces the market's changing view. The contracts whose
thresholds sit near the expected rate move; the ones far above or below it stay pinned, because
no news plausibly changes their answer.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
Every path is a staircase rather than a curve, and that shape is the sample rather than the
market: with a handful of price revisions per contract over three months, the series is flat
between them by construction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
## 6. Features, and what this sample supports

The features a rate-sensitive strategy would take from this feed are the ones any probability
path suggests: how far it has moved recently, how variable those moves are, where it sits
against its own recent range, and whether it has settled near certainty.

The intraday range is deliberately not among them. After the repair, a non-traded bar has a high
and a low equal to its close, so a range feature would be zero on every bar except the five that
traded, and would be measuring the repair rather than the market.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
The last two columns are the measurement this section exists for. The momentum feature is
defined on most bars and non-zero on few of them, and the z-score is undefined wherever the
price held still for the whole window. A model fitted on these columns would be fitting a
handful of events dressed as a daily panel.

That is a statement about this snapshot and not about the method. The construction is the right
one and the feed will support it once the market is older; what a reader should take from the
table is the habit of counting how many of a feature's values are real before using it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## 7. Saving the feature panel
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## Key Takeaways

1. A binary contract's price is a probability with no model between the two, which is what makes
   a prediction market worth reading: every other forecast in a pipeline has to be calibrated,
   and this one is quoted. Check which price the feed carries, though. This one is the highest
   standing bid for the YES side, so it is short of the market's view by a spread that a thin
   book can make large.
2. A ladder of thresholds on the same event is a distribution, and its ordering is worth
   checking: a higher threshold's probability cannot exceed a lower one's. On bid prices that is
   a staleness diagnostic rather than an arbitrage test, since an arbitrage compares a bid
   against an ask.
3. Separate the bars that traded from the bars that were carried. A carried quote still holds
   information, but a statistic computed over both is measuring quote revisions, and a feature
   named for volume or for intraday range is measuring the carry.
4. Repair forward, never backward. Filling a leading gap from a later value puts tomorrow's
   price on today's date, and nothing downstream will show that it happened.
5. Count how many of a feature's values are real before fitting anything on it. A column that is
   defined on every row and non-zero on a handful is a panel in shape only.

**Next**: [[[ML4T_A3_0001]]](13_polymarket_prediction_markets.ipynb) reads the
unregulated venue, where the volume is orders of magnitude larger and the trade-offs are
different.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>
