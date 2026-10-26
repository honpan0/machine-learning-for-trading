# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/04_ipca.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Asset returns → 資產報酬率
- Factor → 因子
- Hyperparameter → 超參數
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Instrumented PCA: Conditional Betas and Factor Forecasts

**Docker image**: [[ML4T_A3_0001]]

**Chapter 14: Latent Factor Models**

Instrumented PCA (IPCA) makes an asset's factor loadings linear functions of
characteristics observed before the return:

[[ML4T_A3_0002]]

This notebook uses a synthetic panel with known [[ML4T_A3_0003]] for two separate
checks. First, it verifies that alternating least squares (ALS) recovers the
loading *subspace*. Second, it passes the estimated factors through the
chapter's three-stage forecasting adapter without assuming that the factors
are predictable.

**Learning objectives**

- implement the two ALS updates for IPCA;
- evaluate recovery with rotation-invariant subspace diagnostics;
- map genuinely walk-forward factor forecasts back to asset returns; and
- report forecast uncertainty and sensitivity to the factor count.

**Evaluation contract**: the synthetic characteristics at [[ML4T_A3_0004]] generate only
[[ML4T_A3_0005]]. The structural model uses 349 training pairs, followed by a
one-period embargo and 150 evaluation pairs. The evaluation window is a
teaching demonstration: it is neither a holdout kept untouched for a final
measurement nor a set used to choose between models.

**Prerequisite**: [[[ML4T_A3_0006]]](01_pca_equity_sectors.ipynb)

**Book section**: Section 14.5, "Bridging economics and statistics with advanced models"

**Next**: [[[ML4T_A3_0007]]](05_rp_pca.ipynb) changes the Stage 1 objective to
emphasize priced variation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
The adapter keeps three responsibilities separate. IPCA estimates the
conditional loadings and realized factor history in Stage 1. Stage 2 uses
only factor realizations available at each decision. Stage 3 combines the
current characteristics with the fixed, train-only loading map.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Alternating least squares

For fixed [[ML4T_A3_0001]], each date is a small cross-sectional least-squares
problem for [[ML4T_A3_0002]]. A small ridge term protects the solve when the
conditional beta matrix is nearly singular.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
For fixed factors, stack the characteristic-factor interactions into one
pooled regression. The coefficient vector reshapes directly into [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
IPCA is unchanged by invertible rotations of [[ML4T_A3_0001]] and the factors.
Orthonormalizing the loading map and ordering directions by factor variance
chooses a stable representation without changing fitted returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The initializer applies PCA to characteristic-managed returns. ALS then
alternates the two closed-form updates until both objects stabilize.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 3. A timing-correct synthetic panel

Characteristics follow persistent AR(1) processes and are standardized
within each cross-section. The return paired with [[ML4T_A3_0001]] is generated from
the independent factor shock at [[ML4T_A3_0002]], exactly matching the model equation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
## 4. Stage 1: recover the loading subspace

Individual columns of [[ML4T_A3_0001]] are not identified: rotations and sign flips
leave fitted returns unchanged. Principal-angle cosines and the distance
between projection matrices therefore test the estimable object.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
Both panels below use the same color scale. Similar vertical patterns after
orthogonal alignment indicate recovery of the loading subspace, not recovery
of arbitrarily labeled columns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## 5. Stage 2: one-step factor forecasts

Each forecast is computed before the matching evaluation factor is appended
to history. The embargo-period return is observable at the first evaluation
decision, so it updates the factor history but never enters the Stage 1 fit.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0028-p000

~~~~~~markdown
## 6. Stage 3: asset forecasts and uncertainty

The mapper uses only current characteristics and the train-only [[ML4T_A3_0001]].
Forecast [[ML4T_A3_0002]] uses the economically neutral zero-return forecast as its
denominator. Cross-sectional IC uncertainty uses a Newey-West standard error;
the displayed interval is not an independence-based shortcut.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0033-p000

~~~~~~markdown
The zero-return benchmark is deliberately hard to beat when latent premia
are independent draws with mean zero. The IC intervals show whether any
apparent cross-sectional ordering is larger than the time-series uncertainty
around it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
## 7. Factor-count sensitivity

This is a sensitivity analysis, not hyperparameter selection. Every value of
[[ML4T_A3_0001]] is fit on the same training panel and evaluated with the expanding-mean
forecaster. The evaluation window never chooses the reported factor count.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>
