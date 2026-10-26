# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/01_ols_inference.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Validation set → 驗證集
- Clustering → 分群
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# OLS and the Inferential Toolkit

**Chapter 11 | Section 11.1**

**Docker image**: [[ML4T_A3_0001]]

This notebook shows what classical inference looks like before we leave it behind.
Using the same ETF features and labels as the rest of Chapter 11, we fit a
statsmodels OLS model and walk through the full inferential toolkit: coefficient
significance, Gauss-Markov diagnostics, and robust standard errors.

**Learning objectives**

- Interpret a statsmodels OLS summary: coefficients, standard errors, t-statistics, p-values
- Test the spherical-errors condition on a panel: heteroscedasticity and residual autocorrelation
- Identify multicollinearity via Variance Inflation Factors (VIF)
- Separate what robust standard errors repair from what they cannot
- Understand why inference diagnostics do not answer the prediction question

**Book reference**

Section 11.1 ("From Inference to Prediction"). The next notebook,
[[ML4T_A3_0002]], transitions to the prediction-oriented framework.

**Prerequisites**

- Familiarity with linear regression and the Gauss-Markov assumptions.
- Conceptual exposure to heteroscedasticity, autocorrelation, and VIF.
- ETF case-study features at [[ML4T_A3_0003]]
  (Ch8 output) and labels at [[ML4T_A3_0004]]
  (Ch7 output).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## Load Features and Labels

We use the same ETF case study data as the rest of Chapter 11: financial
features from Ch8 and 21-day forward return labels from Ch7.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0008-p000

~~~~~~markdown
Ch8 builds the [[ML4T_A3_0001]] and [[ML4T_A3_0002]] features as differences of return
horizons, so [[ML4T_A3_0003]] is [[ML4T_A3_0004]]. Keeping both the raw
returns and the derived differences makes the design matrix singular, which is
a violation of the no-perfect-multicollinearity assumption severe enough that
the robust covariance estimators below cannot be computed at all. We drop the
five composites.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### What is in the panel

Two properties of this dataset decide how the diagnostics below have to be
computed, so we look at them before computing anything.

The first is what the features are. They are not unrelated measurements:
they come in families that describe the same price history over different
windows - returns over several horizons, volatility over several windows,
moving-average ratios, oscillators. Members of a family move together, which
is what the collinearity diagnostic will find.

The second is how much history each ETF has. The panel is unbalanced. An ETF
that listed in 2015 has no rows before it, and a row is dropped wherever a
feature could not be computed, so a symbol's rows can skip trading sessions
that other symbols have. Any statistic that reads "the previous observation"
off row order will silently cross those gaps.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The history each symbol brings. One row per ETF, drawn only over the sessions
it actually appears on, so a break in a row is a stretch of sessions the panel
has for other symbols and not for this one.

**What to read off it.** The rows form a staircase: symbols enter the panel over
the whole sample rather than all at the start, and a few rows break mid-series.
The panel is therefore unbalanced, and two things follow for what comes next. A
pooled fit weights the later years more heavily, because that is where most of
the rows are. And the cross-section a date-clustered standard error averages over
is much narrower early in the sample than late, so an estimator that assumes a
fixed panel width is assuming something this picture rules out.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Select a Single Training Fold

Inference is an in-sample exercise - we fit one model on one training window
and examine its properties. We use the first walk-forward fold and hold back
the validation set for a prediction comparison at the end.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Section 1: Statsmodels OLS Summary

Statsmodels provides the full inferential output that scikit-learn omits:
coefficient standard errors, t-statistics, p-values, and model-level diagnostics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
**Reading the summary**: The coefficients table shows many features with small
p-values in the [[ML4T_A3_0001]] column, which might seem to indicate "significant" predictors.
But the overall [[ML4T_A3_0002]] is very low - typical for cross-sectional return prediction.
A large sample (hundreds of thousands of observations) makes even tiny effects
"significant" in the statistical sense, while the economic magnitude may be
negligible. Note that even after removing the five exact linear combinations,
the remaining features are still pervasively correlated (as VIF will confirm),
so coefficient estimates are unstable across samples.

Crucially, these standard errors assume **spherical errors**: constant variance,
uncorrelated across observations. We now test that condition, and the
no-perfect-multicollinearity condition alongside it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
## Section 2: Gauss-Markov Diagnostic Battery

Section 11.1 states the four Gauss-Markov assumptions: linearity in the
parameters, strict exogeneity, no perfect multicollinearity, and spherical
errors. When all four hold, OLS is the Best Linear Unbiased Estimator (BLUE).

Only two of the four are testable from residuals. Spherical errors decompose
into constant variance (Breusch-Pagan, below) and no correlation across
observations (residual autocorrelation, below); multicollinearity is read off
the design matrix via VIF. Linearity and exogeneity are assumptions about the
data-generating process that residuals cannot confirm - a misspecified model
can produce well-behaved residuals.

We also test normality, which is **not** a Gauss-Markov assumption. It is
required for exact finite-sample t and F distributions, not for BLUE.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
### Heteroscedasticity: Breusch-Pagan Test

Tests whether the error variance depends on the regressors. Financial returns
exhibit time-varying volatility (volatility clustering), so we expect rejection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>
