# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/02_microstructure_features.ipynb；A3 Pack 002；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Look-ahead bias → 前瞻偏誤
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0023-p000

~~~~~~markdown
## Feature Timing: Alpha vs Feasibility

**Critical distinction**: Some microstructure features are alpha signals;
others are feasibility/cost state variables.

| Feature | Category | Lag Requirement | Use Case |
|---------|----------|-----------------|----------|
| **OFI** | Alpha | Lagged 1+ bar | Predict next-bar returns |
| **Kyle λ** | Feasibility | Contemporaneous OK | Execution cost estimate |
| **Amihud** | Feasibility | Contemporaneous OK | Position sizing |
| **Trade Intensity** | Context | Contemporaneous OK | Regime detection |

### Alpha Features Must Be Lagged

When using OFI or similar flow features as **predictors**, you must lag them
to avoid look-ahead bias:

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
**Interpretation**: the same-bar correlation is the larger of the two, and it is the one
that cannot be traded. A bar with a buy imbalance is usually a bar whose price rose, so
the same-bar number is mostly the definition of an up bar read back to you; a strategy
that uses it is assuming it knows the bar's outcome while the bar is still open. The gap
between the two numbers is what look-ahead bias is worth here.

The lagged correlation is the one a strategy could act on, and this sample does not
establish that it is different from zero: its interval spans zero while the same-bar
interval does not. That is the honest reading, and it is not a disappointing one. What
the notebook demonstrates is the construction and the size of the bias, both of which
are visible in a single session. Whether lagged OFI carries tradable content is a
question for many sessions and many names, and the right response to a wide interval is
to widen the sample rather than to quote the point estimate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0026-p000

~~~~~~markdown
## Flow vs State: Critical Distinction

> **WARNING: Flow vs State Confusion**
>
> Many practitioners confuse **flow features** (events over a window) with
> **state features** (snapshot at a point in time).

| Concept | Example | Correct Computation |
|---------|---------|---------------------|
| **Flow** | Trades in last 5 min | Count events in window |
| **State** | Current bid-ask spread | Snapshot of book state |
| **Flow** | Volume imbalance | Sum buy vs sell volume |
| **State** | Book depth at best bid | Current LOB level |

### Order Book Spread: A State Feature

The bid-ask spread is a **state** property: the current top of book.
You cannot compute it from order **flow** (arrivals) because:

1. Cancellations remove orders but aren't in arrival flow
2. Executions remove orders from the book
3. The book has memory; flow only captures additions

**Correct approach**: Reconstruct the full LOB state (see Chapter 3).
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## Composite Liquidity Score

Combining multiple liquidity metrics into a single score via z-score
normalization then summation.

### Scope: descriptive composite construction, not a prediction signal

The z-scores below use **full-sample** mean and standard deviation across the
entire history of each metric. The resulting composite is an *ex-post*
characterization of how the three illiquidity measures combine on this sample, which is
what the dashboard below needs. It is **not** a lookahead-safe feature: each z-score
divides by a mean and variance taken over the whole history, future bars included, so
[[ML4T_A3_0001]] carries information from after the bar it is attached to. Feed it to
a regression and the fit is scored partly on knowledge the model would not have had.

The lookahead-safe construction (expanding-window percentiles / rolling
z-scores) is demonstrated in
[[[ML4T_A3_0002]]](06_robustness_sensitivity.ipynb), which
uses expanding-window quantiles to threshold a state variable without
leaking future values, and again in the per-case-study feature pipelines
under [[ML4T_A3_0003]] where production features are
constructed inside walk-forward folds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0031-p000

~~~~~~markdown
## Cross-Stock Comparison

Microstructure features help identify which stocks are more liquid
and thus have lower trading costs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0032-p000

~~~~~~markdown
The summary below carries the two estimators and the quantities they are built from, so
the orderings can be traced rather than asserted. The last column is Amihud's own per-bar
ratio, formed bar by bar and then summarised: a median of ratios, not a ratio of medians.
The distinction matters because a ratio of medians discards the pairing between each
return and the dollar volume that accompanied it, and can order the names differently.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
**Interpretation**: compare the two orderings printed above before drawing anything from
either. On this session they do not merely differ at the margin; read the lists and see
how much of the disagreement is a reordering and how much is a reversal. A reader who
had taken one measure as *the* liquidity ranking and sized positions against it would
have sized them against the other measure's answer inverted.

Neither measure is wrong, and on this sample the five orderings printed above say where
the disagreement comes from. Compare the Kyle ordering against the median absolute
return, and the Amihud ordering against the median absolute return per million dollars.
Each estimator's ordering is the ordering of one of those two raw quantities.

That is what the denominators do. Kyle's ratio divides volume by its own rolling mean,
which is close to one on a typical bar, so across names it is left ranking by how large
a typical return is. Amihud divides by dollar volume in dollars, which differs across
names by a large factor, so it ranks by return per dollar traded. A name whose returns
are the largest and whose dollar volume is also the largest therefore lands at the
illiquid end of one list and the liquid end of the other. The reversal is a property of
these three names on this session rather than something that must happen; what is
general is that the two estimators rank by different quantities, and the orderings above
are how you check which.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0034-p001

~~~~~~markdown

What follows for practice is that "illiquid" has to name a measure, and a feasibility
overlay has to say which one it gates on and why. It also follows that one session of
three names settles none of this: the orderings above are an illustration of how far two
proxies can part, not an estimate of these three stocks' liquidity. In production these
features feed the overlay that gates position size (see [[ML4T_A3_0001]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p001>>>
<<<ML4T-ZH-END:c0034-p001>>>
