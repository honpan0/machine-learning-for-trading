# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/05_signal_evaluation.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Market microstructure → 市場微觀結構
- Momentum → 動能
- Transaction costs → 交易成本
- Feature → 特徵
- Out-of-sample → 樣本外
- Walk-forward validation → 滾動向前驗證
- Overfitting → 過度擬合
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0029-p000

~~~~~~markdown
## Quantile Analysis

Examine returns by signal quantile to assess **monotonicity** (do higher signal
values lead to higher returns?) and **spread** (what's the return difference
between top and bottom quantiles?).
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
The bars do not rise with the quantile in any of the three panels, and in the shortest
horizon they fall - the bottom quantile of the signal earns the most. A long-short book
built the obvious way round would be short the better-performing leg. The spread and
monotonicity numbers below put figures on that, and the sign is the part to read first.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
### Monotonicity Interpretation

[[ML4T_A3_0001]] reports monotonicity as the **Spearman rank correlation between the
quantile ranks and their mean returns**, so it runs from [[ML4T_A3_0002]] to [[ML4T_A3_0003]]: [[ML4T_A3_0004]] is a
perfectly increasing ladder of quantile returns, [[ML4T_A3_0005]] a perfectly decreasing one, and
[[ML4T_A3_0006]] no rank association at all. It is a correlation, not a percentage, and is reported
as such below.

That is not the same statistic as the one the fold section computes further down, which
is the *fraction of adjacent quantile steps that move upward* and runs from [[ML4T_A3_0007]] to [[ML4T_A3_0008]].
The two answer the same question differently and do not share a scale; where both appear
they are named apart.

The bands below score the **strength** of the ordering, so they read the magnitude. The
sign is a separate fact and the more important one here: a strongly ordered signal
pointing the wrong way is not a weak signal, it is an inverted one, and the two call for
opposite actions. The bands are kept in a declared table so the reading the prose gives
is the one the code applies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
## Horizon Comparison

Compare IC across different forward return horizons to identify the optimal
holding period for the signal.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
Read the two panels together. The left panel's bars change sign across horizons, which
invites a story about reversal giving way to momentum; the right panel says the whole
left panel is inside the noise, because an ICIR of essentially zero means the daily IC
series has a standard deviation orders of magnitude larger than its mean. The sign
pattern is not a finding at these magnitudes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000

~~~~~~markdown
### Overlapping Returns Warning

When comparing IC across horizons, be aware that **longer horizons have overlapping
forward returns**, which introduces autocorrelation in the IC series.

For example, 21-day forward returns on consecutive days share 20 days of overlap.
This means:

1. **IC series are autocorrelated** at longer horizons
2. **Standard errors are understated** without HAC adjustment
3. **Comparing IC across horizons requires caution** - higher IC at longer
   horizons may reflect overlap, not better predictability

**Best practice**: Use HAC-adjusted t-statistics (as provided by [[ML4T_A3_0001]])
and be skeptical of IC that increases monotonically with horizon.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0040-p000

~~~~~~markdown
### IC Decay Analysis

IC decay determines the optimal rebalancing frequency: a signal whose IC halves within a
week should not be held for a month. We compute IC on a finer horizon grid to estimate
the signal's useful life.

The half-peak marker below is drawn only for a crossing that comes **after** the peak.
Searching from the shortest horizon instead puts the marker on the first grid point
whenever the profile rises, which is the opposite of decay and reads to a reader as
decay. Where IC never falls back within the grid - the peak being the longest horizon on
it - no marker is drawn at all.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0043-p000

~~~~~~markdown
**Interpretation**: The horizon-IC curve is the tool for choosing a rebalancing
frequency - for a cleanly decaying signal you rebalance near where IC peaks and stop
before it fades. This factor does *not* show that decay. Every horizon IC printed above
sits within a few thousandths of zero, none is statistically distinct from zero, and the
profile is still rising at the longest horizon on the grid rather than falling away from
a peak. The half-peak marker is drawn only when a crossing exists *after* the peak, so
on this profile there is nothing to mark; a marker placed at the first horizon would
have described decay running backwards. The honest read is a factor with no exploitable
cross-sectional horizon structure on this universe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
## Turnover Analysis

High turnover erodes returns through transaction costs. A signal with high IC
but excessive turnover may not be profitable after costs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0046-p000

~~~~~~markdown
### Turnover and Costs

A simple cost-adjusted IC (Grinold approximation):

[[ML4T_A3_0001]]

Where [[ML4T_A3_0002]] is round-trip transaction cost and [[ML4T_A3_0003]] is expected return. For most equity
strategies, turning the whole book over once a month or more erodes alpha materially.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0047-p000

~~~~~~markdown
### Break-Even Cost Analysis

A feasibility check asks: **could this signal survive transaction costs?**

We compare the expected spread (top-bottom quantile return) to the cost of
achieving that spread. If round-trip costs exceed the expected edge, the
signal is not tradeable at the given rebalancing frequency.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0050-p000

~~~~~~markdown
### Feasibility Guidelines

Three checks for signal feasibility, from the chapter's *Preliminary feasibility
checks* section:

1. **Turnover proxies**: Measure entry/exit rates in the top-k set (see above)
2. **Break-even cost checks**: Compare spread to conservative cost estimates
3. **Capacity warnings**: Recompute IC by liquidity bucket (deferred to Ch8)

**Note**: Liquidity-bucket analysis requires actual market microstructure data
(average volume, bid-ask spreads) which is not available for this placeholder
feature. Chapter 8 demonstrates this check with real case study data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
## Fold-Aware Evaluation

**Critical**: The IC computed above pools all dates into a single statistic. However,
real trading strategies are evaluated on **out-of-sample** data using walk-forward
validation. This section demonstrates fold-aware IC computation.

### Why Folds Matter

Global IC can be misleading because:
1. **Regime dependence**: IC may be high in some periods and zero in others
2. **Lookahead contamination**: Parameters tuned on full data leak future information
3. **Overfitting detection**: Consistent IC across folds suggests robust signal

The text emphasizes computing IC **per fold** and reporting the distribution of
fold-level statistics, not just their pooled mean.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0052-p000

~~~~~~markdown
The splits below use an expanding window: train on everything up to the split point,
test on the period that follows.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>
