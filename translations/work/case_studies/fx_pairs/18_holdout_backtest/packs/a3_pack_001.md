# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/18_holdout_backtest.ipynb；A3 Pack 001；單元 5 個。


## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Holdout Backtest - FX Pairs

This notebook runs the selected configuration's own backtest specification against the holdout
predictions [[ML4T_A3_0001]] registered. It changes nothing about the strategy: signal,
allocation, risk controls, rebalance rule, costs and account configuration are the selected
configuration's registered specification. What does change is what the specification points at -
the prediction set, and the price frame identity, which names the holdout frame the run actually
reads.

Keeping this separate from the refit is what makes the holdout diagnosable. While the two ran
as one transaction, a failure in the backtest half discarded the model half with it, and the
retrain needed to investigate was the exact thing the transaction forbade.

**Learning objectives**

- Replay one registered strategy specification against a new prediction set.
- Distinguish reproducing a strategy from re-choosing one.
- Read a holdout result without letting it revise anything upstream.

**Book reference**: Chapters 16-20

**Prerequisite**: [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Resolve the same configuration, and require its holdout predictions

The selected configuration is re-resolved here rather than handed over from the previous
notebook. The resolution is a query against registered validation backtests, so it returns the
same configuration; passing it through a file or a parameter would add a way for the two
notebooks to disagree without either being wrong about anything it did itself.

What this notebook cannot derive is whether the refit has run. When it has not, the missing
result is named rather than reported as an empty query.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## Run the selected configuration on the holdout

The specification is the selected configuration's own registered one with the prediction set
re-pointed and the chapter re-tagged. Nothing else is rebuilt from this notebook's defaults,
because a holdout number is only comparable to its validation number when the only difference
between the two runs is the interval they cover.

The price frame is loaded with the strategy's own warmup, read from the specification rather
than assumed. [[ML4T_A3_0001]] does not trim the lower bound for exactly this reason - it names
[[ML4T_A3_0002]], which is this configuration's allocator, among the rolling estimators whose
callers are expected to load a prefix - and it slices the returns frame to the window
afterwards, so the warmup rows extend what the allocator can see without extending what is
measured.

On this configuration they change nothing: the holdout return series is bit-identical with and
without the 63-observation prefix, so the number below does not depend on this. It is loaded
anyway because the specification asks for it, and a run that silently ignores a declared
warmup is only correct by accident.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Validation and holdout, side by side

Both rows are printed without interpretation. Whether the difference between them is evidence
of anything is [[ML4T_A3_0001]]'s question, and answering it needs the candidate
distribution and the interval evidence - neither of which belongs in a notebook whose job is
to produce one result.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## Key takeaways

- The configuration run here is the selected configuration's registered specification, not
  a strategy rebuilt from this notebook's own defaults.
- The holdout prediction set is matched by the training identity derived here, not by the
  configuration's family and name, which several training specifications share.
- The price frame carries the strategy's declared warmup. It makes no difference to this
  configuration's result, which is a measurement rather than an assumption.
- Nothing here revises the selection, which was made on validation and is already registered.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>
