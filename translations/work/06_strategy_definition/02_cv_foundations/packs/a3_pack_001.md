# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：06_strategy_definition/02_cv_foundations.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Feature → 特徵
- Label → 標籤
- Training set → 訓練集
- Test set → 測試集
- Cross-validation → 交叉驗證
- Overfitting → 過度擬合
- Hyperparameter → 超參數
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Cross-Validation for Financial Machine Learning

**ML4T Third Edition — Chapter 6: Strategy Research Framework**

**Docker image**: [[ML4T_A3_0001]]

This notebook builds cross-validation from first principles for time series:

1. **Decision-time admissibility** — the central design constraint
2. **Three dataset roles** — train, validation, and holdout test
3. **K-fold CV** — and why random shuffling fails for time series
4. **Walk-forward CV** — expanding and rolling windows
5. **Label buffer (purging)** — preventing forward-looking label leakage
6. **Feature buffer (embargo)** — preventing backward-looking feature leakage
7. **Calendar-aware CV** — trading days vs calendar days
8. **Nested walk-forward** — retuning across multiple test years
9. **Combinatorial purged CV (CPCV)** — multiple backtest paths
10. **Putting it together** — from config to protocol

**Book Reference**: Section 6.5 (Evaluation Protocol for Time Series)

**References**:
- López de Prado (2018). *Advances in Financial Machine Learning*, Ch. 7
- Bailey, Borwein, López de Prado, and Zhu (2014). "The Probability of Backtest Overfitting"
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
The CV schematics use three palette roles throughout: training is the main series,
the validation fold is the amber highlight, and a buffer is a light neutral.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0006-p000

~~~~~~markdown
---

## Data Setup

We use 12 years of NYSE trading sessions (2014–2025) throughout.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Visualization Helper
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
---

## 1. Decision-Time Admissibility

The central question behind every CV design choice:

> **At decision time [[ML4T_A3_0001]], which labeled samples were actually available?**

Any sample whose label, feature, or selection criterion depends on
information unavailable at [[ML4T_A3_0002]] must be excluded from training.
Section 6.5 identifies five channels through which future information can
leak into past decisions:

| Leakage Channel | Example | Prevention |
|---|---|---|
| **Label leakage** | 21-day forward return overlaps validation | Label buffer (purging) |
| **Standardization leakage** | Z-scoring with full-sample mean/std | Expanding-window transforms |
| **Threshold leakage** | Percentile labels from full sample | Rolling percentile thresholds |
| **Survivorship leakage** | Training only on surviving firms | Rebalance universe per period |
| **Point-in-time leakage** | Fundamentals reported after decision | Conservative publication lag |

The CV schemes in this notebook operationalize the first channel (label
leakage via the **label buffer**) and flag where the others apply.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
---

## 2. Three Dataset Roles

Before any experiment, partition data into three disjoint sets:

| Dataset | Role | When Accessed |
|---|---|---|
| **Training** | Fit model parameters | During training |
| **Validation** | Select hyperparameters, compare models | During development |
| **Holdout Test** | Final unbiased performance estimate | Once, at the end |

The **holdout test set is set aside** at the start and not opened again. Using it
for any development decision contaminates the final estimate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
**Rule**: The holdout test set is NEVER used for model selection,
hyperparameter tuning, or any development decision.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
---

## 3. K-Fold Cross-Validation

Standard k-fold CV shuffles samples randomly and rotates the held-out fold.
This works for i.i.d. data but **destroys temporal structure** in time series:
the model trains on future data to predict the past.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
In Fold 1, the model trains on samples from the future (indices 80–100) to
predict the past. This violates decision-time admissibility.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
---

## 4. Walk-Forward Cross-Validation

**Walk-forward CV** respects temporal ordering: training always **precedes**
validation. Two variants — **expanding** and **rolling** windows.

We use [[ML4T_A3_0001]] from [[ML4T_A3_0002]] to generate the
actual folds on NYSE trading sessions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0018-p000

~~~~~~markdown
### Expanding Window

Training grows with each fold — uses all available history.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
**Advantage**: Uses all available data. **Disadvantage**: Training set size
varies, which can affect model behavior.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
### Rolling Window

Fixed training window — old data drops off as we move forward.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
**Advantage**: Consistent training size; stale data doesn't influence the model.
**Disadvantage**: Discards data. Choose expanding if older data is still
relevant, rolling if you believe regimes change.

The chart shows where that consistency starts. [[ML4T_A3_0001]] asks for five years of
sessions, and the first two folds cannot reach back that far, so their training
windows are clipped at the beginning of the sample and match the expanding chart
exactly. Only folds 3 to 5 hold the requested window. A rolling scheme guarantees a
fixed training size from the first fold whose window fits inside the data, not from
the first fold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>
