# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/01_timegan.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# TimeGAN: Time-series Generative Adversarial Networks

**Docker image**: [[ML4T_A3_0001]]

**Book Reference**: Chapter 5, Section 5.5 (GANs for financial time series)

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 05_synthetic_data/01_timegan.py
> ```


This notebook implements **TimeGAN** (Yoon, Jarrett & van der Schaar, NeurIPS 2019),
the foundational architecture for synthetic financial time series generation.

## Learning Objectives

- Understand TimeGAN's five-component architecture and why latent-space training matters
- Implement the three-phase training approach (embedding → supervisor → joint GAN)
- Evaluate synthetic data using the Fidelity-Utility-Privacy framework
- Apply Train-Synthetic-Test-Real (TSTR) validation with proper temporal splits

## Why TimeGAN Matters

TimeGAN introduced two key innovations that address limitations of standard GANs:

1. **Stepwise Supervised Loss**: Standard GANs only learn the overall distribution.
   TimeGAN adds explicit supervision on temporal transitions (how t → t+1).

2. **Learned Embedding Space**: Instead of operating directly on raw data, TimeGAN
   learns a latent representation where adversarial training is more stable.

TimeGAN remains a common baseline against which newer methods are compared.

## Data Format

We use six stocks (BA, CAT, DIS, GE, IBM, KO) and model their **daily log
returns**. The multi-stock panel exposes the model to a wider distribution of
volatility and trend regimes than single-stock OHLCV.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

The choice of returns over price levels is forced by the evaluation, not a
stylistic preference. Every module here ends in a sigmoid, so the generator can
only emit values in [[ML4T_A3_0001]], and the inputs are min-max scaled to that range
using statistics fitted on the training period. Price levels trend, so a later
holdout period leaves the range the scaler was fitted on. A TSTR score computed
against such a holdout is then measuring predictive utility across a severe
shift in support — the synthetic training data cannot go above one, most of the
holdout targets do — which confounds any reading of it as a statement about
temporal fidelity. Log returns are stationary enough that the holdout stays
inside the fitted range, removing the confound. Both halves of that are
measured below rather than asserted.

## References

- **Paper**: Yoon, J., Jarrett, D., & van der Schaar, M. (2019).
  "Time-series Generative Adversarial Networks." NeurIPS 2019.
- **Official Code**: [[ML4T_A3_0002]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0005-p000

~~~~~~markdown
## TimeGAN Architecture

TimeGAN consists of five interconnected modules that operate in a shared latent space:

| Module | Purpose | Training Phase |
|--------|---------|----------------|
| **Embedder** | Maps raw data → latent space | Phase 1 (autoencoder) |
| **Recovery** | Reconstructs latent → raw data | Phase 1 (autoencoder) |
| **Supervisor** | Predicts next latent step | Phase 2 (temporal) |
| **Generator** | Produces latent sequences from noise | Phase 3 (joint GAN) |
| **Discriminator** | Classifies real vs fake latent sequences | Phase 3 (joint GAN) |
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## 1. Load Data

Six stocks with different volatility and trend regimes, converted to daily log
returns. The returned array is one row shorter than the price panel, and its
timestamps are those of the *later* day of each return.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Why Not Price Levels

Before loading returns, measure what levels would have cost. Fit the same
min-max scaler on the same training fraction of the price panel, transform the
holdout, and count the cells the generator could never reach.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
### Temporal Train/Holdout Split

We split temporally to enable unbiased TSTR evaluation.
The generator never sees holdout data during training.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 2. Normalize and Create Sequences
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
The scaler is fitted on the training period only, so nothing about the holdout
reaches the model. That makes the holdout's scaled range a property of the
data rather than something the code can arrange, and it is the quantity the
choice of returns over levels turns on: every module ends in a sigmoid, so a
holdout cell outside [[ML4T_A3_0001]] names a value the generator cannot emit and the
TSTR comparison cannot fairly ask for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0019-p000

~~~~~~markdown
## 3. Model Components

We use ModuleList with separate GRU layers to match TensorFlow's layer-by-layer
construction exactly. This ensures consistent behavior with the official implementation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0025-p000

~~~~~~markdown
## 4. Initialize Models
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
### Reusing a Checkpoint

A checkpoint is only interchangeable with a fresh run if it was trained on the
same thing. The weights alone cannot say what they were fitted to, so the
config saved beside them is compared field by field and a mismatch retrains
instead of loading. Without that check a checkpoint trained on price levels
would load silently into this returns-based notebook and every number below
would describe a model fitted to a different target.

The comparison has to cover everything that moves the weights, not just what
describes the data. A seed, a batch size, a learning rate and the discriminator
gating threshold all produce different models from the same inputs, so all four
are compared too. A checkpoint written before they were is missing them, which
reads as a mismatch and retrains - the safe direction.

[[ML4T_A3_0001]] names the columns but not their contents, and the equity data is refreshed
outside this notebook. A refresh moves the training rows, which moves the scaler
fitted on them, and the run would then evaluate weights fitted under one
normalization on data scaled under another, and overwrite [[ML4T_A3_0002]] with the
second one. A digest of the training rows is what closes that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## Three-Phase Training

TimeGAN uses a sequential training approach with step-based iteration
(matching the official implementation):

1. **Embedding Phase**: Train Embedder + Recovery as autoencoder
2. **Supervisor Phase**: Train Supervisor to predict next latent step
3. **Joint Phase**: Train Generator + Discriminator adversarially
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
## 5. Phase 1: Embedding Training

Train Embedder + Recovery as autoencoder with loss: [[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## 6. Phase 2: Supervisor Training

Train Supervisor to predict next latent step: [[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>
