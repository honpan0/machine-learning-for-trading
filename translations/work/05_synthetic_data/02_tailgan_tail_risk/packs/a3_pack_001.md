# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/02_tailgan_tail_risk.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Hyperparameter → 超參數
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Tail-GAN: Learning to Generate Tail-Risk Preserving Scenarios

**Chapter 5: Synthetic Data Generation**
**Section Reference**: Section 5.5 (GANs for financial time series)

**Docker image**: [[ML4T_A3_0001]]

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 05_synthetic_data/02_tailgan_tail_risk.py
> ```


## Purpose

This notebook implements **Tail-GAN** (Cont, Xu, and Zhang 2022), a GAN
architecture that uses differentiable sorting to preserve tail risk
characteristics (VaR, ES) in synthetic financial scenarios.

## Learning Objectives

- Understand how differentiable sorting enables gradient flow through quantile
  computation (VaR/ES)
- Implement constraint projection to enforce the relationship [[ML4T_A3_0002]]
- Generate portfolio PnL scenarios that preserve tail risk structure
- Evaluate generation quality using relative VaR/ES error

## Book Reference

Section 5.5 discusses how Tail-GAN targets specific risk metrics rather
than general distributional matching, filling a gap left by TimeGAN.

## Prerequisites

Requires ETF data. The generator clamps outputs to [-1, 1], so returns are
divided by their largest absolute value to keep the full tail inside the clamp
without saturating it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## Tail-GAN Architecture

Tail-GAN uses **differentiable sorting** to compute VaR and ES in a way that
allows gradients to flow through quantile estimates. The generator learns to
produce scenarios where the relationship [[ML4T_A3_0001]] holds, ensuring
realistic tail risk structure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 1. Configuration

Hyperparameters following Zhang et al. (2022):
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 2. Data Loading

We use ETF returns and create portfolio strategies to generate PnL scenarios.

**Important**: the generator clamps its output to [-1, 1], so any scaled input
beyond that range can never be reproduced - fatal for a *tail* model whose whole
purpose is to match the extremes. Scaling divides by the largest absolute return,
mapping it just inside the clamp, so the entire empirical support including both
tails stays reachable. The bulk of returns then sits well within the range,
leaving the outer part of it for the tail the model is built to learn.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 3. Scenario and Strategy Generation

Create return scenarios and portfolio strategies for PnL computation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Portfolio Strategy Weights

Random long-short portfolios whose PnL distributions we want to preserve.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 4. Neural Sort (Differentiable Sorting)

Differentiable sorting is critical for gradient flow through VaR/ES computation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## 5. Score Functions

Scoring functions for VaR/ES constraint enforcement.
The S_quant function has better optimization properties than the general S_stats.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### Quantile Score Function

The core scoring function combines VaR and ES constraints with indicator
functions. This formulation has better optimization properties than
general scoring rules because it directly targets quantile risk.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## 6. Score Criterion Module

Wraps the scoring function for use in training.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## 7. PnL Computation

Simplified version of Transform.py - computes portfolio PnL from returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## 8. Generator Architecture

4-layer MLP with BatchNorm, clamp output to [-1, 1].
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 9. Discriminator Architecture

Takes sorted PnL, outputs VaR/ES estimates with constraint projection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## 10. Initialize Models
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>
