# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/04_gtgan_irregular.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Time series → 時間序列

## 待翻譯英文單元

### c0017-p000

~~~~~~markdown
## Neural ODE Components

The core building block is a neural network that defines the derivative:

[[ML4T_A3_0001]]

Given an initial state [[ML4T_A3_0002]], the ODE solver integrates forward to compute:

[[ML4T_A3_0003]]

This allows querying the hidden state at **any** time point, not just discrete steps.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0018-p000

~~~~~~markdown
### ODEFunc: Dynamics Network

Defines the derivative [[ML4T_A3_0001]] used by [[ML4T_A3_0002]]. This is the
core "physics" that governs how latent states evolve continuously in time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
### Advancing a batch by its own inter-arrival times

[[ML4T_A3_0001]] integrates one time grid for the whole batch, so a batch of
sequences observed at different times has to be reduced to a single grid before it
can be passed. That reduction is what the irregular timestamps are supposed to
carry, so the step below takes a [[ML4T_A3_0002]] per row instead. Both drift networks ignore
[[ML4T_A3_0003]], which is what makes a per-row step size well defined: over an interval the
state change depends on the width of the interval and not on where it sits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
### GRU-ODE Cell: Continuous-Time GRU

Combines discrete GRU updates (at observation times) with continuous ODE evolution
(between observations). Each sample's hidden state evolves according to its own
inter-arrival time -- no batch averaging. Based on De Brouwer et al. (2019).
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## Encoder and Decoder
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### ODE Decoder

Decodes latent representations back to time series observations at given
query times using a Neural ODE to evolve hidden states continuously.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## Generator and Discriminator

The GAN components operate in latent space. The generator maps noise through a
Neural ODE to produce latent codes, while the discriminator uses the same GRU-ODE
architecture to classify sequences as real or synthetic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0029-p000

~~~~~~markdown
### ODE Generator

Maps random noise to latent codes by evolving initial states through
a Neural ODE. The ODE trajectory acts as a learned nonlinear transformation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
### ODE Discriminator

Processes sequences through GRU-ODE (respecting irregular timestamps) and
outputs a real/fake classification. The time-awareness is what distinguishes
this from a standard GRU discriminator.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## GT-GAN Model
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
### Reusing a checkpoint, and when not to

Training is the expensive step, so a saved checkpoint is loaded when one matches. What
counts as a match is the question. [[ML4T_A3_0001]] below names every setting that
moves the weights, including [[ML4T_A3_0002]], because [[ML4T_A3_0003]] names the features and the
window and not the bars they are cut from.

The digest matters most on the path a reader is most likely to take. This notebook falls
back to synthetic bars when the Chapter 3 outputs are absent, so a first run trains on
the fallback and a later run, after Chapter 3 has been executed, sees real bars. Without
the digest that second run loads the fallback-trained weights. It also takes the
checkpoint's scaler, while [[ML4T_A3_0004]] above was scaled from the new bars, which
would leave the holdout comparison and the training data on different scales. A digest
mismatch retrains instead, which is the only answer that keeps the two consistent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
## Training Loop
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000

~~~~~~markdown
### Run Training

Execute step-based training. Progress is logged at regular intervals.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
## Training Progress
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>
