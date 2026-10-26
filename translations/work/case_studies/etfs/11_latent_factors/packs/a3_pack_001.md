# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11_latent_factors.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: what the latent-factor family is, and who publishes what

The three modelling notebooks before this one predicted the return from the feature row
directly. [[[ML4T_A3_0001]]](06_linear.ipynb) gave each column a coefficient,
[[[ML4T_A3_0002]]](07_gbm.ipynb) split on them, [[[ML4T_A3_0003]]](08_tabular_dl.ipynb) mixed them in a
hidden layer, and they differ only in the shape of the function they may write down.

The latent-factor family starts somewhere else. It supposes the hundred funds move together
along a handful of common directions, and treats a feature as evidence about **how exposed a
fund is to them** rather than about its return. What gets estimated is a map from features to
exposures, shared by every fund and every date, so it is fitted on the whole panel instead of one
cross-section at a time.

Five members are declared, and they are **one baseline and two pairs, not five points on one
axis**:

| notebook | model | what it assumes |
|---|---|---|
| [[[ML4T_A3_0004]]](11a_pca.ipynb) | principal components | the return panel alone; reads no features |
| [[[ML4T_A3_0005]]](11b_ipca.ipynb) | instrumented PCA | exposures are a **linear** function of the features |
| [[[ML4T_A3_0006]]](11c_conditional_autoencoder.ipynb) | conditional autoencoder | same structure, the map is a **network** |
| [[[ML4T_A3_0007]]](11d_stochastic_discount_factor.ipynb) | stochastic discount factor | no two-stage split: prices the cross-section directly |
| [[[ML4T_A3_0008]]](11e_supervised_autoencoder.ipynb) | supervised autoencoder | no two-stage split: predicts the return directly, keeping only the bottleneck |
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

[[ML4T_A3_0001]] is the bar rather than a rung: it conditions on nothing, so what the four conditioned
members beat it by is what conditioning bought. It is available here only because an ETF is the
same fund throughout the sample, which [[[ML4T_A3_0002]]](11a_pca.ipynb) sets out - a panel whose
members enter and leave cannot support it, and the runner refuses it there.

The first pair differs in the shape of one function, which is what makes those two worth reading
against each other. The second pair breaks the two-stage shape from opposite ends - one because
it prices, one because it predicts - and [[ML4T_A3_0003]] is the only member fitted without the family's
central assumption at all: it keeps a low-dimensional bottleneck and drops the factor
interpretation. It is not a controlled comparison with [[ML4T_A3_0004]], whose network it does not share.

**Learning objectives**

- Say what the family asserts that the direct predictors do not.
- Read a family whose members are split across notebooks as one declared population.
- Check that the notebooks that exist cover the menu that is declared.
- Say why five members that share a menu cannot share a population.

**Book reference**: Chapter 14, Sections 14.5 to 14.7 (bridging economics and statistics,
the conditional autoencoder, and the stochastic discount factor and supervised autoencoder).
Chapter 13, Section 13.3 covers the return-panel PCA that [[ML4T_A3_0005]] publishes.

**Prerequisites**: [[[ML4T_A3_0006]]](03_financial_features.ipynb) and
[[[ML4T_A3_0007]]](04_model_based_features.ipynb) for the feature matrix, and
[[[ML4T_A3_0008]]](05_evaluation.ipynb) for the walk-forward folds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**What it writes**: nothing. This notebook fits no model, registers no run and opens no holdout.
All five notebooks it points at are on the research boundary and each publishes its own
population, which section 3 reads out of the sources rather than asserting here.
[[[ML4T_A3_0001]]](13_model_analysis.ipynb) is where they are compared against the other
families.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0004-p000

~~~~~~markdown
## 1. The declared menu

[[ML4T_A3_0001]] lists the family's members for each label, and every declared
label declares the same five. That is the population the five execution notebooks are between
them responsible for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## 2. Which notebook claims which member

The menu says what must be produced; it does not say by whom. The family is split across five
notebooks, each publishing one model under its own population name, so the mapping between the
two lives in the notebooks and is read back here rather than restated.

**A member the menu declares and no notebook claims publishes nothing, and nothing else would
catch it**: each execution notebook checks the labels it covers against its own declared rows, so
none of them can see a model that no notebook requests at all. That is what this cell is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
## 3. What each one costs to publish

The number of prediction sets a member contributes is its labels times its checkpoints, and the
checkpoints come from how the estimator is trained rather than from a shared setting. PCA and
IPCA solve to completion and have one state per fold; the two autoencoders train for a declared
epoch budget and save at a declared interval; the stochastic discount factor trains in phases and
saves at a declared list of cumulative epochs.

The schedule below is read out of each estimator's own configuration, so it is the declaration
and not a copy of one. The authoritative count is the [[ML4T_A3_0001]] column in each notebook's own
resolved plan, which is derived from these fields and printed before that notebook fits anything.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
This is why the family cannot publish one population. A population is an immutable list of
prediction identities, and the five members are fitted by five notebooks at different times, so
one shared name would mean the first to run either blocks the others or publishes a snapshot
missing them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>
