# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/02_regularization_paths.ipynb；A3 Pack 002；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market regime → 市場狀態
- Feature → 特徵
- Label → 標籤
- Cross-validation → 交叉驗證
- Overfitting → 過度擬合
- Standard deviation → 標準差

## 待翻譯英文單元

### c0028-p000

~~~~~~markdown
Compare the two ICs printed above. Recency weighting is a bet that the recent
past resembles the near future more than the distant past does, and the
effective sample size says what the bet costs: the decay leaves the fit with
the equivalent of a fraction of its training rows. Where the bet does not pay,
the model has traded data for nothing. One fold decides none of this - the
effect varies across folds and market regimes, and after a structural break
recency weighting is what lets a model respond at all. What to take from the
cell is the mechanics and the size of the sample-size cost, not the sign of
the difference on one window. The [[ML4T_A3_0001]] parameter is available on
all sklearn estimators, including the logistic models in [[ML4T_A3_0002]]
and gradient boosting in Ch12.

> **Note on uniqueness weighting**: The text also discusses [[ML4T_A3_0003]]-bar
> uniqueness weighting to correct for label overlap. Computing uniqueness weights
> requires the concurrency structure from Chapter 7's triple-barrier labels, which
> the ETF case study does not use (it uses simple forward returns). The per-case-study
> runner notebooks ([[ML4T_A3_0004]]) apply uniqueness weighting where applicable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0029-p000

~~~~~~markdown
## LASSO Regression (L1)

LASSO drives some coefficients to exactly zero - automatic feature selection.
To find a meaningful alpha grid, we first compute [[ML4T_A3_0001]], the smallest
alpha that sets every coefficient to zero, from the first fold's training data.
Above it there is nothing to see, because every model is the same empty model.
The grid then runs log-spaced from there down to a small fraction of it, which
is where the model is close to unpenalized.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
LASSO achieves comparable IC to Ridge while zeroing out a substantial fraction of
features. The [[ML4T_A3_0001]] column shows the sparsity-performance tradeoff: too few
features (high [[ML4T_A3_0002]]) loses signal, while too many (low [[ML4T_A3_0003]]) approaches
OLS overfitting. Which features survive varies across folds - LASSO's instability
with correlated inputs, as discussed in the text.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
### LASSO Feature Selection Stability

Which features survive varies across folds - a binary heatmap reveals the
instability. Columns that flicker on and off confirm LASSO's sensitivity
to the training window when features are correlated.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
Features present in all folds represent robust LASSO selections. Features that
flicker on and off are unstable - their inclusion depends on which training
window the model sees. This motivates Elastic Net, which retains correlated
feature groups rather than picking one arbitrarily.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
## Elastic Net (L1 + L2)

Elastic Net blends the two penalties, and [[ML4T_A3_0001]] sets the mix: at one it is
LASSO, at zero it is Ridge. Holding alpha at the value the LASSO sweep selected
and varying only the ratio isolates what the mix decides, which is how much
sparsity you get for a given total penalty.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0040-p000

~~~~~~markdown
Higher [[ML4T_A3_0001]] produces more sparsity, closer to LASSO; lower values retain
more features, closer to Ridge. Holding alpha fixed is what makes the row-to-row
difference readable, and it also means the mix has not been tuned against the
alpha. Joint optimization of both [[ML4T_A3_0002]] and
[[ML4T_A3_0003]] is demonstrated in [[ML4T_A3_0004]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0041-p000

~~~~~~markdown
## Loss Function Comparison

The section text discusses MSE, MAE, and Huber loss. [[ML4T_A3_0001]] provides a
unified interface: all three accept an L2 penalty and [[ML4T_A3_0002]]. Fitting
them at one alpha, on one set of folds, isolates the loss function as the only
thing that differs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0044-p000

~~~~~~markdown
The three losses differ in how much weight they give a large residual. Squared
error grows with the square of it, so one extreme return can move the fit more
than a hundred ordinary ones. Huber is quadratic for small residuals and linear
beyond a threshold, so an outlier still counts but stops dominating.
The epsilon-insensitive loss ignores residuals smaller than epsilon entirely
and is linear outside that band. Return distributions are heavy-tailed, which
is the condition under which that difference shows up in a ranking metric, and
it is why the case-study pipelines in Ch12 reach for LightGBM's Huber
objective.

Read the table for the ordering, not for the level. [[ML4T_A3_0001]] optimizes
by stochastic gradient descent under a learning-rate schedule, so its ICs are
not comparable with the closed-form Ridge solution above even at the same
alpha; only the comparison between the three losses, fitted the same way on
the same folds, is meaningful here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0045-p000

~~~~~~markdown
### LASSO Coefficient Path

We use [[ML4T_A3_0001]] on the first fold for an efficient
warm-started coefficient path (much faster than refitting per alpha).
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0047-p000

~~~~~~markdown
### Save Cache
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
## Model Comparison

Each method is summarized by its mean IC across the walk-forward folds and by
the standard deviation of that IC, which says how much the number depends on
which fold you look at.

One caveat governs the whole comparison, and it is the reason [[ML4T_A3_0001]]
exists. The alpha for each penalized model was chosen by taking the highest mean
IC over these same validation folds, and the score reported here is that same
highest mean IC. A number picked as the maximum of a sweep is biased upward by
the picking: some of it is the penalty helping, and some of it is the luck of
whichever alpha happened to suit these folds. Nothing here is held back to
measure the difference, so read the chart as a comparison of methods under a
tuning budget, not as an estimate of what any of them would score on data
nobody selected on. Nested cross-validation, in [[ML4T_A3_0002]], is what
separates the two.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
The error bars are wider than the gaps between the bars, which is worth seeing and is less
than it looks. Every method is scored on the same folds, so their scores rise and fall
together with whatever each fold happens to contain - and a method can be consistently
ahead of another while both have wide marginal spreads. Overlapping error bars across
methods do not settle whether one is ahead of another.

What settles it is the paired difference: subtract the two methods' IC fold by fold and
look at the spread of that series, which cancels the fold effect these bars are dominated
by. This chart shows the spread; it does not compare the methods.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>
