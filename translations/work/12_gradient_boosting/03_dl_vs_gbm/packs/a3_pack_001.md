# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/03_dl_vs_gbm.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Deep learning → 深度學習
- Feature → 特徵
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Deep Learning vs GBMs for Tabular Financial Data

**Docker image**: [[ML4T_A3_0001]]

**Chapter 12, Section 12.3**: Deep Learning Alternatives for Tabular Data

## Purpose
This notebook compares gradient boosting machines against modern deep learning
alternatives on the ETF case study, measuring rank IC and training time across
walk-forward folds. The comparison grounds Section 12.3's decision framework
with empirical evidence.

## Learning Objectives
After completing this notebook, you will be able to:
- Compare GBM, MLP, TabM, and TabPFN on financial tabular data
- Evaluate models across walk-forward folds (not a single split)
- Understand when deep learning offers practical advantages over GBMs
- Interpret IC and training-time trade-offs for model selection

**Prerequisites**: Requires case study features from
[[ML4T_A3_0002]] and modeling artifacts from Chapter 11 setup.

## Models Compared
1. **LightGBM**: Production GBM baseline
2. **MLP**: PyTorch neural network (minimal baseline)
3. **TabM**: Rank-one adapter MLP ensemble (Gorishniy et al., ICLR 2025)
4. **TabPFN**: Foundation model for small tabular data (if installed)

## Cross-References
- **Section 12.3**: Decision framework and benchmark discussion
- **Related**: [[ML4T_A3_0003]] (GBM library comparison), [[ML4T_A3_0004]] (HPO)
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
## 2. Load ETF Features
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 3. Model Definitions

### TabM: Rank-one Adapter MLP Ensemble

TabM (Gorishniy et al., ICLR 2025) trains [[ML4T_A3_0001]] MLPs that share their weight
matrices and differ by rank-one adapters. Every linear layer multiplies its
input and its output by a per-member vector, so the nonlinearity that follows
sees a different pre-activation for each member and the members are different
functions of the input. The loss is the mean of the [[ML4T_A3_0002]] per-member losses, so
each member fits the target on its own and they overfit in different
directions; the prediction averages them. Placing the adapters after the last
nonlinearity instead, or training one loss on the averaged output, leaves a
single MLP: [[ML4T_A3_0003]] is one linear readout of one backbone. This implements
the core idea with PyTorch directly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
### TabM Architecture
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### TabM Training
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### TabM Inference
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Minimal MLP Baseline (PyTorch, GPU)

A 64-32 ReLU MLP with Adam and L1 (MAE) loss, the simplest neural
network we could write, implemented in PyTorch so it runs on the same
GPU as TabM. This is the "minimal neural baseline" the chapter section
refers to: fewer parameters than TabM, no ensembling, no architectural
tricks. Same val/early-stop framework as TabM.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 4. Walk-Forward Evaluation

We evaluate each model across all walk-forward folds, collecting per-fold IC
and training time. This matches the temporal validation protocol emphasized
in Section 12.3: single-split comparisons are unreliable for financial data.

Rather than fix an epoch or tree count in advance, we carve a chronological
**validation slice** off the end of each fold's train window - [[ML4T_A3_0001]] of it -
and use it as a held-out set during fitting:

* **LightGBM**: [[ML4T_A3_0002]] plus [[ML4T_A3_0003]];
  we report the iteration count picked by early stopping ([[ML4T_A3_0004]]).
* **MLP**: minimal 64-32 ReLU MLP in PyTorch, on whichever device this run has;
  loop as TabM, with [[ML4T_A3_0005]] epochs on val-loss plateau.
* **TabM**: track per-epoch train + val L1 (MAE) loss, restore the
  best-val checkpoint at predict time, report [[ML4T_A3_0006]] per fold.

All three trainable models use **L1 (MAE)** loss, not MSE. On the codebase's
9 case-study GBM benchmark, MAE achieves the highest IC on 8 of 9
regression-primary case studies (see [[ML4T_A3_0007]] §3a),
because financial returns are heavy-tailed and squared-error loss chases
the few large residuals at the expense of the cross-sectional ranking that
IC rewards. A LightGBM regressor trained with MSE ([[ML4T_A3_0008]]) on this
fold structure still fits normally, dozens of trees, non-degenerate
predictions, but its test IC comes out lower, negative on fold 0 where the
MAE model is positive, which is why every trainable model here defaults to
MAE.
* **TabPFN**: zero-shot: no training, no validation needed.

The test slice is held strictly out, none of the early-stopping signals
touches it, so reported IC remains a fair walk-forward estimate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
### TabPFN Evaluation
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
TabPFN ships its weights under a gated license, so the first prediction needs a free
Prior Labs token: register at [[ML4T_A3_0001]] accept the license, and set
[[ML4T_A3_0002]] (see [[ML4T_A3_0003]]). The model is free for research and evaluation
like this notebook and not for commercial use. Where the package or the token is
missing the notebook says so and carries on without it; the comparison between the
other three models is unaffected.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0023-p000

~~~~~~markdown
### Fold Data Preparation
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0027-p000

~~~~~~markdown
## 5. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## 6. Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>
