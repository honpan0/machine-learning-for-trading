# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/04_gtgan_irregular.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Chapter 5: GT-GAN - Neural ODEs for Irregular Time Series

**Docker image**: [[ML4T_A3_0001]]

This notebook implements a **GT-GAN-inspired** model (based on Jeon et al., NeurIPS 2022)
using **Neural ODEs** to handle time series with **naturally irregular timestamps**.

**Learning Objectives**:
- Understand how Neural ODEs handle irregular time intervals via continuous dynamics
- Implement a GRU-ODE encoder that processes observations at arbitrary timestamps
- Train a GAN with ODE-based generator and discriminator for irregular series
- Evaluate interpolation quality at unobserved timestamps (GT-GAN's unique capability)
- Compare GT-GAN's irregular-data approach with fixed-grid generators (TimeGAN, Sig-CWGAN)

**Book Reference**: Chapter 5, Section 5.5 (GANs for financial time series) - GT-GAN
is treated here as a hybrid GAN + continuous-time generator for irregular observations.

**Prerequisites**: Familiarity with GANs ([[ML4T_A3_0002]]) and Chapter 3 bar data.

## Key Innovation: Genuine Irregularity

Unlike other notebooks that use daily returns on regular grids, GT-GAN is designed
for **naturally irregular** data. We use Chapter 3's information-theoretic bars:

- **Tick bars**: Fixed number of trades → variable time between bars
- **Volume bars**: Fixed volume threshold → variable time between bars
- **Dollar bars**: Fixed dollar volume → variable time between bars

These bars have genuine irregular timestamps driven by market activity, not
artificial random masking.

## Neural ODEs: The Key Innovation

Instead of discrete recurrence:

[[ML4T_A3_0003]]

Neural ODEs define continuous dynamics:

[[ML4T_A3_0004]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

The hidden state evolves continuously, and we can query it at any time point.
This naturally handles:
- Variable time intervals between observations
- Interpolation to any desired time grid
- Generation at arbitrary timestamps

## Model Architecture (Simplified GT-GAN)

GT-GAN uses Neural ODEs to handle continuous-time dynamics:
1. **GRU-ODE Encoder**: Maps irregular observations to latent space
2. **ODE Generator**: Generates synthetic latent trajectories
3. **ODE Discriminator**: Classifies real vs synthetic in latent space
4. **ODE Decoder**: Reconstructs observations from latent space

See [[ML4T_A3_0001]] for the full architecture diagram.

## References

- **GT-GAN Paper**: Jeon et al. (2022). "GT-GAN: General Purpose Time Series
  Synthesis with Generative Adversarial Networks." NeurIPS 2022.
- **Neural ODEs**: Chen et al. (2018). "Neural Ordinary Differential Equations."
- **Information Bars**: López de Prado (2018). "Advances in Financial Machine Learning."

---

## WARNING: IMPORTANT: Data Source Requirement

**GT-GAN requires naturally irregular data** - that's its core design goal.

| Data Source | Natural Irregularity? | Suitability |
|-------------|----------------------|-------------|
| Chapter 3 bar data | [OK] Yes (activity-driven) | [OK] Ideal |
| Synthetic fallback | WARNING: Simulated | WARNING: Demo only |
| Daily returns + masking | [FAIL] Artificial | [FAIL] Not recommended |

**If Chapter 3 bar data is unavailable**, this notebook falls back to generating
synthetic bars with log-normal inter-arrival times. While this demonstrates the
Neural ODE architecture, the statistical properties are artificial.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**For production use**: Ensure Chapter 3's microstructure bar data is available.
Run Chapter 3 notebooks first to generate tick/volume/dollar bars.

### What this run reports

Three numbers say how the run went, all printed in the evaluation cells below:
reconstruction MSE for the autoencoder round-trip, the KS statistic against the
real marginal, and the smoothness ratio of the ODE interpolation against the real
bars. This is a short training pass over a small sample, so read them as a
demonstration of the architecture rather than as achievable quality.

---

## Per-Sample Time Integration

[[ML4T_A3_0001]] selects one of two fixed-step solvers, and both advance each row of a
batch by that row's own interval:

- **Euler**: one evaluation per step, [[ML4T_A3_0002]].
- **RK4**: four evaluations per step, combined as [[ML4T_A3_0003]].

Neither drift network takes the time as an input, so a step depends only on the width
of the interval and a column of [[ML4T_A3_0004]] values is enough to give every row its own step.
That is what [[ML4T_A3_0005]] below does. [[ML4T_A3_0006]] is still used for the
generator, whose whole batch genuinely shares one time span; it takes a single grid
for a batched initial state, so it cannot be used where the rows differ.

An adaptive solver would need per-sample step control. The GT-GAN paper used
[[ML4T_A3_0007]] (Lienen & Günnemann, 2022) for that, but its [[ML4T_A3_0008]] dependency is
incompatible with current PyTorch, so the config cell rejects any method other than
the two above.

**Reference**: Lienen, M. & Günnemann, S. (2022). "torchode: A Parallel ODE
Solver for PyTorch." [[ML4T_A3_0009]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0002-p000

~~~~~~markdown
## GT-GAN Architecture

GT-GAN uses Neural ODEs to handle continuous-time dynamics with genuine irregularity.
Unlike discrete RNNs, the hidden state evolves continuously and can be queried at
any time point.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0007-p000

~~~~~~markdown
## Data: Chapter 3 Information-Theoretic Bars

The key insight is that GT-GAN's Neural ODE architecture is designed for
**genuinely irregular timestamps**. Information bars from Chapter 3 provide this:

| Bar Type | Trigger Condition | Inter-arrival Time |
|----------|------------------|-------------------|
| Tick bars | Every N trades | Variable (activity-driven) |
| Volume bars | Every V shares | Variable (liquidity-driven) |
| Dollar bars | Every [[ML4T_A3_0001]] traded | Variable (value-driven) |

This is fundamentally different from daily returns with artificial masking.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Load Chapter 3 Bar Data

Loads information-theoretic bars generated in Chapter 3's microstructure notebooks.
Falls back to synthetic bars if the data is unavailable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Compute Inter-Arrival Times

Normalizes bar timestamps to the [0, 1] range for ODE integration. The variable
spacing between bars is the key signal that GT-GAN's Neural ODE exploits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Create Irregular Sequences

Slides a window over the bar data to create training sequences, preserving
the per-sequence normalized timestamps that encode irregular spacing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Prepare Training Data

Load bars, compute inter-arrival times, split into train/holdout, and
create normalized sequences for model input.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>
