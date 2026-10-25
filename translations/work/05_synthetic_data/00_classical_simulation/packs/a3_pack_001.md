# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/00_classical_simulation.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Asset returns → 資產報酬率
- Backtesting → 回測
- Feature → 特徵
- Clustering → 分群
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Chapter 5: Classical Simulation Methods

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: Implement and compare classical Monte Carlo methods for generating
synthetic financial data, building the foundation for the learned generative
models that follow.

This notebook teaches the **mechanics** of established Monte Carlo methods for
generating synthetic financial data. We cover both the underlying mathematics
and practical implementation, then show library shortcuts for production use.

## Why Simulate?

Historical market data provides only **one path** through an infinite space of
possibilities. Simulation generates alternative scenarios for:

1. **Risk Management**: VaR, stress testing, tail risk assessment
2. **Backtesting**: Validate strategies beyond historical experience
3. **Data Augmentation**: Larger datasets for ML model training
4. **Privacy**: Share synthetic data without exposing proprietary signals

## Learning Objectives

After completing this notebook, you will be able to:

1. **Implement** each classical stochastic model from scratch
2. **Explain** the assumptions and limitations of each model
3. **Choose** the appropriate model for your use case
4. **Use** library implementations for production work

**Book Reference**: Chapter 5, Section 5.3 (Classical simulation baselines)

**Prerequisites**: Basic probability and stochastic processes; familiarity
with NumPy array operations. Requires ETF data from Chapter 2 ([[ML4T_A3_0002]]).

## Notebook Structure

1. **Part 1**: Continuous-Time Price Models (GBM, Jump-Diffusion, OU, Heston)
2. **Part 2**: Discrete-Time Volatility Model (GARCH with calibration)
3. **Part 3**: Bootstrap Methods (IID, Block, Stationary)
4. **Part 4**: Model Comparison

## Statistical Note
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

We use **log-returns** throughout for consistency with continuous-time SDEs:
- Log-return: [[ML4T_A3_0001]]
- Kurtosis values are **Fisher (excess) kurtosis**: Gaussian = 0

## References

- Glasserman, P. (2003). "Monte Carlo Methods in Financial Engineering"
- Politis, D. & Romano, J. (1994). "The Stationary Bootstrap"
- Cont, R. (2001). "Empirical Properties of Asset Returns: Stylized Facts"
- Heston, S. (1993). "A Closed-Form Solution for Options with Stochastic Volatility"
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
Every generator below is spawned from [[ML4T_A3_0001]], so overriding the parameter
moves every simulation in the notebook rather than only the ones that happen
to read a global. [[ML4T_A3_0002]] names one independent stream per use, and
[[ML4T_A3_0003]] hands out its generator.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
---
# Part 1: Continuous-Time Price Models

These models specify stochastic differential equations (SDEs) for price dynamics.
Each captures different market phenomena:

| Model | Key Feature | Best For |
|-------|-------------|----------|
| **GBM** | Log-normal prices, constant vol | Option pricing, baseline |
| **Jump-Diffusion** | Rare extreme moves | Crash scenarios, tail risk |
| **Mean-Reversion** | Prices drift to equilibrium | Spreads, commodities, rates |
| **Heston** | Stochastic volatility | Vol surfaces, leverage effect |

We implement each from scratch using local RNG for reproducibility,
then show the equivalent library call.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0006-p000

~~~~~~markdown
## Geometric Brownian Motion

The foundation of quantitative finance. Price [[ML4T_A3_0001]] follows the stochastic
differential equation:

[[ML4T_A3_0002]]

where:
- [[ML4T_A3_0003]] = drift (expected annual return)
- [[ML4T_A3_0004]] = volatility (annualized)
- [[ML4T_A3_0005]] = Wiener process increment (Brownian motion)

### Key Properties

- **Log-returns are Gaussian**: [[ML4T_A3_0006]]
- **Prices are log-normal**: Always positive, no crashes below zero
- **No memory**: Future returns independent of past (no autocorrelation)
- **Constant volatility**: Same vol every day (unrealistic)

### Discretization (Euler-Maruyama)

[[ML4T_A3_0007]]

where [[ML4T_A3_0008]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### GBM Simulation

Generate two years of daily data (504 trading days) and inspect the return
distribution. Excess kurtosis should sit near zero: GBM's log-returns are
Gaussian by construction, and any departure is sampling noise from one path.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Library Usage: GBM

[[ML4T_A3_0001]] in the [[ML4T_A3_0002]] package generates the same processes
behind an OHLCV interface. It draws from its own generator, so a provider path
never matches a from-scratch path step for step; what should agree is the
distribution the two draw from. GBM is the one model whose full parameter set
the provider exposes ([[ML4T_A3_0003]], [[ML4T_A3_0004]]), so it is the one
case where the two are the same process and the realized moments are
comparable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### GBM Limitations

GBM assumes returns are **i.i.d. Gaussian**, which contradicts observed
"stylized facts" of financial returns:

1. **Fat tails**: Real returns have excess kurtosis (more extremes than Gaussian)
2. **Volatility clustering**: High-vol days tend to follow high-vol days
3. **Leverage effect**: Negative returns often increase future volatility

Despite these limitations, GBM remains the workhorse for option pricing
(Black-Scholes) due to its analytical tractability.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0013-p000

~~~~~~markdown
## Jump-Diffusion (Merton)

Adds occasional extreme moves to GBM via a compound Poisson process:

[[ML4T_A3_0001]]

where:
- [[ML4T_A3_0002]] = Poisson process with intensity [[ML4T_A3_0003]] (jumps per year)
- [[ML4T_A3_0004]] = log jump size

### Drift Compensator

To ensure [[ML4T_A3_0005]] represents the *total* expected return (including jumps),
we subtract the expected jump contribution:

[[ML4T_A3_0006]]

### Discretization

[[ML4T_A3_0007]]

where [[ML4T_A3_0008]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Jump-Diffusion Simulation

Simulate jumps with a negative mean log size, so the jump distribution is
tilted downward without being one-sided: log jump sizes are Gaussian, so a
minority of jumps are still upward, and the cell prints that share rather than
leaving the reader to infer it. The compensator is computed from the same
parameters rather than retyped, so changing one cannot leave the printed
diagnostic describing a different model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### Library Usage: Jump-Diffusion

The provider's [[ML4T_A3_0001]] model is **not** the model above. It exposes only
[[ML4T_A3_0002]] and [[ML4T_A3_0003]]; the jump process is fixed internally
at five jumps per year with a **zero-mean** jump size. Symmetric jumps produce
fat tails without skew, while the downward-tilted jumps above produce both. The
printed skewness shows the difference, and it is the reason to implement the
jump process yourself when the asymmetry is the point.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>
