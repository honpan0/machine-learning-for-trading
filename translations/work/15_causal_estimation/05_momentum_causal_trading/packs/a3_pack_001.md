# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/05_momentum_causal_trading.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Transaction costs → 交易成本
- Feature → 特徵
- Label → 標籤
- Look-ahead bias → 前瞻偏誤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Causal Analysis for Trading Decisions: A Momentum Case Study

**Chapter 15: Causal Estimation with ML**
**Docker image**: [[ML4T_A3_0001]]

Causal inference applied to a trading decision, and what it does and does not settle once
the strategy meets a holdout period.

**Section Reference**: Section 15.4, and its regime-conditional position-sizing case study

**The Question**: Does momentum have a causal effect on forward returns, and
does this effect vary by volatility regime?

**Methodological Approach**:
1. Define a clear train/test split (no look-ahead bias)
2. Estimate causal effects using only training data
3. Apply regime-conditional allocation to held-out test period
4. Compare to naive baseline and simple alternatives
5. Include transaction costs

What the notebook shows is the workflow, and what the workflow produces on this data is a
case where the in-sample improvement does not carry to the holdout. That is the usual
outcome and it is the reason the split exists.

**Learning Outcomes**:
- Estimate causal effects on training data alone and apply them to a holdout period
- Separate what a causal estimate establishes from what it earns in a backtest
- Turn a regime-conditional effect into a position size, and compare it against a
  baseline that uses no causal machinery at all

**Prerequisites**: [[[ML4T_A3_0002]]](03_econml_dml.ipynb) for the DML machinery, and an
ETF modeling dataset built by the features pipeline

## Causal Design Contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

| Element                   | This notebook                                                                                |
|---------------------------|----------------------------------------------------------------------------------------------|
| Unit                      | ETF-date row from the ETF modeling panel                                                     |
| Treatment                 | [[ML4T_A3_0001]] momentum (continuous)                                                       |
| Outcome                   | [[ML4T_A3_0002]] - 21-day forward return                                                         |
| Controls (W)              | [[ML4T_A3_0003]], [[ML4T_A3_0004]], [[ML4T_A3_0005]], [[ML4T_A3_0006]]                                         |
| Effect modifiers (X)      | [[ML4T_A3_0007]] (SPY 63-day vol) + high-/low-vol regime indicators, via CausalForestDML   |
| Identification assumption | Selection on observables given the four controls; CATE varies smoothly with realized vol     |
| Main failure modes        | Unobserved confounding; CATE generalization failure out of sample; trading cost erosion       |
| Estimand                  | ATE and regime-conditional CATE from CausalForestDML; downstream trading rule scales position by sign-of-CATE × magnitude |
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## 1. Setup and Configuration
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## 2. Load ETF Features from Modeling Pipeline

We use [[ML4T_A3_0001]] to load pre-computed momentum features (Ch8),
temporal features (Ch9), and labels from the case study pipeline.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### Defining the Market Volatility Regime

We define regime based on market-wide volatility (SPY as proxy).
This is a potential confounder OR effect modifier.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### The Train/Test Split

We use the walk-forward splits from the modeling pipeline.
Training: all folds except last validation period.
Test: last validation period (most recent data).
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## 3. Training Period: Estimate Causal Effects

We fit all causal models on the TRAINING data only. These estimates will
then be applied to the held-out test period.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Estimating the Effect with DML

We estimate:
1. Average Treatment Effect (ATE) - overall momentum effect
2. Conditional Average Treatment Effect (CATE) by regime
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Walk-Forward Cross-Fitting Splits

Cross-fitting uses the chapter pipeline's walk-forward schedule ([[ML4T_A3_0001]])
restricted to the training period. No sklearn [[ML4T_A3_0002]] fallback is used.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### Cached DML Artifacts

The causal-forest fit is the expensive step, so the estimates it produces are written to a
cache beside the notebook. [[ML4T_A3_0001]] defaults to [[ML4T_A3_0002]], which means every run refits from
the raw modeling dataset and the cache is only ever written. A published render has to be
something the shipped code reproduces, and a cache hit is not a reproduction: the cached
numbers came from whatever the estimator looked like when they were written.

Set it to [[ML4T_A3_0003]] while iterating on the strategy code below, where the causal estimates
are an input you are not changing. The cache records the effect-modifier and control
columns it was built with and refuses itself if either has moved, so it cannot silently
answer for a different specification - but it cannot detect a change inside the estimator.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
### Fitting LinearDML and CausalForestDML
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
### The ATE and the CATE by Regime
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## 4. Define Trading Strategies

We define three strategies to compare:
1. **Naive**: Equal momentum exposure across all regimes
2. **Causal-Informed**: Scale by estimated CATE from training
3. **Simple Heuristic**: Reduce exposure in high-vol (no causal machinery)

### Where the Heuristic Factors Come From

[[ML4T_A3_0001]] encodes practitioner intuition rather than an estimate: raise exposure
in calm markets, hold it neutral in the middle, cut it when volatility is high, because
momentum is widely held to break down in crises. The factors are printed below. They exist
to give the causal strategy something to beat that costs nothing to build, which is the
comparison that decides whether the causal machinery earned its place.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### Backtest Helpers

Helper functions for the momentum backtest: quintile assignment,
position-weighted returns, and turnover-based transaction costs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
