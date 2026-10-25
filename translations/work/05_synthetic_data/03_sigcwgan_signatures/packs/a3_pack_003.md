# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/03_sigcwgan_signatures.ipynb；A3 Pack 003；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Hyperparameter → 超參數

## 待翻譯英文單元

### c0043-p000

~~~~~~markdown
### LSTM Generator

The paper's generator processes Brownian motion noise (cumulative sum of
Gaussian) through an LSTM, producing smooth output paths. This is different
from AR-FNN approaches that use independent noise at each step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
### Initialize Generator

Instantiate the LSTM generator with paper hyperparameters.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0047-p000

~~~~~~markdown
## 6. Sig-W1 Loss (PAPER IMPLEMENTATION)

**Paper Loss**: The Sig-W1 metric is the L2 norm (NOT squared MSE) of the
difference between expected signatures:

[[ML4T_A3_0001]]

For training:
- Generate a batch of fake paths
- Compute their expected signature (mean over batch)
- Compare to precomputed expected signature of real data
- Loss = L2 norm of difference (RMSE style)

**FACTORIAL NORMALIZATION**: Applied to signatures during training too!
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0050-p000

~~~~~~markdown
### GPU Lead-Lag and Visibility Transforms

Differentiable versions of the structural transforms, needed for
backpropagation through the signature computation during training.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0053-p000

~~~~~~markdown
### GPU Augmentation Pipeline and Expected Signature

The full differentiable pipeline: augment → compute signature → average →
normalize. This is used during training to compute the Sig-W1 loss.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0055-p000

~~~~~~markdown
### Expected Signature with Factorial Normalization (GPU)

Compute the mean signature over a batch of augmented paths, applying
factorial rescaling per level to equalize magnitude across depths.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
## 7. Training Loop (PAPER: Unconditional Sig-W1)

**Paper Algorithm** (lib/trainers/sig_wgan.py):

[[ML4T_A3_0001]]

**Sig-W1 Loss**:
[[ML4T_A3_0002]]

The generator produces paths unconditionally - no conditioning on past.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0059-p000

~~~~~~markdown
### Run Training

Execute the Sig-W1 optimization loop with paper-exact settings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0062-p000

~~~~~~markdown
## 8. Training Progress Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0062-p000>>>
<<<ML4T-ZH-END:c0062-p000>>>

### c0064-p000

~~~~~~markdown
**Interpretation**: The Sig-W1 loss measures the L2 distance between expected
signatures of real and generated paths. A decreasing loss curve confirms the
generator is learning to produce paths whose signature statistics match the
training data. The absolute Sig-W1 value is **not** comparable to the paper's
reference printed above - the metric's scale depends on the signature depth,
augmentation choices, and the magnitude of the input series (see the caveat in
the Key Takeaways). What matters here is the shape of the curve: a rapid drop
in the first ~150 steps followed by a low, stable plateau.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0065-p000

~~~~~~markdown
## 9. Generate Synthetic Paths

The LSTM generator produces paths UNCONDITIONALLY - no conditioning on past.
Each call generates a fresh batch of paths from Brownian motion noise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0067-p000

~~~~~~markdown
## 10. Evaluation

### Fidelity: visual comparison with PCA and t-SNE

We project both real and synthetic paths into 2D to assess whether the
generator covers the same regions of the data manifold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p000>>>
<<<ML4T-ZH-END:c0067-p000>>>

### c0069-p000

~~~~~~markdown
**Interpretation**: In the dense core, the synthetic point cloud overlaps the
real one - the generator reproduces the bulk of the distribution. The PCA panel
also exposes the model's main weakness: real returns have far-flung outliers
(extreme days) that the synthetic samples never reach, a first visual hint that
the generator under-produces the fat tails we quantify in the stylized-facts
table below. The signature-based metrics that follow provide a more rigorous
assessment than visual inspection alone.
~~~~~~

<<<ML4T-ZH-BEGIN:c0069-p000>>>
<<<ML4T-ZH-END:c0069-p000>>>

### c0070-p000

~~~~~~markdown
### Comparing signature distributions

**Paper Evaluation**: Compare expected signatures of real vs synthetic paths.
This is the same metric used for training (Sig-W1).
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>
