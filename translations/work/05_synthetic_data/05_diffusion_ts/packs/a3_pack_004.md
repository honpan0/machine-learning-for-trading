# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/05_diffusion_ts.ipynb；A3 Pack 004；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market regime → 市場狀態
- Feature → 特徵
- Label → 標籤
- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0071-p000

~~~~~~markdown
## 10. Regime-Conditional Generation

This section implements **classifier guidance** for conditional diffusion:

1. Fit a Gaussian HMM on SPY returns to identify market regimes
2. Train a classifier on noised sequences labeled by regime
3. At sampling time, compute [[ML4T_A3_0001]] and
   shift the denoising trajectory toward the target regime

### Hidden Markov Models for Regime Detection

A **Hidden Markov Model (HMM)** assumes the market cycles through unobserved
"states" (regimes), each with its own return distribution. The Gaussian HMM
assumes each regime has a distinct mean and variance. Given observed returns,
the Viterbi algorithm infers the most likely regime sequence.

Here we use a simple 2-state HMM as a label source for conditional generation.
**Chapter 9 (Model-Based Feature Extraction)** covers HMMs in depth, including:
- Multi-state regime models for volatility forecasting
- Regime-switching strategies
- Comparison with Markov-switching GARCH
~~~~~~

<<<ML4T-ZH-BEGIN:c0071-p000>>>
<<<ML4T-ZH-END:c0071-p000>>>

### c0073-p000

~~~~~~markdown
### Label Training Sequences by Majority Regime

Each training sequence of length [[ML4T_A3_0001]] spans multiple days. We assign the
regime label that covers the majority of days in the window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0073-p000>>>
<<<ML4T-ZH-END:c0073-p000>>>

### c0075-p000

~~~~~~markdown
### Regime Classifier on Noised Data

The classifier must operate on noised sequences [[ML4T_A3_0001]] (not clean data),
because during sampling we compute gradients w.r.t. partially-denoised
samples. We reuse the Encoder architecture from Diffusion-TS with an
attention pooling head for classification.
~~~~~~

<<<ML4T-ZH-BEGIN:c0075-p000>>>
<<<ML4T-ZH-END:c0075-p000>>>

### c0080-p000

~~~~~~markdown
### Train the Classifier

Training samples noised sequences at random timesteps and classifies them.
The classifier must learn to identify regime characteristics even through
heavy noise -- this is what makes the gradient signal useful during sampling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0080-p000>>>
<<<ML4T-ZH-END:c0080-p000>>>

### c0082-p000

~~~~~~markdown
### Classifier Guidance Function

The [[ML4T_A3_0001]] computes [[ML4T_A3_0002]] -- the gradient of the
classifier's log-probability for the target regime with respect to the
noised input. This gradient steers the diffusion sampling toward
sequences that the classifier recognizes as belonging to the target regime.
~~~~~~

<<<ML4T-ZH-BEGIN:c0082-p000>>>
<<<ML4T-ZH-END:c0082-p000>>>

### c0084-p000

~~~~~~markdown
### Generate Regime-Conditional Samples

For each regime, we generate synthetic sequences steered by the classifier.
Then we compare the volatility characteristics of generated samples against
historical data from that regime.
~~~~~~

<<<ML4T-ZH-BEGIN:c0084-p000>>>
<<<ML4T-ZH-END:c0084-p000>>>

### c0086-p000

~~~~~~markdown
### Compare Regime-Conditional Statistics

For each regime, we compare the volatility and mean return of the generated
samples against the historical sequences labeled with that regime.
~~~~~~

<<<ML4T-ZH-BEGIN:c0086-p000>>>
<<<ML4T-ZH-END:c0086-p000>>>

### c0089-p000

~~~~~~markdown
**Interpretation**: classifier guidance separates the regimes. Read the table above
against three things it is doing.

1. **Variance scaling**: the model generates less variance than the real series in
   normalized space. That is expected of a diffusion model built on a trend and
   seasonal decomposition, whose smooth components cannot carry high-frequency
   variation, so the notebook applies a post-hoc variance rescaling to the training
   distribution. The ratio it needed is printed above.

2. **The majority regime**: unconditional samples already resemble the low-volatility
   regime, so gentle guidance is enough and the generated volatility lands near the
   historical level.

3. **The minority regime**: classifier gradients have to push harder to move samples
   into the high-volatility regime, and pushing adds variance of its own. Whether the
   result overshoots is exactly what the volatility ratio in the table measures.

**Scale tuning**: a higher guidance scale buys more regime separation and costs more
variance. The per-regime settings are declared in [[ML4T_A3_0001]] in the config
cell, where the minority class is deliberately steered less hard than the majority
one, to keep it from collapsing onto extreme volatility.
~~~~~~

<<<ML4T-ZH-BEGIN:c0089-p000>>>
<<<ML4T-ZH-END:c0089-p000>>>

### c0090-p000

~~~~~~markdown
Historical and generated sequences side by side, one row per regime. Every panel
shares a y-axis, so the volatility difference between regimes and between real and
generated is a difference in the picture rather than in the axis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0090-p000>>>
<<<ML4T-ZH-END:c0090-p000>>>

### c0092-p000

~~~~~~markdown
**Interpretation**: the two historical panels differ the way the regime labels say
they should, the low-volatility one visibly calmer than the high-volatility one. The
two generated panels are harder to tell apart by eye, and both range wider than their
historical counterparts.

Ten paths per panel is too thin a sample to conclude from, which is what the next
figure is for: it compares the full volatility distributions of these same
regime-conditional samples, where the separation the guidance is meant to produce
either shows up or does not. Read that one before deciding what this one means.

One thing this figure does show that a distribution cannot: the generated paths widen
from left to right, and the historical ones do not. Volatility that grows with
position in the window is an artifact of the sampler, not a property of the regime.
~~~~~~

<<<ML4T-ZH-BEGIN:c0092-p000>>>
<<<ML4T-ZH-END:c0092-p000>>>

### c0095-p000

~~~~~~markdown
## 11. Save Samples (Model checkpoint saved after training)
~~~~~~

<<<ML4T-ZH-BEGIN:c0095-p000>>>
<<<ML4T-ZH-END:c0095-p000>>>

### c0097-p000

~~~~~~markdown
## Key Takeaways

1. **Interpretable decomposition**: Diffusion-TS separates denoising predictions
   into trend (polynomial), seasonal (Fourier), and residual components, making
   the generator's behavior inspectable.

2. **Fourier loss preserves spectral structure**: The frequency-domain regularizer
   encourages the model to match autocorrelation and periodicity patterns, which
   is critical for realistic financial time series.

3. **Classifier guidance enables conditional generation**: By training a separate
   classifier on noised data, we can steer sampling toward specific regimes
   (low-volatility vs high-volatility) -- enabling regime-specific stress testing
   with synthetic data.

4. **DDIM fast sampling**: Reducing reverse steps from 500 to 50 provides ~10x
   speedup with minimal quality loss, making generation practical.

**Limitations**:
- Classifier guidance quality depends on regime label accuracy (HMM is simple)
- The guidance scale requires tuning per application
- High-dimensional generation (here 20 assets) is computationally intensive;
  scaling to broader universes raises cost further

**Next**: Section 5.8 applies the Fidelity-Utility-Privacy framework to
systematic evaluation of any synthetic generator.
~~~~~~

<<<ML4T-ZH-BEGIN:c0097-p000>>>
<<<ML4T-ZH-END:c0097-p000>>>
