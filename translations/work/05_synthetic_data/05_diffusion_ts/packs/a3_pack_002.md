# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/05_diffusion_ts.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Cluster → 群集
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0023-p000

~~~~~~markdown
## 3. Interpretable Decomposition

The key innovation of Diffusion-TS: each decoder layer extracts **trend**
and **seasonal** components from its intermediate representation.

- **TrendBlock**: Learns a polynomial basis (degree 3) via 1D convolutions,
  then multiplies by a polynomial space [[ML4T_A3_0001]] to produce a smooth trend.
- **FourierLayer**: Computes the DFT of the latent, selects top-[[ML4T_A3_0002]] frequencies
  by magnitude, then reconstructs via inverse DFT. This extracts dominant
  periodic patterns without assuming a fixed period.

Across decoder layers, trend and seasonal residuals accumulate, building up
the full decomposition progressively.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
### FourierLayer: Top-k Frequency Selection

Rather than using all Fourier coefficients, the layer selects the top-[[ML4T_A3_0001]]
frequencies (by magnitude) and reconstructs only those. This acts as a
learned bandpass filter that adapts to the data's spectral content.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## 4. Transformer Architecture

The encoder-decoder Transformer processes noised sequences. The **encoder**
creates a contextual representation conditioned on the diffusion timestep.
The **decoder** cross-attends to the encoder output and, at each layer,
extracts trend and seasonal residuals that accumulate across layers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
### Cross-Attention

The decoder cross-attends to the encoder's output. Queries come from the
decoder, while keys and values come from the encoder -- this lets each
decoder position gather relevant context from the full encoded sequence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
### Encoder and Decoder Blocks

Each encoder block applies adaptive layer norm → self-attention → FFN.
Each decoder block adds cross-attention to the encoder output, then
splits the representation into two branches: one for trend extraction
(polynomial regression) and one for seasonal extraction (Fourier layer).
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0036-p000

~~~~~~markdown
### Full Transformer

The Transformer wraps encoder and decoder with input/output projections.
The forward pass returns two tensors whose sum is [[ML4T_A3_0001]]: [[ML4T_A3_0002]], which is the
trend accumulated across decoder layers plus the residual's mean, and [[ML4T_A3_0003]],
which is the seasonal component projected back to feature space plus the residual with
that mean removed. Splitting the residual this way keeps the trend term carrying the
level and the seasonal term carrying the variation around it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
## 5. Diffusion Process

The [[ML4T_A3_0001]] class implements the full DDPM framework with [[ML4T_A3_0002]]
prediction. Key methods:
- [[ML4T_A3_0003]]: Forward process -- add noise to clean data
- [[ML4T_A3_0004]]: Get model's [[ML4T_A3_0005]] and derived noise
- [[ML4T_A3_0006]]: Compute posterior [[ML4T_A3_0007]] -- **no clamp**
- the training loss, internally: L1 in the time domain plus a Fourier term in the
  frequency domain
- [[ML4T_A3_0008]]: DDIM-style accelerated sampling

**Critical adaptation**: We remove [[ML4T_A3_0009]] from [[ML4T_A3_0010]]
and [[ML4T_A3_0011]]. Financial returns are StandardScaler-normalized
but unbounded -- clamping would truncate the distribution tails.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0041-p000

~~~~~~markdown
## 6. Exponential Moving Average

EMA maintains a shadow copy of model weights that is updated as a running
average: [[ML4T_A3_0001]].
Sampling from the EMA model produces smoother, higher-quality outputs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
## 7. Training

Training follows the standard diffusion objective: sample a timestep [[ML4T_A3_0001]],
add noise to create [[ML4T_A3_0002]], predict [[ML4T_A3_0003]], and minimize the combined
time-domain + Fourier loss. We use gradient clipping, warmup scheduler,
gradient accumulation, and EMA for stable convergence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0046-p000

~~~~~~markdown
### Checkpoint Loading

If a trained model exists and [[ML4T_A3_0001]], we skip training and load
the saved weights. This allows iterating on evaluation/visualization
without retraining.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0049-p000

~~~~~~markdown
### Training (or Loading from Checkpoint)
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0053-p000

~~~~~~markdown
### Training Progress
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0055-p000

~~~~~~markdown
## 8. Generate Synthetic Sequences

We sample from the EMA model using DDIM fast sampling (50 steps instead
of 500). The samples are generated in normalized space and then
denormalized back to original return scale.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
## 9. Unconditional Evaluation

We evaluate the generated data on three axes:

### Statistical Tests

- **Kolmogorov-Smirnov (KS) test**: Measures the maximum distance between
  two empirical CDFs. Values range from 0 for identical distributions to 1 for
  completely separated ones, so a small value indicates a close marginal fit.

- **Correlation error**: Mean absolute difference between real and synthetic
  cross-asset correlation matrices. Captures whether the model learned
  dependence structure (e.g., sector correlations).

- **Autocorrelation error**: Compares lag-1 autocorrelation. Returns have
  near-zero AC (weak form efficiency) but volatility clusters (squared returns
  have positive AC). Good generators preserve these stylized facts.

### Visual Comparison

- **PCA/t-SNE**: Project high-dimensional sequences to 2D. Real and synthetic
  distributions should overlap if the generator captures the data manifold.

### Utility (TSTR)

- **Train-Synthetic-Test-Real**: Train a classifier on synthetic data, test
  on real data. High accuracy means synthetic data is useful for downstream
  ML tasks -- the ultimate practical validation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>
