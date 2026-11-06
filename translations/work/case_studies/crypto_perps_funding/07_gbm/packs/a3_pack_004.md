# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/07_gbm.ipynb；A3 Pack 004；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0031-p000

~~~~~~markdown
## 5. What to notice

**The size-against-direction gap the linear notebook found is a property of that family, not of
these labels.** [[ML4T_A3_0001]] reached an order of magnitude more on the direction cut of
[[ML4T_A3_0002]] than on the return itself, and concluded that the sign was the far more rankable
target. Read [[ML4T_A3_0003]] down the [[ML4T_A3_0004]] frame here: the return labels and the direction
labels land in the same range, with every configuration of every label above zero. The two
formulations end up in the same place once the model can
condition one feature on another. What the linear grid measured was its own inability to rank
magnitudes on this feature set, not a fact about what is predictable at this horizon. That
correction is available only because both notebooks now fit all four labels; with one label per
run the two halves of it would have sat in different runs and never met.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0031-p001

~~~~~~markdown

**The loss function is the axis that matters on the return labels, and it separates almost
cleanly.** [[ML4T_A3_0001]] puts Huber first, absolute error second and squared error last on
both return labels, and the curves show the groups stacked rather than interleaved. The tails
frame supports the usual mechanism here, unlike in some other case studies: [[ML4T_A3_0002]] carries
excess kurtosis around 25 and [[ML4T_A3_0003]] far more than that, so squared error - which weights
an observation by the square of its error - is fitted mostly to the largest moves. The
information coefficient is a rank correlation and cares about order rather than magnitude, so
accuracy on the extremes buys nothing it measures. **An objective is a claim about which errors
matter, and squared error makes a claim this metric does not reward.** The direction menus
declare one objective each and vary only capacity, so their panels isolate leaf count and say
nothing about the loss.

**Most configurations peak early and then drift down.** [[ML4T_A3_0004]] gives the median peak
checkpoint as 100 or 150 of the 500 iterations the grid runs, and the median configuration ends
below where it started on every label. On a feature set that is one quantity measured many ways
that is what one would expect: there is not much independent structure to find, and the trees
that follow are splitting on near-copies of columns already used. The practical reading is that
the iteration count in these presets is generous for this data and a shorter schedule would lose
little. The interior-peak count is in the frame but not read as evidence - the ten checkpoints of
one configuration are the same model with more trees, so where the maximum of that path falls
tells you little without a baseline this notebook does not compute.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p001>>>
<<<ML4T-ZH-END:c0031-p001>>>

### c0031-p002

~~~~~~markdown

**The checkpoint still moves the answer, by between a third and two thirds of what the model
choice does.** The comparison frame puts the spread across configurations at fixed training
length against the median configuration's own range across its ten checkpoints, and the ratio
is a small single-digit multiple at every label. So the stopping point is a smaller dial than
the model - but not a negligible one, and the leading row of the table is still the maximum of
a configuration count times ten. The fixed-iteration chart is the comparison that does not
require choosing anything after the fact.

**Two folds is the number to hold on to.** Every statement above rests on two validation years of
a market that changed structurally over them, and the search that produced it had 400 members.
That combination - many candidates, little data - is the one where a best member looks convincing
for reasons unrelated to the data. Nothing here is a small effect measured precisely; it is a
moderate effect measured on a short sample, and the honest summary is the direction rather than
the magnitude. [[[ML4T_A3_0001]]](12_model_analysis.ipynb) is where the search is accounted
for across families.

**Gradient boosting finds more than the penalty grid did, on every label.** The linear
notebook's return grid sat close to zero and its L1 path reduced to a single volatility column.
Every configuration here is positive at the end of training, and on the return labels the
weakest of them is above anything the linear family reached. A tree can condition one feature on
another, and on this feature set that appears to be worth something a weighted sum of the same
columns is not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p002>>>
<<<ML4T-ZH-END:c0031-p002>>>

### c0031-p003

~~~~~~markdown

**None of this selects anything.** IC measures whether predictions rank contracts correctly, not
whether a strategy trading them makes money after costs and funding - and those are unusually far
apart here, because funding is a cash flow the holder receives or pays regardless of what the
price does, so a position can pay while its price prediction is wrong. Selection is on validation
backtest Sharpe over the population just published, in [[[ML4T_A3_0001]]](13_backtest.ipynb), where
the checkpoint is part of what is selected.

**Known limitations.** Two folds, and a short one at that. The IC is an average of per-timestamp
rank correlations with no adjustment for the serial dependence overlapping eight-hour returns
create, so it is a diagnostic rather than a test, and it carries no interval that would say
whether these configurations differ from one another. The grid varies capacity and loss at a
fixed learning rate. And every number is measured on validation folds already read many times by
the time a case study reaches this notebook.

**Next**: [[[ML4T_A3_0002]]](08_tabular_dl.ipynb) asks the same question of a neural network built
for tabular data. The thing to watch is whether it prefers the same loss functions - if the tails
are what separates the objectives here, a different model class fitted with the same objectives
should separate the same way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p003>>>
<<<ML4T-ZH-END:c0031-p003>>>
