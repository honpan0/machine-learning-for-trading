# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/05_diffusion_ts.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Diffusion-TS: Interpretable Diffusion with Conditional Generation

**Chapter 5: Synthetic Data Generation**
**Section Reference**: Section 5.6 (Diffusion models for financial time series)

**Docker image**: [[ML4T_A3_0001]]

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 05_synthetic_data/05_diffusion_ts.py
> ```


## Purpose

This notebook implements **Diffusion-TS** (Yuan & Qiao, ICLR 2024), a diffusion
model that decomposes the denoising prediction into **trend** (polynomial regression)
and **seasonal** (Fourier basis) components. This interpretable structure encourages
the model to separate slow drift from periodic patterns, analogous to classical STL
decomposition but learned end-to-end within the diffusion framework.

Unlike vanilla diffusion models that predict noise [[ML4T_A3_0002]], Diffusion-TS
predicts [[ML4T_A3_0003]] directly. The Fourier-domain loss further regularizes spectral
fidelity -- critical for preserving autocorrelation structure in financial returns.

## Learning Objectives

By completing this notebook, you will:
- Implement a diffusion model with **interpretable trend+seasonal decomposition**
- Train with a combined **time-domain + Fourier-domain** loss
- Use **DDIM** fast sampling to reduce generation from 500 to 50 reverse steps
- Build a **regime classifier** on noised data and apply **classifier guidance**
  to generate regime-conditional synthetic returns
- Evaluate unconditional and conditional generation quality

## Cross-References
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- **Upstream**: ETF Universe loader ([[ML4T_A3_0001]])
- **Downstream**: Regime-conditioned synthetic data for stress testing (Ch 20)
- **Book**: Section 5.6 discusses diffusion and conditional generation
- **Related**: [[[ML4T_A3_0002]]](02_tailgan_tail_risk.ipynb) (GAN), [[[ML4T_A3_0003]]](03_sigcwgan_signatures.ipynb) (GAN)

---

## From GANs to Interpretable Diffusion

GANs face training instability, mode collapse, and limited interpretability.
Diffusion models solve the first two by replacing adversarial training with a
simple regression objective. Diffusion-TS goes further by decomposing the
denoising network's output into components with known semantics:

[[ML4T_A3_0004]]

where [[ML4T_A3_0005]] is the latent representation at diffusion step [[ML4T_A3_0006]]. The trend block
uses polynomial regression, the seasonal block selects top-[[ML4T_A3_0007]] Fourier modes,
and the residual captures everything else. This makes the model's behavior
inspectable -- you can visualize what the model attributes to drift versus
cyclical patterns.

## References

- **Paper**: Yuan, X. & Qiao, Y. (2024). "Diffusion-TS: Interpretable Diffusion
  for General Time Series Generation." ICLR 2024.
- **Code**: [[ML4T_A3_0008]]

## Key Adaptation Decisions
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

1. **No clamp(-1, 1)**: The original code clamps predicted [[ML4T_A3_0001]] to [-1, 1] for
   image-like data. Financial returns are StandardScaler-normalized (unbounded),
   so we remove the clamp entirely.
2. **Predict [[ML4T_A3_0002]]** (not noise): The model outputs [[ML4T_A3_0003]], then derives noise analytically. This pairs naturally with the
   decomposition.
3. **Fourier loss preserved**: The frequency-domain regularizer matches spectral
   properties -- essential for autocorrelation fidelity in returns.
4. **Classifier guidance**: A separate Transformer classifier trained on noised
   sequences enables regime-conditional generation at sampling time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0002-p000

~~~~~~markdown
## Diffusion Process Overview

Diffusion models work by gradually adding noise (forward process) and then
learning to reverse it (denoising). Diffusion-TS adds interpretable
trend+seasonal decomposition to the denoiser.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## Configuration

The original Diffusion-TS paper uses seq_length=24, 6 stocks, and 10,000 epochs.
We adapt for financial applications with the following considerations:

| Parameter | Paper | Ours | Rationale |
|-----------|-------|------|-----------|
| seq_length | 24 | 60 | ~3 months of trading context |
| feature_size | 6 | 20 | Balance diversity vs complexity |
| epochs | 10,000 | 10,000 | Match paper for convergence |
| lr | 1e-5→8e-4 | 1e-5→8e-4 | Warmup schedule from paper |

With 20 assets × 60 timesteps = 1,200 values per sample (vs paper's 144),
we train longer to capture the richer cross-asset structure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
Guidance is set per regime rather than globally. The minority high-volatility regime
needs *gentler* steering than the majority one, which is the opposite of the intuition
that a rarer target needs a harder push: classifier gradients toward a rare class are
strong enough to drive every sample to extreme volatility, collapsing the mode the
guidance was meant to reach. Its lower scale is paired with a higher temperature, which
buys back diversity, and a larger eta, which leaves more noise in each sampling step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
## 1. Data Loading and Preparation

We load daily ETF returns and create overlapping sequences. The temporal
train/holdout split at 2024-01-01 ensures unbiased TSTR evaluation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Create Overlapping Sequences

Sliding windows maximize sample count from limited financial data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0014-p000

~~~~~~markdown
## 2. Utility Modules

These building blocks support the Transformer architecture: sinusoidal
timestep embeddings, learnable positional encoding, and adaptive layer
normalization that conditions on the diffusion timestep.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
### Adaptive Layer Normalization

AdaLayerNorm modulates the normalized activations by a scale and shift
derived from the diffusion timestep embedding. This gives each Transformer
layer information about the current noise level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
### Learnable Positional Encoding and Conv Embedding

LearnablePositionalEncoding adds a learned position vector to each timestep.
Conv_MLP projects the input feature dimension to the model dimension using
a 1D convolution, which captures local patterns in the feature axis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
