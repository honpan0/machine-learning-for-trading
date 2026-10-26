# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11c_conditional_autoencoder.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Factor returns → 因子報酬率
- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: the same factor structure with a network in place of the linear map

[[[ML4T_A3_0001]]](11b_ipca.ipynb) made a fund's exposure a **linear** function of its feature row.
That is a strong claim: doubling a fund's momentum doubles its exposure to the momentum-like
factor, and two features can only combine by adding. The conditional autoencoder keeps everything
else about that structure - features to exposures, exposures times factor returns, both fitted on
the training window alone - and replaces the linear map with a small neural network.

**So the difference between these two notebooks is the shape of one function and nothing else.**
That is what makes them worth reading against each other. If the network ranks the cross-section
better, the relationship between a feature and the exposure it implies is not linear; if it does
not, the extra capacity bought nothing and the linear constraint was not what was holding IPCA
back. Neither outcome is decided here - [[[ML4T_A3_0002]]](13_model_analysis.ipynb) compares
the populations with every family in front of it.

**The network is trained rather than solved, which changes what this notebook publishes.** IPCA
runs alternating least squares to convergence and has one fitted state per fold. A network is
trained for a declared number of passes over the training rows - **epochs** - and has a
meaningful state at every one of them. [[ML4T_A3_0003]] declares 50 epochs
saved every 5, so each label produces ten scoreable models rather than one, each registered
separately.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**All ten are published, and that is deliberate.** Fixing one reporting checkpoint in advance
would be the right instinct about the trap - picking the epoch with the best validation IC is
choosing after seeing the answer - and the wrong remedy, because it throws away nine models the
case study paid to train and leaves the choice to be made again, undocumented, downstream.
Publishing the whole schedule lets
[[[ML4T_A3_0001]]](14_backtest.ipynb) select on validation backtest Sharpe with every candidate
visible and the rule stated. **Selection happens there, not here.**

**Learning objectives.** By the end of this notebook you will be able to:

- Say what a conditional autoencoder relaxes relative to instrumented PCA, and what it keeps.
- Read an epoch schedule out of a declared configuration and say how many prediction sets a
  label will owe.
- Read a curve of out-of-sample ranking accuracy against training epoch, and tell a model still
  learning from one that has begun fitting its training window.
- Say why the training device is part of a model's identity rather than a note about how it ran.

**Book reference**: Chapter 14, Section 14.6 (The conditional autoencoder). Chapter 6,
Section 6.7 (Search accounting and run logging) introduces the run log this notebook writes to.

**Prerequisites**: [[[ML4T_A3_0002]]](03_financial_features.ipynb) and
[[[ML4T_A3_0003]]](04_model_based_features.ipynb) for the feature matrix,
[[[ML4T_A3_0004]]](05_evaluation.ipynb) for the walk-forward folds, and
[[[ML4T_A3_0005]]](11b_ipca.ipynb), which is this estimator with the network replaced by a linear map.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**What it writes**: one training run per label and one complete validation prediction set per
label and epoch checkpoint, in [[ML4T_A3_0001]] and under [[ML4T_A3_0002]] and
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
thing over five. The network's exposures are fitted against the label, so these are two separate
fits rather than one fit scored twice. [[ML4T_A3_0004]] restricts the run to a subset when you want one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
[[ML4T_A3_0001]] declares the estimator and its schedule. [[ML4T_A3_0002]] is the
width of the bottleneck - how many exposures the network maps a feature row onto. [[ML4T_A3_0003]] and
[[ML4T_A3_0004]] decide how many prediction sets each label owes: 50 epochs saved every 5 is
ten. They are declared beside the architecture rather than passed in here, because a run that
quietly trained for fewer would publish a different population under the same name.
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

The device is checked in the same cell. A network trained on a GPU and the same network trained
on a CPU accumulate their sums in different orders and reach different weights, so the device is
part of what the fitted model is and is recorded inside the computation's identity rather than
beside it. [[ML4T_A3_0003]] is the device this population was fitted on; the runner refuses to
substitute a CPU for a requested GPU rather than publishing a different model under the published
name, so on a machine with no NVIDIA card this notebook stops at the next cell. Set
[[ML4T_A3_0004]] and pass a [[ML4T_A3_0005]] to fit the same schedule there.

This is where the family stops being uniform. [[[ML4T_A3_0006]]](11a_pca.ipynb) and
[[[ML4T_A3_0007]]](11b_ipca.ipynb) declare CPU because they have no GPU implementation at all; the
three neural members declare CUDA. One family, two runtimes, and both inside the identity.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>
