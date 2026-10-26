# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/13_regime_as_feature.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Clustering → 分群
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Regime as Feature

**Chapter 9 | Section 9.5**

**Docker image**: [[ML4T_A3_0001]]

The last three notebooks built regime labels and probabilities. This one spends them, and
the question is not whether the regime is real but how a predictive model should receive it.
Two designs are available and they differ in what happens when the regime call is wrong.

Give the model the regime probability as one more column and it stays one model, fitted on
every session, free to use the column or ignore it. Split the training data by regime and
fit one model per state, and each model sees only its own regime's sessions and a
misclassified session at prediction time is routed to a model that never saw its kind.

The comparison only means something if the regime feature is built the way it would be in
production, which is the constraint that shapes the whole notebook: the hidden Markov model
is refit inside every fold, on the training block alone, and the probabilities it produces
come from a forward recursion that conditions on the past.

**Learning objectives**

- Build a regime feature inside a walk-forward loop, so that no fold's feature was fitted
  on that fold's test block.
- Fit the same predictive model with and without that feature and read the difference
  against the spread across folds rather than as a single number.
- Build the mixture-of-experts alternative and see what splitting the training data costs.
- Read a feature importance that comes out near zero, and say what it does and does not
  tell you about the feature.

**Book reference**

Chapter 9, Section 9.5 (Regime features).

**Prerequisites**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

[[ML4T_A3_0001]] for the hidden Markov model and for the filtered-against-smoothed
distinction. [[ML4T_A3_0002]] for the clustering alternative.
[[ML4T_A3_0003]] for why the folds below carry a gap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## The data and the target

SPY daily closes and the volatility index, joined on the session. The features are the ones
a reader has already met: the return, a rolling standard deviation of it, two momentum sums
over different lengths, and the volatility index measured against its own recent level so
the column is comparable across two decades in which the index's average moved.

The target is the sum of the next [[ML4T_A3_0001]] returns. It reaches that many sessions
into the future, which is what makes the gap in the folds below necessary: a training block
ending at session [[ML4T_A3_0002]] contains targets built from returns up to [[ML4T_A3_0003]] (the rolling sum at
[[ML4T_A3_0004]], shifted back by the horizon, is [[ML4T_A3_0005]]), so a test block
starting at [[ML4T_A3_0006]] would be predicting sessions its own training labels already saw.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## The regime feature, built one fold at a time

This is the cell the notebook exists for. [[ML4T_A3_0001]] gives five expanding training
blocks, each followed by a test block, and a gap of [[ML4T_A3_0002]] sessions between them
so no training target overlaps a test session. Inside each fold:

1. The hidden Markov model is fitted on the training block's returns and volatility, from
   several starts, keeping the fit with the highest training likelihood. Nothing from the
   test block enters the fit.
2. Its states are renumbered by fitted variance, so state one is the more volatile one in
   every fold. Expectation maximization returns states in an arbitrary order, and a feature
   named for one of them means different things across folds without this step.
3. Filtered probabilities are computed by forward recursion over every session up to the end
   of the test block. The recursion at session [[ML4T_A3_0003]] conditions on sessions up to [[ML4T_A3_0004]], and the
   parameters it uses were fitted on the training block, so a test-block value is a quantity
   that could have been computed on the day.

What this costs is that the feature is not one column but five, one per fold, and they
disagree with each other on the sessions they share. That is the honest situation: a regime
probability is a function of what had been fitted at the time, and the number a reader sees
for a given session depends on which fold asked.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The mean probability of the volatile state differs across the test blocks, which is what a
regime feature is supposed to do, and the fold covering 2020 is the one to check that
against. The restart column should be read too: a fold where restarts failed is a fold whose
feature came from fewer starting points than the others.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0010-p000

~~~~~~markdown
## Three designs, one loop

Every design sees the same folds, the same features and the same fold-local regime feature.
They differ only in what they do with it.

- **Baseline** fits one model on [[ML4T_A3_0001]] and never sees the regime.
- **Regime as feature** fits one model on [[ML4T_A3_0002]] plus the filtered probability of
  the volatile state.
- **Mixture of experts** fits one model per hard state on [[ML4T_A3_0003]] alone, using the
  training block's states to split the training rows, and routes each test session to the
  model for its own state. A state with fewer than [[ML4T_A3_0004]] training rows
  gets no model of its own, and its test sessions fall back to the other one.

The scaler is refitted on each fold's training block and applied to the test block, which
matters more than it looks: a scaler fitted on the whole sample carries the test block's
mean and variance into the training data, and does it silently.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0013-p000

~~~~~~markdown
Read the spread column before the mean. The five folds cover different market conditions, and
the error moves between folds by roughly an order of magnitude more than it moves between
designs. That is the first thing the table says, and it is the reason a single averaged number
with no spread beside it would mislead.

The r squared column is the other thing to read, and it is negative or close to zero
throughout. A negative r squared means the model predicts the test block worse than that
block's own mean would, which is the normal outcome for a five-session return forecast from
five features and is why the chapter treats regime information as conditioning rather than
as a signal.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
