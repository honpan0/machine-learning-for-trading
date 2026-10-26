# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/01_ols_inference.ipynb；A3 Pack 004；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Training set → 訓練集
- Validation set → 驗證集
- Out-of-sample → 樣本外
- Cross-validation → 交叉驗證
- Clustering → 分群
- Cross-sectional → 橫斷面
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0049-p001

~~~~~~markdown

[[ML4T_A3_0001]]

The denominator [[ML4T_A3_0002]] measures total variance around the mean; the
numerator [[ML4T_A3_0003]] measures residual variance after the model's
predictions. When [[ML4T_A3_0004]], the model is no better than predicting [[ML4T_A3_0005]]
for every observation.

**In-sample**, OLS with an intercept guarantees [[ML4T_A3_0006]]. The intercept
ensures that the predicted mean equals the observed mean
([[ML4T_A3_0007]]), so the model can always do at least as well as
the constant-mean baseline. The fitted coefficients minimize [[ML4T_A3_0008]]
by construction.

**Out-of-sample**, both guarantees break. First, the coefficients were optimized
for the training set, not the validation set - they may amplify noise rather
than capture signal, making [[ML4T_A3_0009]] and driving
[[ML4T_A3_0010]] below zero. Second, the intercept was calibrated to the training-period
mean return. If the validation period has a different mean (as it usually does
with non-stationary financial data), predictions are systematically shifted to
the wrong level. This level error inflates [[ML4T_A3_0011]] even if the model
ranks returns correctly.

Both effects are visible in the out-of-sample [[ML4T_A3_0012]] printed above. Read it
against zero: below zero, the fitted coefficients and the training-period
intercept together predict worse than having used the validation period's own
mean return for every observation.

The IC answers a different question, and the two can disagree. IC (Spearman
rank correlation) is invariant to level shifts and scaling, so a model whose
magnitudes are badly calibrated can still rank correctly - which is why it,
not [[ML4T_A3_0013]], is the standard metric for cross-sectional return prediction in
quantitative finance. Read the IC against its HAC p-value rather than its
sign: this is one validation fold of one case study, and the naive statistic
printed beside it overstates the evidence, because it counts overlapping
windows as independent observations.

None of the diagnostic tests - Breusch-Pagan, residual autocorrelation,
Jarque-Bera, VIF - measure out-of-sample ranking accuracy. A coefficient can be
statistically significant yet contribute nothing to prediction (large sample,
tiny effect), and vice versa. The diagnostics tell us whether our *inference*
about parameter values is reliable; they say nothing about whether those
parameters produce useful *forecasts*.

This is the core insight of Section 11.1: the inferential toolkit and the
predictive toolkit answer different questions. For algorithmic trading, the
relevant question is "does this model rank future returns accurately?" - and
the relevant tool is out-of-sample evaluation, not hypothesis testing.

Section 11.2 introduces regularization - the tool that directly targets
prediction quality by trading bias for variance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p001>>>
<<<ML4T-ZH-END:c0049-p001>>>

### c0050-p000

~~~~~~markdown
## Key Takeaways

1. **Statsmodels provides the full inferential toolkit**: standard errors,
   t-statistics, p-values, F-tests, and a battery of diagnostic tests that
   scikit-learn intentionally omits.

2. **The ETF panel violates the spherical-errors assumption in both of its
   parts**: the error variance depends on the regressors (Breusch-Pagan
   rejects) and residuals are autocorrelated within each asset, largely
   because a 21-day forward label makes consecutive observations overlap.
   Features are also pervasively collinear (many with VIF > 10).

3. **A statistic computed on a panel measures what its row order says it
   measures.** Durbin-Watson on a date-ordered panel reports cross-sectional
   dependence under the name of serial correlation; the same ordering makes
   Newey-West lag across assets rather than across time. Regroup by asset, pick
   a covariance estimator that assumes independence only where the diagnostics
   did not find dependence, and say which one the number came from. Here the
   overlapping label correlates residuals across symbols *and* across nearby
   dates, which rules out clustering on either dimension and leaves
   Driscoll-Kraay.

4. **Robust standard errors repair one failure only.** They fix the variance
   estimate when errors are non-spherical. They cannot rescue a model whose
   exogeneity or functional form is wrong, where the point estimates
   themselves are not consistent - and they do not improve predictions.

5. **For prediction, we need a different approach**: regularization +
   out-of-sample evaluation. The next notebook introduces Ridge, LASSO,
   and Elastic Net.

**Next**: [[ML4T_A3_0001]] introduces the prediction-oriented framework
with regularized regression and walk-forward cross-validation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>
