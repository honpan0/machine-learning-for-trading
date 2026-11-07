# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/13_backtest.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Equal-Weight Backtest - FX Pairs

This notebook establishes the strategy baseline. At each decision time it ranks the currency-pair
scores, takes equal-sized long and short sleeves, and runs the existing FX backtest engine. Every
complete model configuration and checkpoint is evaluated. The input is a Polars catalog selection,
so no prediction hash is copied into orchestration code.

This is the step that turns a model into a strategy. Everything before it scored pairs; nothing
before it has said what you would have held or what it would have returned. Rank correlation
and AUC measure whether the ordering carries information, and a model can be clearly informative
by both and still lose money once the ordering is turned into positions - the information may
sit in pairs too illiquid to hold, or in a part of the distribution the sleeves never reach.
The return series produced here is the first quantity in the chain that a trader could have
experienced, and it is the reference every later stage is measured against.

Equal weight is used deliberately rather than for convenience. It is the choice not to choose a
size, so the resulting return series carries the ranking's contribution and nothing else. Any
other weighting would blend the model's information with a view about sizing, and the
allocation notebook could then no longer attribute its improvement to allocation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**A note on how this appears in the registry.** These runs register with [[ML4T_A3_0001]], and
the notebook asserts it. That stored value names the strategy component being varied - here the
signal mapping - and it does not mean there is a separate "signal stage" upstream of a backtest.
These *are* the baseline backtests. In prose, write "the baseline backtests" and "baseline
(equal-weight) Sharpe", never "signal Sharpe", which reads as a metric of the predictions rather
than of a traded strategy.

**Learning objectives**

- Freeze the exact prediction population before running a baseline sweep.
- Send selected catalog rows to the canonical FX engine.
- Verify that every declared prediction and portfolio-size combination produces one backtest.
- Read the baseline as the reference the allocation, risk and cost stages are measured against.

**Book reference**: Chapter 16

**Prerequisite**: [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
## Select the exact prediction population

Canonical production includes every complete validation prediction the model notebooks currently
publish. Label, configuration, or population limits are preview controls and cannot define the
official baseline.

**"Currently publish" is a question about lineage, and the catalog cannot answer it.** A row's
[[ML4T_A3_0001]] is derived from the schema version it was written under, so it says the registry
still understands the row - not that the row is the one its producer stands behind. The two agree
until a model notebook refits. Then it publishes a second generation of its population under the
same name, the first generation's prediction sets stay in the registry complete and current, and a
sweep selecting on the catalog alone runs over both. It would not fail; it would report every
member complete, over twice the population, and freeze the retired half into the baseline the rest
of the case study is measured against.

[[ML4T_A3_0002]] asks the registry which identities a later generation retired and no
generation in force still lists, which is exactly the set to drop. The [[ML4T_A3_0003]] and
[[ML4T_A3_0004]] populations each have a retired generation here, because a training identity
covers the runner's own source file and both runners changed after their first fits were
registered. The count of what that excludes is printed rather than left implicit.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0003-p001

~~~~~~markdown

**A published population can need a second generation too.** The two names this notebook
publishes are lists of identities, and the exclusion above changes both of them the moment a
model notebook refits: the prediction population loses the retired members, and every baseline
backtest resolved from them goes with it. [[ML4T_A3_0001]] refuses a changed list
under an existing name without being told which snapshot it replaces, so each name has its own
declaration and each is offered through [[ML4T_A3_0002]] on the same rule the model
notebooks use. Both are empty here because neither name has published a first generation yet;
after the first canonical run, a refit upstream is answered by filling in the hash that run
printed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p001>>>
<<<ML4T-ZH-END:c0003-p001>>>

### c0005-p000

~~~~~~markdown
## Build the baseline strategy grid

[[ML4T_A3_0001]] is the number of pairs in each sleeve. This account allows short selling, so the engine
holds [[ML4T_A3_0002]] long and [[ML4T_A3_0003]] short and clamps each sleeve to half the universe to keep them
disjoint. Two consequences worth stating exactly, because both shape how the grid reads:

- At [[ML4T_A3_0004]] below half the universe, ranking decides *which* pairs are held.
- At [[ML4T_A3_0005]] equal to half the universe, every pair is held at every rebalance and ranking decides
  only the *side*. The grid then varies concentration and sign exposure, not membership.

A [[ML4T_A3_0006]] above half the universe cannot express anything the half-universe value does not: the
engine clamps it to the same sleeves, so it would register a distinct identity carrying an
identical weight series. The grid is refused rather than allowed to contain that duplicate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Freeze the expected baseline population

Planning resolves every backtest identity without running or writing it. Production freezes that
complete expected set before the first member executes, so a failed member remains visible.

Visibility is the whole point, and it is worth being explicit about the alternative. A sweep that
collected whatever finished would publish a baseline whose membership depends on which runs
happened to succeed. Failures are not random with respect to the thing being measured: a
configuration that produces degenerate scores, or one whose predictions are too sparse to fill a
sleeve, is more likely to fail and would silently leave the population. The surviving baseline
would then look better than the sweep that produced it, and nothing in the output would record
that anything was dropped. Declaring the expected set first converts that from a silent
improvement into an incomplete population that refuses to publish.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>
