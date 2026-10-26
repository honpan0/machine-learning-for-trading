# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/03_logistic_classification.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cross-validation → 交叉驗證

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Logistic Regression for Return Direction Prediction

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: apply logistic regression to predict the direction of 21-day forward
returns on the ETF panel, using the same walk-forward folds as
[[ML4T_A3_0002]].

**Learning objectives**

- Convert a continuous return label into a binary classification target
- Fit L2- and L1-regularized logistic regression on walk-forward folds
- Evaluate with classification metrics: accuracy, AUC-ROC, precision, recall
- Assess probability calibration and its importance for position sizing
- Compare feature importance from L1 logistic coefficients

**Book reference**: Section 11.3 - Predicting Direction with Logistic Regression.

**Prerequisites**

- Ch7 21-day forward return labels at [[ML4T_A3_0003]]
- Ch8 ETF features at [[ML4T_A3_0004]]
- Walk-forward CV configuration in [[ML4T_A3_0005]]

**Downstream**: [[ML4T_A3_0006]] (HPO with nested CV), [[ML4T_A3_0007]]
(uncertainty quantification), Ch12 (gradient boosting on the same task).
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

We reuse the same pre-computed features (Ch8) and 21-day forward return labels
(Ch7) as [[ML4T_A3_0001]]. The only difference is that we convert the
continuous return into a binary direction target.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### Create Binary Direction Target

We convert the continuous 21-day forward return into a binary label:
1 if the return is positive (up), 0 otherwise (down). This transforms
the regression problem from NB02 into a classification problem.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Class Balance

A significant imbalance would require stratified sampling or reweighting.
With 21-day returns on diversified ETFs over a long-term bull market, we
expect a moderate positive skew.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Walk-Forward Cross-Validation Setup

We reuse the same walk-forward splits from [[ML4T_A3_0001]] as
[[ML4T_A3_0002]]: rolling train/validation windows with purge gap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## Helper Functions

### Solver Selection

sklearn's [[ML4T_A3_0001]] offers several solvers optimized for different
penalty structures:

| Solver | L1 | L2 | ElasticNet | Multinomial | Best for |
|------------|----|----|------------|-------------|----------------------------------------------|
| [[ML4T_A3_0002]] | no | yes | no | yes | Default L2; fast quasi-Newton |
| [[ML4T_A3_0003]] | yes | yes | no | no | Pure L1 binary; coordinate descent |
| [[ML4T_A3_0004]] | yes | yes | yes | yes | ElasticNet, large [[ML4T_A3_0005]], [[ML4T_A3_0006]] |

We use [[ML4T_A3_0007]] for L2 (fast, numerically stable), [[ML4T_A3_0008]] for pure L1
binary classification, and [[ML4T_A3_0009]] only when ElasticNet mixing is needed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Logistic Estimator

Penalty-specific solver choices live in one constructor so the cache signature
and every fold share the same training contract.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### One Walk-Forward Fold

Every fold learns preprocessing and model state from its training rows only.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
### Walk-Forward Logistic CV

The wrapper collects fold metrics, predictions, coefficients, and fitted state.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
## Model Cache

Training results are cached to disk so subsequent runs skip model fitting.
Its signature binds the cleaned arrays, split state, model configuration, source
implementation, and relevant library versions. Any semantic change therefore
triggers a genuine retrain rather than silently reusing stale predictions.
Set [[ML4T_A3_0001]] to force retraining even when the hashes match.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
The three digests the contract is built from are shared with the other notebooks
that cache a fit, in [[ML4T_A3_0001]]: a content hash of each input file, an
array hash that also covers filtering, symbol limits, row order, feature order
and cleaning semantics, and a canonical hash of the nested contract itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
The training contract records every choice that can change fitted predictions.
A canonical digest keeps the cache comparison compact and deterministic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
The data and split contracts include both declared configuration and the resolved
rows. This catches changes in cleaning, symbol limits, calendar mapping, or fold order.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
