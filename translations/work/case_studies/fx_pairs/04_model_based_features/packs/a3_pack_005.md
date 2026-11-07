# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/04_model_based_features.ipynb；A3 Pack 005；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Covariance → 共變異數

## 待翻譯英文單元

### c0053-p000

~~~~~~markdown
Two columns come out. [[ML4T_A3_0001]] is the probability the session was in
the higher-variance state, and [[ML4T_A3_0002]] is how much that probability
has moved over the last five sessions, which turns a level into a measure of a regime
changing.

Only the first is fitted. The five-session difference is arithmetic on the emitted
probability with nothing estimated in it, so it is taken once over the whole column
rather than inside the walk. It is null rather than zero where there is no session five
back to difference against: the panel already carries rows on which the difference is
genuinely zero because the probability did not move, and writing a zero would make the
two indistinguishable.

A difference that straddles a refit is a difference between two parameter vintages. That
is not a defect - it is what a reader watching this feature in production would see on
the day the model was refreshed - but it is worth naming, because it is the one place a
jump in the column can come from something other than the market.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0055-p000

~~~~~~markdown
### Why the Model Reads Percent and Not Decimals

The series handed to the model is multiplied by 100, so a dollar move of a few tenths of
a percent arrives as a number near one rather than as a number near one thousandth. The
reason has nothing to do with the market and everything to do with two constants inside
[[ML4T_A3_0001]], each of which adds a fixed amount to a state's variance and neither of
which scales with the data it is given:

- [[ML4T_A3_0002]] is added to the covariance the fit *starts* from, so it decides where the
  search begins rather than where it ends. It is not a floor on the fitted value.
- [[ML4T_A3_0003]] is added at every step of the fit, divided by how many observations the
  state currently holds. It inflates each state's variance estimate by an amount that
  shrinks as the state takes on more observations.

Both defaults are sized for data of order one. A daily FX return is three orders of
magnitude smaller than that and its variance five, which puts the variance below either
constant - so on decimal returns the fit would begin from a covariance that is
essentially the constant rather than the data, and would return variances visibly
inflated by the second. Multiplying by
100 multiplies the variance by 10,000 and puts it in the range those defaults were
chosen for.

The cell below measures both effects against the series they act on rather than
asserting them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
The walk runs over the whole series, holdout sessions included, because the holdout needs
a value on every one of them. What must not reach into the holdout is an *estimate*, and
that is [[ML4T_A3_0001]]'s job rather than a cut on the input: past the last pre-holdout
session the walk stops re-estimating and keeps applying what it last fitted.

The variance printed below is measured on the pre-holdout part alone. It is the
measurement the whole scaling argument rests on, and a constant chosen by looking at the
holdout is a parameter estimated on the holdout whatever the code around it does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0059-p000

~~~~~~markdown
Both comparisons are against the variance of the return column the model actually reads.
The second constant is divided by the number of observations a state holds, so splitting
the fitted sample evenly between the two states gives its order of magnitude without
refitting anything.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0061-p000

~~~~~~markdown
One walk over the whole series, and the loop keeps the restart count it had to discard
along with the transition matrix behind every estimate. There is one market-level series,
so this is one walk rather than one per pair.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0063-p000

~~~~~~markdown
The matrix below is the **first** estimate the walk made - the one fitted on the burn-in
alone, and therefore on the oldest window in the run. It is named rather than taken from
wherever the loop stopped, because the last estimate is the one carried across the
holdout and describes the most recent history rather than the period the text discusses.

Each row is the state the session starts in and each column the probability of the next
session's state, so the diagonal says how often a state persists. A state that persists
with probability [[ML4T_A3_0001]] lasts [[ML4T_A3_0002]] sessions on average, which is the last column and is
easier to read than the probability itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0065-p000

~~~~~~markdown
The five-session difference is taken here, over the emitted column, as the section text
said. [[ML4T_A3_0001]] leaves the first five valued sessions null because there is nothing five
back to difference against, and the burn-in prefix stays null throughout.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0067-p000

~~~~~~markdown
**The three checks, against what this section emits.** The schedule check first, then the
burn-in report, then the truncation test. The forward recursion is written out rather
than taken from a library call, so the truncation test is the only thing standing between
it and the probability given the whole series - which would carry every later session
into each earlier value.
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p000>>>
<<<ML4T-ZH-END:c0067-p000>>>

### c0070-p000

~~~~~~markdown
## 6. What the Return Model Did Not See Coming

The third model is the smallest of the three and its output is the most direct. An
ARIMA(1,0,1) fitted to a pair's daily returns says that today's return is partly
predictable from yesterday's return and partly from yesterday's forecast error - one
autoregressive term and one moving-average term, which is the shortest memory the model
family offers. Daily currency returns are close to unpredictable, so a fit like this
explains very little, and that is the point: the feature kept is not the forecast but
**what the forecast missed**. A large error is a session that moved unlike the recent
past, which is a different quantity from a large return.

Three columns come out: the forecast itself, the error, and that error divided by the
spread of the errors the *estimation window* showed, so a quiet pair and a volatile one
are comparable. That spread moves with the coefficients and is carried alongside them,
so it ends where they do.

The fitted coefficients must not move when the recursion is extended past the window they
were estimated on. [[ML4T_A3_0001]] is the call that guarantees it: the state
recursion advances with each new observation while the coefficients stay where the fit left
them. It is shared with cme_futures rather than written here, because the same guarantee is
wanted in both and a copy of a guarantee agrees with the original only by luck.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>
