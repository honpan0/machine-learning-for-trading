# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/03_sigcwgan_signatures.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Chapter 5: Sig-WGAN - Signature-Based Wasserstein GANs

**Chapter 5: Synthetic Data Generation**
**Section Reference**: Section 5.5 (GANs for financial time series)

**Docker image**: [[ML4T_A3_0001]]

> **Docker required**: This notebook uses [[ML4T_A3_0002]] and [[ML4T_A3_0003]], which are x86-only
> packages not included in the default environment. Run with:
> ```bash
> docker compose --profile py312 run --rm py312 python 05_synthetic_data/03_sigcwgan_signatures.py
> ```

## Purpose

This notebook implements the **unconditional Sig-Wasserstein GAN** — the core of
Sig-CWGAN (Ni et al., Mathematical Finance 2024) — which uses **path signatures**
as a principled distance metric for comparing time-series distributions. We build
and train the unconditional variant; the conditional extension P(future | past) is
explained conceptually but not implemented here.

## Learning Objectives

By completing this notebook, you will:
- Transform financial time series into path signatures using the [[ML4T_A3_0004]] library
- Implement an (unconditional) Sig-Wasserstein GAN that matches expected signatures
- Use the expected signature (Sig-W1) as the training objective instead of a
  trained discriminator
- **Understand how the conditional Sig-CWGAN extends this** with a Monte Carlo
  expected-signature objective (the key paper insight; the conditional path is
  described, not built, in this notebook)
- Evaluate generative fidelity using signature-based metrics and TSTR

## Cross-References

- **Upstream**: ETF Universe loader ([[ML4T_A3_0005]])
- **Downstream**: Conditional generation for scenario analysis
- **Book**: Section 5.5 discusses signature-based methods

---

## The Evolution from TimeGAN
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

TimeGAN (2019) introduced embedding spaces and stepwise supervision. But its
discriminator still uses a binary classifier to distinguish real/fake - which
doesn't provide a smooth gradient landscape for generator training.

Sig-CWGAN (2020→2024) introduces two innovations:

1. **Signature Distance**: Instead of a trained discriminator, use the
   **expected signature** to characterize time series distributions. The
   signature is a universal feature set that uniquely identifies probability
   measures on path space.

2. **Conditional W1 Metric** (the paper's full method): learn the conditional
   distribution P(future | past) rather than the unconditional law — more useful
   for finance (given what happened yesterday, what might happen tomorrow?). This
   notebook implements the unconditional Sig-W1 core; the conditional metric is
   described here but left as an extension.

## What Are Path Signatures?

The signature of a path is an infinite series of iterated integrals that
completely characterizes the path up to reparameterization:

[[ML4T_A3_0001]]

**Key Properties**:
- **Uniqueness**: The expected signature E[Sig(X)] uniquely determines
  the law of the stochastic process X (under mild conditions)
- **Universality**: Any continuous function of paths can be approximated
  by a linear function of the signature
- **Computability**: Truncated signatures are tractable to compute

## Architecture Overview

Sig-CWGAN consists of three main components:
1. **Path Augmentation**: Transform raw returns into signature-ready paths
2. **Signature Computation**: Compute truncated path signatures
3. **AR-FNN Generator**: Autoregressive feedforward network conditioned on past
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

See [[ML4T_A3_0001]] for the full architecture diagram.

**Key Insight**: The loss is on **expected signatures**, not single-sample signatures.
For each past, we generate m futures with different noise, compute their signatures,
and average before comparing to the target. This is the core Sig-CWGAN algorithm.

## References

- **Paper**: Ni, H., Szpruch, L., Wiese, M., Liao, S., & Xiao, B. (2024).
  "Sig-Wasserstein GANs for Conditional Time Series Generation."
  Mathematical Finance, 34(4), 1179-1227.
  [[ML4T_A3_0002]]
- **ArXiv (2020)**: [[ML4T_A3_0003]]
- **Code**: [[ML4T_A3_0004]]

---

## Paper-Exact Data Source

**This notebook now uses the EXACT same data as the paper**:
- **Source**: S&P 500 index daily close prices
- **Returns**: Log returns: [[ML4T_A3_0005]]
- **Period**: 2005-01-01 to 2020-06-01 (paper period)
- **Single asset**: Paper uses [[ML4T_A3_0006]] only (not multiple assets)

The original paper used Oxford MAN Realized Library (now defunct), which
provided the same S&P 500 index prices, loaded via [[ML4T_A3_0007]].

## WARNING: Signature Dimension Scaling

Signature dimension scales as O(d^depth) where d = feature count after augmentations.

| Assets | After Augmentations | Depth 4 Sig Dim | Feasibility |
|--------|---------------------|-----------------|-------------|
| 1      | 5 features          | 780 dims        | [OK] Fast      |
| 2      | 7 features          | 2,800 dims      | [OK] Feasible  |
| 5      | 13 features         | 30,940 dims     | WARNING: Slow     |
| 10     | 23 features         | 303,600 dims    | [FAIL] OOM       |
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0000-p003

~~~~~~markdown

**This notebook uses 1 asset (S&P 500) to match the paper exactly.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p003>>>
<<<ML4T-ZH-END:c0000-p003>>>

### c0002-p000

~~~~~~markdown
## Sig-CWGAN Architecture

The architecture uses path signatures as an analytic discriminator, replacing
trained neural networks with a mathematically principled distance metric.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0006-p000

~~~~~~markdown
Training needs path signatures that autograd can differentiate through. [[ML4T_A3_0001]]
provides GPU-accelerated differentiable signatures; it installs with
[[ML4T_A3_0002]], and torch must already be present.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0010-p000

~~~~~~markdown
### Configuration (Ni et al., Mathematical Finance 2024)

Following the original paper exactly:
- [[ML4T_A3_0001]] specifies the exact settings
- LSTMGenerator with Brownian motion noise input
- Augmentations: Scale(2, dim=0) &rarr; AddTime &rarr; LeadLag &rarr; VisiTrans("I")
- Factorial normalization on signature levels
- batch_size=2000, depth=4, lr=1e-3, n_gradient_steps=2500

**Data source**: S&P 500 index daily close prices (matching Oxford MAN source).
Paper uses log returns of close prices for a single asset (.SPX),
period 2005-01-01 to 2020-06-01.

Signature dimension scales as [[ML4T_A3_0002]] where [[ML4T_A3_0003]] is the feature count.
With depth=4 and proper augmentations, we match the paper's methodology.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
[[ML4T_A3_0001]] holds the values Ni et al. (2024) report for S&P 500 log returns
over their sample. The notebook prints them beside what this run achieves, so the
comparison stays visible in the output rather than being asserted in prose.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>
