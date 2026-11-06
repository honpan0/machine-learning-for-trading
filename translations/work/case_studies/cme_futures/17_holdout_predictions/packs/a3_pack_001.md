# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/17_holdout_predictions.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Holdout Predictions

**Chapter 20 - Out-of-sample evaluation**

Every number in this case study so far was measured on the validation periods, and every
choice was made by looking at them: which model family, which configuration, how the
positions are sized, whether a risk overlay earns its place. A result selected that way
cannot also be evidence that the selection was sound - the ranking and the evidence would
be the same measurement.

The holdout is the window nothing has been selected on: 2024-01-01 to 2025-12-31. This
notebook fits the selected configuration on the history available before that window
opens and writes its predictions over it.
[[[ML4T_A3_0001]]](18_holdout_backtest.ipynb) turns those predictions into a return
series with the sizing this case study settled on, and
[[[ML4T_A3_0002]]](19_strategy_analysis.ipynb) reads both back.

**What this notebook is careful about**

A holdout prediction is not the validation model scored on a later window. Those two
differ in what the model saw while fitting, and only the first is out of sample. Section
3 fits again, and the new training identity is what makes the refit visible rather than
asserted - a run that came back carrying the validation training hash would mean no refit
happened.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

There is a second thing this case study had to fix before the refit could mean anything.
[[ML4T_A3_0001]] fits ARIMA and a hidden Markov model per period, so a period
the file never wrote carries no forecast and no regime probability. The holdout period
was being appended to the fold spec without those features being generated for it, which
left a model reading two of nine features over the window it is judged on. The artifact
now carries a holdout vintage: coefficients estimated at the last session before the
window opens, rolled forward across it frozen.

**Prerequisites:** [[[ML4T_A3_0002]]](16_costs.ipynb), which fixes the configuration the
holdout runs.

**Scope:** one training run and one prediction set. No backtest, no selection, no
comparison - those are 18 and 19.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## 1. Which configuration the holdout runs

The holdout runs the configuration the case study reports, resolved through the same
[[ML4T_A3_0001]] [[[ML4T_A3_0002]]](16_costs.ipynb) uses. Resolving it again here
rather than passing it along is deliberate: the two notebooks must agree by construction,
and a hash written down in one and read in the other agrees only until the sweep is
rebuilt.

Nothing about the holdout enters this choice. The selected configuration is the validation
rank-1, and it was fixed before this notebook ran.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The checkpoint is part of the configuration, and it is read from the selected configuration's own
prediction set rather than assumed. Every family this case study fits publishes at the
end of training, so the value here is [[ML4T_A3_0001]] and carries no iteration - but reading it
is what keeps that true rather than asserted: a family that later publishes on a
schedule would name one of its checkpoints here, and refitting without it would produce
the model at the end of training instead of the one that was ranked.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 2. The window, and the model that is allowed to see it

The holdout window is not a choice made here. It is [[ML4T_A3_0001]] and
[[ML4T_A3_0002]] from the case study's own [[ML4T_A3_0003]], read through the same
[[ML4T_A3_0004]] the fold derivation and the backtest slice both go through, so the
three cannot disagree.

The training interval is everything available before that window, bounded above by a
label buffer. The buffer is what stops the last training label's outcome from resolving
inside the holdout: this case study dates each row by the session the decision is taken
on and the label looks forward from there, so a row dated inside a horizon's reach of
2024-01-01 has its outcome realised in the holdout. The buffer is therefore a horizon's
worth of sessions - 5 for [[ML4T_A3_0005]], 21 for [[ML4T_A3_0006]] - and the derivation seals
on the widest of the declared labels rather than on the one being fitted, so no label
can reach past its own boundary. A zero gap would be a leak, not a conservative choice,
so the derivation refuses to default it.

Everything else about the configuration is carried across unchanged, and the fields that
cannot be - the eligibility manifest, and any parameter this family resolves from a
fold's own training rows - are recomputed against the holdout fold. Carrying those
forward would fit a model keyed to the validation folds and call it a retrain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 3. Fit, and register the predictions

[[ML4T_A3_0001]] builds the request from the spec above. Its name
comes from the locked holdout path this case study no longer uses; it takes a training
specification and a checkpoint, not a lock, and it is used here because it is the one
call that refuses a request that is not exactly the spec it was handed - the training
identity, the checkpoint schedule, the feature lineage and the runtime parameters are
all checked before anything is fitted.

The training identity below is new. It has to be: it covers the CV interval, and the
holdout fold is not one of the validation folds. A run that came back with the
validation training hash would mean the refit did not happen.

**The window carries one configuration at a time.** The holdout is re-runnable, and that
is not the same as free: every configuration evaluated on it is another look at a period
the case study reports as unseen, and two evaluated quietly would make that report false.

So the check below is on the selected configuration rather than on the notebook, and it has
exactly two outcomes. With the selected configuration unchanged this is an idempotent replay: the
derivation is deterministic and the training identity covers it, so the same identity comes back
and the fit is served from the registry. With the selected configuration changed it refuses,
names both configurations, and stops.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0010-p001

~~~~~~markdown

It refuses rather than offering a replacement switch, and the reason is that a replacement
would not be one. Deleting the earlier generation's rows does not undo having observed its
result: the selection that produced the new configuration may have been informed by the old
holdout number, and no deletion reaches that. A switch here would let the case study take a
second look at the window while leaving a registry that shows only one, which is the
specific thing that would make the out-of-sample claim false rather than merely weak.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p001>>>
<<<ML4T-ZH-END:c0010-p001>>>
