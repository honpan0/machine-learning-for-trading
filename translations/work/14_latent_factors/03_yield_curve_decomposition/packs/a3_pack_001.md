# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/03_yield_curve_decomposition.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Label → 標籤
- Time series → 時間序列
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Yield Curve Decomposition: Level, Slope, and Curvature

**Docker image**: [[ML4T_A3_0001]]

**Chapter 14: Latent Factors**

This notebook demonstrates one of PCA's most celebrated applications:
decomposing the Treasury yield curve into its three primary factors.

**Learning Objectives:**
- Apply PCA to Treasury yield changes and interpret the resulting factors
- Understand why PCA works exceptionally well for yield curves (low-dimensional macro drivers)
- Visualize factor loadings, time series, and reconstruction quality
- Connect the decomposition to practical factor-based hedging

## Where this fits in the framework

Yield-curve PCA is a textbook **Stage 1** decomposition (Figure 14.9):
the cross-section of yields is compressed to three orthogonal factors.
Stage 1 is essentially where the yield curve story ends in this notebook:
the factors are interpretable risk dimensions used for hedging and risk
decomposition, not return forecasts. The two-step framework's Stage 2 +
Stage 3 mechanics become relevant when factors are used predictively;
see [[[ML4T_A3_0002]]](04_ipca.ipynb) for that pipeline on equity panels.
This notebook uses the complete sample only for descriptive decomposition and
local sensitivity analysis. It contains no target, model selection, backtest,
or performance claim, so a train/validation/test split is not applicable.

**Key Concepts (Litterman & Scheinkman, 1991):** the first three components of a
yield-curve panel take a recognisable form, and the loading figure below is where each
is read off rather than taken on trust.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- PC1 (Level): a shift of the whole curve in one direction, so its loadings share a sign
- PC2 (Slope): steepening or flattening, so its loadings change sign between the short
  and long ends
- PC3 (Curvature): a butterfly twist, so the middle of the curve loads opposite to both
  ends

The share of variance each carries is printed with the loadings, alongside a bootstrap
interval, because it is a property of this sample rather than of the yield curve.

**Prerequisites**: Complete [[[ML4T_A3_0001]]](01_pca_equity_sectors.ipynb); requires FRED macro data.

**Data Source**: FRED macro parquet (canonical data, no API calls). Uses 8
Treasury constant-maturity series (1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y), a
dense enough grid for the classical Level / Slope / Curvature pattern to
emerge clearly.

**Book Reference**: Chapter 14, Section 14.4 (Decoding the yield curve)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## 1. Setup and Imports
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## 2. Data Loading: Treasury Yields from FRED Parquet

We load eight Treasury constant-maturity yields (DGS1 through DGS30) from the
canonical FRED macro parquet. This is the densest grid available from FRED's
constant-maturity series and spans the yield curve from the front end (1Y)
to the long end (30Y) in eight points.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0009-p000

~~~~~~markdown
## 3. Yield Curve Visualization

Sample yield curves at different dates show how the term structure has
evolved over the sample period, from the post-dot-com era to today's
higher-rate regime.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
## 4. Yield Changes for PCA

PCA is typically applied to yield *changes* rather than levels, as changes
are more stationary and capture the dynamics we want to model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0015-p000

~~~~~~markdown
We standardize yield changes before PCA (correlation-matrix PCA). This
equalizes the influence of each maturity regardless of its volatility level.
Some practitioners apply PCA to the covariance matrix directly when
maturity-level variance differences are economically meaningful, for example,
to let the volatile short end dominate the first component. With standardization,
each maturity contributes equally to the factor structure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 5. PCA on Yield Changes

PCA decomposes yield changes into orthogonal factors:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is a standardized yield change, [[ML4T_A3_0003]] is a principal
component score, and [[ML4T_A3_0004]] is its correlation-PCA loading. Section 10
converts the fitted moves back to basis points before applying key-rate DV01s.
With eight maturities, we expect the first three components to reproduce the
classical Litterman–Scheinkman (1991) Level / Slope / Curvature pattern.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
An eigenvector's sign is arbitrary - [[ML4T_A3_0001]] and [[ML4T_A3_0002]] describe the same direction - so the
signs below are fixed to make each component's name mean what it says: all-positive
loadings for Level, so the component is a parallel shift up; long-end positive and
short-end negative for Slope, so a positive score is a steepening; and a positive
middle for Curvature, so a positive score lifts the belly against the wings. Without
this, half the runs would name a flattening a steepening.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
**Interpretation**: PC1 explains the bulk of the variance, PC2 captures a
steepening/flattening dimension orthogonal to it, and PC3 captures a
middle-vs-ends curvature twist. Together the three components account for
essentially all of the daily-change variance, confirming the classical
Litterman–Scheinkman finding that the yield curve is effectively
three-dimensional. The loadings below establish the economic interpretation
of each factor.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
### Moving-block stability check

A single full-sample PCA does not show whether the economic labels are stable.
We resample contiguous 21-observation blocks, refit the scaler and PCA inside
each bootstrap sample, and align all components to the full-sample basis by
permutation and sign. The intervals quantify sampling variation in the loading
curves while respecting short-run dependence in yield changes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
The circular index sampler joins randomly selected contiguous blocks until it
reaches the original sample length. Circular wrapping avoids giving the sample
endpoints special treatment.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
Bootstrap components may change sign or order without changing their economic
content. A one-to-one Hungarian assignment aligns the complete orthonormal basis
to the reference before intervals are computed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0031-p000

~~~~~~markdown
## 6. Factor Loadings (Figure 14.4)

The loadings reveal how each factor distributes across maturities. With a
dense maturity grid spanning 1Y to 30Y, the classical Level / Slope / Curvature
pattern emerges in the first three components.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>
