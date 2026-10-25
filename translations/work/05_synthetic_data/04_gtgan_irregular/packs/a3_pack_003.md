# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/04_gtgan_irregular.ipynb；A3 Pack 003；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Time series → 時間序列
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0043-p000

~~~~~~markdown
**Interpretation**: The reconstruction loss should decrease steadily, indicating the
autoencoder learns to compress and reconstruct irregular sequences through the ODE
bottleneck. The adversarial losses (D real, D fake, Generator) should oscillate and
roughly balance -- if the discriminator dominates (D losses near 0), the generator
receives no useful gradient. The notebook prints the reconstruction MSE against
[[ML4T_A3_0001]] below; when it clears that bar, the GAN component is
refining a latent space the autoencoder has already learned to invert.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
## Generate Synthetic Irregular Sequences

Training draws random numbers and loading a checkpoint draws none, so the two paths
reach this point with different torch RNG states. The latent noise the generator is
fed, and the initializations inside the evaluation protocol, would then differ between
the run that fitted the weights and a later run that loaded the same weights back:
same model, same data, same seed, different reported scores. That was measured, not
assumed: before this reseed the training path and the loading path returned different
TSTR ratios from one set of weights. Reseeding here is what makes them agree.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0047-p000

~~~~~~markdown
### Choosing the sequences to evaluate against

The sequences are rolling windows at stride one, so the first N of them start on N
consecutive bars: one stretch of the tape repeated, not N samples of it, and a quiet
or a violent week would stand in for the whole period. Everything below compares
against [[ML4T_A3_0001]], drawn at random, and the synthetic sequences are generated on
that same draw's time grids so the two stay paired.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
## Evaluation

### Fidelity: Visual Comparison with PCA and t-SNE

We project both real and synthetic sequences into 2D to assess whether the
generator covers the same regions of the data manifold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
**Interpretation**: the two point clouds do not cover the same region. The synthetic
sequences project onto a narrow band in both panels while the real ones fall elsewhere,
which is what a generator producing a family of similar sequences looks like under a
projection. Neither panel is a measurement: a projection into two dimensions can
separate sets a model cannot, and can hide a difference a model finds easily. The
discriminative score reported later in the notebook is the measured version of the
same question, and the interpolation section immediately below asks a different one -
whether the decoder returns sensible values at times it was not given.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0052-p000

~~~~~~markdown
### Interpolation at Arbitrary Timestamps

GT-GAN's key capability: query the model at any timestamp, not just observed ones.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
**Interpretation**: a smoothness ratio near one means the ODE-based interpolation
varies from step to step about as much as the real data does, so the model has learned
continuous dynamics rather than averaging adjacent points. A ratio well below one is
over-smoothing, the ODE being too rigid to follow the data; a ratio above one is noisy
interpolation. The reconstruction MSE measures how faithfully the encode-decode
round-trip recovers the input, and is printed above beside the bar it is judged against.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
## Statistical Comparison
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
**Interpretation**: the KS statistic measures distributional divergence, from zero for
identical distributions to one for completely separated ones. A middling value is
typical of small-sample generative models and indicates a partial distributional match.
A high value is expected when training on a few hundred bars and does not on its own
mean the model has failed - it reflects how little distributional structure a short
irregular series carries. The correlation error measures how well the cross-feature
covariance is preserved.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0058-p000

~~~~~~markdown
## Visualization: Real vs Synthetic with Irregular Timestamps
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0060-p000

~~~~~~markdown
**Interpretation**: both panels carry the same observation times, because the time
grid is an argument to [[ML4T_A3_0001]] rather than something the model produces.
So nothing in this figure can say whether GT-GAN reproduces the arrival process of
information-driven bars: it is handed that process, not asked for it. What the two
panels compare is the values the decoder returns when it is given a real window's
timestamps, against the values that window actually took, on a shared vertical scale.

On this window the two differ in both. The real series stays inside a narrow band and
reverses direction repeatedly between observations; the synthetic one rises across most
of the shared vertical scale without a single reversal. A decoder
whose output is the state of an ODE evolving between query points is smooth wherever
the fitted dynamics are smooth, so one window raises that question rather than
settling it. The interpolation section earlier in the notebook is the measured
version: it decodes at the observed times and again at the midpoints between them,
and reports the smoothness of each beside the real series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0061-p000

~~~~~~markdown
## Evaluation: GT-GAN Protocol

**Reference**: Jeon et al. (2022) "GT-GAN: General Purpose Time Series Synthesis" [NeurIPS 2022]

GT-GAN's evaluation follows the TimeGAN protocol with additional focus on:
1. **Discriminative Score**: Can a classifier distinguish real from synthetic?
2. **Predictive Score (TSTR)**: Train on synthetic, predict on real holdout
3. **Interpolation Quality**: Unique to GT-GAN - measure reconstruction at irregular timestamps

The key GT-GAN advantage is handling naturally irregular data. We evaluate whether
the model preserves both statistical properties AND irregular timing patterns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0063-p000

~~~~~~markdown
### Run Evaluation

Execute the full GT-GAN evaluation protocol: discriminative score,
predictive score (TSTR), and interpolation quality.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>
