# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/18_holdout_predictions.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Training set → 訓練集
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: Holdout Predictions

**Chapter 20 - Out-of-sample evaluation**

Every number in this case study so far was measured on the validation folds, and every
choice was made by looking at them: which model family, which configuration, how many
funds to hold, how to size them, which risk control to overlay, what to charge. A result
selected that way cannot also be evidence that the selection was sound - the ranking and
the evidence would be the same measurement.

The holdout is the window nothing has been selected on. This notebook fits the selected
configuration on the history available before that window opens and writes its
predictions over it. [[[ML4T_A3_0001]]](19_holdout_backtest.ipynb) turns those
predictions into a return series with the sizing and the overlay the case study settled
on, and [[[ML4T_A3_0002]]](20_strategy_analysis.ipynb) reads both back.

**What this notebook is careful about**

A holdout prediction is not the validation model scored on a later window. Section 2
fits again, over a training interval that ends before the window opens, and the new
training identity is what makes the refit visible rather than asserted: the identity
covers the CV interval, so a run that came back with the validation training hash would
mean no refit happened. The check is in section 3 and it raises.

**Prerequisites:** [[[ML4T_A3_0003]]](17_costs.ipynb), which is the last stage that selects.

**Scope:** one training run and one prediction set. No backtest, no selection, no
comparison - those are 19 and 20.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Which configuration the holdout runs

The holdout runs the configuration the case study reports, resolved through the same
[[ML4T_A3_0001]] [[[ML4T_A3_0002]]](17_costs.ipynb) prices. Resolving it again here
rather than passing it along is deliberate: the two notebooks must agree by construction,
and a hash written down in one and read in the other agrees only until the sweep is
rebuilt.

Nothing about the holdout enters this choice. The selected configuration is the cross-stage
validation rank-1 - which for this case study is a risk-overlay run, not the allocation leader -
and it was fixed before this notebook ran.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The checkpoint is part of the configuration. Where a family publishes a prediction set per
checkpoint on a declared schedule, the selected configuration's prediction set names one of them,
and refitting without it would produce a model at the end of training rather than the one that
was ranked. A family with no checkpoint dimension stores NULL in both columns and carries that
NULL through unchanged.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 2. The window, and the model that is allowed to see it

The holdout window is not a choice made here. It is [[ML4T_A3_0001]] and
[[ML4T_A3_0002]] from this case study's own [[ML4T_A3_0003]], read through the same
[[ML4T_A3_0004]] the fold derivation and the backtest slice both go through, so the three
cannot disagree.

The training interval is everything available before that window, bounded above by a label
buffer. **For this case study the buffer is doing real work.** The label is a 21-day forward
return, so a row dated [[ML4T_A3_0005]] records an outcome that is not known until [[ML4T_A3_0006]] sessions - and
a training set running to the day the window opens would be fitted on labels whose returns
resolve inside it. The buffer is therefore a horizon's worth rather than a formality, and the
derivation refuses to default it: a zero gap here would be a leak.

Everything else about the configuration is carried across unchanged, and the fields that
cannot be - the eligibility manifest, and any parameter this family resolves from a fold's
own training rows - are recomputed against the holdout fold. Carrying those forward would fit
a model keyed to the validation folds and call it a retrain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 3. Fit, and register the predictions

[[ML4T_A3_0001]] builds the request from the spec above. Its name comes
from a locked holdout path this case study does not use; it takes a training specification
and a checkpoint, not a lock, and it is used here because it is the one call that refuses a
request that is not exactly the spec it was handed - the training identity, the checkpoint
schedule, the feature lineage and the runtime parameters are all checked before anything is
fitted.

The training identity below is new. It has to be: it covers the CV interval, and the holdout
fold is not one of the validation folds. A run that came back with the validation training
hash would mean the refit did not happen, so that is checked rather than assumed.

**The window carries one configuration, and this notebook has no way past that.** The check below
is on the selected configuration rather than on the notebook, and it has exactly two outcomes.
With the selected configuration unchanged this is an idempotent replay: the derivation is
deterministic and the training identity covers it, so the same identity comes back and the fit is
served from the registry, which is why re-running the notebook is free and safe. With the
selected configuration changed it refuses, names both configurations, and stops.
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

### c0013-p000

~~~~~~markdown
What the prediction set covers, read back from the registry rather than from the request.
The two agree only if the fit published what it declared, and the counts are what a reader
checks the window against: this is a daily panel, so the date count is trading sessions in
the window and the row count is those sessions times the funds eligible on each.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
Every holdout prediction set the registry holds, and whether the model behind it was
refitted for the window. All of them are listed rather than one silently preferred, because
the registry is immutable and a reader looking at it later will see whatever is there. A row
marked VALIDATION-FITTED is not an out-of-sample result whatever its numbers say.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>
