# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/17_holdout_predictions.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto Perpetuals Funding: Holdout Predictions

**Chapter 20 - Out-of-sample evaluation**

Every number this case study has reported was measured on the validation folds, and every
choice was made by looking at them: the label, the model family, the entry rule, the
allocator, the risk control. A result selected that way cannot also be the evidence that
the selection was sound, because the ranking and the evidence would be the same
measurement.

The holdout is the window nothing has been selected on. This notebook fits the selected
configuration on the history that ends before that window opens and writes its predictions
over it. [[[ML4T_A3_0001]]](18_holdout_backtest.ipynb) turns those predictions into a
return series with the sizing and the overlay the case study settled on, and
[[[ML4T_A3_0002]]](19_strategy_analysis.ipynb) reads both back.

**What this notebook is careful about**

A holdout prediction is not the validation model scored on a later window. Section 3 fits
again, and the new training identity is what makes the refit visible rather than asserted:
a run that came back with the validation training hash would mean no refit happened, and
it raises.

**Prerequisites:** [[[ML4T_A3_0003]]](16_costs.ipynb), which is the last stage that could still
move the selection.

**Scope:** one training run and one prediction set. No backtest, no selection, no
comparison - those are 18 and 19.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## 1. Which configuration the holdout runs

The holdout runs the configuration the case study reports. [[ML4T_A3_0001]]
applies the selection rule this case study's funnel already implements: compare the
registered validation backtests across the signal, allocation and risk stages, and take
the highest Sharpe. It is resolved here rather than passed in from
[[[ML4T_A3_0002]]](16_costs.ipynb), so the two agree by construction rather than by a hash
copied between them.

The two routes to that configuration were checked against each other rather than assumed
to agree: this resolver and the [[ML4T_A3_0003]] candidate sets that
[[[ML4T_A3_0004]]](15_risk_management.ipynb) freezes return the same backtest.

Nothing about the holdout enters this choice. The selected configuration was fixed before this
notebook ran.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The checkpoint is part of the configuration. Families that checkpoint through training publish
one prediction set per declared iteration, and the selected configuration's prediction set names
one of them - so refitting without it would produce a model at the end of training rather than
the one that was ranked. A family that checkpoints once carries nulls here, and passing them
through unchanged is what keeps the lookup exact either way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 2. The window, and the model that is allowed to see it

The holdout window is not a choice made here. It is [[ML4T_A3_0001]] and
[[ML4T_A3_0002]] from this case study's own [[ML4T_A3_0003]] - 2024 and 2025 - read
through the same [[ML4T_A3_0004]] the fold derivation and the backtest slice both go
through, so the three cannot disagree.

The training interval is everything available before that window, bounded above by a label
buffer. The buffer is what stops the last training label's outcome from resolving inside
the holdout, and here it is a real horizon rather than a formality: these labels are
forward returns over 8 and 24 hours, so a row observed at the last training timestamp is
still unrealised for a full horizon after it. The derivation takes the widest declared
horizon across the case study's labels and refuses to default it - a zero gap would be a
leak, not a conservative choice.

Everything else about the configuration is carried across unchanged, and the fields that
cannot be - the eligibility manifest, and any parameter this family resolves from a fold's
own training rows - are recomputed against the holdout fold. Carrying those forward would
fit a model keyed to the validation folds and call it a retrain.
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

The training identity below is new. It has to be: it covers the CV interval, and the
holdout fold is not one of the validation folds. A run that came back with the validation
training hash would mean the refit did not happen, and the check after it raises.

**The window carries one configuration at a time.** The holdout is re-runnable, and that is
not the same as free: every configuration evaluated on it is another look at a period the
case study reports as unseen, and two evaluated quietly would make that report false.

So the check below is on the selected configuration rather than on the notebook, and it has
exactly two outcomes. With the selected configuration unchanged this is an idempotent replay: the
derivation is deterministic and the training identity covers it, so the same identity comes back
and the fit is served from the registry. With the selected configuration changed it refuses,
names both configurations, and stops.

[[ML4T_A3_0002]] is the only way past that, and it is a replacement rather than an
addition: the superseded generation's rows are deleted, so the registry never holds two
refits of the holdout window and no downstream resolver has to choose between them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0013-p000

~~~~~~markdown
What the prediction set covers, read back from the registry rather than from the request.
The two agree only if the fit published what it declared, and the counts are what a reader
can check the window against: perpetual funding settles every eight hours, so two years is
on the order of two thousand decision timestamps, and the row count is those timestamps
times the names eligible at each. The panel is unbalanced - assets enter at listing - so
the name count is an upper bound rather than a constant.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
Every holdout prediction set the registry holds, and whether the model behind it was
fitted for this window. Both are listed rather than one silently preferred: the registry is
immutable, and a reader looking at it later sees whatever is there.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>
