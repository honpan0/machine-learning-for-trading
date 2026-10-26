# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/02_eigenportfolios.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Transaction costs → 交易成本
- Label → 標籤
- Out-of-sample → 樣本外
- Clustering → 分群
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0024-p000

~~~~~~markdown
**Interpretation**: PC1 weights are predominantly positive, confirming its role as a broad
market mode. Their magnitude is a PCA portfolio weight, not CAPM beta; economic labels require
separate characteristics or a prespecified market regression.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
## 8. Sector Loading Heatmap (Figure 14.3)

To interpret eigenportfolios economically, we map stocks to approximate GICS sectors
using their correlations with sector ETFs. This data-driven approach avoids requiring
an external sector lookup table.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
### Map Stocks to Sectors via Correlation

We assign each stock to its highest-correlation sector ETF using overlapping
return dates, providing a data-driven sector classification.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
### Compute Mean Loadings by Sector
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
**Reading it**: take one column at a time and ask two questions. Do the sectors all
fall on the same side of zero, or does the column split them? A column with one sign
throughout is a common direction; a column that splits them is a contrast, and the
sectors at its two ends say what the contrast is between.

The first component is the common direction here, and the cells are printed so the
clustering is checkable rather than asserted. The later components are contrasts, and
which contrast lands on which component is not fixed - the components are ordered by
variance, so a contrast that happens to be large in this sample outranks one that is
not, and reading a familiar name onto a component number is the mistake this section
is guarding against. This ordering is universe- and period-specific:
on a 2006–2018 top-500 US equity panel, commodity exposure dominates PC2 because
Energy and Materials returns share a strong common driver outside the broad market.
Higher-order components capture progressively more nuanced sector tilts.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
## 9. Eigenportfolio Score Trajectories

Standardized PCA scores cannot be compounded as returns. Instead, we apply the
gross-normalized raw-return-space weights derived in Section 7 to each day's stock returns.
These are actual in-sample portfolio returns. Their signs remain conventional for PC2 onward,
and their paths are descriptive rather than out-of-sample performance estimates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
**Finding**: PC1 tracks the broad equity market because its raw-return-space weights are
predominantly positive. PC2 through PC5 are long-short portfolios whose paths depend on the
arbitrary component sign, so direction is not an economic forecast. For regime-switching models
applied to factor histories, see Section 9.4 (HMM).
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
## 10. Factor Characteristics
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
**Interpretation**: The gross-normalized portfolios are valid return series, but their gross
normalization differs by component, so their volatility ranking need not equal the standardized
score eigenvalue ranking. In-sample mean return or Sharpe is not a forecast. Risk premia require a
separately specified Stage 2 factor-premium forecast and a point-in-time evaluation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000

~~~~~~markdown
## 11. Market Factor Validation
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
The correlation printed above is the whole question for this section: it says how
closely the first eigenportfolio's return series and the equal-weight market's move
together. It is a measure of linear association and not a decomposition - it does not
split the eigenportfolio into a market part and a remainder, and squaring it would
give the shared variance share of a single-predictor regression, which is a different
quantity again. Read it before reading any interpretation of PC1 elsewhere in the
notebook.

Whatever it says, a PCA loading is a common-factor exposure and not a CAPM beta. Beta
is defined against a prespecified market portfolio and estimated by regression; this
is an eigenvector of a sample covariance matrix. Neither is a statement about whether
the exposure is priced.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
## 12. Hierarchical PCA (HPCA)

Standard PCA produces factors that maximize variance globally, but higher-order components
can be difficult to interpret economically. Avellaneda's (2019) Hierarchical PCA addresses
this by injecting known economic structure.

**Step 1**: PCA within each sector to identify the dominant factor for Technology stocks,
another for Financials, etc.

**Step 2**: PCA across sector-level factors to capture cross-sector dynamics.

> **HPCA ≠ HRP.** Hierarchical PCA (factor discovery) and Hierarchical Risk Parity
> (portfolio construction, Chapter 19) share a name but not a purpose.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0045-p000

~~~~~~markdown
**Reading it**: a row is one sector's first-stage factor and a column is one Step 2
component, so read down the columns. A column whose loadings all carry the same sign is
a direction the sectors move along together; a column carrying both signs sets one group
of sectors against another, and the cell values say which. What HPCA buys over plain PCA
here is the naming: the rows are named sectors rather than anonymous stocks, so an
opposition can be read off the chart instead of inferred from the constituents.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0046-p000

~~~~~~markdown
## 13. Statistical Arbitrage: Residual Analysis

Regressing individual stock returns on the top-K eigenportfolios isolates residuals
hypothesized to mean-revert. We estimate the Ornstein-Uhlenbeck half-life:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is the AR(1) slope. A positive [[ML4T_A3_0003]] maps to an OU-style half-life;
negative slopes imply alternating signs and are reported without an OU half-life.

**Caveat**: mean-reversion parameters are unstable
out-of-sample and transaction costs typically dominate any theoretical edge.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>
