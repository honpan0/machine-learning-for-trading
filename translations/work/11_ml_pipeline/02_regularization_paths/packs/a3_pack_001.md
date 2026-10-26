# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/02_regularization_paths.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Backtesting → 回測
- Feature → 特徵
- Label → 標籤
- Cross-validation → 交叉驗證
- Look-ahead bias → 前瞻偏誤
- Overfitting → 過度擬合
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Regularized Regression for Return Prediction

**Chapter 11 | Section 11.2**

**Docker image**: [[ML4T_A3_0001]]

This notebook compares OLS, Ridge (L2), LASSO (L1), and Elastic Net regression
for predicting 21-day forward returns on the ETF universe. Every model is fitted
on the same walk-forward folds, declared once in [[ML4T_A3_0002]] and loaded by
[[ML4T_A3_0003]], so that any difference between them comes from the
penalty and not from the split.

**Learning objectives**

- Understand the bias-variance tradeoff in regularized regression
- Compare Ridge, LASSO, and Elastic Net on real financial features
- Analyze regularization paths and LASSO feature selection
- Evaluate predictive performance via Information Coefficient (IC)

**Book reference**

Section 11.2 ("Regularized Regression"). The next notebook,
[[ML4T_A3_0004]], applies the same regularization toolkit to the
direction-prediction task; [[ML4T_A3_0005]] extends the alpha sweep into
nested cross-validation.

**Prerequisites**

- Working knowledge of OLS and the bias-variance tradeoff.
- Conceptual exposure to L1, L2, and Elastic-Net penalties.
- ETF case-study features at [[ML4T_A3_0006]]
  (Ch8) and labels at [[ML4T_A3_0007]] (Ch7).

**Downstream**: Ch12 (gradient boosting), Ch16-17 (backtesting + portfolio).
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

We load pre-computed ETF features from Ch8 and 21-day forward return labels
from Ch7. No synthetic fallback - if files are missing, run upstream notebooks.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0008-p000

~~~~~~markdown
## Walk-Forward Cross-Validation Setup

We load the canonical walk-forward splits from [[ML4T_A3_0001]] via
[[ML4T_A3_0002]]: rolling train/validation windows with purge gap.
This ensures consistency across all Ch11 notebooks and case studies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## Helper Functions

Every model below is scored the same way: rank the cross-section on each
validation date, correlate that ranking with the realized forward return, and
average over the dates where that correlation exists. Two kinds of date have
none. A date with fewer symbols quoting than the minimum cross-section is not
scored at all. A date where the model gives every symbol the same prediction
has no ranking to correlate, so its Spearman coefficient is undefined. Strong
regularization produces exactly that: at a high enough alpha every coefficient
is zero and the model predicts one constant for everything.

[[ML4T_A3_0001]] is the shared implementation, and
dropping those dates is the part worth knowing about - a single undefined date
left in the series turns the average of the whole series into NaN.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Winsorization

Clipping features at the 1st and 99th percentiles (computed on training data)
limits the influence of extreme observations on standardization. Without
winsorization, a single outlier can inflate [[ML4T_A3_0001]] and compress all other
observations toward zero. The percentile bounds are fitted on training data
only to prevent look-ahead bias.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Walk-Forward Cross-Validation
Run walk-forward CV with per-fold winsorization and standardization.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Model Cache

Training results (including fitted models and scalers) are cached to disk.
Set [[ML4T_A3_0001]] to force retraining.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## OLS Baseline

Ordinary Least Squares provides the unregularized reference point every
penalty below is measured against. It minimizes squared error on the training
fold with nothing holding its coefficients back, which on this many correlated
features and this little signal is the condition overfitting needs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
## Ridge Regression (L2)

Ridge shrinks all coefficients towards zero without setting any exactly to zero.
We sweep 23 log-spaced [[ML4T_A3_0001]] values from [[ML4T_A3_0002]] to [[ML4T_A3_0003]], covering the
full transition from under-regularized (indistinguishable from OLS) through the
optimal range to over-regularized (coefficients crushed to near zero).
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0024-p000

~~~~~~markdown
Read the sweep for its shape rather than its maximum. A flat stretch means the
penalty is doing little; a rise means shrinkage is buying more in variance than
it costs in bias; a fall at the far end means the coefficients have been
crushed to the point where the model has stopped ranking. Where the turn comes
is a property of how much signal the features carry, which is why a sweep this
wide is worth running on a new dataset rather than reusing an alpha from an
old one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
### Sample Weighting: Recency via Exponential Decay

Section 11.2 discusses sample weighting as a way to emphasize recent data
without discarding older observations. The weight decays exponentially with
age, [[ML4T_A3_0001]], so the newest observation counts fully and
older ones fade smoothly rather than falling off a cliff at a cutoff date.

Age has to be measured in trading sessions, not in rows. This is a panel: every
session contributes one row per symbol, so about a hundred rows share each
date. Counting age down the rows would decay the weight roughly a hundred times
faster than intended, and would hand two symbols quoting on the same day
different weights for no reason. Each row is therefore aged by the session it
belongs to.

The decay rate is set below as a half-life: the number of sessions after which
an observation counts half as much as today's. The effective sample size turns
that rate into the quantity that decides whether the trade is worth making,
which is how many rows the fit is effectively left with. It is Kish's,

[[ML4T_A3_0002]]

rather than [[ML4T_A3_0003]], because only this form is unchanged when every weight
is multiplied by a constant. That matters here: the weights are rescaled to
mean one before fitting, so [[ML4T_A3_0004]] would answer for a vector the fit does
not use and would report the full sample every time. We compare a single Ridge fit with and without weighting
on the last fold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>
