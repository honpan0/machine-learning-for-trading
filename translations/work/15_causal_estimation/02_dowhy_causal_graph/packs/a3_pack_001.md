# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/02_dowhy_causal_graph.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Feature engineering → 特徵工程
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Outcome Choice and Causal Credibility in Crypto Funding Premiums

**Chapter 15: Causal Estimation with ML**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 15.2 on outcome choice, Section 15.3 for the validation
workflow, and Section 15.4 (Table 15.2) for the two-outcome contrast

## Purpose
One treatment, two outcomes, and two very different levels of causal credibility.
The treatment is the premium *state* rather than the funding payment: the perpetual
trading above spot by more than two standard deviations, which creates funding
pressure and an arbitrage incentive. The outcomes are forward returns, a broad market
variable exposed to everything that moves crypto, and forward premium reversion, which
the funding mechanism acts on directly. The same estimator, the same adjustment set and
the same validation battery reach different conclusions about the two.

## Learning Objectives
After completing this notebook, you will be able to:
- LO1: Specify a DAG in DoWhy and read the adjustment set it identifies
- LO2: Explain how the tightness of the treatment-outcome mechanism bounds credibility
- LO3: Judge whether the available controls can plausibly block the backdoor paths a
  given treatment-outcome pair opens
- LO4: Read a partial-R2 sensitivity analysis and the robustness value it reports

## Cross-References
- **Upstream**: crypto premium index and perpetual OHLCV from [[ML4T_A3_0002]]
- **Downstream**: [[[ML4T_A3_0003]]](04_dml_crypto_regime.ipynb) applies DML to the
  same data with regime heterogeneity
- **Related**: [[[ML4T_A3_0004]]](01_library_overview.ipynb) for where DoWhy sits
  among the chapter's libraries
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Data Requirements
- Crypto premium index at 8h frequency - loaded via [[ML4T_A3_0001]]
- Crypto perpetual futures OHLCV at 1h frequency - loaded via [[ML4T_A3_0002]]

Both are produced by [[ML4T_A3_0003]].

## Causal Design

| Outcome              | Mechanism                              | Main validation tests                                                              |
|----------------------|----------------------------------------|------------------------------------------------------------------------------------|
| Forward 24h returns  | Indirect sentiment and risk channel    | OOS stability, placebo-date shift, return-scale and reversion-scale negative controls, partial-R2 sensitivity |
| Forward 24h premium  | Direct arbitrage-pressure channel      | OOS stability, placebo-date shift, return-scale and reversion-scale negative controls, partial-R2 sensitivity |

The computed comparison table appears at the end of the notebook.

## Causal Design Contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

| Element                   | Definition                                                                            |
|---------------------------|---------------------------------------------------------------------------------------|
| Unit                      | One BTC 8-hour bar                                                                    |
| Treatment                 | [[ML4T_A3_0001]] = [[ML4T_A3_0002]] (binary indicator of premium state)     |
| Outcomes                  | [[ML4T_A3_0003]] (3 bars) and [[ML4T_A3_0004]] (3 bars)                           |
| Controls                  | [[ML4T_A3_0005]], [[ML4T_A3_0006]] (both backward-looking, strictly pre-treatment)        |
| Effect modifiers          | None in this notebook                                                                 |
| Identification assumption | Selection on observables given the specified DAG; no contemporaneous unobserved cause |
| Main failure modes        | Unobserved confounding (sentiment shocks), bad controls, mistimed treatment           |
| Estimand                  | ATE of entering the extreme-high-premium state - not the marginal effect of a one-unit change in premium z-score |

**Prerequisites**: [[[ML4T_A3_0007]]](01_library_overview.ipynb) for library context
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0001-p000

~~~~~~markdown
## The Crypto Funding Rate Mechanism

In perpetual futures markets:
- **Premium** = (perp price - spot price) / spot price
- **Funding rate** = periodic payment to close the gap
- **High premium** [[ML4T_A3_0001]] longs pay shorts [[ML4T_A3_0002]] pressure to close longs

**Two causal questions**:
1. Does an extreme high premium cause future **returns**? This is what a directional
   trader wants to know.
2. Does an extreme high premium cause premium **reversion**? This is what an
   arbitrageur acts on.

The two questions share a treatment and differ in how much of the world sits between
that treatment and the outcome.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0002-p000

~~~~~~markdown
## Setup

Three third-party warnings are silenced by category and module. DoWhy compiles regular
expressions and docstrings with unescaped backslashes, which Python reports while
importing the package. pydot, which parses the graph string, calls pyparsing methods that
pyparsing has renamed. The third is a dead branch in DoWhy's [[ML4T_A3_0001]]:
under its default significance level it compares against [[ML4T_A3_0002]] where
[[ML4T_A3_0003]] is zero by construction, so the comparison is against infinity and never
fires. Convergence warnings and every other numerical warning stay visible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0003-p000

~~~~~~markdown
## Timing Protocol

Causal validity here rests entirely on the ordering below: every confounder is
computed from bars that close before the treatment is measured, and every outcome
from bars that open after it.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0007-p000

~~~~~~markdown
## Configuration
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## 1. Load and Prepare Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
### Feature Engineering

Every confounder is built from bars that close before the treatment is measured, and the
[[ML4T_A3_0001]] on each rolling window is what enforces it. At the 8-hour cadence, 3 bars span
24 hours and 21 bars span 7 days.

The cell also builds two negative-control outcomes over 24-hour windows that end 48 hours
*before* the treatment, so the treatment cannot reach them. There is one on each headline
outcome's scale, a return and a premium change, so each estimate has a control measured in
its own units.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## 2. Train/Test Split

We use a temporal split consistent with the pre-treatment timing discipline
discussed in Section 15.2.

Because the outcome is 24-hour forward (3 bars at 8h frequency), training
rows within the last [[ML4T_A3_0001]] of the cutoff would realize outcomes
*inside* the test window. That boundary band is purged, so every training outcome is
fully observed before the test period begins. The split boundary is cast to the data's
own timestamp dtype, which avoids a resolution or timezone mismatch.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>
