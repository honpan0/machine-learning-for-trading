# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11b_ipca.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Factor returns → 因子報酬率
- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: letting the features set the exposures

[[[ML4T_A3_0001]]](11a_pca.ipynb) gave each fund one loading per factor, fitted once on the training
window's return matrix, and never looked at a feature. That is a strong assumption about these
hundred funds: whatever a fund's momentum, volatility or yield-curve exposure was doing, its
share of each common movement was a constant for the whole training window.

**Instrumented PCA keeps the factor structure and drops that constant.** A fund's exposure on a
given date is a linear function of its own feature row on that date - one map, shared by every
fund and every date, from features to exposures - and the factor returns are then whatever best
explains that date's cross-section given those exposures. The two are fitted together, by
alternating between them until neither moves.

What that buys is a constraint rather than more capacity. [[[ML4T_A3_0002]]](06_linear.ipynb) had one
free coefficient per feature and one cross-section at a time to find them in. IPCA has one map
from the features to [[ML4T_A3_0003]] exposures, estimated on every fund-date in the training window
at once. That is fewer free parameters against more data, and it is the whole argument for the
family. It is also its limitation: if the relationship between a feature and the exposure it
implies is not linear, the constraint is wrong rather than merely tight, which is what
[[[ML4T_A3_0004]]](11c_conditional_autoencoder.ipynb) relaxes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**The estimator can fail to fit, and this notebook refuses to publish when it does.** Alternating
least squares is not guaranteed to converge, and it does not when the cross-section is too narrow
to identify the number of factors asked for - a hundred funds against five factors is
comfortable; a handful of funds against five is not. [[ML4T_A3_0001]] in
[[[ML4T_A3_0002]]](../utils/latent_factors/cv.py) raises rather than
registering predictions from a fit that never settled, so an unconverged run is a failure here
and not a quiet row in the population.

**Learning objectives.** By the end of this notebook you will be able to:

- Say what changes between a factor model with fixed exposures and one whose exposures are a
  function of observable features, and what each buys.
- Read an alternating-least-squares configuration - iteration cap, tolerance, two ridge
  penalties - and say what each controls.
- Explain why a fit that has not converged must not be published, and where that is enforced.
- Read a population published for every declared label rather than only the traded one.

**Book reference**: Chapter 14, Section 14.5 (Bridging economics and statistics with advanced
models). Chapter 6, Section 6.7 (Search accounting and run logging) introduces the run log this
notebook writes to.

**Prerequisites**: [[[ML4T_A3_0003]]](03_financial_features.ipynb) and
[[[ML4T_A3_0004]]](04_model_based_features.ipynb) for the feature matrix this one reads,
[[[ML4T_A3_0005]]](05_evaluation.ipynb) for the walk-forward folds, and
[[[ML4T_A3_0006]]](11a_pca.ipynb), which is the same factor structure with the conditioning removed.
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
thing over five. Unlike [[[ML4T_A3_0004]]](11a_pca.ipynb), the label is part of what is being estimated
here - the factor returns are the ones that best explain the cross-section of *that* forward
return - so the two rows below are two different fits and not one fit scored twice. [[ML4T_A3_0005]]
restricts the run to a subset when you want one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The configuration comes from two files, and they say different kinds of thing.
[[ML4T_A3_0001]] declares [[ML4T_A3_0002]], how many common factors to extract,
and [[ML4T_A3_0003]], which says there is no intermediate training state to publish:
alternating least squares runs to convergence rather than for a number of epochs, so a fold
produces one fitted map and one set of predictions. There is no point at which a reader could
have stopped it, and publishing a checkpoint schedule would invent a choice the estimator does
not offer.

[[ML4T_A3_0004]] declares the solver itself under [[ML4T_A3_0005]]:
[[ML4T_A3_0006]], the cap on alternations; [[ML4T_A3_0007]], how small a step counts as settled; and
[[ML4T_A3_0008]] and [[ML4T_A3_0009]], penalties on the two least-squares steps. Those four are inside
the training identity rather than recorded beside it, because a fit stopped at a different
tolerance is a different fitted model.
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
it. IPCA is alternating least squares over the panel and has no GPU implementation, so this
notebook declares CPU explicitly, and a bounded number of fold workers with it: the folds are
independent fits and this is the one member of the family the runner allows to run them in
parallel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>
