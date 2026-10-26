# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/04_model_based_features.ipynb；A3 Pack 003；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0017-p000

~~~~~~markdown
### Fitting the model, and keeping the states comparable

Four practical problems come with this model. Three are handled by helpers shared across the
case studies in [[ML4T_A3_0001]], and the fourth is the schedule itself.

The first is that fitting is a local search. The algorithm improves an initial guess until it
stops improving, and where it stops depends on where it started, so a poor start returns a
poor description of the data. [[ML4T_A3_0002]] starts the state distributions from a
k-means partition of the observations, which is a guess the data chose, and [[ML4T_A3_0003]]
repeats it from several starting points, keeping the one with the highest likelihood. That loop
used to live in this notebook; [[ML4T_A3_0004]] and [[ML4T_A3_0005]] each wrote their own, so it
now lives in the shared module and this notebook declares how many starts it wants. The restarts
earn their cost: measured on this panel, ten of them give ten distinct log-likelihoods, spread
2.31 nats at the first refit block, so the k-means start does not land every seed in the same
place.

The second is that the states come back in an arbitrary order. Nothing in the algorithm says
which of the two is state zero, so the same fitted regime can be state zero at one refit and
state one at the next - and a feature named for one of them would then mean different things
in different stretches of the series. [[ML4T_A3_0006]] puts them in a fixed order by
how dispersed each state's observations are, so state zero is always the calm one and state
one always the stressed one. The ordering is applied inside the block that fitted the model,
which is the only place it can be applied consistently.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0017-p001

~~~~~~markdown

The third is that a seeded fit is not yet a reproducible fit. Both k-means and the
expectation-maximisation steps behind it sum over the observations in parallel, and addition
in floating point is not associative, so the total depends on how the work was divided between
threads. On this data that moves the fitted parameters in their last few digits, which moves
the emitted probabilities by around [[ML4T_A3_0001]] - invisible in any printed table and enough to
change the content digest of the saved file, so that two runs of identical code produce
artifacts that cannot be shown to be the same. [[ML4T_A3_0002]] pins the thread pool to
one for the duration of the fit, and the fit then reproduces exactly whatever else the machine
is doing.

The fourth is the one section A named. [[ML4T_A3_0003]] refits on the declared schedule
and hands each fitted model the prefix of the series up to the end of the block it speaks for;
[[ML4T_A3_0004]] then runs it forward through that prefix, so the probability reported
for a session is conditioned on that session and everything before it. The library's own
convenience methods return the smoothed probabilities, conditioned on the whole window
including sessions that had not happened yet, and the same is true of its [[ML4T_A3_0005]], which
returns the single most likely state *sequence* and so decides each session's state partly
from what came after it. Neither can be a feature.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p001>>>
<<<ML4T-ZH-END:c0017-p001>>>

### c0019-p000

~~~~~~markdown
The regime probability is the quantity the walk emits. The other two regime features are
derived from it afterwards, over the whole emitted series rather than block by block, because
both are running statistics: the transition size is the change from the previous session and
the duration is a count of how long the prevailing state has held. Deriving them per block
would restart both at every refit boundary, which is the defect the per-fold design had at
every fold boundary. Each still reads only the sessions before it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
Two properties are asserted rather than described. No parameter set may be estimated from a
session inside the holdout, which is the freeze; and every emitted value must come from a
block whose fit window ended before the first session it speaks for, which is the schedule.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
### What the model inferred, on validation sessions

The shading is the filtered probability of the stressed state on the sessions the folds
validate on - the same quantity the saved feature carries, restricted to the sessions the
evaluation at the end is allowed to read. Every shaded band was produced by parameters
estimated before it.

The holdout is not drawn. Its features are computed and saved like every other session's, but
looking at them now is the use the holdout is held back from, and the evaluation at the end
excludes them for the same reason.

The bands mark where the probability of the stressed state exceeds one half. That threshold
is a reading aid for the figure only; the emitted feature is the probability itself and
nothing downstream compares it to a cutoff.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### C.2 Fractional differencing

A price series is not stationary: its mean wanders, so a model fitted on one stretch of it
describes a different distribution from the one that generated the next stretch. The usual
repair is to take returns - to difference the log price once - which is stationary but throws
away the level entirely. Everything the series remembered about where it had been is gone.

**Fractional differencing** interpolates between the two. Differencing by an order [[ML4T_A3_0001]] between
zero and one applies a weighted sum of all past values, with weights that decay as they reach
further back; at [[ML4T_A3_0002]] nothing is removed and the series is the log price, at [[ML4T_A3_0003]] it is
the log return, and in between enough of the trend is removed to make the series stable while
some of the memory is left.

The orders are fixed in advance rather than searched for. Choosing [[ML4T_A3_0004]] per series by testing
which value passes a stationarity test would make the transform depend on the data it is
applied to, which is the estimation channel section A described. A fixed order is purely
mechanical, so no part of it can read the future, and nothing about it needs a schedule: the
filter is applied once over each series' whole history. It is a fixed-weight causal filter,
so a value at a session is the same number whether the series it was computed over stops that
day or runs another decade. Rate-sensitive bond and credit funds get the higher order because
their log prices carry a stronger trend; the check below is what says whether that is enough.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
