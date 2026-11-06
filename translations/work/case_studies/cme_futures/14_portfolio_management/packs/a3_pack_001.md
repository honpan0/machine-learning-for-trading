# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/14_portfolio_management.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Label → 標籤
- Volatility → 波動率
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Portfolio Allocation

The baseline stage ranks complete configurations by equal-weight validation backtest Sharpe. For
each label, this notebook retains the strongest checkpoint and signal concentration for each of
the configured number of distinct model configurations, then evaluates the declared alternative
position sizing methods. Equal weight is not among them: it is the baseline itself, and because
[[ML4T_A3_0001]] is not part of [[ML4T_A3_0002]], running it again here produces a row hashing
identically to its baseline parent, so one of the two is silently lost. Measured in this
case study's own pre-rebuild store: 48 rows stamped [[ML4T_A3_0003]] while carrying
[[ML4T_A3_0004]], and no allocation-stage equal-weight rows at all.

All allocator lookbacks come from the case-study configuration. The official population is fixed
before execution; machine speed and caught failures cannot change which allocators run.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What allocation decides, and why it is not a detail

The baseline held every selected product in the same size. That is a real choice, not the
absence of one, and it says something specific: that the signal's ranking carries information
about *which* products to hold and nothing about *how much* of each.

An allocator disputes that. It sizes positions by some property the ranking does not capture -
how volatile a product has been, how it co-moves with the others, how confident the model was.
The claim is that two products the signal ranks equally are not equally worth the same dollar
risk.

For futures this is a larger effect than it would be in equities, and the reason is in the
instruments. A gold contract and a natural-gas contract with equal notional exposure carry
entirely different risk, because their volatilities differ by a wide margin and they do not
move together. An equal-weight book of futures is therefore not a neutral book: it is one
whose realized risk is dominated by whichever contracts happen to be most volatile, and its
overall behaviour can be driven by two or three positions out of thirty regardless of what the
signal said.

### What the alternatives are actually doing
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

The declared methods differ in how much they estimate, and that is the axis to read them on.
Sizing inversely to a product's own volatility uses one number per product and no relationship
between them - it equalizes risk contribution under the assumption that the products are
independent, which they are not, but it is robust because a single volatility is estimated
accurately from little data. Methods that use the covariance between products can in principle
do better, because diversification is a property of the relationships rather than of any one
series. In practice they must estimate far more quantities from the same history, and a
covariance matrix estimated from a short window is dominated by noise that the optimizer then
treats as signal - which is why the more sophisticated method is not reliably the better one
and why they are compared here rather than assumed.

### Why the lookbacks are declared in configuration

Every allocator reads a history to estimate from, and the length of that history is a free
parameter that materially changes the result: a short window tracks a regime change quickly
and is noisy, a long one is stable and stale. Choosing it by validation Sharpe would be fitting
the allocator to the same path it is then assessed on, and the improvement would be
indistinguishable from a real one. The lookbacks come from [[ML4T_A3_0001]] for the same
reason the risk-overlay parameters do.

### Why equal weight is excluded here rather than re-run
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

Equal weight is the baseline, and the paragraph above the parameter cell records what happens
if it is run again in this stage: because [[ML4T_A3_0001]] is not part of [[ML4T_A3_0002]], the row
hashes identically to its baseline parent and one of the two is silently lost. Measured in
this case study's own pre-rebuild store, 48 rows carried [[ML4T_A3_0003]] while declaring
[[ML4T_A3_0004]], and there were no allocation-stage equal-weight rows at
all. The comparison a reader wants - allocator against equal weight - is made against the
baseline population, not by recomputing it here.

### These candidates stay eligible

Allocation results are part of the final selection pool, so an allocator that genuinely
improves validation Sharpe can be what the case study ships. One consequence to carry forward:
every allocator except equal weight re-sizes positions as its estimates move, which is
turnover the baseline did not have. [[ML4T_A3_0005]] is where that is priced, and an allocator's
advantage here is a gross number.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>

### c0004-p000

~~~~~~markdown
## Select signal configurations by validation Sharpe

The shortlist is deterministic. It scans the immutable signal candidate set in descending Sharpe
order with the backtest identity as tie-break, and keeps one exact checkpoint and strategy per
distinct [[ML4T_A3_0001]] pair.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>
