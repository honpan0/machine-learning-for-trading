# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/04_dml_crypto_regime.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Machine learning → 機器學習
- Feature → 特徵
- Label → 標籤
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Double Machine Learning on Crypto Premium Index with Regime Conditioning

**Chapter 15: Causal Estimation with ML**
**Docker image**: [[ML4T_A3_0001]]

**Section Reference**: Section 15.4 for DML, and Section 15.3 for the refutation tests

## Purpose
Double machine learning applied to the perpetual-futures premium: does a stretched premium
cause the next 8-hour return, and does the answer differ between calm and volatile markets?
The panel is nineteen perpetuals sharing every timestamp, which is what makes the second
half of the notebook about how a correction knows what "nearby" means.

The estimand is the marginal effect of a one-unit change in the 14-day
premium z-score on the next-bar return, after adjustment for observed
pre-treatment controls:

[[ML4T_A3_0002]]

Regime-specific estimates apply this same estimand within volatility strata
(subgroup ATEs), not Conditional Average Treatment Effects (CATE), which
would require a single heterogeneity model rather than separate
regime-stratified fits.

## Causal Design Contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

| Element                   | This notebook                                                                                          |
|---------------------------|--------------------------------------------------------------------------------------------------------|
| Unit                      | Crypto-symbol × 8-hour-bar from the crypto perps panel (19 symbols)                                    |
| Treatment                 | [[ML4T_A3_0001]] (continuous)                                                                       |
| Outcome                   | [[ML4T_A3_0002]] (next-bar return)                                                                          |
| Controls (W in EconML)    | [[ML4T_A3_0003]], [[ML4T_A3_0004]], [[ML4T_A3_0005]], [[ML4T_A3_0006]], [[ML4T_A3_0007]], [[ML4T_A3_0008]] |
| Effect modifiers (X)      | Volatility regime (high vs low), entered via regime-stratified DML and a single-model interaction |
| Identification assumption | Selection on observables given the six controls; controls are constructed strictly pre-treatment       |
| Main failure modes        | Bad-control bias from premium-derived controls; mistimed treatment relative to control horizons; cross-symbol contagion that the controls don't capture |
| Estimand                  | Marginal effect of a one-unit z-score change; ATE within each volatility regime; interaction coefficient on T × regime |

**Learning Outcomes**:
- Fit DML on a multi-symbol panel and report a standard error that counts in bars
- Estimate a treatment effect within volatility regimes and test the difference in one model
- Build a block permutation whose blocks are the durations their labels claim
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**Methodological Notes** (per Chernozhukov et al. 2017):
- **WalkForwardCV**: cross-fitting with purging and embargo over decision times
- **Driscoll-Kraay standard errors**: the score is aggregated by timestamp before the
  Newey-West kernel is applied, so nineteen perpetuals in one bar are one period
- **Block permutation within symbol**: the placebo treatment keeps its persistence

**Timing Protocol**: confounders are pre-computed features known before [[ML4T_A3_0001]], the treatment
is [[ML4T_A3_0002]] measured at [[ML4T_A3_0003]], and the outcome is the return over the bar that
follows.

**Cross-References**:
- Chapter 15: [[[ML4T_A3_0004]]](03_econml_dml.ipynb) (ETF momentum DML)
- Chapter 8: Crypto premium features
- Chapter 14: Latent factor regime detection

**Prerequisites**: [[[ML4T_A3_0005]]](03_econml_dml.ipynb) for DML methodology;
crypto premium data from Ch2 data pipeline
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0001-p000

~~~~~~markdown
## 1. Setup and Imports
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0003-p000

~~~~~~markdown
### Settings, and What the Bandwidth Is Derived From

The serial-correlation bandwidth is the one setting here that is not free. Consecutive
observations of one symbol share up to 14 days of input to the premium z-score, so that
window is what the correction has to cover, and [[ML4T_A3_0001]] is it expressed in 8-hour bars.
The forward return spans a single bar and does not overlap, so unlike a 21-day label it
contributes nothing to the bandwidth.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Load Pre-Computed Features from Modeling Pipeline

We use [[ML4T_A3_0001]] to load pre-computed premium features (Ch8)
and labels, joined and ready for analysis. This replaces manual OHLCV loading
and confounder engineering. Real-data only; no synthetic fallback. If the
modeling dataset is missing, the notebook fails loudly rather than silently
switching to a synthetic substitute.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
### The Panel Keys

A row is a symbol and an 8-hour bar, and the frame is sorted by timestamp, so nineteen
consecutive rows are nineteen perpetuals in the same bar rather than nineteen bars. Every
correction below that has a notion of "nearby" - the standard errors, the cross-fitting
folds and embargo, the permutation blocks - takes the two arrays below and counts in
decision times, not in rows. Counted in rows, a [[ML4T_A3_0001]] of twelve would spend its whole
bandwidth inside a single bar.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## 3. Define Treatment, Outcome, and Confounders
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## 4. Naive Estimate (Biased)
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
## 5. DML with Walk-Forward CV + Embargo

Uses shared [[ML4T_A3_0001]] from [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 6. Compare Naive vs DML
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 7. Regime-Conditional Effects

**Estimand and terminology**. The target quantity in this notebook is the
marginal effect of a one-unit change in the 14-day premium z-score on the
next-bar return, after adjustment for observed pre-treatment controls:

[[ML4T_A3_0001]]

Regime-specific estimates apply this same estimand within volatility
strata; these are **subgroup ATEs**, not Conditional Average Treatment
Effects (CATE). CATE refers to individual-level or covariate-conditional
heterogeneity estimated by a single model (Causal Forest, X-learner). We
repeat the estimand inside each regime rather than fitting a single
heterogeneity model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
