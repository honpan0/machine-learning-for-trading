# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/09_dl_lstm.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Sequence Models

This notebook evaluates the declared NLinear and LSTM sequence configurations. Each input window
contains observations from one product and ends before its prediction timestamp. Purge gaps and
fold boundaries prevent a sequence from crossing into another validation interval, and hidden
state does not pass between products or folds.

Every declared epoch checkpoint is published with fitted weights and exact chronological
eligibility. MC dropout is not an undeclared side experiment. Configuration selection remains the
validation backtest decision in [[ML4T_A3_0001]].

Prerequisites: [[ML4T_A3_0002]], [[ML4T_A3_0003]], and [[ML4T_A3_0004]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What a sequence model reads that the other families do not

Every family up to this point saw one row per product per decision: a vector of features
describing that product at that moment. Anything about how it got there had to be engineered
into a column - a 21-session volatility, a momentum composite, a carry z-score against a
rolling window. The model saw the summary, never the path.

A sequence model reads the path. Its input is a window of consecutive observations for one
product, and the architecture is built to make use of their order. The claim being tested is
that the shape of recent history carries information that no fixed set of summary statistics
captured - that a product whose carry rose steadily to its current level differs from one that
spiked and fell back, even where both end at the same value with the same 21-session
volatility.

For thirty futures products the windows are also the scarcest data in the case study. A
feature-row model gets one training example per product per session; a sequence model needs a
whole window per example, so the same history yields fewer independent examples and they
overlap heavily with each other. That is the structural reason to expect these models to
struggle here relative to a benchmark with millions of series, and it is worth holding
alongside whatever the backtest reports.

### Two architectures, and why both

**LSTM** processes the window one step at a time, carrying a hidden state forward and learning
what to keep and what to forget. It is the general answer, and its generality is the cost: it
has many parameters, it trains slowly, and on a short noisy series it has ample capacity to
memorize.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

**NLinear** is close to the opposite. It is a linear map from the window to the forecast, with
a normalization step that subtracts the window's last value before the map and adds it back
afterwards. That subtraction is the whole idea: it makes the model predict the *change* from
where the series currently sits rather than the level, which removes the drift that otherwise
dominates a naive fit.

It is here because a body of recent work found that simple linear baselines matched or beat
elaborate sequence architectures on many forecasting benchmarks once evaluated carefully - a
finding that survived enough scrutiny to be worth designing around. Running both is what turns
"the sophisticated model should win" into something this case study measures rather than
assumes.

## Where a sequence model can leak, and what stops it

A window is a span of time rather than a point, which gives leakage more places to enter than
the other families have.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

- **Each window ends before its prediction timestamp.** The last observation a window contains
  is strictly earlier than the moment being predicted, so a forecast never reads the bar it is
  forecasting.
- **Purge gaps and fold boundaries stop a window crossing into another interval.** Without them
  a window ending just after a fold boundary would extend back across it, and validation rows
  would be predicted from a window overlapping the training period. The failure would be
  invisible in the output: the prediction is dated correctly and the returns are real.
- **Hidden state does not pass between products or folds.** An LSTM's state accumulates
  whatever it has seen, so carrying it across a boundary carries information across that
  boundary too - and unlike a feature column, the state never appears in any frame, so nothing
  downstream could detect it.

The three are separate mechanisms rather than one guarantee stated three times, which is why
they are enforced separately rather than by a single check on the output.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>

### c0004-p000

~~~~~~markdown
## Declared requests

The request rows identify architecture, label, and published configuration. Sequence length,
checkpoint schedule, seed, gap policy, and device enter the resolved computation identity.

**The device is declared here rather than inherited.** With no override the shared sequence
adapter falls back to a literal [[ML4T_A3_0001]] written in [[ML4T_A3_0002]], and
resolving the request raises [[ML4T_A3_0003]]
rather than quietly moving the fit to the CPU. That refusal comes from resolving the request, so
it arrives before any fitting starts. Stating it in the request puts that requirement where a
reader meets it instead of two layers below. The resolved specification hash is the same with the
override as without, so this names what the published run already did.

The device is part of what the fitted model is, not a note beside it: the same architecture
trained on a GPU and on a CPU accumulates its sums in different orders and reaches different
weights. [[ML4T_A3_0004]] is the device this population was fitted on, and the canonical
population accepts no other. A reader without an NVIDIA card sets [[ML4T_A3_0005]] and passes a
[[ML4T_A3_0006]] to fit the same grid into a population of its own, which the backtest does
not read.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>
