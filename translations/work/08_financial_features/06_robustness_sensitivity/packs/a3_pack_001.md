# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/06_robustness_sensitivity.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market regime → 市場狀態
- Momentum → 動能
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Robustness and Sensitivity Analysis

**Chapter 8: Feature Engineering**
**Section Reference**: 8.6, Combining Features and Controlling Search

**Docker image**: [[ML4T_A3_0001]]

## Purpose

A robust signal maintains performance across reasonable variations in
parameters, regimes, and implementation choices. This notebook teaches how
to assess robustness through parameter sweeps, regime conditioning, and
signal × state interactions.

## Learning Objectives

1. Conduct parameter sweeps as response-surface analysis
2. Define robustness as the **breadth of the near-optimal region**
3. Analyze regime-conditional IC with clean conditioning variables
4. Build signal × state interaction features (gating, scaling, conditional)
5. Apply RAS correction for parameter snooping

## Data Policy

All examples use **real ETF data**.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## Data Loading
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
Parameter sweeps and robustness diagnostics are development decisions, so the holdout
must not inform them; the rule is set out in [[ML4T_A3_0001]].
The boundary comes from the case study's own [[ML4T_A3_0002]] under
[[ML4T_A3_0003]], and the analysis window is clamped to it so that an
[[ML4T_A3_0004]] override cannot reach past it. Every IC computed below, in the sweep, the
snooping correction, the regime conditioning and the implementation variants alike,
reads pre-holdout data only.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
## IC Computation Helpers

All IC statistics use HAC standard errors via the [[ML4T_A3_0001]] library
to account for serial dependence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Compute IC Series for a Momentum Signal
For each date, compute cross-sectional Spearman IC between the momentum
signal and forward returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## Parameter Sweep: Response Surface

We vary the momentum lookback period and observe how IC changes. The goal
is not to find the "best" parameter but to understand the **response
surface** and identify a **robust region**.

**One knob at a time**: The sweep varies lookback while holding everything
else constant (return metric, normalization, label horizon). Changing
multiple parameters simultaneously makes it impossible to attribute
performance changes to any single choice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0016-p000

~~~~~~markdown
## Robustness: Breadth of Near-Optimal Region

Robustness is **not** a scalar score such as a mean-over-standard-deviation ratio. It is
the breadth of the near-optimal region: how many parameter values reach a performance
within [[ML4T_A3_0001]] of the peak. A robust signal has a broad plateau; a fragile
one has a narrow peak, and a single tall value surrounded by poor neighbours is the
shape that does not survive contact with new data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0021-p000

~~~~~~markdown
Read the robust fraction printed above against the shaded region in the figure. On this
sweep the region is a single point: one lookback reaches the threshold and none of its
neighbours do. That is the narrow-peak shape, and it is the one to distrust. A lookback
that works at its own value and fails a step either side is more plausibly the luckiest
draw from the sweep than a property of the signal.

The line printed beneath it is the stronger statement, and it is worth pausing on. Not
one lookback in the sweep produces a mean IC distinguishable from zero at the usual
threshold, and the error bars in the response-surface figure show the same thing: every
band crosses the zero line, the one at the peak included. So "best lookback" here names
the largest of a set of estimates that are individually consistent with no signal at
all. Ranking them is still the right diagnostic, because the shape of the surface is
informative even when its level is not, but the ranking does not license a claim that
the top-scoring window carries an edge. The snooping correction below quantifies how much of that peak is
attributable to having looked at several windows.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
### RAS Correction for Parameter Snooping

After sweeping N parameter combinations, the highest IC in the sweep is biased upward:
it was chosen for being highest. RAS deflates it with a correlation-aware multiple-
testing correction, in which nearby parameters produce correlated IC estimates and so
count as fewer independent tests than their number suggests.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## Regime-Conditional Performance

A robust signal maintains predictive power across market regimes. We use
42-day realized volatility on SPY as a clean, pre-defined conditioning
variable. Tercile thresholds use expanding-window percentiles to avoid
lookahead bias.

**Warning**: Avoid conditioning on variables derived from the signal itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### Compute Regime-Conditional IC
Split the IC series by volatility regime to check signal stability.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0029-p000

~~~~~~markdown
### Conditional IC Distribution by Regime

Box plots of the daily IC observations within each volatility tercile, with
the raw daily ICs overlaid, show how the distribution shifts across regimes -
not just the mean, but the spread and skew.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
The regime table above carries the reading the figure invites: mean IC is highest in the
low-volatility regime, smaller in the normal one, and negative in the high-volatility
one, and only the low-volatility estimate reaches significance on its own t-statistic.
Note what that does and does not license. Three regimes is three tests, the split points
are choices, and an IC that changes sign across them is a claim about this sample. The
printed IC range is the quantity the conditioning decision keys on, and it clears
[[ML4T_A3_0001]] here comfortably enough that the interaction features below are
worth building.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0032-p000

~~~~~~markdown
## Signal and State Interaction Features

Three interaction templates, each demonstrated with momentum as the signal and realized
volatility as the state.

| Template | Construction | What changes |
|---|---|---|
| **Gating** | Zero signal in high-vol regime | Active sample (turnover, capacity) |
| **Scaling** | Divide signal by volatility | Position size |
| **Conditional** | IC computed within each regime | Separate testable hypotheses |
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>
