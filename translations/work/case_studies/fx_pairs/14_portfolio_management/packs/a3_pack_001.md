# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/14_portfolio_management.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Portfolio Allocation - FX Pairs

The baseline backtests answered whether a model's ranking is worth trading at all, by holding
every selected pair in equal size. That deliberately confounds two decisions. Which pairs to
hold comes from the model; how much to hold in each comes from nothing, because equal weight
is the choice not to choose. This notebook separates them: it takes the positions the baseline
already selected and varies only the sizing rule.

The separation is what makes the comparison readable. If a run changed the allocator and the
signal together and the Sharpe improved, there would be no way to say which change earned it.
So the prediction, the [[ML4T_A3_0001]] mapping, the cost model and the execution assumptions all pass
through from the winning baseline untouched, and the notebook enforces that rather than
assuming it: after every allocation result is computed, its strategy specification is compared
leaf by leaf against its baseline sibling, and a difference in any field that is not an
allocation field is an error. Without that check, "allocation improved Sharpe" would be a
statement about whatever else happened to move with it.

Production advances the ten model configurations with the highest validation backtest Sharpe
for each label, each carrying its own best checkpoint and signal mapping. Preview mode uses a
deterministic reduced catalog selection and never writes an official population or candidate
set, so a reduced run cannot publish a partial grid under a canonical name.

**Learning objectives**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Select configurations from an immutable equal-weight candidate set.
- Preserve the selected checkpoint and signal mapping when configurations advance to allocation.
- Change allocation while holding prediction, signal, costs, and execution fixed.
- Recognise why a sweep declares its expected results before it computes any of them.

**Book reference**: Chapter 17

**Prerequisite**: [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
## Resolve the equal-weight inputs

Canonical execution reads the exact population frozen by the baseline notebook. Its label-specific
candidate sets provide the only performance ranking used here. The selected unit is a model
configuration. After a configuration advances, its best checkpoint and signal mapping advance.

Reading the frozen population rather than rebuilding the catalog is the point of this cell, and
the reason is worth stating because the shortcut looks harmless. This notebook could query the
registry for complete validation predictions itself and get a list that looks right. It would
not be the list the baselines were computed from: a narrowed upstream run covers fewer labels
than the catalog holds, so reconstructing the input here means reproducing another notebook's
reduction by convention, and a convention that drifts produces a comparison whose two sides
were never measured on the same set.

One filter below carries a failure that no output frame can show. `identity_status ==
"current"` records the schema version a row was written under. It says nothing about whether
the notebook that produced the row still publishes it. When a model notebook refits, the
generation it replaced stays in the registry, complete and marked current, and a filter on
those three columns alone pulls it into the sweep. Nothing errors. Every backtest runs, every
Sharpe is computed correctly, and the table at the end looks exactly as it should - while part
of the grid rests on predictions the baseline population no longer contains. [[ML4T_A3_0001]]
reads the lineage instead of the status column, which is the only way the retired generation is
visible at all.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## Advance one checkpoint and mapping per configuration

Production ranks the complete baseline results for each label. The first result for a model
configuration is its best checkpoint and signal mapping by validation Sharpe. That result occupies
one declared slot and is the only member of the configuration that advances.

The deduplication is what makes the ten slots comparable across families. A configuration is
backtested once per checkpoint and once per [[ML4T_A3_0001]] mapping, so a family that saves ten
checkpoints enters the ranking with ten results and a family that saves two enters with two.
Taking the ten best results outright would hand most of the grid to whichever family happened
to checkpoint most often, and the allocation comparison would then be reporting a difference in
training bookkeeping. [[ML4T_A3_0002]] keeps the best result per distinct
[[ML4T_A3_0003]] and drops the rest, so each configuration occupies exactly one slot and
arrives with the checkpoint that earned it.

The [[ML4T_A3_0004]] that travels with the configuration is read from the winning result's own
specification, never restated here. [[ML4T_A3_0005]] is a check rather than a setting for that reason:
a reduced run that passes a different value does not quietly re-map the positions, it raises.
A silent re-map would change which pairs are held, which is exactly the variable this notebook
exists to hold fixed, and the resulting table would still be a valid backtest of something.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0005-p001

~~~~~~markdown

A candidate set is sealed once written. That is why a run whose membership has changed has to
name the generation it replaces rather than overwrite it: the ranking that selected these ten
configurations is itself a published object, and a later reader has to be able to see the set
the selection was made from, not the set that exists now.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p001>>>
<<<ML4T-ZH-END:c0005-p001>>>
