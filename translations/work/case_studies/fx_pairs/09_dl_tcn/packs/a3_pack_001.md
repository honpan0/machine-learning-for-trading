# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/09_dl_tcn.ipynb；A3 Pack 001；單元 6 個。


## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Temporal Convolutional Network - FX Pairs

A temporal convolutional network reads a fixed number of consecutive daily observations for each
currency pair. A missing daily observation invalidates every lookback window that crosses it. The
shared sequence runner derives that eligible endpoint grid, primes each validation fold only with
observable earlier rows, saves epoch checkpoints, and publishes predictions against the same grid.

**Learning objectives**

- Define one sequence-model request without rebuilding windows in the notebook.
- Inspect the cadence-aware eligibility and checkpoint identities recorded by the runner.
- Reload fitted weights and pass complete predictions through the shared catalog.

**Book reference**: Chapter 13, Sections 13.2 and 13.4

**Prerequisites**: [[ML4T_A3_0001]], [[ML4T_A3_0002]], and [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Plan the sequence request

Fold and symbol reductions create a preview. Epochs, lookback length, and batch size are visible
model overrides: changing any of them creates a different training identity. Planning resolves
that identity, the eligible validation keys, and every declared epoch checkpoint before any
training starts.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## Inspect the declared checkpoints and gap policy

The resolved request records exact validation keys and the rule that excludes windows crossing a
missing expected day. Checkpoint values below are training epochs, not IC-selected summaries.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Record the official population, then fit or reload the TCN

The same resolved request is used by the notebook and direct Python callers. Publication fails if
any fold is missing, any prediction is non-finite, or the prediction keys differ from eligibility.

[[ML4T_A3_0001]] names the population hash this run replaces. A population is the set of
prediction identities it publishes, so anything that moves a training identity produces a
different population under the same name, and the registry refuses to write it without being
told which snapshot it supersedes. That lineage is the only record of which generation is which,
and what moved the identities here was a change to the family's own source file rather than to
anything the notebook declares.

[[ML4T_A3_0002]] decides whether the declared hash may be offered. It is offered when the
name already carries the generation this declaration produced, so a re-run resolves to the
population it published, and when the declaration names the generation in force, so a refit
publishes the next one. It is withheld everywhere else - on a reader's clean clone, where
[[ML4T_A3_0003]] is gitignored and the registry has no generation at all; under a caller's own
[[ML4T_A3_0004]]; and in a preview, whose isolated registry holds nothing under this name.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## Reload the fitted state

An identical call validates the saved weights and returns the same prediction identities. The
comparison with other model families belongs in [[ML4T_A3_0001]] after every family completes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Key takeaways

- Eligibility is defined by consecutive observations at the declared daily cadence.
- Validation priming uses earlier observable rows without admitting training targets.
- Every saved epoch checkpoint remains available to the backtest stage.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>
