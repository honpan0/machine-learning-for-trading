# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/08_tabular_dl.ipynb；A3 Pack 004；單元 3 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0025-p000

~~~~~~markdown
## 5. What to notice

**An epoch checkpoint is part of the configuration, not a detail of how it was fitted.** Three
declared configurations at eight checkpoints each are 24 candidate models per label, and the
[[ML4T_A3_0001]] frame is how you tell whether that distinction is doing work: compare
the spread a single configuration covers over its own training run against the spread across the
configurations at a fixed training length. Where the first is comparable to the second, a
stopping point chosen after seeing the curves would be doing about as much of the ranking as the
choice of architecture. That is why every checkpoint is registered as its own prediction set
rather than each configuration reporting its own best one.

**Read the ranking with the coverage column or it will mislead you.** A network that has settled
into predicting nearly the same value for every fund contributes no rank correlation on those
dates, and its IC is then an average over the dates where it stayed non-degenerate. [[ML4T_A3_0002]]
is what makes that visible, and it is the same failure mode the most aggressive L1 settings
produced in [[[ML4T_A3_0003]]](06_linear.ipynb) by a different mechanism. A metric averaged over a set
the model itself selected is not a metric.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0025-p001

~~~~~~markdown

**Capacity is not a dial you turn up.** The grid steps width and ensemble size together across a
factor of four, on a cross-section of fewer than a hundred funds and a few hundred features. A
larger network has more ways to describe the training window exactly, and on a panel this small
there is not much more structure for it to find, so the useful thing to read from the capacity
chart is whether the ranking measure moves at all rather than which end wins. On a wider panel -
thousands of names rather than dozens - the same grid usually behaves differently, and that is
the comparison to make on your own data before spending a sweep on the largest configuration.

**The ensemble is what makes this cheap enough to sweep.** Averaging *k* independently trained
networks costs *k* training runs. Sharing the backbone and giving each member only its own
scaling vector and output layer costs close to one, and the parameter count grows with
[[ML4T_A3_0001]] far more slowly than a separate network per member would. That is a design choice
worth recognising in other architectures: where an ensemble helps because it averages away
initialization noise rather than because its members are genuinely different models, most of the
benefit is still there once the bulk of the parameters are shared.

**None of this selects anything.** IC measures whether predictions order the cross-section
correctly, not whether a strategy trading them makes money after costs and turnover. Those are
different questions and a configuration can win the first while losing the second. Selection is
on validation backtest Sharpe over the population this notebook just published, and it happens in
[[[ML4T_A3_0002]]](14_backtest.ipynb), where the checkpoint is part of what is selected.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p001>>>
<<<ML4T-ZH-END:c0025-p001>>>

### c0025-p002

~~~~~~markdown

**Known limitations.** The IC is an average of daily rank correlations with no adjustment for the
serial dependence that overlapping 21-day returns create, so it is a ranking diagnostic rather
than a test, and it carries no interval that would say whether these configurations differ from
each other or from the linear and boosted ones. The grid moves width and ensemble size together
at a fixed dropout, learning rate and batch size, so it cannot attribute a difference to either
dial alone. The checkpoint schedule searches training lengths in steps of 25 epochs up to 200,
and says nothing about what happens outside that range. And every number here is measured on the
validation folds, which have been read many times over by the time a case study reaches this
notebook.

**Next**: [[[ML4T_A3_0001]]](09_dl_lstm.ipynb) stops treating each decision date as an independent
row and feeds the network the recent history of each fund as a sequence, which is the one thing
none of the three families so far can see.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p002>>>
<<<ML4T-ZH-END:c0025-p002>>>
