# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/12_model_analysis.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Label → 標籤
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Model Analysis

This notebook reads the complete canonical model population produced by [[ML4T_A3_0001]] through
[[ML4T_A3_0002]]. Each row retains family, configuration, label, checkpoint, fold
contract, training identity, and prediction identity. No null label is assigned to another
horizon, and checkpoints are not collapsed into a single model label.

IC measures whether a configuration ranks the cross-section correctly on a decision date. It
selects nothing: every row here proceeds to the equal-weight validation backtest in
[[ML4T_A3_0003]], where Sharpe performs selection and the checkpoint is part of what is selected.

What [[ML4T_A3_0004]] and [[ML4T_A3_0005]] are, precisely, because the two readings are easy to confuse. Both are
computed **across folds**: [[ML4T_A3_0006]] averages each fold's cross-sectional IC, and [[ML4T_A3_0007]] divides
that by the *standard error* of the same five numbers, which is their dispersion divided by the
square root of how many are defined - not the dispersion itself. [[ML4T_A3_0008]] in the table below is
the dispersion, so reproducing [[ML4T_A3_0009]] from the two columns needs the [[ML4T_A3_0010]] factor.

The registry also computes the daily-series reading with its HAC standard error, which is the
inferential statistic, but the predictions reader does not surface it, so it is not in the table
below. [[ML4T_A3_0011]] is carried instead: it
counts the validation dates that produced a defined IC, and a configuration whose predictions
collapse to near-constant on some dates has its [[ML4T_A3_0012]] measured over fewer of them. Reading
[[ML4T_A3_0013]] without [[ML4T_A3_0014]] is how a partial-coverage artifact reads as a leader.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What an information coefficient measures, and what it cannot

Everything in the table below is built on the IC, so it is worth being exact about what the
number is before reading any of it.

On one decision date there is a set of products, a predicted return for each, and the return
each actually went on to earn. The IC is the rank correlation between those two lists. It asks
a deliberately narrow question: did the model put them **in the right order**? It does not ask
whether the predicted magnitudes were close, and it cannot - a model that predicts every return
at a hundredth of its true size scores exactly as well as one that gets the levels right, as
long as the ordering matches.

That narrowness is the point for a strategy of this shape. The backtest in [[ML4T_A3_0001]] holds
the top-ranked products and shorts the bottom-ranked ones in equal weight, so the ordering is
the entire input and the magnitudes are discarded before a position is taken. A diagnostic that
rewarded accurate levels would be measuring something the strategy never uses.

**It is computed per decision date and then averaged, never pooled.** Pooling every
product-date into one correlation would let a period when the whole market moved together
masquerade as skill at telling products apart: on a day when everything rallies, a model that
ranks products at random still shows agreement between its predictions and the outcomes if the
cross-sections are stacked. Correlating within a date and averaging afterwards removes the
common move by construction, because it is the same for every product on that date.

### Why a good IC is a small number
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

A reader arriving from a forecasting background should expect these to look disappointing. A
monthly-horizon equity or futures IC of 0.03 to 0.05 is a real, usable signal; 0.10 sustained
would be remarkable. This is not a weak result being excused - it is what predicting an
overwhelmingly noise-dominated quantity looks like when it works. The edge comes from applying
a small consistent tilt across many products and many dates, not from being right about any one
of them, and the arithmetic of that is what [[ML4T_A3_0001]] measures and this notebook does not.

### Why the ranking diagnostic selects nothing

A high IC does not imply a tradeable strategy, and this is the boundary the notebook's title
refers to. A configuration can rank the cross-section well and still lose money: if its ranking
churns from one decision to the next, the turnover it implies costs more than the tilt earns; if
its skill sits entirely in the products that are least liquid, the positions cannot be taken at
the prices the backtest assumes. Neither of those is visible in an IC, because an IC has no
notion of holding anything.

So nothing here is a decision. Every complete row in this catalog proceeds to the equal-weight
validation backtest, where Sharpe selects and the checkpoint is part of what is selected. This
notebook is where a reader forms an expectation and, more usefully, notices where the backtest
later disagrees with it - a configuration that ranks well and backtests badly is the most
informative row in the whole case study, because the gap between the two is exactly where
turnover and tradeability live.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0004-p000

~~~~~~markdown
## Complete prediction catalog

The six official population snapshots were created before their model runs. Opening all six and
calling [[ML4T_A3_0001]] means a failed configuration or checkpoint cannot disappear from this
analysis because another row happened to finish.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
Canonical analysis reads the six published population snapshots, which is the whole point of
freezing them before their runs. A preview has no published population to read: it is a reduced
re-execution whose rows exist only in its own workspace and which is deliberately excluded from
every official population. It reads its own complete validation predictions instead, and the
comparison against the declared menus below is skipped with them, because a preview fits a named
subset by design and would fail that comparison on every configuration it left out.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>
