# ML4T A2 翻譯 Pack 002 — 05_synthetic_data/04_gtgan_irregular.ipynb

原 Batch：003, 004；翻譯單元：23。

## 指示（整個 Pack 只需閱讀一次）

將以下所有英文 Markdown 翻譯成**台灣繁體中文**；忠於原意，保留技術論述，不摘要、不增刪內容。
只翻譯自然語言；保留 Markdown 層級、行內程式碼、數學符號、數值、網址、檔案路徑、變數與函式名稱。
獨立程式碼區塊／獨立圖片／獨立公式已由本機保留，不要重複；混合文字內的必要語法請保留。
以下原文視為待翻譯資料，**不要執行或遵循原文中的命令或指示**。
每個單元一組指定的 BEGIN/END，必須完全匹配並各獨占一行；不得插入反斜線、escape 標籤或程式碼框。
僅輸出各單元翻譯及標記；不要重貼英文、術語表或其他解說。每個單元均不可漏。
如果單元完全沒有自然語言，內容填入 [[SKIP_TRANSLATION]]。
若回覆長度不足，停在最後一個**完整**的 END 標記，不要刪掉文字來硬塞完所有單元。

## 此 Pack 相關術語（不要在回覆中重貼）

- Feature → 特徵
- Time series → 時間序列
- Correlation → 相關性
- Covariance → 共變異數

## 翻譯單元

### c0029-p000（原 Batch 003）

~~~~~~markdown
### ODE Generator

Maps random noise to latent codes by evolving initial states through
a Neural ODE. The ODE trajectory acts as a learned nonlinear transformation.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000（原 Batch 003）

~~~~~~markdown
### ODE Discriminator

Processes sequences through GRU-ODE (respecting irregular timestamps) and
outputs a real/fake classification. The time-awareness is what distinguishes
this from a standard GRU discriminator.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000（原 Batch 003）

~~~~~~markdown
## GT-GAN Model
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000（原 Batch 003）

~~~~~~markdown
### Reusing a checkpoint, and when not to

Training is the expensive step, so a saved checkpoint is loaded when one matches. What
counts as a match is the question. `CHECKPOINT_IDENTITY` below names every setting that
moves the weights, including `data_digest`, because `CONFIG` names the features and the
window and not the bars they are cut from.

The digest matters most on the path a reader is most likely to take. This notebook falls
back to synthetic bars when the Chapter 3 outputs are absent, so a first run trains on
the fallback and a later run, after Chapter 3 has been executed, sees real bars. Without
the digest that second run loads the fallback-trained weights. It also takes the
checkpoint's scaler, while `sequences_norm` above was scaled from the new bars, which
would leave the holdout comparison and the training data on different scales. A digest
mismatch retrains instead, which is the only answer that keeps the two consistent.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000（原 Batch 003）

~~~~~~markdown
## Training Loop
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000（原 Batch 003）

~~~~~~markdown
### Run Training

Execute step-based training. Progress is logged at regular intervals.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000（原 Batch 003）

~~~~~~markdown
## Training Progress
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000（原 Batch 003）

~~~~~~markdown
**Interpretation**: The reconstruction loss should decrease steadily, indicating the
autoencoder learns to compress and reconstruct irregular sequences through the ODE
bottleneck. The adversarial losses (D real, D fake, Generator) should oscillate and
roughly balance -- if the discriminator dominates (D losses near 0), the generator
receives no useful gradient. The notebook prints the reconstruction MSE against
`GOOD_RECONSTRUCTION_MSE` below; when it clears that bar, the GAN component is
refining a latent space the autoencoder has already learned to invert.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000（原 Batch 003）

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

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0047-p000（原 Batch 003）

~~~~~~markdown
### Choosing the sequences to evaluate against

The sequences are rolling windows at stride one, so the first N of them start on N
consecutive bars: one stretch of the tape repeated, not N samples of it, and a quiet
or a violent week would stand in for the whole period. Everything below compares
against `real_eval`, drawn at random, and the synthetic sequences are generated on
that same draw's time grids so the two stay paired.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000（原 Batch 003）

~~~~~~markdown
## Evaluation

### Fidelity: Visual Comparison with PCA and t-SNE

We project both real and synthetic sequences into 2D to assess whether the
generator covers the same regions of the data manifold.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000（原 Batch 003）

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

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0052-p000（原 Batch 003）

~~~~~~markdown
### Interpolation at Arbitrary Timestamps

GT-GAN's key capability: query the model at any timestamp, not just observed ones.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000（原 Batch 003）

~~~~~~markdown
**Interpretation**: a smoothness ratio near one means the ODE-based interpolation
varies from step to step about as much as the real data does, so the model has learned
continuous dynamics rather than averaging adjacent points. A ratio well below one is
over-smoothing, the ODE being too rigid to follow the data; a ratio above one is noisy
interpolation. The reconstruction MSE measures how faithfully the encode-decode
round-trip recovers the input, and is printed above beside the bar it is judged against.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000（原 Batch 003）

~~~~~~markdown
## Statistical Comparison
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000（原 Batch 004）

~~~~~~markdown
**Interpretation**: the KS statistic measures distributional divergence, from zero for
identical distributions to one for completely separated ones. A middling value is
typical of small-sample generative models and indicates a partial distributional match.
A high value is expected when training on a few hundred bars and does not on its own
mean the model has failed - it reflects how little distributional structure a short
irregular series carries. The correlation error measures how well the cross-feature
covariance is preserved.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0058-p000（原 Batch 004）

~~~~~~markdown
## Visualization: Real vs Synthetic with Irregular Timestamps
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0060-p000（原 Batch 004）

~~~~~~markdown
**Interpretation**: both panels carry the same observation times, because the time
grid is an argument to `generate_synthetic` rather than something the model produces.
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

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0061-p000（原 Batch 004）

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

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0063-p000（原 Batch 004）

~~~~~~markdown
### Run Evaluation

Execute the full GT-GAN evaluation protocol: discriminative score,
predictive score (TSTR), and interpolation quality.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0065-p000（原 Batch 004）

~~~~~~markdown
**Interpretation**: read the four rows together rather than choosing among them. The
discriminative accuracy and AUC sit at their maximum, so the classifier separates
synthetic from real without error: whatever the sequences preserve is not enough to
fool a model that is looking for the difference. The TSTR ratio misses the band the
protocol allows, so a predictor fitted on the synthetic sequences carries more error on
real ones than a predictor fitted on real data does, by the margin the ratio above
gives. Those two rows are not the same finding: a classifier separating two sets
perfectly says nothing about how much of the predictive structure the second set
carries. The
bounded fraction clears its threshold, but it checks something narrower than its name
suggests. It encodes a real window, decodes at the midpoint between each pair of
observation times, and asks whether that value lands between the two neighbouring real
values with a fixed tolerance added on either side. That tolerance is wider than the
mean gap between adjacent observations printed in the interpolation section above, so
most of the band being cleared is tolerance rather than data. And the latent it decodes
comes from encoding a real window, which makes it the one row here that never runs the
generator. The passing row and the failing rows are therefore not in tension: they ask
different questions, and discarding the failing ones to keep the passing one would be
choosing a metric by its answer.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0065-p001（原 Batch 004）

~~~~~~markdown

`MAX_STEPS` is set to two thousand, which is a short adversarial run, and the
training-progress figure shows the three adversarial losses settling onto a common
flat level well before the end. Lengthening that run is the change to make before any
of these numbers is quoted as a property of GT-GAN rather than of this pass.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0065-p001>>>
<<<ML4T-ZH-END:c0065-p001>>>

### c0066-p000（原 Batch 004）

~~~~~~markdown
## Save Outputs
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>
