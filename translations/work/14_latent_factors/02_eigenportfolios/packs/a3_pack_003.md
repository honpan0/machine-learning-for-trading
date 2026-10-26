# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/02_eigenportfolios.ipynb；A3 Pack 003；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Label → 標籤
- Out-of-sample → 樣本外
- Volatility → 波動率
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0049-p000

~~~~~~markdown
**Interpretation**: Slopes near zero indicate little one-day residual persistence in this
seeded sample. Negative slopes do not admit the positive-[[ML4T_A3_0001]] OU half-life formula. The
full-sample fit, random stock choice, and absence of cost-aware out-of-sample evaluation rule
out a trading conclusion.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0050-p000

~~~~~~markdown
## 14. Risk Decomposition

Any portfolio's total risk can be decomposed into exposures (betas) to the orthogonal
eigenportfolios. This provides a data-driven view of underlying risk drivers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0052-p000

~~~~~~markdown
**Finding**: The market factor (PC1) dominates portfolio risk, explaining
the largest share of total variance for this seeded portfolio. This is an in-sample
attribution, not a universal 80-90% range or a hedge recommendation. The residual is variation
not spanned by the first five fitted components.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0053-p000

~~~~~~markdown
## 15. Eigenvector Stability: Cosine Similarity and Procrustes Rotation

Rolling PCA loadings can "flip" between adjacent windows when eigenvalues are
close in magnitude, a mathematical pathology rather than a structural change. This
creates phantom turnover in downstream allocation. We diagnose this with cosine
similarity, then fix it with Procrustes rotation (Section 14.3).
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0056-p000

~~~~~~markdown
**Finding**: The signed diagnostic separates arbitrary sign reversals from genuine loading
instability. The absolute diagnostic treats [[ML4T_A3_0001]] and [[ML4T_A3_0002]] as equivalent; values below 0.8 then
flag rotations or component swaps that a sign correction alone cannot repair.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0057-p000

~~~~~~markdown
### Aligning each window's basis to the one before it

Procrustes rotation removes the coordinate ambiguity. Each [[ML4T_A3_0001]] has
shape (K, N), components by assets, so the factor basis is its transpose [[ML4T_A3_0002]] with
shape (N, K). Alignment in factor space solves

[[ML4T_A3_0003]]

whose closed-form solution is [[ML4T_A3_0004]] from the SVD of [[ML4T_A3_0005]]. Note the
shape of [[ML4T_A3_0006]]: it is [[ML4T_A3_0007]], a rotation within the K-dimensional factor space, not
an [[ML4T_A3_0008]] rotation of the assets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0060-p000

~~~~~~markdown
**Reading the figure**: The Procrustes rotation is a [[ML4T_A3_0001]] orthogonal transform in
factor space, not an [[ML4T_A3_0002]] asset-space rotation. Adjacent alignment removes arbitrary
signs and rotations inside the retained subspace. It does not prove that named PCs are stable,
nor does it by itself define production portfolio weights. A downstream covariance model must
rotate scores and factor covariance consistently and still monitor subspace drift.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0061-p000

~~~~~~markdown
## 16. Two-Stage Production PCA

Production risk models separate two dynamics: volatility changes quickly (days),
while correlation structure changes slowly (months). The two-stage procedure from
Paleologo (2025, Ch. 7) handles this separation. Stage 1 captures short-term
volatility; Stage 2 estimates the stable correlation factor structure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0066-p000

~~~~~~markdown
**Finding**: The as-of-end-date estimate separates fast residual volatility from a slowly
weighted factor structure, retains eigenvalue excess above a BBP-informed noise edge, and places
the remaining variance on the diagonal. Its condition number differs from the uniform sample
covariance. That numerical diagnostic does not establish better realized portfolio risk; a
point-in-time walk-forward comparison belongs in Chapter 17.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0067-p000

~~~~~~markdown
## Key Takeaways

1. **The first eigenportfolio is a market mode, and the correlation printed above says
   how closely.** It is a description of covariance, not a CAPM beta and not a claim
   that the direction is priced; neither is tested here.
2. **Which contrast lands on which component is a property of the sample.** The
   components are ordered by variance, so a contrast that happens to be large in this
   universe and period outranks one that is not, and the heatmap above is where to
   check what each column actually holds before naming it. On this panel the
   conventional defensive-versus-cyclical rotation does not appear where a reader
   might expect it (Utilities, Staples, Healthcare positive against Financials, Energy,
   Materials negative). The labeling depends on which common drivers dominate after the
   market is removed
3. **HPCA improves labeling**: two-step hierarchical PCA exposes named sector contrasts, while
   the full-sample ETF-correlation labels remain proxies rather than point-in-time GICS data
4. **Eigenvector stability**: signed cosine reveals arbitrary reversals; absolute cosine reveals
   rotations and swaps. Adjacent-window [[ML4T_A3_0001]] Procrustes alignment removes coordinate
   ambiguity, but downstream use must rotate scores and factor covariance consistently
5. **Two-speed covariance estimation**: fast residual volatility and slow normalized covariance
   can be combined with a BBP-informed noise threshold. Better conditioning alone is not evidence
   of better out-of-sample portfolio risk
6. **Risk decomposition**: PC1 is the largest variance component for the seeded 20-stock example,
   but its fitted share is sample- and portfolio-specific

### Stage 1 Outputs Feed Stage 2
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p000>>>
<<<ML4T-ZH-END:c0067-p000>>>

### c0067-p001

~~~~~~markdown

The full-sample PCA, HPCA, residual, and risk sections are descriptive Stage 1 analyses. The
final as-of-end-date covariance example is a risk-estimation adapter, still not a return forecast.
The two-step framework (Figure 14.9) treats fitted factors and loadings as inputs to a Stage 2
forecaster that predicts factor premia, then a Stage 3 mapper that turns the forecast back into
per-asset signals. PCA plus the simplest Stage 2 (sample mean) reduces to per-asset historical
mean, useful as a baseline but not a meaningful forecaster. The next-tier Stage 2 forecasters (AR(1),
EWMA, ML) are demonstrated in [[[ML4T_A3_0001]]](04_ipca.ipynb).

**Next Steps**:
- For Stage 1 + 2 + 3 end-to-end with characteristic-driven loadings, see [[[ML4T_A3_0002]]](04_ipca.ipynb)
- For IPCA and CAE on firm characteristics, see [[[ML4T_A3_0003]]](../case_studies/us_firm_characteristics/08_latent_factors.ipynb)
- For cross-asset PCA on futures, see [[[ML4T_A3_0004]]](../case_studies/cme_futures/10_latent_factors.ipynb)
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p001>>>
<<<ML4T-ZH-END:c0067-p001>>>
