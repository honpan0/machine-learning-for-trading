# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/07_mamba_ssm.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# A selective state space model, written out step by step

**Docker image**: [[ML4T_A3_0001]]

[[ML4T_A3_0002]] related the days in a window with one dense [[ML4T_A3_0003]] map, and
[[ML4T_A3_0004]] related every day to every other through attention. Both cost
[[ML4T_A3_0005]], and both gave up the idea that a sequence can be walked once while carrying a
state - the idea [[ML4T_A3_0006]] measured the price of, because a state
updated one day at a time cannot be computed in parallel across days.

A **state space model** takes the recurrence back and changes what is carried. Its
state has a fixed size and each step does a bounded amount of work, so one sweep is
[[ML4T_A3_0007]] - which an LSTM also manages. What the *linear* update adds is that the steps
compose: the recurrence is affine, and each step's coefficients can be computed
without knowing the previous state, so the sweep is an associative scan that runs in
parallel across the sequence instead of a loop that waits for its own output. **Mamba** (Gu and Dao, 2023) adds what makes that
competitive: the matrices reading the input into the state and the state into the
output, and the step size itself, are computed *from the input at that step*. The
model decides what to keep as it goes, which a fixed-parameter SSM cannot.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Learning objectives**:
- Read the discrete recurrence off the code and say which of its terms are constant
  across the sequence and which are functions of the current input.
- Say what "selective" buys over a fixed-parameter SSM, in terms of what the state
  can be made to forget.
- Name the simplifications this implementation makes against the paper, and find
  each one in the code rather than taking the list on trust.
- Score the result against a penalised linear map on the same window, and read the
  comparison for what a capped training budget allows it to say.

**Book Reference**: Chapter 13, Section 13.6 (Alternative architectures and foundation models)

**What this implementation is.** A pedagogical selective SSM in pure PyTorch,
written so the recurrence is readable rather than fast. It carries Mamba's defining
mechanism - [[ML4T_A3_0001]], [[ML4T_A3_0002]] and [[ML4T_A3_0003]] computed from the input at step [[ML4T_A3_0004]] - and
departs from the reference [[ML4T_A3_0005]] package in four ways you can find in the code
below:

- The scan is a Python [[ML4T_A3_0006]] loop over timesteps, not a parallel associative scan in
  a CUDA kernel. The [[ML4T_A3_0007]] work is the same; the constant is roughly a hundred times
  worse, which is why the sample is capped further down.
- [[ML4T_A3_0008]] is one scalar per timestep, shared across all channels: [[ML4T_A3_0009]] emits
  [[ML4T_A3_0010]] values and the last one is the step size. Mamba gives each channel
  its own.
- The input discretization is approximated as [[ML4T_A3_0011]] rather
  than the full zero-order-hold expression.
- There is no depthwise causal convolution before the SSM branch, which the paper's
  block includes.

Read it as a sketch of the selective-state-space idea, not as a drop-in replacement.

**Prerequisites**: ETF features ([[ML4T_A3_0012]])
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## Data Loading

We use eight fixed momentum horizons from the ETF case-study pipeline.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## Sequence Creation and Temporal Split
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Splitting by date, with a gap for the label horizon

The split is by date, at fixed fractions of the trading days, and an example belongs
to the partition the date it carries falls in. The label is a [[ML4T_A3_0001]]-day
forward return, so an example dated within that many days of a boundary has an
outcome resolved by days on the far side; those examples are dropped. Input windows
may still reach back over a boundary, which is right - at decision time the model has
every past observation available.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Pedagogical subsampling

The pure-Python selective scan is roughly 100× slower than the production
CUDA kernel, so we cap each split at a few thousand sequences for tractable
wall-clock. Critically we subsample by **complete dates**, not row-count: a
raw [[ML4T_A3_0001]] slice would start mid-date and leave a partial
cross-section, which biases the per-date Spearman IC. We instead keep the
most recent dates whose total row count fits under the cap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Cross-sectional IC helper

The same per-date rank correlation used across this section, so the architectures
are compared on one number.

A date's IC is undefined when a model predicts the same value for every fund on it:
the predicted ranks are all tied and there is nothing to correlate. The library
returns [[ML4T_A3_0001]] for such a date, and polars treats [[ML4T_A3_0002]] and null as different values,
so [[ML4T_A3_0003]] alone leaves it in place and one of them makes the whole mean [[ML4T_A3_0004]].
Both are filtered here, and the count of dates the mean was taken over is printed
beside it - which matters more here than elsewhere in the chapter, because the
subsampling below leaves far fewer dates to average over.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Selective state space - what the code computes

At each timestep [[ML4T_A3_0001]] we discretize a continuous-time SSM via zero-order
hold and run an input-dependent recurrence on a hidden state [[ML4T_A3_0002]]. In
Mamba the matrices [[ML4T_A3_0003]], [[ML4T_A3_0004]] and step size [[ML4T_A3_0005]] are functions of
the input [[ML4T_A3_0006]] (the **selective** ingredient), while [[ML4T_A3_0007]] is a learned
diagonal that stays time-invariant. The state update and output are:

[[ML4T_A3_0008]]
[[ML4T_A3_0009]]

The full continuous-time formulation and the derivation of ZOH live in
Section 13.6; this notebook focuses on the discrete recurrence as
implemented in [[ML4T_A3_0010]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
## Selective SSM Block

The block is read in three pieces - the recurrence itself, the shapes its
constructor sets up, and the gated forward pass - so each stands on its own.

> **Runtime warning**: [[ML4T_A3_0001]] uses a Python [[ML4T_A3_0002]] loop over
> [[ML4T_A3_0003]], making it ~100× slower than the production Mamba CUDA kernels.
> Expect several minutes on the full ETF dataset. This is intentional: the
> loop exposes the recurrence mechanics that hardware-efficient kernels hide.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>
