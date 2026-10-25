# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/02_structural_breaks.ipynb；A3 Pack 004；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Training set → 訓練集
- Cross-validation → 交叉驗證
- Standard deviation → 標準差

## 待翻譯英文單元

### c0037-p000

~~~~~~markdown
## The feature matrix

Each family is a function of the series and the boundary, so the matrix is the five of
them applied to every example. The map from column to family is built from the same
functions rather than typed out, which is what keeps the contribution chart below
honest when a family gains or loses a column.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000

~~~~~~markdown
## Classification

A gradient-boosted tree ensemble combines the columns. It is the right shape of model
for this: the families disagree with each other in ways that depend on the kind of
break, which is an interaction, and trees represent interactions without being told
where to look. Five-fold cross-validation gives the score, and the same folds supply
out-of-fold probabilities for the ROC curve, so no example is scored by a model that
saw it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0042-p000

~~~~~~markdown
The score describes the examples it was measured on, and those were built to carry
the changes the features were built to see. It says the wiring works. It says nothing
about how the same detector behaves on a market series, which the last section tests.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
## Which family carries the signal

Summing the split counts within each family says where the trees found their splits.
Read it as a statement about these examples: the generator produces four kinds of break
in equal proportion, so a family that sees only one of them can carry at most a quarter
of the work however good it is at that quarter.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
## The same detector on market data

The test that matters is whether a detector trained on constructed breaks transfers.
Each period below takes an equal number of sessions either side of a named date and
scores that date as the candidate boundary. Three of the dates are episodes nobody
disputes; three are quiet mid-year dates chosen for having no such episode near them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0049-p000

~~~~~~markdown
The detector is not miscoded, and the features are not useless: the distributional
statistics in the table rank the periods sensibly, with the crisis windows separating
further than the quiet ones on the same measures. What has failed is calibration, and
the reason is in the training set. The examples were 500 constant-variance steps with a
single change of a stated size at the midpoint. A 500-session window of a real index
contains a dozen changes of comparable size before anything a person would call a
crisis, so almost every real window looks, to this detector, like the positive class.

The lesson generalises past this example. A supervised detector inherits the definition
of its positive class from its labels, and synthetic labels define the class by
construction rather than by consequence. Two ways out: label real history against dated
events, which buys a definition someone can argue with, or drop the probability and feed
the feature columns to the downstream model directly, which is what the rest of this
chapter does with model-based features generally.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0050-p000

~~~~~~markdown
## The same statistics as Polars expressions

The functions above take NumPy arrays and one boundary, which is the right shape for
scoring a candidate date. A production feature has the opposite shape: one long frame,
one column per statistic, recomputed on a rolling window. [[ML4T_A3_0001]] supplies these
as Polars expressions over the same frame the rest of the chapter uses.

[[ML4T_A3_0002]] is the standard deviation over the absolute mean, so it is
only meaningful on a series whose mean stays away from zero. Daily returns average
almost exactly zero, which makes the ratio explode; it is applied here to the absolute
return, whose mean is safely positive, and then reads as the relative variability of
move size.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0052-p000

~~~~~~markdown
Each column compares a recent window against the one before it, so together they are a
rolling version of the distribution family above and can be read on any session without
refitting anything. That makes them usable next to the monitoring statistics as
continuous inputs, which is the form the caveat two sections up recommends.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0053-p000

~~~~~~markdown
## Key takeaways

1. **A single-break test and a segmentation answer different questions.**
   Zivot-Andrews tests a hypothesis and estimates one date; a segmentation minimises a
   cost and returns as many dates as the penalty or the requested count allows. Neither
   reports the true number of breaks, because neither has a notion of one.
2. **A break detected on the full sample is not a feature.** Refit the detector forward
   through the sample so that every value is computable from what preceded it, and
   expect the causal column to be coarser and to revise itself as history accumulates.
3. **CUSUM and MOSUM trade memory against readability.** The cumulative statistic keeps
   every deviation and therefore never resets; the moving one forgets outside its window
   and stays readable for the next break. Both need a reference period that is fixed
   rather than re-estimated, or they are not causal.
4. **Five families cover the ways two windows can differ**: where they sit, how spread
   out they are, what shape they have, how each value depends on the last, and whether a
   free detector agrees the boundary is where the change is. A detector that reads only
   one family can only see the breaks that family is sensitive to.
5. **A learned detector inherits its definition of a break from its labels.** Trained on
   constructed examples it separates constructed examples; on market windows the same
   model returns a probability whose threshold means nothing, while the underlying
   statistics still rank the windows sensibly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0053-p001

~~~~~~markdown

**Known limitations.** The classification section trains and evaluates on the same
constructed distribution, so its cross-validated score bounds nothing about market data.
The causal feature refits quarterly, which is a cost decision rather than a statistical
one, and a break occurring just after a refit is invisible for up to a quarter. And the
monitoring statistics are drawn without decision thresholds: the level at which a
crossing should trigger action depends on how much a false alarm costs, which is a
question this notebook does not have the information to answer.

**Previous**: [[ML4T_A3_0001]] for stationarity testing.
**Next**: [[ML4T_A3_0002]] for reaching stationarity without discarding the
level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p001>>>
<<<ML4T-ZH-END:c0053-p001>>>
