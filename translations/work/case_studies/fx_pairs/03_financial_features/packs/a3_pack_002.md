# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/03_financial_features.ipynb；A3 Pack 002；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Drawdown → 回撤
- Sharpe ratio → 夏普比率
- Feature → 特徵
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0010-p000

~~~~~~markdown
The twenty pairs are not twenty independent markets, and the way the market groups them is the
way the features below will behave. Seven have the dollar on one of their two legs and share
whatever the dollar does, which is the common component Section C.5 measures. Which leg it is
matters and is not the same across the seven: the dollar is the second currency in [[ML4T_A3_0001]] and
the first in [[ML4T_A3_0002]], so the same dollar move pushes those two quotes in opposite directions,
and C.5 has to sign each of them before it can average them. Six of the remaining pairs are yen
crosses, which the domestic rate cycle moves together and which travel the widest daily range of
the three groups; the last seven are crosses among the European and Antipodean currencies. Every
pair has the same number of sessions, so the panel is balanced and no feature below has to reason
about a pair joining or leaving part-way through.

The range column is in basis points, hundredths of a percent, which is already a division by the
price level - and that division is why every feature below is a return or a ratio rather than a
price. The pairs are quoted on scales orders of magnitude apart, so a move of one unit means
something different in each of them, and the table shows that even after scaling they do not
travel the same distance in a session.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## C. Feature construction, one subsection per family

### C.1 Momentum, volatility and their differences

Three quantities come out of the same trailing window and a shared helper computes them
together: the return over the window, the annualized standard deviation of the daily log returns
inside it, and the ratio of the two, which is a trailing Sharpe ratio. Reading the same window
three ways separates a move that was steady from one that was a single jump.

What stays local is specific to this universe. [[ML4T_A3_0001]] is the return over a year that
stops a month short of the decision, because the most recent month of an FX move is the part
most likely to reverse, and leaving it out asks whether the slower trend is still there.
[[ML4T_A3_0002]] and [[ML4T_A3_0003]] are differences between horizons, and say whether a trend is
speeding up or bleeding away.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### C.2 Garman-Klass volatility

A close-to-close deviation sees two prices a session apart and discards everything that happened
between them, so a session that travelled a long way and came back reads as quiet. The
Garman-Klass estimator uses all four prices in the bar, combining the high-to-low range with the
open-to-close move:

[[ML4T_A3_0001]]

For a session of the same true volatility that is several times less noisy than the
close-to-close estimate, which is why Chapter 8 uses it here: the range is where most of an FX
session's information about dispersion sits. The columns carry the square root of the window
mean of that variance, annualized, so they are on the same scale as the close-to-close deviation
beside them. The two ratios read the regime rather than the level - a short window against a
longer one says whether dispersion is rising or falling, which no single window can.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### C.3 Mean reversion: z-scores, channel position and Bollinger %B

These are the columns the ranking is formed on. Each multi-horizon return is standardized
against its own trailing year, so the z-score says how unusual the move is for that pair rather
than how large it is in price terms. The universe table above is the reason that matters: the
same move is unremarkable in a pair that travels the widest daily range here and a large one in
the pair that travels the narrowest, and standardizing each pair against its own history is what
makes the two comparable on the day the ranking is formed.

Channel position and Bollinger %B ask the same question of the level instead of the change:
where does price sit in the range it has recently traded through? Channel position measures that
against the highest and lowest close of the window, so it reads zero at the bottom of the range
and one at the top. Bollinger bands replace the range with a moving average of the close plus
and minus two standard deviations of it, so the band widens when the pair is volatile instead of
staying pinned by one old extreme for the length of the window. %B is where the close sits
between the two bands, on the same zero-to-one reading:

[[ML4T_A3_0001]]

It leaves that interval whenever price is more than two deviations away from the average, which
is why the column runs a little below zero and a little above one rather than stopping at the
ends. All three are trailing statistics within one pair, so nothing here is estimated across
pairs or across the sample.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### C.4 Drawdown, range and oscillators

[[ML4T_A3_0001]] is the share by which price sits below its highest close of the trailing quarter,
so it is zero at a new high and negative otherwise. That is the *current* drawdown and not the
worst peak-to-trough decline anywhere inside the window: the two are different statistics, and a
pair that sold off early in the quarter and then made the whole move back scores nothing on the
current drawdown and its full decline on the worst one.

The relative strength index, RSI, compares how much price gained on the sessions that closed up
with how much it lost on the sessions that closed down over a trailing window, and maps the
comparison onto a nought-to-hundred scale where fifty is as much up move as down. The averaging
is Wilder's recursive one, which folds each new session into the running average with weight
[[ML4T_A3_0002]] rather than taking a plain mean of the last [[ML4T_A3_0003]] sessions; the two give different
numbers on the same data, and Wilder's is the convention the library implements.

The last two families are plainer. [[ML4T_A3_0004]] is the high-to-low range as a share of the
close, averaged over the window, which says how far a pair typically travels within a session.
[[ML4T_A3_0005]] is how far price sits above or below its own moving average.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>
