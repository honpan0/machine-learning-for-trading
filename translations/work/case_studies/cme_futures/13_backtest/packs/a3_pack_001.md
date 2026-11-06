# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/13_backtest.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Sharpe ratio → 夏普比率
- Label → 標籤
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Equal-Weight Signal Backtests

This notebook sends every complete model configuration and checkpoint through the same signal
baseline. At each weekly decision, the signal ranks products by the selected prediction row and
holds equal-weight long and short groups for each configured concentration. This is
[[ML4T_A3_0001]]; equal weight is not an allocation method in the next stage.

Reader-facing prices and decisions use [[ML4T_A3_0002]]. The shared boundary records the front-contract
position, raw-to-adjusted roll identity, cumulative-ratio transitions, expiry reference, contract
specifications, prediction lineage, and state-transition policy before converting [[ML4T_A3_0003]] to
the existing engine's internal [[ML4T_A3_0004]] key.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What this stage is for, and what it deliberately does not do

A model that predicts returns well is not yet a strategy, and the gap between the two is where
most of the disappointment in quantitative investing lives. A prediction is a number attached to
a product and a date. Turning it into a position requires deciding how many products to hold,
how much of each, when to change, and what that changing costs - and each of those decisions can
destroy a real edge or manufacture a fake one.

This stage answers only the first of those questions, and answers it in the plainest way
available. At each weekly decision the products are ranked by their predicted return, the top
[[ML4T_A3_0001]] are held long, the bottom [[ML4T_A3_0002]] short, and every position in a leg is the same size. Nothing
is optimized. There is no covariance matrix, no risk target, no position limit, no cost model.

The plainness is the point. This is the **baseline** every later stage is measured against, so
it has to be a construction whose behaviour comes from the predictions and from nothing else.
When the portfolio-construction stage reports a higher Sharpe, the question a reader should be
able to ask is "higher than what?" - and the answer has to be a number that no modelling choice
of ours is hiding inside.

Two consequences follow, and both are easy to misread later:
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

- **Equal weight here is not an allocation method.** It is the absence of one. The next stage's
  allocation methods are compared against this, and one of them being equal-weight-like is a
  result about that stage rather than a repetition of this one.
- **These Sharpe ratios are not the case study's results.** They are the reference the results
  are quoted against. Reporting one of them as the strategy's performance would be quoting the
  control arm as the finding.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0004-p000

~~~~~~markdown
## Futures data used by the strategy

The model predicts a continuous front-contract return. [[ML4T_A3_0001]] is the traded contract level;
[[ML4T_A3_0002]] is the multiplicatively back-adjusted level used for continuous returns. A change in
[[ML4T_A3_0003]] identifies a roll transition. The backtest consumes adjusted OHLC while retaining this
audit table and the product expiry rules in its identity.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## Complete baseline requests

The source rows come from the six official model populations. Each population must be complete
before this cell can construct a request. No registry ordering, row cap, cached metric, or caught
failure can remove a candidate.

**Why completeness is enforced rather than assumed.** A backtest sweep that silently skipped a
configuration would still produce a leaderboard, and the leaderboard would still look sensible.
What it would no longer support is the comparison it exists for: selecting the best validation
Sharpe out of a population means nothing if the population is whatever happened to finish. The
failure mode is not a wrong number, it is a right-looking number computed over a set nobody can
reconstruct - so the completeness check runs before any request is built rather than after.

**What a request is.** One row here is one backtest to run: a prediction set identified by its
hash, the label it was fitted against, and a signal specification. The [[ML4T_A3_0001]], [[ML4T_A3_0002]] and
[[ML4T_A3_0003]] fields are all None, which is what makes these the baseline - later chapters fill them
in and re-run this same machinery.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0007-p001

~~~~~~markdown

**Why several [[ML4T_A3_0001]] values rather than one.** [[ML4T_A3_0002]] is how many products each leg holds, and
it is the one dial this stage does turn. It decides concentration, and concentration trades two
things against each other: a small [[ML4T_A3_0003]] puts more weight behind the predictions the model is most
confident about, and a large [[ML4T_A3_0004]] averages across more of them so a single product's idiosyncratic
move matters less. Which wins is a property of the signal's strength and of how quickly its
ranking decays, neither of which is known before running it. Sweeping the values that
[[ML4T_A3_0005]] derives from the tradeable universe answers the question with the data
rather than by picking a round number, and it means a configuration that only works at one
concentration is visible as such rather than being represented by its best case.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p001>>>
<<<ML4T-ZH-END:c0007-p001>>>
