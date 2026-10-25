# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/09_har_rough_volatility.ipynb；A3 Pack 003；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0024-p000

~~~~~~markdown
## Fitting it, and correcting the standard errors

The regression is ordinary least squares. Its textbook standard errors assume the
residuals are homoscedastic and serially uncorrelated, and neither assumption is safe on
a volatility series: volatility is heteroscedastic almost by definition, and a
misspecified dynamic leaves autocorrelation behind in the residuals.

Note what the overlapping regressors do and do not imply. The weekly and monthly
regressors are rolling averages, so consecutive rows share most of their inputs; that
makes the *regressors* correlated across rows, which ordinary least squares handles.
It does not by itself make the *residuals* correlated: a correctly specified model of
this shape can have independent innovations. So overlap is a reason to check rather than
a proof of a problem.

Four standard errors for the same coefficients are computed below, and the reason there
are four rather than two is that isolating one relaxation requires holding the other
estimator choices fixed. The textbook ones assume homoscedastic, serially uncorrelated
residuals. [[ML4T_A3_0001]] relaxes the first assumption with a leverage adjustment. The last two
are the same **Newey-West** estimator run twice, once with a zero-lag window and once
over a window set to the longest horizon in the model, which is where any dependence the
regressors' overlap could induce would reach. Those two differ in the lag window and in
nothing else, so their ratio is what the lagged covariance terms contribute; [[ML4T_A3_0002]]
against the textbook column is a separate reading of heteroscedasticity alone.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
Nothing about the coefficients changed. What changed is how much confidence the fit
reports in them, and the two ratio columns say where that change comes from.

The first ratio is heteroscedasticity, read on its own. The second is the lag window, read
with everything else held fixed. A second ratio near one says the lagged covariance terms
add little to the zero-lag version; it is a statement about the estimate, not about the
residuals, because what Newey-West sums over the window is the covariance of the
regressor-residual products rather than of the residuals themselves. Serially correlated
residuals whose products with these regressors happen to be close to uncorrelated would
produce the same ratio.

The coefficients themselves are the reason to fit HAR rather than GARCH. Each one is the
weight the model puts on one horizon, so their relative sizes say which horizon is
carrying the current level, and that is a statement a person can act on. GARCH answers
the same forecasting question with one decay rate and no such decomposition.

Two things to watch when reading them. They are not constrained to be positive, and a
negative coefficient on one horizon usually means it is collinear with another rather
than that volatility at that horizon predicts less volatility next session. And they sum
to close to one on a persistent series, so a rise in one is generally a fall in another;
read the three together rather than one at a time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0027-p000

~~~~~~markdown
## Against GARCH, out of sample

Both models are fitted on the same training block and asked for one-step-ahead forecasts
over the same test block. They are not forecasting exactly the same quantity, which is
the first thing the comparison has to state: HAR targets the range-based volatility it
was built from, and GARCH targets the variance of close-to-close returns. The levels
therefore differ for a reason that has nothing to do with forecast quality, and the error
measures below carry that difference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0030-p000

~~~~~~markdown
Read the mean forecast column before the error columns. The two models sit at different
levels because they are estimating different quantities, and a squared error between a
forecast and a target measured a different way charges the model for that difference as
though it were inaccuracy. The correlation column is the part of the comparison that
the level difference does not touch, because a correlation is invariant to it.

So the comparison establishes less than it looks like it does. What it does establish is
that a linear regression on three lagged averages tracks realized volatility about as
well as a fitted GARCH does, at a fraction of the machinery, which is the reason HAR is
the standard baseline in the realized-volatility literature.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0031-p000

~~~~~~markdown
## The coefficients as features

Refitting on a moving window turns the three weights into three slowly varying columns,
and their movement is a statement about which horizon is driving volatility now. The
window is long because the coefficients are estimated rather than observed, and the step
is a month because refitting daily would produce three columns whose variation is mostly
estimation noise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0034-p000

~~~~~~markdown
## The shape of the term structure

The ratio of the short horizon to the long one is a single number saying whether
volatility right now is above or below where it has been. Above one, the recent past has
been more volatile than the month; below one, less. It is bounded in practice, means the
same thing in every year, and is the form a conditioning feature usually wants for the
reason [[ML4T_A3_0001]] gave about ranks. The figure draws it smoothed over a
month, because the unsmoothed daily ratio is dominated by whichever single session
sits in its numerator and reaches several times the average.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
# Part 3: how jagged is the path

The **Hurst exponent** [[ML4T_A3_0001]] describes how the size of a series' movement scales with the
length of the interval measured. For a random walk the distance covered grows with the
square root of the interval, which is [[ML4T_A3_0002]]. Above a half the series is persistent:
a move is more likely to be followed by another in the same direction, so the path
wanders further than a random walk would. Below a half it is anti-persistent, or
**rough**: moves tend to be reversed, so the path is jagged and covers less ground.

Two things are worth separating before estimating it. Applied to **returns**, [[ML4T_A3_0003]] says
whether a price is trending or reverting, and for a liquid market it comes out near a
half because anything else would be a tradable pattern. Applied to **log-volatility**,
it says how jagged the volatility path is, and Gatheral, Jaisson and Rosenbaum (2018)
found it comes out near a tenth across every asset they measured, far below the half
that the standard volatility models had assumed for decades.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>
