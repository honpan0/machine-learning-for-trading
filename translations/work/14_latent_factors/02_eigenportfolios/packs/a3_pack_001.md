# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/02_eigenportfolios.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Eigenportfolios from US Equities

**Docker image**: [[ML4T_A3_0001]]

**Chapter 14: Latent Factors**
**Section Reference**: Section 14.3 (Eigenportfolios for Equity Strategies)

## Purpose
This notebook applies PCA to a liquid subset of the US Equities dataset to extract latent
risk factors and construct gross-normalized eigenportfolios. It demonstrates standard PCA,
sector loading analysis, hierarchical PCA (HPCA), residual diagnostics, risk decomposition,
loading stability, and an as-of-end-date two-speed covariance estimate.

## Where this fits in the framework

This notebook stays within **Stage 1** of the two-step latent-factor
framework (Figure 14.9). The PCA decomposition produces factors [[ML4T_A3_0002]]
(eigenportfolios) and loadings [[ML4T_A3_0003]] (factor exposures); these are the
Stage 1 outputs that downstream notebooks combine with Stage 2 forecasters
to produce return forecasts. Eigenportfolios are also natural risk-model
inputs in their own right; see the statistical arbitrage and risk
decomposition sections.

## Learning Objectives
- LO1: Apply PCA to large cross-sectional equity data and interpret variance decomposition
- LO2: Interpret eigenportfolios economically via sector loading analysis
- LO3: Implement Hierarchical PCA (HPCA) for improved factor interpretability
- LO4: Diagnose residual persistence and decompose portfolio risk without making a trading claim
- LO5: Separate sign ambiguity from subspace drift in rolling PCA

**Prerequisites**: Complete [[[ML4T_A3_0004]]](01_pca_equity_sectors.ipynb); requires US equities data.

## Cross-References
- **Upstream**: [[[ML4T_A3_0005]]](01_pca_equity_sectors.ipynb) (sector ETF PCA, bootstrap stability)
- **Downstream**: Chapter 18 (factor-based portfolio construction)
- **Related**: Section 9.5 (Regime features)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Data Source
US Equities (NASDAQ Data Link), with sector ETF returns used only for descriptive labels
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## 1. Setup and Imports
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## 2. Load US Equities Data

US Equities contains adjusted OHLCV for 3,199 stocks from 1962–2018.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## 3. Universe Selection: Top N by Dollar Volume

We select the most liquid stocks by average dollar volume over the declared sample. This is a
descriptive, full-sample universe definition. It must not be reused as a point-in-time trading
universe because later observations affect which stocks qualify.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## 4. Compute Returns and Create Return Matrix
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
**NaN handling**: Missing returns are filled with zero after a 90% coverage filter. This
attenuates covariance for stocks with gaps, so the printed missing-cell share is part of the
result. A production estimate should compare this convention with a complete-case or
missing-data covariance estimator.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
## 5. PCA: Extract Eigenportfolios
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Variance Decomposition
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
**Finding**: PC1 alone captures a substantial share of total variance as the dominant market
factor. The first 5 components together explain roughly half the cross-sectional variation,
with diminishing returns beyond PC5.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
## 6. Scree Plot
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 7. Eigenportfolio Loadings

The PCA eigenvectors define portfolio weights. Positive and negative loadings create
long-short factor portfolios.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
Each eigenvector defines portfolio weights. The [[ML4T_A3_0001]]-th eigenportfolio weight vector is:

[[ML4T_A3_0002]]

where [[ML4T_A3_0003]] is converted from standardized to raw-return space and [[ML4T_A3_0004]] fixes
gross exposure. L1 normalization does not make signed weights sum to one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
### PC1 (Market Factor): Top and Bottom Weights
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>
