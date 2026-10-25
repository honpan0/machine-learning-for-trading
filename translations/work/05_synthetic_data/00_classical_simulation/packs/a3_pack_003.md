# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/00_classical_simulation.ipynb；A3 Pack 003；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Drawdown → 回撤
- Feature → 特徵
- Clustering → 分群
- Volatility → 波動率

## 待翻譯英文單元

### c0046-p000

~~~~~~markdown
### Normalized Price Paths (Grayscale-Compatible)

A matplotlib companion to the plotly grid above, using distinct line styles
that remain distinguishable in grayscale print.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0048-p000

~~~~~~markdown
These are five single realizations, one per model, and a picture of five
paths cannot separate a model's properties from the draw that produced them.
That includes the two features most tempting to read as structural. The
jump-diffusion panel does not show discontinuities: the series is sampled
daily, so every step is already a gap on the page, and GBM's Gaussian log
increments produce occasional large days of their own. The mean-reversion
panel does not show a band either, because the log-OU process here has
unbounded Gaussian innovations and only drifts back toward equilibrium.
What actually separates these models is that jump-diffusion is discontinuous
in continuous time and mean reversion carries a restoring drift, and this
figure can show neither. Which path looks calmest and which drew the deepest
drawdown are properties of the draw. The next section measures the model
properties across many draws instead.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0049-p000

~~~~~~markdown
## Model Statistics Comparison

Each model is simulated [[ML4T_A3_0001]] times so the comparison describes the
**model** rather than one path. The sample excess kurtosis of a Gaussian
series of length [[ML4T_A3_0002]] has a standard error of [[ML4T_A3_0003]], which at
this path length is large relative to the gaps between several of these
models, so an ordering read off one path per model is mostly noise. The cell
below prints it alongside GBM's measured spread.

The models are also **not** run at a common volatility: [[ML4T_A3_0004]] and
[[ML4T_A3_0005]] set one level, [[ML4T_A3_0006]] and [[ML4T_A3_0007]]
another, and GARCH inherits whatever the SPY fit implies. The volatility
column therefore reports the input, not a finding, and drawdown depth is not
comparable across rows for the same reason. Excess kurtosis and skewness are
the columns that describe the models, because no parameter sets them
directly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
### Simulating a Population of Paths

[[ML4T_A3_0001]] re-runs each generator [[ML4T_A3_0002]] times from
independent child streams of the [[ML4T_A3_0003]] seed, so the paths are
independent of each other and of the illustrative paths plotted above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0054-p000

~~~~~~markdown
### Which Models Separate

Rather than reading an ordering off the medians, compare each model's excess
kurtosis against GBM's. GBM is the null here: its log-returns are Gaussian by
construction, so its spread over [[ML4T_A3_0001]] paths is the sampling noise of the
statistic at this path length, and a model separates only if its own spread
sits clear of that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0056-p000

~~~~~~markdown
### Volatility Clustering in the Same Populations

Fat tails and volatility clustering are separate properties, and so far only
the first has been measured. Summarize clustering the same way the bootstrap
section does — the sum of the autocorrelations of squared returns over the
first [[ML4T_A3_0001]] lags — and read it against GBM, whose returns are independent
by construction and whose spread is therefore the null.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0058-p000

~~~~~~markdown
**What the comparison establishes.** Three models generate excess kurtosis and
they order the same way in every pairwise comparison: jump-diffusion above
GARCH above Heston. Jump-diffusion is the clearest, exceeding GBM's 95th
percentile on nearly every path, which is what an explicit jump component is
for. GARCH exceeds Heston on close to three quarters of path pairs, so the
ordering between those two is real even though their ranges overlap and a
single path from each would not have shown it.

Mean-reversion is indistinguishable from GBM on kurtosis: it clears GBM's 95th
percentile at about the rate chance alone would produce. Its visibly narrower
price range comes from the lower volatility it was parameterized with and from
the pull toward equilibrium, neither of which is a tail property.

On clustering the split is different and cleaner. GBM, mean-reversion and
jump-diffusion all sit at the GBM null rate: jumps arrive independently, so
adding them fattens the tails without making one volatile day predict the
next. Heston and GARCH both clear the null on the large majority of paths,
which is what a mean-reverting variance process and a variance recursion are
for, and GARCH does so on every path and at roughly three times Heston's
median.

The comparison against SPY needs the same window length on both sides. The
statistic sums twenty autocorrelation estimates, and both the bias and the
variance of each estimate depend on the sample length, so a value computed on
SPY's whole history and a value computed on a simulated path of [[ML4T_A3_0001]] are
not two measurements of the same quantity. Equal-length windows make them
comparable; they do not make either one a better estimate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0058-p001

~~~~~~markdown

Measured that way, GARCH's distribution is centered slightly **above** SPY's
median rather than short of it, and Heston's sits below. Read the nine SPY
windows before reading that as a stable ranking: they span most of the range
the models occupy, and they differ in the volatility regimes they cover as
well as in sampling noise, so neither the spread across windows nor the gap to
the full-history value has a single cause the notebook has isolated.

So the two properties order the models differently. Jump-diffusion has the
heaviest tails and no clustering at all; GARCH has the most clustering and the
second-heaviest tails; Heston has both, more weakly than GARCH on each.

For risk work: GBM and mean-reversion put no more weight in the tails than a
Gaussian, so VaR and ES computed from them understate tail loss by
construction. The magnitudes separating the other three are large enough to
matter — the jump model's median excess kurtosis is an order of magnitude
above the other two — so the choice among them is not a rounding difference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p001>>>
<<<ML4T-ZH-END:c0058-p001>>>
