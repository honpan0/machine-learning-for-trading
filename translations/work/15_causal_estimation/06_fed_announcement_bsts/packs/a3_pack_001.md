# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/06_fed_announcement_bsts.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Machine learning → 機器學習
- Time series → 時間序列

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Fed Announcement Event Study with BSTS

**Chapter 15: Causal Machine Learning**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: See Section 15.5 for BSTS theory and event study methodology

> **[[ML4T_A3_0002]] image required.** [[ML4T_A3_0003]] (the TensorFlow-Probability
> BSTS package) does not support the Python the main [[ML4T_A3_0004]] image runs, so this
> notebook runs in the [[ML4T_A3_0005]] image instead:
>
> ```bash
> docker compose --profile py312 run --rm py312 \
>     /opt/bsts/bin/python 15_causal_estimation/06_fed_announcement_bsts.py
> ```

## Purpose
This notebook implements a **Bayesian Structural Time-Series (BSTS)** event study
to measure the causal impact of Federal Reserve announcements on bond ETFs. We
demonstrate counterfactual construction, control selection, and validation through
placebo tests - the complete event study workflow.

## Learning Objectives
After completing this notebook, you will be able to:
- LO1: Construct data-driven counterfactuals using BSTS models
- LO2: Select appropriate control series that avoid spillover contamination
- LO3: Measure cumulative effects and interpret posterior credible intervals
- LO4: Validate event study results using placebo tests

## Cross-References
- **Upstream**: ETF Universe data (Chapter 3), macro data (Chapter 5)
- **Downstream**: Strategy evaluation (Chapter 16), risk events (Chapter 19)
- **Related**: [[[ML4T_A3_0006]]](01_library_overview.ipynb) (library selection), [[[ML4T_A3_0007]]](07_tigramite_time_series.ipynb) (time series)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Key Concepts
1. **Counterfactual construction**: Build "synthetic twin" of what would have happened
2. **Control series selection**: Choose correlated but unaffected time series
3. **Causal impact measurement**: Difference between actual and counterfactual
4. **Placebo validation**: Verify model doesn't find false positives

**Prerequisites**: [[[ML4T_A3_0001]]](01_library_overview.ipynb) for library context;
ETF OHLCV data from Ch2 data pipeline
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## Configuration

### Window Length Justification (Brodersen et al., 2015)

**Pre-period (60 trading days, ~3 months)**:
- Sufficient to learn stable control relationships
- Short enough to avoid regime changes (Fed policy cycles ~6 months)
- This notebook reports the 60-day baseline only; a sensitivity sweep
  over pre_days ∈ {45, 60, 90} and post_days ∈ {10, 20, 30} is left
  to the reader as the BSTS MCMC fit is the bottleneck.

**Post-period (20 trading days, ~1 month)**:
- Allows 2-3 weeks for bond-market repricing
- Captures full policy transmission to yields
- Balances impact capture vs contamination from subsequent events

## Causal Design Contract
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0004-p001

~~~~~~markdown

| Element                   | This notebook                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| Unit                      | Trading day in the IEF + control-ETF panel                                                          |
| Treatment                 | FOMC announcement on the event date (discrete event)                                                |
| Outcome                   | Cumulative abnormal log return on IEF over the 20-trading-day post-window                           |
| Controls                  | Daily log returns of VEA, EFA, DBC entered into the BSTS counterfactual model                        |
| Effect modifiers          | None - separate event studies per FOMC date                                                          |
| Identification assumption | Controls move with IEF in the pre-period and are *not affected by the FOMC event* in the post-window |
| Main failure modes        | Control spillover (Fed shocks the dollar and global risk; international ETFs are not unaffected); placebo-date contamination by other macro releases; daily bars mix pre- and post-announcement trading |
| Estimand                  | Cumulative abnormal log return attributable to the FOMC event; reported with the BSTS posterior credible interval |

The panel is whatever [[ML4T_A3_0001]] and [[ML4T_A3_0002]] name in the parameters
cell. This table describes the production defaults - IEF against VEA, EFA and
DBC - which is what the committed run studies; change those parameters and the
unit, outcome and controls change with them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p001>>>
<<<ML4T-ZH-END:c0004-p001>>>

### c0004-p002

~~~~~~markdown

FOMC decisions are announced before the market close. The event-day close-to-close
return therefore contains both the pre-announcement portion of that trading day and
the post-announcement response. This timing is part of the estimand, not a claim that
the full event-day return was known when the announcement occurred.

### Control Selection Rationale

Fed decisions can affect broad US financial markets. Using SPY or VNQ as
controls is problematic because they may react to the same announcement.
The argument rests on two categories, international and commodity, rather than
on the particular tickers, so [[ML4T_A3_0001]] should cover both. The default set
and the panel the CI run substitutes are both two international controls and one
commodity control. The defaults are:
- **International ETFs** (VEA, EFA): Correlated through global risk factors
  but less directly affected by FOMC (which targets US policy rates)
- **Commodities** (DBC): Affected by USD but different transmission mechanism

**Caveat - control affectedness is real**: This is the *plausible* control
set, not an unaffected one. FOMC announcements move the dollar, global
risk appetite, global yields, and commodities through cross-border
capital flows and the dollar funding channel. The placebo test and the
per-event spillover test below bound the residual contamination; a
more conservative design would use non-US sovereign-bond ETFs or a
local-level model with no ETF controls and a longer pre-window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p002>>>
<<<ML4T-ZH-END:c0004-p002>>>

### c0007-p000

~~~~~~markdown
## 1. Load ETF Price Data

We need daily prices for the target ETF and its controls - IEF against VEA,
EFA and DBC by default. Data loaded from curated ETF universe (book data
pipeline).
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The target and controls are daily log returns, so summing the post-period point effects
estimates a cumulative abnormal log return. A specification on log price *levels* would
sum level gaps in log-point-days instead, which is not the estimand declared above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>
