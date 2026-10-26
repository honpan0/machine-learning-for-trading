# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/01_ols_inference.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Clustering → 分群
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0023-p000

~~~~~~markdown
### Correlated Errors: Residual Autocorrelation Within Each Asset

This is a panel: many symbols observed on the same dates. The residual vector
is stored in date order, so its neighbouring entries are *different assets on
the same day*, not consecutive observations of one asset. A Durbin-Watson or
Breusch-Godfrey statistic computed on that vector measures cross-sectional
dependence and reports it under the name of serial correlation.

To test serial correlation we regroup the residuals into one time-ordered
series per symbol and measure autocorrelation within each. Three lags are
informative here. Lag 1 asks whether yesterday's error predicts today's. Lag 5
is one trading week. Lag 21 sits at the label horizon: [[ML4T_A3_0001]] is a
21-day forward return, so consecutive daily observations of one asset share 20
of 21 days of outcome window. That overlap induces autocorrelation by
construction out to lag 20 and is the dominant source of the correlation we
find. At lag 21 the outcome windows no longer overlap, so what is left is
whatever serial correlation the data has of its own.

The lag has to be counted on the session grid the panel is dated on, not on
row position. As the unbalanced histories above showed, a symbol's rows skip
sessions wherever a feature could not be computed or the ETF was not trading,
and three symbols in this training window resume after a break of a year or
more. Pairing rows by position would file those gap-crossing pairs under "lag
1". So each residual is placed at the number of the session it belongs to, and
a pair counts towards a lag only when its two sessions are exactly that far
apart. Durbin-Watson is computed the same way, over consecutive-session pairs
only.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0028-p000

~~~~~~markdown
### Normality: Jarque-Bera Test

Normality of the errors is not one of the four Gauss-Markov assumptions, and
OLS remains BLUE without it. It is what makes the t and F statistics follow
exactly those distributions in a finite sample. At this sample size the
central limit theorem delivers approximate normality of the coefficient
estimates regardless, so a rejection here is the least consequential of the
diagnostics in this section.

Financial returns have fat tails and excess kurtosis, so this will almost
certainly reject.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
### Multicollinearity: Variance Inflation Factors

VIF measures how much each coefficient's variance is inflated by correlation
with other features. VIF > 5 is a common concern threshold; VIF > 10 indicates
severe multicollinearity. Financial features (momentum at different horizons,
volatility measures) are pervasively correlated.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
High VIF confirms what Section 11.1 discusses: financial features are pervasively
correlated. Momentum at 5-day and 21-day horizons, different volatility measures,
and volume-price indicators share overlapping information. OLS distributes weight
arbitrarily among correlated features, producing unstable coefficient estimates
that flip sign across samples.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
## Section 3: When Standard Errors Fail - Robust Alternatives

Robust standard errors address exactly one failure: non-spherical errors. The
point estimates are unchanged and, if linearity and exogeneity hold, they stay
consistent; only the variance estimate around them is repaired.

They do nothing for the other two assumptions. If the model omits a relevant
variable or gets the functional form wrong, exogeneity fails, the coefficients
themselves are not consistent, and a robust standard error is a more careful
statement about the wrong quantity. Section 11.1 makes this point directly:
when the model is misspecified, the unbiasedness guarantee fails and the
coefficients stop being interpretable as structural parameters. No covariance
estimator recovers it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
### Comparing Standard Error Estimates

Each estimator below assumes some pairs of residuals are uncorrelated, and the
question is whether the diagnostics above have already shown that assumption to
be false.

- **OLS** (default): every pair uncorrelated, and equal variance throughout
- **HC3**: still every pair uncorrelated, but variance may vary with the regressors
- **Clustered by date**: any two observations sharing a date may correlate;
  different dates may not
- **Clustered by date and symbol**: adds any two observations of one symbol;
  still assumes independence when the symbol *and* the date both differ
- **Driscoll-Kraay**: no independence assumption within a window of nearby
  dates, across the whole cross-section

That last assumption is the one this panel breaks in a way the others do not.
[[ML4T_A3_0001]] is a 21-day forward return, so one symbol on date *t* and a
*different* symbol on date *t+5* share sixteen days of outcome window, and
whatever moved the market in those sixteen days is in both residuals. Two-way
clustering treats that pair as independent. Driscoll-Kraay does not: it sums
the moment conditions across the cross-section within each date and then applies
a Newey-West correction over dates, so arbitrary cross-sectional correlation and
serial correlation out to the lag length are both admitted. We set that lag to
the label horizon, which is where the mechanical overlap ends.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0034-p001

~~~~~~markdown

Plain HAC (Newey-West) is the usual answer to autocorrelation, but it reads its
lags off the row order of a single time series. On a pooled panel stored in date
order those lags run across the cross-section, so it does not estimate what its
name promises here. It becomes the right tool once the panel is collapsed to
one observation per date, which is what the IC calculation below does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p001>>>
<<<ML4T-ZH-END:c0034-p001>>>

### c0036-p000

~~~~~~markdown
Each estimator admits a different set of correlated pairs, and admitting a pair
costs precision: the standard error grows. The chart shows, for each estimator,
how much larger its standard error is than the OLS one, over all
features. A value of 1 means the estimator finds no dependence to correct for;
a value of 3 means OLS was overstating that coefficient's precision threefold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
Every estimator that admits more dependence produces wider standard errors, and the order
is the order of what each one allows for. HC3 admits only that the variance differs across
observations. Clustering by date admits that observations sharing a date move together,
which on a panel of this shape is most of the dependence there is. Clustering on both
dimensions and then Driscoll-Kraay add correlation within a symbol over time.

None of this changes a coefficient. What changes is how much of it you are entitled to
believe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>
