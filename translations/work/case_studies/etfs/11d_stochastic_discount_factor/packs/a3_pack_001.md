# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11d_stochastic_discount_factor.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: a model that prices the cross-section instead of predicting it

The three members before this one share a shape. [[[ML4T_A3_0001]]](11a_pca.ipynb),
[[[ML4T_A3_0002]]](11b_ipca.ipynb) and
[[[ML4T_A3_0003]]](11c_conditional_autoencoder.ipynb) all split the problem in two:
estimate what each fund is exposed to, estimate what those exposures earned, multiply. They
differ in how the first half is written down - not at all, a linear map, a network - and in
nothing else.

**The stochastic discount factor does not split it.** It asks for a single series that prices
every fund at once: a weighting of the cross-section whose covariance with each fund's return
accounts for that fund's average return. That is a statement about *no arbitrage* rather than
about forecasting, and it is fitted by driving pricing errors toward zero rather than by
minimising a forecast error. The two networks it trains - one producing the discount-factor
weights from the cross-section, one producing each fund's exposure to it - are trained against
that pricing objective.

A predicted return still comes out, which is why this notebook sits beside the others and is
scored the same way. But the number being optimised is not the number being reported, and that
gap is the thing to hold on to while reading the result.

**It is also the only member that reads macro data.** The other four see the fund panel and the
feature matrix. This one additionally takes eleven macro series as context for the
discount factor, which raises a question none of the others have to answer: what was actually
knowable on the decision date. Section 2 is where that contract is read back out of the resolved
specification rather than asserted here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**The checkpoint schedule is phased, and all of it is published.** Training runs an
unconditional stage and then a conditional one, and [[ML4T_A3_0001]] declares
saves inside each. Fixing the last of them in advance would be the right instinct about the
trap - picking the checkpoint with the best validation IC is choosing after seeing the answer -
and the wrong remedy, because it discards models the case study paid to train and leaves the
choice to be made again, undocumented, downstream. Publishing the whole schedule lets
[[[ML4T_A3_0002]]](14_backtest.ipynb) select on validation backtest Sharpe with every candidate
visible and the rule stated. **Selection happens there, not here.**

**Learning objectives.** By the end of this notebook you will be able to:

- Say what a pricing objective asks for that a forecasting objective does not.
- Read a phased training schedule and work out how many prediction sets a label will owe.
- Read a point-in-time data contract out of a resolved specification and say what it rules out.
- Say why the macro context belongs inside the model's identity rather than beside it.

**Book reference**: Chapter 14, Section 14.7 (The stochastic discount factor and the supervised
autoencoder models). Chapter 6, Section 6.7 (Search accounting and run logging) introduces the
run log this notebook writes to.

**Prerequisites**: [[[ML4T_A3_0003]]](03_financial_features.ipynb) and
[[[ML4T_A3_0004]]](04_model_based_features.ipynb) for the feature matrix,
[[[ML4T_A3_0005]]](05_evaluation.ipynb) for the walk-forward folds, and
[[[ML4T_A3_0006]]](11c_conditional_autoencoder.ipynb), which is the two-stage model
this one abandons.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**What it writes**: one training run per label and one complete validation prediction set per
label and checkpoint, in [[ML4T_A3_0001]] and under [[ML4T_A3_0002]] and
[[ML4T_A3_0003]], grouped under a population named for this model. The family splits across
five notebooks, so each publishes its own population rather than one shared one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0004-p000

~~~~~~markdown
## 1. Which labels, and what the configuration says

Every label whose training menu declares [[ML4T_A3_0001]] is fitted, and both do: [[ML4T_A3_0002]],
the total return over the 21 trading days after the decision date, and [[ML4T_A3_0003]], the same
thing over five. The pricing objective is written against the label's returns, so these are two
separate fits rather than one fit scored twice. [[ML4T_A3_0004]] restricts the run to a subset when you
want one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
[[ML4T_A3_0001]] declares the estimator and its schedule, and the schedule has
more structure here than in the two autoencoders. [[ML4T_A3_0002]] trains the unconditional stage,
[[ML4T_A3_0003]] the conditional one that follows it, and [[ML4T_A3_0004]] lists the saves
inside a stage. The resolved plan in section 2 turns those into the actual list of checkpoints,
which is what decides how many prediction sets each label owes - the count is not the length of
the declared list, because a save inside the unconditional stage and the same offset inside the
conditional one are two different states of the model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
[[ML4T_A3_0001]] narrows what is fitted, and a narrowed run declares a different set of members than the
canonical population does. A population is immutable once written, so such a run must publish
under its own name: on a fresh workspace it would otherwise register an incomplete snapshot under
the canonical one, and where the full population already exists the registry refuses it.

The comparison is against this model's own declared rows rather than the whole [[ML4T_A3_0002]]
catalog. The family is split across five notebooks and each publishes one model, so the complete
catalog is five times what this one publishes, and comparing against it would report every
canonical run as narrowed.

The device is checked in the same cell. Two networks trained on a GPU and the same two trained on
a CPU accumulate their sums in different orders and reach different weights, so the device is
part of what the fitted model is and is recorded inside the computation's identity rather than
beside it. [[ML4T_A3_0003]] is the device this population was fitted on; the runner refuses to
substitute a CPU for a requested GPU rather than publishing a different model under the published
name, so on a machine with no NVIDIA card this notebook stops at the next cell. Set
[[ML4T_A3_0004]] and pass a [[ML4T_A3_0005]] to fit the same schedule there.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>
