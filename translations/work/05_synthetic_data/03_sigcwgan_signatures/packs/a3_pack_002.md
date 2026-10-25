# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/03_sigcwgan_signatures.ipynb；A3 Pack 002；單元 14 個。


## 待翻譯英文單元

### c0014-p000

~~~~~~markdown
## Data Integrity and TSTR Methodology

**Critical**: This notebook implements a proper train/holdout split to enable
unbiased Train-Synthetic-Test-Real (TSTR) evaluation.

### Normalization: Preserving Sign (CRITICAL)

**IMPORTANT**: We use z-score normalization (mean 0, std 1), NOT MinMax to [0,1].

Why? The path signature uses cumulative sums. If returns are mapped to [0,1],
every coordinate becomes monotonically increasing - the path can only "go up".
This destroys the sign structure of returns, which is essential for meaningful
financial paths and signatures.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
## 1. Load Financial Data

**PAPER-EXACT DATA SOURCE**: S&P 500 index daily close prices

The paper uses the Oxford MAN Realized Library which provided S&P 500 index
prices (now defunct). We use bundled S&P 500 data which is equivalent.

**Key difference from previous implementation**:
- **Before**: ETF percent returns (SPY, QQQ)
- **Now**: S&P 500 index LOG returns (single asset, paper-exact)
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 2. Path Augmentation and Signature Computation

Raw return paths need **augmentation** before signature computation.

**PAPER PIPELINE** (configs/STOCKS/SigWGAN.json):
1. **Scale(2, dim=0)**: Scale first dimension by 2
2. **AddTime**: Prepend time coordinate [0,1]
3. **LeadLag**: Lead-lag transform for quadratic variation
4. **VisiTrans("I")**: I-visibility transform (adds 2 rows + 1 column)

**CRITICAL**: Our previous implementation used cumsum_concat + lag_added,
which is NOT what the paper uses. The paper's augmentations are specifically
designed for their signature-based loss.

The signature depth of 4 with these augmentations matches the paper methodology.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
### Lead-Lag Transform

The lead-lag transform recovers quadratic variation from discrete observations
by doubling the path with offset copies. This is critical because discrete
sampling loses continuous-path information that signatures need.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
### Visibility Transform

The I-visibility transform adds boundary rows and a visibility marker column,
ensuring signature terms handle path initialization correctly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0025-p000

~~~~~~markdown
### Paper Augmentation Pipeline

The full pipeline from [[ML4T_A3_0001]]:
Scale(2, dim=0) → AddTime → LeadLag → VisiTrans("I").
This specific ordering is critical for reproducing paper results.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
### Signature Dimension Helpers

Path and signature dimensions scale exponentially with augmentation count
and signature depth. These helpers compute exact sizes for verification.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0030-p000

~~~~~~markdown
### Factorial-Normalized Signatures

Without normalization, signature level [[ML4T_A3_0001]] has magnitude [[ML4T_A3_0002]], making
higher levels invisible to the loss. The paper multiplies each level
by [[ML4T_A3_0003]] to bring all levels to comparable scale.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
### Augment and Compute Signature

Convenience function combining the full augmentation pipeline with
factorial-normalized signature computation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
### Verify Augmentation Pipeline

Confirm dimension calculations match actual signature output.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
## 3. Create Training Dataset

**Paper Approach**: The paper trains on UNCONDITIONAL generation - matching
the distribution of full paths, not conditional on past.

We create rolling windows of length [[ML4T_A3_0001]] for signature computation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
## 4. Compute Expected Signature of Real Data

**Paper Approach (UNCONDITIONAL)**: The Sig-W1 metric compares expected signatures:

[[ML4T_A3_0001]]

We precompute the expected signature of the REAL training data. During training,
we minimize the distance between generated and real expected signatures.

**FACTORIAL NORMALIZATION**: The paper multiplies level k signature terms by k!
to rescale them to comparable magnitudes (higher levels have smaller raw values).
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
## 5. Generator Architecture (PAPER: LSTMGenerator)

**CRITICAL FIX**: The paper uses an **LSTMGenerator** with **Brownian motion noise**,
NOT an AR-FNN with independent Gaussian noise.

The generator draws Gaussian increments scaled by [[ML4T_A3_0001]], takes their
cumulative sum to form a Brownian path, runs that through an LSTM, and projects the
result linearly to the output dimension.

The Brownian motion noise is KEY - it provides smooth, continuous input paths
to the LSTM, which then transforms them into realistic output paths.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0041-p000

~~~~~~markdown
### Residual Feedforward Network

Helper network for initializing LSTM hidden states from noise input.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>
