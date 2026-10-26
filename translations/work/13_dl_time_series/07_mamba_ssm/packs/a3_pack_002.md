# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/07_mamba_ssm.ipynb；A3 Pack 002；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Test set → 測試集
- Hyperparameter → 超參數

## 待翻譯英文單元

### c0016-p000

~~~~~~markdown
### Selective scan recurrence

Pure-Python implementation of the discrete selective scan: at each step we
discretize [[ML4T_A3_0001]] via zero-order hold using the per-step size [[ML4T_A3_0002]], then
update the hidden state and read the output through the input-dependent
[[ML4T_A3_0003]]. Following the Mamba paper we approximate the input discretization
as [[ML4T_A3_0004]] rather than the full ZOH form.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### Block parameter geometry

[[ML4T_A3_0001]] doubles the channel count to carry both the SSM branch and the
gate branch. [[ML4T_A3_0002]] produces the time-varying [[ML4T_A3_0003]], [[ML4T_A3_0004]], and
[[ML4T_A3_0005]]-raw from the SSM branch itself. [[ML4T_A3_0006]] is a learnable diagonal we
negate before exponentiating so the recurrence is contractive. [[ML4T_A3_0007]] is the
direct skip from input to output.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## Mamba Regressor

Stacks multiple [[ML4T_A3_0001]] layers with an input projection and
a linear head that reads from the last timestep. This mirrors how an
LSTM uses its final hidden state for prediction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0023-p000

~~~~~~markdown
## Train Mamba
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
### Training convergence

The two curves are what the patience rule reads. Training error alone cannot
separate a model that is learning from one that is memorising, because both look
like progress; the validation curve turning up while the training curve keeps falling
is the signal that stops the run. Whether it fires before the epoch cap is something
to read off the figure, not to assume.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## Evaluate on Test Set
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## Ridge Baseline Comparison

Flattening the window into one vector and fitting a penalised linear map gives the
baseline the selective scan has to beat.

The flattened design is [[ML4T_A3_0001]] x [[ML4T_A3_0002]] columns of overlapping
trailing returns, which are strongly collinear: on this capped sample the Gram
matrix has a condition number around [[ML4T_A3_0003]]. scikit-learn's default solver
forms and factorises that matrix and warns that it is ill-conditioned, so [[ML4T_A3_0004]] is
requested instead. It computes the same ridge estimator without forming the normal
equations - the two agree to four significant figures on test MSE - and the warning
has no cause rather than being filtered away.

Note also that [[ML4T_A3_0005]] is fixed at 1, not tuned. That keeps the baseline identical
across this section's notebooks, and it means the bars below compare an untuned
linear map with an under-trained network. Neither is at its best.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
## The selective SSM against the linear baseline

Two questions, two panels. The left asks whether the model ordered the funds usefully
on each date; the right asks whether its predicted return levels were closer than
predicting zero. A model can do better on one and worse on the other, and both are
reported because acting on a forecast uses the ordering while fitting one minimises
the squared error.

The ridge regression sees the same window flattened into one vector and fits a
penalised linear map straight to the label - no state, no selection, no notion that
the columns are ordered in time. Whatever the recurrence is worth has to appear as a
difference from that, within the budget the next paragraph describes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## What the budget lets this comparison say

Both models see the same data: the subsampling above happens before either is fitted,
so the ridge is trained on exactly the sequences the SSM is. What differs is the
fitting. The ridge solution is closed-form and fully converged at its penalty; the
SSM gets at most [[ML4T_A3_0001]] epochs of gradient descent with early stopping, and the
sample is capped at [[ML4T_A3_0002]] in the first place because the pure-Python
scan runs orders of magnitude slower than the production kernel. Neither model got a
hyperparameter search.

So the figure is a record of what these two models did under this budget, and the
subsampling is the constraint that matters most: both scores are computed over the
most recent complete dates that fit the cap, not over the full test stretch. The
coverage counts printed beside each IC say how many dates each average was taken
over, and they are a small fraction of the dates the other notebooks in this section
score on. Read them before reading the bars.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
## Key takeaways

1. **Separate the two claims about cost.** A fixed-size state and bounded work per
   step give [[ML4T_A3_0001]] total work; a recurrent network already has that, and attention
   gives it up by making each step look at every other. Linearity is a different
   property, and what it buys is parallelism: because the update is affine and each
   step's coefficients depend only on that step's input, the sweep composes into an
   associative scan instead of waiting for its own previous output.
2. **"Selective" means three quantities move with the input.** [[ML4T_A3_0002]], [[ML4T_A3_0003]] and
   [[ML4T_A3_0004]] all come out of [[ML4T_A3_0005]] applied to the current input, while [[ML4T_A3_0006]] is a
   learned diagonal fixed for the whole sequence. A fixed-parameter SSM such as S4
   has all four constant, so its state decays on a schedule set at training time
   rather than one the input can change.
3. **[[ML4T_A3_0007]] is the forget control.** It enters as [[ML4T_A3_0008]] with [[ML4T_A3_0009]]
   negative, so a large step shrinks the previous state hard and a small one
   preserves it. Reading that one line is how you see what the model can be trained
   to forget.
4. **The gate is a second, multiplicative path.** [[ML4T_A3_0010]] splits into an SSM branch
   and a gate branch, and the SSM output is multiplied by [[ML4T_A3_0011]] before the output
   projection - the same shape of interaction an LSTM's gates provide, without a
   recurrence in the gate itself.
5. **The comparison here is bounded by the training budget, not just the
   architecture.** The loop-based scan forces a capped sample and a handful of
   epochs, so the figure says what this model does under this budget. Reading it as
   a general result about selective SSMs for return prediction would be reading past
   what was run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>
