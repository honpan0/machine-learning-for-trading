# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/03_sigcwgan_signatures.ipynb；A3 Pack 004；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Clustering → 分群
- Time series → 時間序列
- Volatility → 波動率
- Standard deviation → 標準差
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0073-p000

~~~~~~markdown
### Signature Analysis: Why Factorial Normalization Matters

Without factorial normalization, signature levels have vastly different scales:
- Level 1: O(1) magnitude
- Level 2: O(1/2!) magnitude
- Level 3: O(1/3!) magnitude
- Level 4: O(1/4!) magnitude

The paper multiplies each level by k! to bring them to comparable scales.
~~~~~~

<<<ML4T-ZH-BEGIN:c0073-p000>>>
<<<ML4T-ZH-END:c0073-p000>>>

### c0075-p000

~~~~~~markdown
## 11. Visualization: Real vs Synthetic Paths

Compare the distributional properties of real and synthetic paths.
~~~~~~

<<<ML4T-ZH-BEGIN:c0075-p000>>>
<<<ML4T-ZH-END:c0075-p000>>>

### c0078-p000

~~~~~~markdown
**Interpretation**: both sets stay symmetric about zero, so the generator has the
location right. What differs is the spread, on a shared vertical scale.

Read that as a property of these sixty windows rather than of the two
distributions. Thirty each is a thin sample, and the real windows overlap one
another, so they carry less independent information than thirty separate paths
would. The stylized-facts table below is the population comparison.

Serial dependence is the candidate explanation for a difference in cumulative
spread, because a sum over fifteen days depends on the covariance between returns
at every lag inside the window and not on the marginal alone. The table reports the
lag-1 autocorrelation of returns for both series: compare its two signs, keeping in
mind that lag one is one term of that sum rather than all of it.

The PCA panel earlier is a different projection of these same windows, not a
different quantity. It projects each flattened fifteen-day window, so a far-flung
point there is a window unusual in some combination of its days, which need not be
one extreme day. The kurtosis row of the table is the separate evidence about how
heavy the daily tails are.
~~~~~~

<<<ML4T-ZH-BEGIN:c0078-p000>>>
<<<ML4T-ZH-END:c0078-p000>>>

### c0079-p000

~~~~~~markdown
## 12. TSTR Evaluation: Train Synthetic, Test Real

TSTR (Train Synthetic, Test Real) measures whether a model trained on
synthetic data can predict real outcomes as well as a model trained on
real data.

For unconditional generation, we use a next-step prediction task.
~~~~~~

<<<ML4T-ZH-BEGIN:c0079-p000>>>
<<<ML4T-ZH-END:c0079-p000>>>

### c0082-p000

~~~~~~markdown
**Interpretation**: a TSTR ratio near one means a classifier trained on
synthetic data performs as well on real holdout data as one trained on actual
data. For return-sign prediction, which is close to a coin flip either way,
a ratio near one is expected even with moderate generation quality. The key diagnostic is
whether the synthetic-trained model significantly underperforms the
real-trained baseline.
~~~~~~

<<<ML4T-ZH-BEGIN:c0082-p000>>>
<<<ML4T-ZH-END:c0082-p000>>>

### c0083-p000

~~~~~~markdown
## 13. Summary Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0083-p000>>>
<<<ML4T-ZH-END:c0083-p000>>>

### c0085-p000

~~~~~~markdown
**Interpretation**: The left panel reports three distributional checks - the
signature-level Sig-W1 distance (scaled down by 10 for visual co-display), the
marginal Kolmogorov-Smirnov statistic, and the absolute mean-error between real
and synthetic samples. A near-zero Mean Error bar is good news (centred
generation), not a missing value - the bar is small because the generator has
learned the marginal location. The right panel reports TSTR: classifier
accuracy when trained on real vs synthetic. Utility is preserved when the two bars
sit at similar heights; a visible gap in favour of the real-trained classifier means
the synthetic data is missing discriminative structure. The TSTR ratio printed in the
evaluation cell is the same comparison as a single number.
~~~~~~

<<<ML4T-ZH-BEGIN:c0085-p000>>>
<<<ML4T-ZH-END:c0085-p000>>>

### c0086-p000

~~~~~~markdown
## 13b. Additional Evaluation Metrics

Beyond Sig-W1, we evaluate:
- Autocorrelation structure (ACF)
- Cross-asset correlation
- Stylized facts (kurtosis, skewness)
~~~~~~

<<<ML4T-ZH-BEGIN:c0086-p000>>>
<<<ML4T-ZH-END:c0086-p000>>>

### c0088-p000

~~~~~~markdown
**Interpretation**: The stylized facts (computed here as *excess* kurtosis, so
a Gaussian scores 0) are where the unconditional Sig-WGAN shows its limits. The
generator matches the marginal **mean and standard deviation** closely, while the
higher moments printed above move toward what a Gaussian would give: excess
kurtosis drops away from the real series' fat tails, the real returns' negative
skew (asymmetric crash risk) is not reproduced, and the lag-1 ACF of squared
returns - the fingerprint of volatility clustering - falls toward zero. Read the
table above for the sizes. This is the key teaching point of the notebook: matching low-order
expected signatures pins down location and scale, but on this single-asset,
depth-4 setup it does **not**, on its own, recover the higher-moment and
temporal-dependence structure of returns. Capturing volatility clustering and
fat tails is exactly what the conditional Sig-CWGAN and richer augmentations are
designed to improve.
~~~~~~

<<<ML4T-ZH-BEGIN:c0088-p000>>>
<<<ML4T-ZH-END:c0088-p000>>>

### c0089-p000

~~~~~~markdown
## 14. Save Outputs
~~~~~~

<<<ML4T-ZH-BEGIN:c0089-p000>>>
<<<ML4T-ZH-END:c0089-p000>>>

### c0094-p000

~~~~~~markdown
## Key Takeaways

**What Sig-WGAN Offers**:

1. **No Adversarial Training**: The "discriminator" is the expected signature,
   eliminating mode collapse and training instability

2. **Principled Distance**: Path signatures provide a mathematically rigorous
   way to compare time series distributions

3. **Factorial Normalization**: Rescales signature levels to comparable magnitudes,
   critical for stable training and meaningful loss values

**Following the paper** (Ni et al., Mathematical Finance 2024). Every numeric setting
below is declared in the [[ML4T_A3_0001]] cell near the top, which is the single place to
change them:

1. **Generator**: an LSTM driven by Brownian motion noise - Gaussian increments
   scaled by [[ML4T_A3_0002]], accumulated into a path

2. **Augmentations**: Scale → AddTime → LeadLag → VisiTrans("I"), applied in that
   order. VisiTrans changes the path's shape, which is why the dimension check
   earlier in the notebook prints both the expected and the actual signature size

3. **Factorial normalization**: level *k* terms are multiplied by *k*!, which brings
   the levels to comparable magnitudes; without it the higher ones are too small to
   influence the loss

4. **Loss**: the RMSE of the difference between expected signatures, an L2 norm
   rather than a squared error

**Paper-Exact Data Source**:

This implementation now uses the SAME data as the paper:
- S&P 500 index daily close prices (paper used Oxford MAN, now defunct)
- Log returns: [[ML4T_A3_0003]]
- Single asset (paper's [[ML4T_A3_0004]])
- Period: 2005-01-01 to 2020-06-01

**Paper reference values** (Ni et al., 2024, on S&P 500 log returns):
~~~~~~

<<<ML4T-ZH-BEGIN:c0094-p000>>>
<<<ML4T-ZH-END:c0094-p000>>>
