# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/01_pca_equity_sectors.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Backtesting → 回測
- Feature → 特徵
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# PCA on Sector ETFs with Bootstrap Loading Stability

**Docker image**: [[ML4T_A3_0001]]

**Chapter 14: Latent Factors**
**Section Reference**: See Section 14.2 for PCA theory and Section 14.3 for eigenportfolios

## Purpose
This notebook applies PCA to sector ETFs to extract latent risk factors and quantifies
loading stability using bootstrap resampling. We demonstrate how PCA captures market
and rotation factors, and how to assess whether factor loadings are statistically reliable.

## Where this fits in the framework

PCA is the simplest realisation of **Stage 1** in the two-step latent-factor
framework (Figure 14.9): it compresses an [[ML4T_A3_0002]] returns panel to
a [[ML4T_A3_0003]] factor history via SVD. This notebook focuses on the
Stage 1 outputs - variance decomposition, loadings, bootstrap stability -
and the structural interpretation of the principal components. The full
Stage 1 + 2 + 3 pipeline (with a Stage 2 forecaster turning factor history
into asset signals) is exercised in [[[ML4T_A3_0004]]](04_ipca.ipynb) and
[[[ML4T_A3_0005]]](05_rp_pca.ipynb).

## Learning Objectives
- LO1: Apply PCA to sector ETF returns and interpret variance decomposition
- LO2: Quantify loading stability with bootstrap confidence intervals
- LO3: Interpret sector factor exposures (market vs rotation)
- LO4: Analyze temporal stability of factor structure using rolling PCA

## Cross-References
- **Upstream**: Chapter 3 (ETF data loading)
- **Downstream**: Chapter 16 (factor investing), Chapter 18 (factor-based backtesting)
- **Related**: [[[ML4T_A3_0006]]](02_eigenportfolios.ipynb) (stock-level PCA), Section 9.5 (Regime features)

## Data Source
ETF Universe parquet (canonical data, no API calls)

**Prerequisites**: Requires ETF Universe data (see Chapter 3).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## 1. Setup and Imports
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## 2. Load Sector ETF Data

Load sector ETFs from the canonical ETF Universe parquet file.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
Daily return distributions reveal whether a few volatile sectors could dominate covariance-PCA.
The interquartile ranges and whiskers make the scale differences visible without a printed
[[ML4T_A3_0001]] table.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## 3. PCA on Sector Returns

We use **correlation-PCA** (standardized returns) rather than covariance-PCA. Standardizing
to unit variance prevents high-volatility sectors (e.g., Energy) from dominating the first
component. For cross-sectional equity analysis this is the standard choice - see the Scale
Sensitivity discussion in Section 14.2.

PCA decomposes the covariance matrix as:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] contains eigenvectors (loadings) and [[ML4T_A3_0003]] is the diagonal matrix of
eigenvalues.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Variance Decomposition

The fraction of total variance explained by component [[ML4T_A3_0001]] is:

[[ML4T_A3_0002]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Scree Plot

The scree plot (Figure 14.2 in the text) shows eigenvalues in descending order. The
"elbow" where explained variance levels off suggests how many components to retain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
**Reading it**: the height of the first bar against the rest is the question. One
component carrying most of the variance is what a market factor looks like in a
sector panel - the sectors move together, and how much they move together is the
first bar.

Where the cumulative line flattens, each further component is adding little to the
variance already accounted for, and the "elbow" is a retention heuristic built on
that. It is a heuristic and not a finding: a component explaining little variance can
still carry systematic structure, and variance explained says nothing about whether a
direction is priced or predictive. Nothing in this notebook tests either. The printed
shares above the chart are the numbers; the shape is what the figure is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
## 4. Loadings Interpretation

Each eigenvector defines a principal component as a linear combination of sector returns.
The loadings can be interpreted as portfolio weights.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
**Interpretation**: PC1 loadings are uniformly positive - the classic "market factor" where
all sectors move together. PC2 separates defensive sectors (positive loadings: Utilities,
Staples) from cyclical sectors (negative loadings: Energy, Financials, Discretionary),
capturing the sector rotation dimension.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## 5. Bootstrap Loading Stability

Are the loadings statistically reliable, or could they be estimation noise? We use a moving-block
bootstrap to construct 95% confidence intervals while preserving short-run return dependence.
The default [[ML4T_A3_0001]] is a teaching budget; increase it for final inference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
### Component Matching

PCA signs are arbitrary, and nearby eigenvalues can swap component order across resamples. We use
maximum absolute loading similarity to match each bootstrap component to the full-sample basis,
then align its sign.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
### Moving-Block Resamples

Twenty-day blocks retain local dependence while resampling the historical sequence. Each draw
concatenates random contiguous blocks until it reaches the original sample length.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
### Bootstrap Confidence Intervals

Each resample receives its own scaler and PCA fit. The component-matching step prevents a PC2/PC3
swap from being misread as loading uncertainty.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>
