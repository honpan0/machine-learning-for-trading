# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/05_rp_pca.ipynb；A3 Pack 001；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Factor premium → 因子溢酬
- Portfolio → 投資組合
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Risk-Premium PCA: Pricing Information in Latent Factors

**Docker image**: [[ML4T_A3_0001]]

**Chapter 14: Latent Factor Models**

Principal component analysis favors directions with high return variance.
Risk-Premium PCA (RP-PCA; Lettau and Pelger, 2020) also rewards directions
that explain the cross-section of mean returns:

[[ML4T_A3_0002]]

The top eigenvectors of [[ML4T_A3_0003]] define static factor portfolios. At
[[ML4T_A3_0004]], the estimator is ordinary covariance PCA. Positive values tilt
Stage 1 toward priced directions that may have modest variance.

**Learning objectives**

- implement RP-PCA from the modified covariance matrix;
- separate training mean fit from evaluation covariance reconstruction;
- compare loading spaces without relying on arbitrary factor signs; and
- produce one-day-ahead factor and asset forecasts with walk-forward updates.

**Evaluation contract**: the loading map is fit before the temporal split.
At each evaluation decision, the current return and its projected factor are
observable; only then is the next factor premium forecast. The evaluation window is a
teaching demonstration: it is neither a holdout kept untouched for a final measurement
nor a set used to choose between models. The pre-specified forecast model uses
[[ML4T_A3_0005]].

**Universe limitation**: the source is a curated present-day ETF set, so the
panel is suitable for method exposition but not a survivorship-free historical
strategy claim. Eligibility is determined from the training window only, and
no missing return is imputed.

**Prerequisites**: [[[ML4T_A3_0006]]](01_pca_equity_sectors.ipynb) and
[[[ML4T_A3_0007]]](04_ipca.ipynb)

**Book section**: Section 14.5, "Bridging economics and statistics with advanced models"
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Next**: [[[ML4T_A3_0001]]](06_conditional_autoencoder.ipynb)
replaces the static linear loading map with a neural network.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## 2. Build a balanced, training-defined panel

Computing returns before the pivot avoids treating a missing price as a zero
return. The initial wide panel retains nulls so eligibility can distinguish
a real zero from a pre-inception observation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
A symbol is eligible only if it has an observed return on every training
date. The rule is fixed before evaluation. The resulting 59 ETFs also happen
to have complete evaluation histories, which we verify rather than assume.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
The one-day target alignment is explicit: the current return at each decision
becomes Stage 2 history, while the following row is the evaluation target.
The current row therefore provides the one-period gap between the Stage 1 fit
and the first target.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## 3. Stage 1: fit RP-PCA

The covariance and mean vector are estimated on the training window only.
Eigenvector signs are anchored deterministically because neither signs nor
rotations within a tied eigenspace change the fitted subspace.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
Pricing fit measures how well the loading subspace spans the training mean
vector. Reconstruction share measures how much raw evaluation return energy
the same subspace retains relative to a zero-return reconstruction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0017-p000

~~~~~~markdown
The three panels expose the intended tradeoff directly. Increasing [[ML4T_A3_0001]]
can improve representation of the training mean only by rotating away from
the variance-dominant PCA space, which may sacrifice evaluation reconstruction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 4. Stage 2: update before forecasting

RP-PCA supplies a fixed loading map and a training factor history. At each
evaluation decision, projecting the current observed return produces the
latest realized factor. Stage 2 appends that factor and forecasts the next
one. No forecaster generates an unattended multi-step path.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0025-p000

~~~~~~markdown
## 5. Stage 3: map and evaluate next-day returns

The static loadings map each factor-premium forecast back to 59 ETF return
forecasts. MSE uses the zero-return forecast as the benchmark. Rank IC is
computed within each decision-time cross-section and averaged over time;
Newey-West inference allows for serial dependence in the daily IC series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0030-p000

~~~~~~markdown
Each interval is around that one forecaster's mean IC, and what it settles is whether
that forecaster's mean is distinguishable from zero. It says nothing about the gap
between two of them: the three IC series run over the same evaluation dates and the
same returns, so the uncertainty in a difference depends on how the two series covary,
which needs the paired daily difference and is not computed here. An IC can also be
statistically nonzero while the squared-error forecast remains economically
indistinguishable from zero at a daily horizon.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
## 6. Takeaways

1. **RP-PCA changes Stage 1.** It rotates the PCA loading space toward the
   training mean vector while leaving the forecasting and mapping interfaces
   unchanged.
2. **Pricing fit and covariance fit are different objectives.** Here the
   training mean fit rises with [[ML4T_A3_0001]] while evaluation reconstruction stays
   nearly flat; the sweep does not choose a weight on evaluation results.
3. **Missing is not zero.** Restricting eligibility to the 59 ETFs with
   complete training histories removes thousands of pre-inception pseudo-zeros.
4. **Walk-forward timing uses current information once.** Each observed factor
   updates history before the following day's premium is forecast.
5. **The figure says which forecasters clear zero, not which one is best.** The MSE
   panel is on an axis spanning a couple of percentage points either side of the
   benchmark, so a visible gap there is a small effect. The IC panel's intervals each
   ask whether that forecaster's mean IC is distinguishable from zero, and reading a
   ranking off them is the mistake the panel invites: separating two forecasters needs
   the interval on their paired daily difference, and overlapping individual intervals
   do not settle it either way. Whatever the run shows, this universe is curated and
   cannot support a survivorship-free strategy claim.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>
