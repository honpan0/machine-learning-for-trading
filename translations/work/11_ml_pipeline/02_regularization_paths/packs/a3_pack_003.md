# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/02_regularization_paths.ipynb；A3 Pack 003；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Feature → 特徵
- Label → 標籤
- Test set → 測試集
- Hyperparameter → 超參數
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0052-p000

~~~~~~markdown
### Prediction Rank Stability

How much do the model's cross-sectional rankings change between consecutive
folds? We apply both models (fold [[ML4T_A3_0001]] and fold [[ML4T_A3_0002]]) to the same test set
and compute their Spearman rank correlation. High correlation means stable
rankings; low means the model learned fold-specific patterns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
High rank correlation confirms that Ridge produces stable cross-sectional
rankings across folds - the same features rank near the top across folds
regardless of the training window. Lower values would indicate instability
and high implied turnover.

> **Turnover**: Rank stability is a proxy for signal turnover - the fraction
> of the portfolio that changes between rebalancing dates. The per-case-study
> runner notebooks ([[ML4T_A3_0001]]) compute explicit turnover alongside IC;
> Chapter 17 develops the full turnover-adjusted evaluation framework.
> [[ML4T_A3_0002]] provides the production implementation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
## Regularization Paths

### What LASSO gives up as the penalty rises

Two things move together as [[ML4T_A3_0001]] increases: the model keeps fewer
features, and its ranking accuracy changes. Plotting them on one axis shows
where dropping features stops being free. The two vertical scales are
different quantities, so each is labelled in the colour of its own series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
The two series come apart, and where they do is the point. The feature count falls away
over a range where mean validation IC does not, so across that range LASSO produces a
sparser model at no observed cost in ranking accuracy.

That is not the same as saying the dropped features carried nothing. Their coefficients
were non-zero and did contribute; what happens on refitting is that correlated features
take up the contribution. The chart shows the trade is available, not that it is free.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0058-p000

~~~~~~markdown
### LASSO Coefficient Path (Top 10 Features)

The coefficient path from [[ML4T_A3_0001]] shows how features enter the model
as [[ML4T_A3_0002]] decreases. We highlight only the 10 features with largest
peak magnitude to keep the plot readable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0060-p000

~~~~~~markdown
### Ridge IC and ICIR vs Alpha

The extended alpha grid reveals the full regularization landscape: a flat zone
where Ridge matches OLS, an improving zone where shrinkage helps, and an
over-regularized zone where coefficients are crushed too aggressively.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0063-p000

~~~~~~markdown
### Ridge IC/ICIR Statistics

Key statistics from the regularization sweep.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0065-p000

~~~~~~markdown
### Ridge Coefficient Path

The same sweep read through the coefficients rather than the score. Every
feature keeps a non-zero weight at every alpha, and the weights shrink towards
zero together as the penalty rises. That is the difference from the LASSO path
above, where features leave the model one at a time and do not come back.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0067-p000

~~~~~~markdown
Compare this against the LASSO paths above. Ridge pulls every coefficient toward zero and
leaves all of them non-zero; LASSO sets them to exactly zero one at a time. That difference
is the reason to reach for one or the other: LASSO answers which features to keep, Ridge
answers how much to believe all of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p000>>>
<<<ML4T-ZH-END:c0067-p000>>>

### c0068-p000

~~~~~~markdown
The two coefficient paths are the whole difference between the penalties in
one picture. Ridge attenuates every weight and keeps every feature; LASSO
removes features one at a time, and which ones it removes depends on the
training window. Elastic Net sits between them: it can zero a coefficient, but
its L2 component keeps correlated features together rather than picking one of
the group arbitrarily.
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0069-p000

~~~~~~markdown
## Key Takeaways

1. **Shrinkage buys variance reduction with bias.** Ridge pulls every
   coefficient towards zero, which costs accuracy on the training fold and can
   repay it on the next one. Where features are many, correlated, and weakly
   related to the target, that trade is usually worth making, and the alpha
   sweep is how you find out where it stops paying.

2. **LASSO performs feature selection**: at the selected alpha some
   coefficients are exactly zero and those features leave the model. The
   coefficient path shows the order in which the rest enter as the penalty
   weakens, and the fold heatmap shows how much of that selection is repeated
   when the training window changes.

3. **Elastic Net** blends both penalties. Higher L1 ratio produces more
   sparsity; the choice depends on whether you value interpretability or
   want to retain correlated features.

4. **Walk-forward CV with purging** is what makes any of these numbers
   meaningful. Standard K-fold trains on data that follows its test window and
   scores a model against outcomes it has already seen, and with a 21-day
   forward label the fold boundary has to be widened by the label horizon
   before the two sides are genuinely separate.

**Next**: See [[ML4T_A3_0001]] for direction prediction, or
[[ML4T_A3_0002]] for hyperparameter optimization with Optuna.
~~~~~~

<<<ML4T-ZH-BEGIN:c0069-p000>>>
<<<ML4T-ZH-END:c0069-p000>>>
