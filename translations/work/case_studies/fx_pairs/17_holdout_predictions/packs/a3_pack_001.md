# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/17_holdout_predictions.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Holdout Predictions - FX Pairs

This notebook refits the one configuration validation selected, on the holdout interval, and
registers its predictions. It writes predictions and nothing else: the backtest is
[[ML4T_A3_0001]], and what any of it is worth is [[ML4T_A3_0002]].

Selection is not a parameter and is not made here. [[ML4T_A3_0003]] reads the
highest-Sharpe registered validation backtest across the baseline, allocation and risk-overlay
stages, restricted to runs that stayed solvent, so this notebook cannot select a configuration
the validation stages did not already rank first.

The holdout is not a one-shot transaction and nothing here pre-registers it. There is no lock,
no seal and no gate: the whole rule is retrain the selected configuration on everything up to
the holdout window, predict, and backtest that same configuration on the result. Re-running is
therefore ordinary. A reader who runs it five hundred times and quotes the best number has
produced something uninterpretable, and that is a property of what they did rather than
something the software can prevent - the earlier design tried to, and bought
unfixability: a holdout found to be wrong after a bug fix could not be corrected, because the
lock was by construction the one artifact that could not be revised.

**Learning objectives**

- Derive a holdout interval from the panel's observation grid rather than the calendar.
- Reconstruct one training identity from an immutable validation specification.
- Register holdout predictions without giving them any influence over selection.

**Book reference**: Chapters 16-20

**Prerequisite**: [[ML4T_A3_0004]]. The selected configuration is resolved from the registered
validation backtests, so every stage that registers one must have run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Resolve the selection and the holdout interval it determines

The label the selection was made on decides which observation grid the holdout interval is
stepped back along, so it is read from the selected lineage rather than assumed. FX carries
three labels on one daily grid, which is exactly the coincidence that would let an assumption
here survive untested.

The training window ends a whole label buffer, counted in observations, before the holdout
opens, so the last training label's outcome cannot resolve inside the holdout. The buffer is
the widest this case study configures rather than the primary label's: a 21-day forward return
resolves three weeks after the session it is stamped on, and a 1-day buffer would leave three
weeks of holdout outcomes reachable from the training window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## Refit the selected configuration on the holdout fold

The request is reconstructed from the immutable validation specification with only the fold
geometry re-keyed, so the holdout model differs from the validation model in what it was
fitted on and in nothing else. It publishes the selected checkpoint alone: a holdout refit
that published its whole checkpoint schedule would hand the next notebook a choice, and
choosing among holdout checkpoints is selection on the holdout under another name.

The one thing checked afterwards that a specification cannot state about itself is that this
is a refit at all. A holdout training identity equal to the validation one means the fold
re-keying changed nothing, and the model is a validation fit predicting forward over a later
window rather than a model trained up to it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## What the holdout refit covers

The coverage is printed rather than assumed: a holdout prediction set that silently covers a
shorter window than the fold declares would make every number downstream a measurement of a
different interval than the one this notebook says it measured.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## Key takeaways

- The configuration refitted here was selected on validation, from an immutable set, upstream.
- The holdout training window stops a full label buffer short of the holdout, counted in
  observations rather than calendar days.
- Only the selected checkpoint is published, so no choice among holdout results remains to be
  made downstream.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>
