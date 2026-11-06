# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/08_tabular_dl.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Deep learning → 深度學習
- Feature → 特徵
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Tabular Deep Learning

TabM applies a parameter-efficient neural ensemble to the same point-in-time feature rows used by
the linear and gradient-boosting families. The declared configurations vary model capacity while
retaining the walk-forward fold and label contracts from [[ML4T_A3_0001]].

The shared runner publishes every declared epoch checkpoint with its fitted weights and exact
validation coverage. The equal-weight validation backtest in [[ML4T_A3_0002]] evaluates all
checkpoints and selects by Sharpe.

Prerequisites: [[ML4T_A3_0003]], [[ML4T_A3_0004]], and [[ML4T_A3_0005]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Why a neural network on a feature table at all

Deep learning earned its reputation on images, audio and text, where the input has structure a
network can exploit: neighbouring pixels are related, words have order, and the architecture is
built to reflect that. A table of engineered features has none of it. Columns can be permuted
with no loss of meaning, and there is no locality for a convolution to use or a sequence for a
recurrence to traverse.

On that kind of input, gradient-boosted trees remain the standard to beat, and they beat neural
networks often enough that "tabular deep learning" is a live research area rather than a
settled one. Trees handle mixed scales without preprocessing, ignore irrelevant columns almost
for free, and split on thresholds - which is exactly the shape of many real relationships in a
feature table, where an effect appears above some level of a variable and not below it.

So this stage runs with a specific question rather than an assumption: on this panel, with
these features, does a network find anything the trees in [[ML4T_A3_0001]] do not? It reads the same
point-in-time feature rows under the same fold and label contracts, so the comparison isolates
the model family.

### What TabM is doing differently

The obvious way to improve a neural network's reliability is to train several and average
them, which reduces the variance that comes from initialization and from the optimizer's path.
The obvious cost is that k models take k times the compute and k times the memory.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

TabM is a parameter-efficient ensemble: it trains what behaves like several models while
sharing most of the weights between them, so the averaging is available at close to the cost of
one. That matters here more than it would on a large dataset, because the thing most likely to
go wrong on a panel this size is not bias but variance - a single network on a small, noisy
feature table can land in a very different place depending on where it started, and the spread
between those places can exceed whatever edge is being measured.

[[ML4T_A3_0001]] in the declared configurations is the other half of the same concern.
Capacity is the dial that trades fitting the training rows against generalizing off them, and
on a noisy panel the best setting is usually much smaller than intuition suggests. Declaring
several and letting the backtest choose is what keeps that from being a guess.

One consequence worth stating for the comparison with [[ML4T_A3_0002]]: a network needs its features
standardized and trees do not. So the two families do not read quite the same inputs even
though they read the same columns, and a difference in their results is partly a difference in
preprocessing rather than purely in model family. That is unavoidable - an unstandardized
network on mixed-scale features does not train - but it is worth knowing before the gap
between the two is attributed entirely to what the models can represent.

### Why every checkpoint is published
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

A neural fit is a trajectory rather than a model: it passes through a sequence of states, and
which one is kept is a choice with the same standing as the architecture. The runner publishes
every declared epoch checkpoint with its own fitted weights and validation coverage, and
[[ML4T_A3_0001]] selects among them on Sharpe like any other configuration.

Publishing them rather than picking one is the honest arrangement. Choosing the best epoch by
looking at validation performance and then reporting that model's validation performance is
selection inside the number being reported, and it does not stop being that because the choice
was made by hand rather than by a search. Declaring the checkpoints puts the choice into the
same funnel and the same trial count as everything else - which the deflated Sharpe downstream
then has to divide by, and which is why the count is not free.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>

### c0004-p000

~~~~~~markdown
## Declared requests

Both configured return horizons enter the same visible request table. Preview epoch or fold limits
must be passed through [[ML4T_A3_0001]], which changes identity and excludes the output from
the canonical catalog.

Routing reductions through identity rather than through a flag is what keeps a reduced run
from being mistaken for a real one later. A preview that trained for two epochs instead of the
declared schedule produces a genuine prediction set with genuine metrics, and nothing about
the numbers announces that they came from a fraction of the work. Because the reduction enters
the hash, the reduced rows cannot resolve to the same identity as canonical ones, cannot be
served back in place of them, and are excluded from the catalog the backtest reads.

The alternative - a boolean that says "this was a preview" - fails the moment anyone queries
the registry without checking it, which is the failure mode that makes a leaderboard quietly
wrong rather than visibly broken.

**TabM runs on the GPU, and the request says so rather than inheriting it.** With no override the
shared adapter falls back to a literal [[ML4T_A3_0002]] written in [[ML4T_A3_0003]], and
[[ML4T_A3_0004]] raises [[ML4T_A3_0005]] rather than quietly moving
the fit to the CPU. Naming it in the request puts that requirement where a reader meets it. The
resolved specification hash is the same with the override as without, so this states what the
published run already did.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>
