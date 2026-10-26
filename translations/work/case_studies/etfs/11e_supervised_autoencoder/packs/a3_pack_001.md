# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11e_supervised_autoencoder.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Factor returns → 因子報酬率
- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: a conditioned network with no factor structure

[[[ML4T_A3_0001]]](11c_conditional_autoencoder.ipynb) maps a fund's feature row to a
small set of exposures, estimates a factor return for each date from the cross-section, and
multiplies the two to get a forecast. The supervised autoencoder keeps the first half of that and
drops the second: a network compresses the feature row to a low-dimensional representation, and a
head predicts the forward return from that representation directly rather than through a factor
return.

**That makes this the one member of the family that asserts no factor structure.** Every other
member says the cross-section is driven by a few common movements and that a fund's return is its
exposure to them. This one keeps a low-dimensional representation and says nothing about what it
represents.

**It is not a controlled comparison with [[ML4T_A3_0002]], and the notebook does not read it as one.** The
two differ in the factor structure and in the network as well.
[[ML4T_A3_0003]] maps the feature row through [[ML4T_A3_0004]] to
five factors at a learning rate of 1e-3;
[[[ML4T_A3_0005]]](../utils/latent_factors/sae.py) maps it through [[ML4T_A3_0006]] to a 96-unit
bottleneck at 1e-4, with Gaussian input noise of 0.035 and a second loss term. Capacity, depth,
width, the learning rate and the objective all move together, so a difference in their results is
not attributable to any one of them. What the pair gives is a member of the family fitted without
the factor assumption, which is worth having and is not the same thing as a measurement of what
the assumption is worth.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**The label enters the fit here, which it does not everywhere in the family.** The reconstruction
term trains the encoder to compress the feature row; the supervised term trains the head against
the fold's forward returns. Both are backpropagated together. So the two rows this notebook fits
are two different models rather than one model scored against two returns, and that is true of
[[ML4T_A3_0001]] as well but for a different reason: there the label enters through the returns matrix the
factor stage reproduces, here it enters through the objective directly.

**The network is trained rather than solved, which decides what this notebook publishes.**
[[ML4T_A3_0002]] declares 50 epochs saved every 5, the same schedule
[[ML4T_A3_0003]] declares, so each label produces ten scoreable models rather than one and each is
registered separately. All ten are published. Fixing one reporting checkpoint in advance and
reporting that one is the right instinct about the trap - reading off the epoch with the best
validation IC is choosing after seeing the answer - and the wrong remedy, because it discards
nine models the case study paid to train and leaves the choice
to be made again, undocumented, downstream. Publishing the whole schedule lets
[[[ML4T_A3_0004]]](14_backtest.ipynb) select on validation backtest Sharpe with every candidate
visible and the rule stated. **Selection happens there, not here.**

**Learning objectives.** By the end of this notebook you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

- Say what a supervised autoencoder keeps from a conditional autoencoder and what it drops.
- Say what a member that imposes no factor structure still shares with the rest of the family.
- Read a curve of out-of-sample ranking accuracy against training epoch, and tell a model still
  learning from one that has begun fitting its training window.
- Say why the training device is part of a model's identity rather than a note about how it ran.

**Book reference**: Chapter 14, Section 14.7 (The stochastic discount factor and the supervised
autoencoder models). Chapter 6, Section 6.7 (Search accounting and run logging) introduces the
run log this notebook writes to.

**Prerequisites**: [[[ML4T_A3_0001]]](03_financial_features.ipynb) and
[[[ML4T_A3_0002]]](04_model_based_features.ipynb) for the feature matrix,
[[[ML4T_A3_0003]]](05_evaluation.ipynb) for the walk-forward folds,
[[[ML4T_A3_0004]]](11_latent_factors.ipynb), which introduces the family, and
[[[ML4T_A3_0005]]](11c_conditional_autoencoder.ipynb), the family's other neural
member, which imposes the factor structure this one drops.

**What it writes**: one training run per label and one complete validation prediction set per
label and epoch checkpoint, in [[ML4T_A3_0006]] and under [[ML4T_A3_0007]] and
[[ML4T_A3_0008]], grouped under a population named for this model. The family splits across
five notebooks, so each publishes its own population rather than one shared one.
[[[ML4T_A3_0009]]](13_model_analysis.ipynb) compares them against the other families and
[[[ML4T_A3_0010]]](14_backtest.ipynb) backtests every member and selects on validation backtest
Sharpe. **Selection happens there, not here.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0004-p000

~~~~~~markdown
## 1. Which labels, and what the configuration says

Every label whose training menu declares [[ML4T_A3_0001]] is fitted, and both do: [[ML4T_A3_0002]],
the total return over the 21 trading days after the decision date, and [[ML4T_A3_0003]], the same
thing over five. The label is inside the objective here rather than only in the scoring, so the
two rows below are two different fits with two different sets of weights. [[ML4T_A3_0004]] restricts the
run to a subset when you want one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>
