# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11a_pca.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: factors taken from the return panel alone

Every model so far has read the feature matrix. [[[ML4T_A3_0001]]](06_linear.ipynb) gave each column
a coefficient, [[[ML4T_A3_0002]]](07_gbm.ipynb) split on them, [[[ML4T_A3_0003]]](08_tabular_dl.ipynb)
mixed them in a hidden layer. All three answer the same question - what does this fund's feature
row say about its next return - and they differ only in the shape of the function they are
allowed to write down.

The latent-factor family asks a different question first. Suppose the returns of these hundred
funds are driven by a handful of common movements, and what distinguishes one fund from another
is **how much of each movement it carries**. Then the thing to estimate is the set of movements
and each fund's exposure to them, and a forecast follows from the exposures rather than from a
feature row.

**PCA is the member of that family that uses no features at all.** It takes the matrix of the
forward returns it is asked to forecast over the training window, one column per fund, and finds
the directions along which that matrix varies most. [[ML4T_A3_0004]] in
[[[ML4T_A3_0005]]](../utils/latent_factors/pca.py) deletes the
characteristic arrays on its first line: whatever [[ML4T_A3_0006]] and
[[ML4T_A3_0007]] built, this estimator never sees it. That is the point of having it
here. It is the bar the four conditioned members of the family have to clear, and if the return
panel's own covariance structure ranks these funds as well as the feature matrix does, that is a
fact worth knowing before reading the more elaborate models.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**It is available here because an ETF is the same fund throughout.** PCA assigns one loading
vector per column of the return matrix and needs that column to mean the same thing from the
first day of the training window to the last. [[ML4T_A3_0001]] declares
[[ML4T_A3_0002]] for this case study, and the runner refuses
PCA outright where that is false. A panel of firms entering and leaving an index cannot promise
it; a fixed list of tickers can.

**Learning objectives.** By the end of this notebook you will be able to:

- Say what a return-panel factor model estimates and what it does not read.
- Work out, from how the forecast is assembled, whether a prediction can change from day to day
  within a fold - and check that against the published predictions rather than assuming it.
- Read a model with no epochs and say why it still publishes a checkpoint.
- Read a population published for every declared label rather than only the traded one.

**Book reference**: Chapter 14, Section 14.2 (Extracting latent factors with PCA) and
Section 14.5 (Bridging economics and statistics with advanced models). Chapter 6, Section 6.7
(Search accounting and run logging) introduces the run log this notebook writes to.

**Prerequisites**: [[[ML4T_A3_0003]]](02_labels.ipynb) for the two forward returns,
[[[ML4T_A3_0004]]](05_evaluation.ipynb) for the walk-forward folds, and
[[[ML4T_A3_0005]]](11_latent_factors.ipynb), which introduces the family and says which of its
five members each notebook publishes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**What it writes**: one training run per label and one complete validation prediction set per
label, in [[ML4T_A3_0001]] and under [[ML4T_A3_0002]] and [[ML4T_A3_0003]], grouped
under a population named for this model. The family splits across five notebooks, so each
publishes its own population rather than one shared one.
[[[ML4T_A3_0004]]](13_model_analysis.ipynb) compares them against the other families and
[[[ML4T_A3_0005]]](14_backtest.ipynb) backtests every member and selects on validation backtest
Sharpe. **Selection happens there, not here.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0004-p000

~~~~~~markdown
## 1. Which labels, and what the configuration says

Every label whose training menu declares [[ML4T_A3_0001]] is fitted, and both do: [[ML4T_A3_0002]],
the total return over the 21 trading days after the decision date, and [[ML4T_A3_0003]], the same
thing over five. The estimator reads none of the 71 feature columns, but it is not blind to the
label: the [[ML4T_A3_0004]] matrix that [[ML4T_A3_0005]]
([[[ML4T_A3_0006]]](../utils/latent_factors/panel.py)) fills from the request's own label column is the
one [[ML4T_A3_0007]] receives as [[ML4T_A3_0008]], so the two rows below are two separate fits, each
with its own loadings and premia, rather than one fit scored against two returns. What
changes between them is the panel as well as the scoring, and the number of validation dates.
[[ML4T_A3_0009]] restricts the run to a subset when you want one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
[[ML4T_A3_0001]] declares two things and nothing else. [[ML4T_A3_0002]] is how many
of the leading directions to keep, and it is the one number that decides how much structure the
model is allowed to find. [[ML4T_A3_0003]] says there is no intermediate training state
to publish: PCA is a singular value decomposition of the training window, not a loop over epochs,
so a fold produces one fitted set of loadings and one set of predictions. That is why the plan
below shows a single checkpoint where [[[ML4T_A3_0004]]](08_tabular_dl.ipynb) shows eight, and it
is a property of the estimator rather than a reduced setting.
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
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Where this one runs

[[ML4T_A3_0001]] puts no device on the latent-factor family, which leaves it to whatever the
machine offers - and a fit that lands on a GPU on one machine and a CPU on another is not the
same computation, because the device is inside the hashed identity rather than recorded beside
it. PCA is a call to [[ML4T_A3_0002]] and has no GPU implementation at all, so this notebook
declares CPU explicitly. The declaration then travels into the training identity, and a run that
changed it would register beside this one rather than over it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>
