# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/07_gbm.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto perpetuals: 400 candidate models from two validation years

[[[ML4T_A3_0001]]](06_linear.ipynb) worked through what a penalty does to a feature set that is one
economic quantity - the premium of the perpetual over spot - measured many ways. The L1 path
reduced to a single column and the ranking stopped moving. Gradient boosting meets the same
feature set with a different constraint: a tree does not weight columns, it splits on them, and
on a block of near-duplicates it can split on one measurement of the premium after another. That
is a way to describe the training window in great detail without adding any information.

Three dials control how far it goes, and this notebook varies all three:

- **Capacity**, set by [[ML4T_A3_0002]]: how many regions one tree may carve the feature space into.
- **The loss function**, which decides what "got wrong" means. Squared error weights an
  observation by the square of its error; absolute error and Huber do not. Eight-hour crypto
  returns are heavy-tailed enough for that to be a real choice rather than a formality.
- **When to stop**, set by the number of trees. A boosted model has a meaningful state at every
  iteration, so this notebook scores each configuration at ten points along its own training run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**The arithmetic of that is the reason to read this notebook carefully.** The four declared
labels bring fifteen configurations each for the two return horizons and five each for the two
direction cuts - forty in all, at ten checkpoints apiece, which is 400 candidate models. This
case study also has the shortest usable history of the nine: [[ML4T_A3_0001]] set two
walk-forward folds from the liquid funding data that exists, so every one of those 400 numbers
is measured on two validation years of a market whose structure changed over them. The more
candidates a search has, the better its best member looks for reasons that have nothing to do
with the data - and here the candidate count is large while the evidence each candidate is
judged on is small.

The comparison is within a label. A candidate is a (label, configuration, checkpoint) triple,
and nothing below ranks a return model against a direction model as if they were competing for
the same slot; what the labels are compared on is how far each one's own grid gets.

**Learning objectives.** By the end of this notebook you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

- Read a declared gradient boosting grid and say what each configuration varies.
- Explain why a boosted model produces one result per checkpoint while a linear model produces
  one result in total, and what that implies for counting candidates.
- Read a learning curve of out-of-sample information coefficient against tree count, and say
  whether an apparent peak is a turning point or the highest of ten noisy readings.
- Say why the choice of loss function is a statement about the label's tails, and relate that to
  what a rank-based metric rewards.
- Judge a result by the number of candidates behind it and the amount of validation data under
  it, rather than by its rank in a table.

**Book reference**: Chapter 12, Section 12.2 (GBM libraries) and Section 12.3 (how to tune a
boosted model). Chapter 6, Section 6.7 (Search accounting and run logging) introduces the run
log this notebook writes to, and Section 6.8 the multiple-testing problem this grid creates.

**Prerequisites**: [[[ML4T_A3_0001]]](03_financial_features.ipynb) and
[[[ML4T_A3_0002]]](04_model_based_features.ipynb) have written the feature matrices,
[[[ML4T_A3_0003]]](05_evaluation.ipynb) has established the walk-forward folds, and
[[[ML4T_A3_0004]]](06_linear.ipynb) fitted the linear population this one is compared against.

**What it writes**: one training run per configuration and one complete validation prediction
set per configuration and checkpoint, in [[ML4T_A3_0005]] and under [[ML4T_A3_0006]] and
[[ML4T_A3_0007]], grouped under a named population.
[[[ML4T_A3_0008]]](13_backtest.ipynb) reads that population and selects on validation backtest
Sharpe. **Selection happens there, not here.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0004-p000

~~~~~~markdown
## 1. Which labels, and which models

The labels are the same ones the linear notebook fitted, and for the same reason: the two
families are compared on identical targets, folds and features, so what separates their results
is the family. Fitting all four here rather than one also carries the linear notebook's finding
forward to be checked - that the sign of the eight-hour move is a far more rankable target than
its size, on the same inputs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
Each label's menu at [[ML4T_A3_0001]] lists its named configurations under [[ML4T_A3_0002]],
and each resolves to a preset in [[ML4T_A3_0003]]. The return labels declare fifteen,
a product of two axes; the direction labels declare a shorter list, because some members of the
return grid have no classifier counterpart.

- **Five capacity profiles.** [[ML4T_A3_0004]] uses the library's own leaf count; the rest fix it at 7,
  15, 31 and 63. Leaf count is the direct control on how finely one tree may partition the
  feature space. On a feature set this redundant the dial does something particular: with many
  near-copies of the premium available, a deeper tree can keep splitting on one measurement of
  it after another and describe the training window in fine detail without adding information.
- **Three objectives.** [[ML4T_A3_0005]] minimizes squared error, [[ML4T_A3_0006]] absolute error, and [[ML4T_A3_0007]] behaves
  like squared error for small residuals and like absolute error beyond a threshold derived from
  each fold's own label spread.

Every configuration runs the same number of boosting iterations with the same learning rate, so
the grid isolates capacity and loss rather than confounding them with training length.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
[[ML4T_A3_0001]] and [[ML4T_A3_0002]] both narrow what is fitted, and a narrowed run declares a different
set of members than the canonical population does. A population is immutable once written, so
such a run must publish under its own name: on a fresh workspace it would otherwise register an
incomplete snapshot under the canonical one, and where the full population already exists the
registry refuses it. Comparing the loaded rows against the complete declared catalog catches
either knob, and says so here rather than several cells later in a message about hashes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>
