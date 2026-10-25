# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/00_classical_simulation.ipynb；A3 Pack 002；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Clustering → 分群
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0019-p000

~~~~~~markdown
## Mean-Reversion (Ornstein-Uhlenbeck)

Prices gravitate toward a long-term equilibrium [[ML4T_A3_0001]]:

[[ML4T_A3_0002]]

where:
- [[ML4T_A3_0003]] = speed of mean reversion
- [[ML4T_A3_0004]] = long-term mean (log-price level)
- Half-life: [[ML4T_A3_0005]]

### Key Properties

- **Stationary**: Prices fluctuate around equilibrium
- **No trends**: Can't capture bull/bear markets
- **Negative autocorrelation**: Today's move partially reversed tomorrow

### Discretization Options

**Euler-Maruyama** (approximate):
[[ML4T_A3_0006]]

**Exact transition** (closed-form for OU):
[[ML4T_A3_0007]]

We implement both to compare discretization error.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
### Exact Transition Density

The OU process has a closed-form transition density, eliminating
discretization error entirely. We implement both to compare accuracy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
### Mean-Reversion Simulation

The half-life is derived from the reversion speed rather than retyped, so it
tracks any change to the parameter. Euler and exact are then run from the
**same** stream of shocks: both consume one standard normal per step in the
same order, so the two paths differ only by discretization error and the gap
between them measures exactly that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
### Library Usage: Mean-Reversion

The provider's [[ML4T_A3_0001]] model reverts the log price to [[ML4T_A3_0002]], so
the equilibrium is a parameter you can set and the call below sets it to the same
[[ML4T_A3_0003]] the from-scratch path uses. The reversion speed is what you cannot
set: it is fixed internally at whatever value the package chose, which happens to be
the one [[ML4T_A3_0004]] carries above, so the two paths line up here by coincidence rather
than by construction. Speed is usually the quantity you want to fit for a spread or a
rate, which is why the from-scratch implementation stays useful.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## Heston (Stochastic Volatility)

Volatility itself is random, following a separate mean-reverting process:

[[ML4T_A3_0001]]
[[ML4T_A3_0002]]
[[ML4T_A3_0003]]

where:
- [[ML4T_A3_0004]] = instantaneous variance
- [[ML4T_A3_0005]] = variance mean-reversion speed
- [[ML4T_A3_0006]] = long-term variance
- [[ML4T_A3_0007]] = volatility of volatility ("vol of vol")
- [[ML4T_A3_0008]] = correlation between price and variance shocks (leverage effect)

### Key Properties

- **Stochastic volatility**: Vol changes unpredictably
- **Leverage effect**: [[ML4T_A3_0009]] means price drops increase volatility
- **Fat tails**: From randomness in volatility
- **Volatility clustering**: From mean-reversion in variance
- **Feller condition**: [[ML4T_A3_0010]] prevents variance from hitting zero

### Discretization: Full Truncation Euler

To handle potential negative variance, we use **full truncation**:
apply [[ML4T_A3_0011]] consistently in both drift and diffusion terms.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
### Heston Simulation

The variance starts at its long-run level, so the long-run volatility is the
square root of [[ML4T_A3_0001]].

The Feller condition, [[ML4T_A3_0002]], decides whether zero is attainable.
Below it the variance reaches zero with positive probability. It is not absorbed
there: the drift [[ML4T_A3_0003]] is positive at zero and pushes the variance
back up. That is a different regime of the same model rather than an invalid one, and
plenty of fitted Heston parameters sit in it. These values satisfy the condition, so
the continuous process stays strictly positive. The assertion reads the same named
parameters that drive the simulation, so an edit that moves them into the other
regime fails here rather than quietly changing what the figure shows.

Satisfying the condition is a statement about the continuous process, not about the
discretization. An Euler step can propose a negative variance under any parameters,
which is why [[ML4T_A3_0004]] truncates at zero either way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
### Library Usage: Heston

The provider exposes the full Heston parameter set except the initial variance,
which it always starts at the long-run level [[ML4T_A3_0001]] — the same choice
made above. Passing all four means the provider runs the same process, so the
realized volatility of the two paths should agree up to sampling noise. Leaving
[[ML4T_A3_0002]] at its default would silently simulate a different, slower
reverting variance process.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
---
# Part 2: Discrete-Time Volatility Model (GARCH)

Unlike the continuous-time SDEs above, GARCH is a **discrete-time model**
for conditional variance. It models how return volatility evolves based on
past shocks.

## GARCH(1,1)

[[ML4T_A3_0001]]
[[ML4T_A3_0002]]

where:
- [[ML4T_A3_0003]] = unconditional mean return (drift)
- [[ML4T_A3_0004]] = base variance (intercept)
- [[ML4T_A3_0005]] = reaction to recent shocks (news impact)
- [[ML4T_A3_0006]] = persistence of past variance (memory)
- [[ML4T_A3_0007]] required for stationarity

### Key Properties

- **Volatility clustering**: [[ML4T_A3_0008]] means vol persists
- **Fat tails**: From time-varying volatility
- **Mean-reverting volatility**: Unconditional variance = [[ML4T_A3_0009]]
- **Leverage effect**: Requires asymmetric extensions (GJR-GARCH, EGARCH)

### GARCH vs Heston

| Aspect | GARCH | Heston |
|--------|-------|--------|
| Time | Discrete | Continuous |
| Leverage | Extensions needed | Built-in ([[ML4T_A3_0010]]) |
| Calibration | MLE from data | Option surface |
| Analytical | Limited | Semi-closed form |

## Calibration: Fitting GARCH to Data

Unlike SDEs where we **choose** parameters (drift, volatility), GARCH is
typically **fitted** to historical data via maximum likelihood estimation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
### Fit GARCH(1,1) to SPY
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
### Simulate from Calibrated Parameters

Now we can simulate new paths using the fitted parameters.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000

~~~~~~markdown
### GARCH Simulation from Calibrated Parameters

Use the fitted SPY parameters to generate a synthetic path and compare
the resulting moments with the calibrated values.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
### Library Usage: GARCH

The provider takes [[ML4T_A3_0001]] and [[ML4T_A3_0002]] but **not** omega: it derives
omega from [[ML4T_A3_0003]] and the requested frequency, and a [[ML4T_A3_0004]]
argument is accepted, ignored, and warned about. Passing the fitted omega
therefore does nothing, and the resulting series is calibrated to SPY in its
persistence but not in its level.

To carry the calibration across, convert the fitted unconditional variance into
an annual volatility and pass that instead. Because [[ML4T_A3_0005]] is fitted on
returns in percent, the conversion divides by 100 before annualizing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
---
## Visualize All Parametric Models
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>
