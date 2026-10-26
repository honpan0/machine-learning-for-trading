# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/07_gbm.ipynb；A3 Pack 004；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Feature → 特徵
- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0033-p000

~~~~~~markdown
## 5. What to notice

**Almost every configuration ranks the cross-section the right way, and the loss function
orders the families.** [[ML4T_A3_0001]] in the [[ML4T_A3_0002]] frame is 14 of 15 on both labels, so one
configuration on each ends training pointing the wrong way, by a margin ([[ML4T_A3_0003]]) small
enough to be indistinguishable from zero. Read [[ML4T_A3_0004]] for the ordering: on both
labels Huber has the highest [[ML4T_A3_0005]], absolute error is next and squared error is last, and
squared error is also the only objective whose [[ML4T_A3_0006]] is not 5 of 5. The families order
on their averages but they overlap on individual configurations, so this is a statement about
objectives and not a ranking of the fifteen. Squared error weights an observation by the square
of its error, so the largest moves dominate what each successive tree is fitted to, while the
information coefficient is a rank correlation that cares about order rather than magnitude:
effort spent getting the extremes right buys nothing on this metric. **An objective is a claim
about which errors matter, and it is worth choosing to match the metric the result will be
judged on.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0033-p001

~~~~~~markdown

**The ordering is what the tails predict; the size of the gap is not.** The prediction in
section 4 was that the heavier-tailed label should separate the objectives further. [[ML4T_A3_0001]]
puts [[ML4T_A3_0002]] at excess kurtosis 10.26 against [[ML4T_A3_0003]]'s 7.00, so five-day is the
heavier-tailed label. But the Huber-minus-squared-error gap in [[ML4T_A3_0004]] is 0.0143
on [[ML4T_A3_0005]] and 0.0075 on [[ML4T_A3_0006]] - the heavier-tailed label separates them by
about half as much. The direction survives on both labels and the magnitude runs the other
way, so tail heaviness is not what sets how far apart the objectives land. Whatever does is
not measured here: the two labels differ in horizon, in autocorrelation and in how much of
each one a fold contains, and this notebook holds none of those fixed.

**The boosted population does not beat the linear one.** The strongest full-coverage
configuration here ranks below the strongest full-coverage configuration in
[[[ML4T_A3_0007]]](06_linear.ipynb), on the same label, the same features and the same folds. This is
the outcome the collinearity argument at the top of this notebook implies, and it is worth
taking seriously rather than treating as a tuning failure. Ridge earned its result by refusing
to choose among near-duplicate columns - spreading weight across a correlated group averages
their noise down. A tree chooses one column at every split, and remakes that choice
independently on every fold, which is the opposite operation on the same feature set. The
interactions the trees can represent and a linear model cannot are real, but on this data they
do not pay for what greedy splitting gives up.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p001>>>
<<<ML4T-ZH-END:c0033-p001>>>

### c0033-p002

~~~~~~markdown

**Almost every configuration is past its peak by the time it is reported.** [[ML4T_A3_0001]] in
the [[ML4T_A3_0002]] frame is 14 of 15 on both labels, and [[ML4T_A3_0003]] is negative on both,
so the typical configuration is worse at the declared training length than it was early on.
[[ML4T_A3_0004]] says the descent is not uniform: 3 configurations on fwd_ret_21d and 5 on
fwd_ret_5d reach their best IC somewhere in the middle of the run rather than at the first
checkpoint. So the declared training length is longer than this data supports, and the
fixed-iteration comparison above is a comparison of fifteen models mostly in their overfitted
regime.
That comparison is still the honest one, because each configuration is measured at the same
amount of training and nothing is chosen after the fact - but the ranking it produces is not the
ranking their best states would produce, and neither is a result until something selects on a
criterion that was fixed in advance.

**The checkpoint moves the IC nearly as far as the model does.** [[ML4T_A3_0005]]
compares the two: [[ML4T_A3_0006]] is the IC range over the fifteen configurations at the
declared training length, [[ML4T_A3_0007]] is the median range a single configuration
covers over its own ten checkpoints. The second is about five eighths of the first on both
labels, which is why [[ML4T_A3_0008]] is false and also why it is not reassuring. A
stopping point chosen after seeing the curves would be doing a comparable amount of work to the
choice of model, which is why reporting the leading row of the results table would be reporting
the maximum of 150 numbers as though it were one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p002>>>
<<<ML4T-ZH-END:c0033-p002>>>

### c0033-p003

~~~~~~markdown

**None of this selects anything.** IC measures whether predictions rank funds correctly, not
whether a strategy trading them makes money after costs and turnover. A monthly-horizon signal
that reorders the portfolio at every rebalance is exactly where a small ranking advantage is
lost. Selection is on validation backtest Sharpe over the population just published, and it
happens in [[[ML4T_A3_0001]]](14_backtest.ipynb), where the checkpoint is part of what is selected.

**Known limitations.** The IC is an average of daily rank correlations with no adjustment for
the serial dependence overlapping 21-day returns create, so it is a diagnostic rather than a
test, and it carries no interval that would say whether these configurations differ from each
other or from the linear ones. The grid varies capacity and loss at a fixed learning rate and a
fixed training length, so it says nothing about trading one against another - and the previous
point is the reason that matters here. And every number is measured on validation folds that
have been read many times over by the time a case study reaches this notebook.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p003>>>
<<<ML4T-ZH-END:c0033-p003>>>

### c0034-p000

~~~~~~markdown
**Next**: [[[ML4T_A3_0001]]](08_tabular_dl.ipynb) asks the same question of a neural network
built for tabular data, which represents interactions in a third way again. The useful thing to
watch there is whether it recovers whatever structure the trees found here, and whether a
collinear feature set costs it what it costs a greedy splitter.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>
