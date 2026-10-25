# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/07_dp_gan.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Deep learning → 深度學習
- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Chapter 5: Differential Privacy for Generative Models

**Chapter 5: Synthetic Data Generation**
**Section Reference**: Section 5.8 (Applying the Fidelity-Utility-Privacy framework)

**Docker image**: [[ML4T_A3_0001]]

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 05_synthetic_data/07_dp_gan.py
> ```


## Purpose

This notebook demonstrates **Differential Privacy (DP)** for training generative models
using **Opacus**, PyTorch's official DP library. We train a GAN with formal privacy
guarantees that limit information leakage about individual records.

## Learning Objectives

By completing this notebook, you will:
- Understand the differential privacy framework and privacy budget (ε)
- Implement DP-SGD training using Opacus (proper per-sample gradients)
- Observe the privacy-utility tradeoff as ε varies
- Evaluate synthetic data quality under privacy constraints

## Cross-References

- **Upstream**: ETF Universe loader ([[ML4T_A3_0002]])
- **Book**: Section 5.8 discusses differential privacy in the FUP framework

---

## Key Concepts

1. **Differential Privacy**: Mathematical framework for privacy guarantees
2. **DP-SGD**: Per-sample gradient clipping + noise (NOT batch-level)
3. **Privacy Budget (ε)**: Trade-off between privacy and utility
4. **Privacy Accountant**: Tracks cumulative privacy cost during training

## Why Opacus?

A correct DP-SGD implementation requires:
- **Per-sample gradients**: Not available in standard PyTorch
- **Proper clipping**: Before aggregation, not after
- **Privacy accounting**: Accurate ε computation via moments accountant

Opacus handles all of this correctly. Manual implementations are error-prone.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## References

- Abadi et al. (2016). "Deep Learning with Differential Privacy"
- [Opacus Documentation]([[ML4T_A3_0001]])
- Yousefpour et al. (2021). "Opacus: User-Friendly Differential Privacy Library in PyTorch"
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0005-p000

~~~~~~markdown
## 1. Differential Privacy Background

A randomized algorithm [[ML4T_A3_0001]] is [[ML4T_A3_0002]]-differentially private
if for any two adjacent datasets [[ML4T_A3_0003]] and [[ML4T_A3_0004]] (differing by one record) and any output [[ML4T_A3_0005]]:

[[ML4T_A3_0006]]

- **ε (epsilon)**: Privacy budget. Lower = more privacy, less utility.
- **δ (delta)**: Probability of privacy breach. Should be << 1/n.

### Common ε Values

| ε Range | Privacy Level | Use Case |
|---------|---------------|----------|
| ε < 1 | Very Strong | Highly sensitive data (medical, financial PII) |
| 1 ≤ ε ≤ 10 | Moderate | Most production applications |
| ε > 10 | Weak | When utility is paramount |

### Why DP-SGD Requires Per-Sample Gradients

Standard gradient clipping clips the **sum** of gradients. This doesn't bound
the contribution of any individual sample. DP-SGD clips **each sample's gradient
independently**, then adds noise proportional to the clipping threshold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Load Real Financial Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 3. Engineer Features for GAN Training
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0011-p000

~~~~~~markdown
## 4. GAN Architecture (Opacus-Compatible)

Opacus has specific requirements for model architecture:
- No in-place operations
- Use [[ML4T_A3_0001]] instead of [[ML4T_A3_0002]] (BatchNorm breaks DP)
- Models must pass [[ML4T_A3_0003]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
### Generator

The generator maps random noise to synthetic feature vectors. It uses [[ML4T_A3_0001]] output
scaled to [-3, 3] to match our normalized data range. The generator does not need
DP modifications because it never sees real data directly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Discriminator (DP-Compatible)

The discriminator must be DP-compatible because it processes real data. The key
architectural constraint: **BatchNorm is replaced with GroupNorm**. BatchNorm computes
statistics across the batch, which leaks information about other samples and violates
the per-sample privacy guarantee. GroupNorm operates within each sample independently.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Initialize and Validate Models

Opacus provides [[ML4T_A3_0001]] to check whether a model is compatible with
DP-SGD and automatically fix common issues (e.g., replacing any remaining
BatchNorm layers).
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## 5. Train with DP-SGD using Opacus

Opacus wraps the model, optimizer, and dataloader to:
1. Compute per-sample gradients via [[ML4T_A3_0001]]
2. Clip each sample's gradient to [[ML4T_A3_0002]]
3. Add calibrated Gaussian noise
4. Track privacy budget via moments accountant

The Lipschitz constraint the WGAN objective needs is enforced by clipping the
discriminator's weights rather than by a gradient penalty. That is a privacy decision,
not a modelling preference: a gradient penalty differentiates through interpolations
between real and generated samples, which puts real records into a term Opacus is not
accounting for. Weight clipping touches only the parameters, so the privacy accounting
stays sound.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
### Run Training

Train the DP-GAN with the configured privacy budget. Opacus automatically
calibrates the noise multiplier to spend exactly the target epsilon over
the specified number of epochs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## 6. Generate Synthetic Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
### Choosing the rows to compare against

[[ML4T_A3_0001]] rows are consecutive trading days, so its first N rows are one stretch
of history rather than N draws from the period the generator was trained on. The
comparisons below read [[ML4T_A3_0002]] and the sweep reads [[ML4T_A3_0003]], both drawn at
random from all of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 7. Fidelity: Visual Comparison with PCA and t-SNE

We project both real and DP-synthetic data into 2D to assess whether the
generator covers the same regions of the data manifold despite privacy noise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
