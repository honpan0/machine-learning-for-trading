# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/05_cross_library_hpo.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Hyperparameter → 超參數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Cross-Library HPO: XGBoost vs LightGBM vs CatBoost

**Docker image**: [[ML4T_A3_0001]]

**Chapter 12, Section 12.4**: Advanced Hyperparameter Tuning with Optuna

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 12_gradient_boosting/05_cross_library_hpo.py
> ```


## Purpose
Optuna-based HPO for XGBoost, LightGBM, and CatBoost on the Chen-Pelger-Zhu
(2020) firm characteristics dataset. **Loss type is a hyperparameter**
within each library's study, treating the choice of MSE vs MAE as a tunable
decision rather than a fixed prior.

## Learning Objectives
- Tune XGBoost, LightGBM, and CatBoost with Optuna under a shared protocol
- Treat loss function selection as a first-class hyperparameter
- Compare best-valid and best-test IC after model reconstruction
- Diagnose which hyperparameters drive gains in noisy financial targets

**Prerequisites**: Requires the firm characteristics dataset and supporting
loaders from [[ML4T_A3_0002]].

## Key Concepts
- TPE with configurable warm-up trials for each library
- MedianPruner for early stopping of unpromising trials
- SQLite persistence for reproducibility
- Loss function as a categorical hyperparameter
- Hyperparameter importance analysis (including loss_type)

## Cross-References
- **Section 12.4**: GBM-specific tuning strategy, pruning
- **Chapter 20**: These results feed into the cross-model synthesis
- **Related**: [[ML4T_A3_0003]] (ETF case study), [[ML4T_A3_0004]] (grid vs Optuna)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0006-p000

~~~~~~markdown
### Device Detection

XGBoost and CatBoost support GPU acceleration. We detect availability
at startup rather than hardcoding [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
> **Reproducibility.** This search runs on a GPU for speed. GPU training is not
> bitwise reproducible: fixed seeds pin each model's random choices but not the
> order in which parallel hardware sums floating-point values, so the selected
> configurations and IC values here are stable across reruns rather
> than identical to the last decimal. For runs that must reproduce exactly, train
> on CPU with deterministic settings; [[ML4T_A3_0001]] measures the
> GPU-versus-CPU prediction gap and gives the deterministic CPU recipe in full.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
## 2. Load Academic Dataset
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
## 3. Study Configuration

SQLite storage enables persistent studies. The database-backed approach
also supports parallel workers in production settings (PostgreSQL/MySQL
for true parallelism; SQLite for single-worker reproducibility).

Persistence has one sharp edge worth flagging: with [[ML4T_A3_0001]],
re-running the notebook against an existing database *appends* new trials to
the old study rather than starting over, so the trial counts and best configs
would creep upward on every execution. To keep the results reproducible we
delete any prior database at the top of the run, so a fresh execution always
optimizes exactly [[ML4T_A3_0002]] seeded trials per library.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 4. Objective Functions with Loss as Hyperparameter

Each library has one study where [[ML4T_A3_0001]] (MSE/MAE) is a categorical
parameter. This treats the loss function as a tunable decision rather than
a fixed choice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### LightGBM Objective Factory
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### CatBoost Objective Factory
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## 5. Model Building Helper

Shared function to reconstruct and evaluate models from Optuna trial
parameters. This eliminates the ~80 lines of duplicated model-building
code that would otherwise appear in the optimization and per-loss sections.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
### Evaluate Best-Config Model
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## 6. Run Optimization
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 7. Per-Loss Analysis

Extract each library's highest-scoring MSE and MAE configuration to
assess whether loss function choice matters.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## 8. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>
