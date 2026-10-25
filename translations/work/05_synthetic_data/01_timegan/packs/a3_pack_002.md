# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/01_timegan.ipynb；A3 Pack 002；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Cluster → 群集
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0035-p000

~~~~~~markdown
## 7. Phase 3: Joint Adversarial Training

Train Generator and Discriminator adversarially while maintaining reconstruction
and supervised losses. Key details:
- 2 generator+embedder updates per discriminator update
- Discriminator gating: a step is taken only when the discriminator loss
  exceeds [[ML4T_A3_0001]], which keeps an already-winning
  discriminator from overwhelming the generator
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0039-p000

~~~~~~markdown
## 8. Generate Synthetic Data

Training draws millions of random numbers and loading a checkpoint draws none, so the
two paths arrive here with different RNG states. Everything below - the noise the
generator is fed, and the initializations inside the evaluation suite - would then
differ between a run that trained the weights and a run that loaded the same weights
back. Reseeding here makes the two paths produce the same synthetic sequences.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
## 9. Evaluation

We evaluate using the Fidelity-Utility-Privacy framework with LSTM-based
evaluation matching the original paper.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
### Diversity: PCA and t-SNE Projections
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0044-p000

~~~~~~markdown
**Read it.** Neither panel shows the two sets sitting on top of each other. In the
PCA projection the synthetic sequences occupy a sliver at the centre of the real
cloud, so they vary far less than the real ones along the directions that carry most
of the real variance. In the t-SNE projection the two sets fall in separate regions.
The discriminative accuracy printed by the evaluation suite below puts a number on
what these panels show.

Read this against the mean and standard deviation printed by the generation cell
above, which are close to the real ones. Those two readings are not in conflict, and
the section at the end of the notebook is about why: the pooled moments are a weak
requirement, and these panels are a picture of what they leave unconstrained.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0045-p000

~~~~~~markdown
### Paper Evaluation Suite (LSTM-based)

Run the full evaluation following Yoon et al. (2019) using LSTM predictors
and discriminators, not tree-based models.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0047-p000

~~~~~~markdown
### Training Curves
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
## 10. Save Outputs
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0052-p000

~~~~~~markdown
### Persisting the Projection Coordinates

The book-repo Hard Rule 15 script
[[ML4T_A3_0001]]
re-renders the publication figure without retraining. It reads vendored copies
under [[ML4T_A3_0002]], so it does not track
these arrays until someone re-vendors them.

The projections are computed with the parameters [[ML4T_A3_0003]]
uses internally, so the inline render and the persisted arrays describe the
same projection. That includes the legacy global-RNG seeding, [[ML4T_A3_0004]]
followed by [[ML4T_A3_0005]], so the subsample indices follow the helper's
MT19937 sequence rather than the PCG64 sequence [[ML4T_A3_0006]] emits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
## Summary

This notebook implemented **TimeGAN** (Yoon et al., NeurIPS 2019):

1. **Data**: 6 diverse stocks (BA, CAT, DIS, GE, IBM, KO) with adjusted close
2. **Architecture**: Five-component system with ModuleList GRUs (matching TF)
3. **Training**: Three-phase, step-based approach (10,000 steps per phase)
4. **Evaluation**: LSTM-based discriminative and predictive scores

### Reading the Two Scores

Both diagnostics are printed above rather than quoted here, because both move
from run to run and a number typed into prose stops tracking the code that
produced it. What is fixed is how to read them.

**Discriminative accuracy** trains a classifier to tell real sequences from
synthetic ones and reports its held-out accuracy. The benchmark is chance, one
half, not zero: a value near one half means the classifier cannot separate the
two, and higher means it can. Held-out accuracy is not bounded below by chance,
so a value well under one half is possible and is not a better result — it
points at sampling variation, a classifier that failed to generalize, or a
shift between the two sets. A substantial departure in either direction is
something to investigate rather than to report.

**The TSTR/TRTR ratio** divides the error of a predictor trained on synthetic
data by the error of the same predictor trained on real data, both scored on
the real holdout. Its target is one, meaning synthetic data substitutes for
real without loss; above one means it is worse.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0054-p001

~~~~~~markdown

The predictor's output layer is linear and unbounded, so it can predict outside
the generator's range and the ratio does not become meaningless when the
holdout leaves it. What it becomes is confounded. On price levels the synthetic
training data is confined to [[ML4T_A3_0001]] while most holdout targets sit above one,
as the cell before the data load shows, and a ratio measured across that gap
cannot separate a generator that missed the temporal structure from targets
that left the support the synthetic data covers. Working in returns keeps the
holdout inside the fitted range, which the assertion in the normalization
section enforces, so the ratio is answering one question rather than two.

### When the Moments Agree and the Discriminator Does Not

The generation cell prints the synthetic and real mean and standard deviation,
and on this run they agree to about two decimal places. The discriminative
accuracy printed just above is nonetheless far from chance. Those two facts are
not in conflict, and holding them together is the point of the section the
chapter devotes to evaluation.

Matching the first two moments of a pooled distribution is a weak requirement.
It says nothing about the order of values within a sequence, about how
volatility clusters, or about the dependence between the six stocks on the same
day. A classifier that reads whole sequences can use any of that, and a high
accuracy says it found something it could use. Which of those the generator
missed is not something the accuracy alone can say — it is a single number, and
diagnosing it needs the stylized-fact and dependence checks the chapter
introduces alongside this score.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p001>>>
<<<ML4T-ZH-END:c0054-p001>>>

### c0054-p002

~~~~~~markdown

This is also why the two diagnostics are reported together rather than one
being chosen. A ratio near one says a downstream predictor trained on synthetic
data transfers to real data for this particular task, which is a claim about
utility. It does not say the synthetic sequences are indistinguishable from
real ones, which is what the discriminator tests.

### Limitations

TimeGAN focuses on matching overall distribution, not tail risk. For alternatives:
- **Tail risk**: See [[[ML4T_A3_0001]]](02_tailgan_tail_risk.ipynb)
- **Path signatures**: See [[[ML4T_A3_0002]]](03_sigcwgan_signatures.ipynb)
- **Diffusion models**: See [[[ML4T_A3_0003]]](05_diffusion_ts.ipynb)
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p002>>>
<<<ML4T-ZH-END:c0054-p002>>>
