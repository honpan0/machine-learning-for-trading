# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/06_fed_announcement_bsts.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Time series → 時間序列

## 待翻譯英文單元

### c0012-p000

~~~~~~markdown
## 2. BSTS Event Study Functions

The event study workflow has three stages:
1. **Window computation**: Define pre/post periods from event date
2. **BSTS estimation**: Run the [[ML4T_A3_0001]] Bayesian structural time series
3. **Dispatcher**: Assemble per-event results into a comparable summary

[[ML4T_A3_0002]] (Willian Fuks, 2025) is the actively maintained TFP port of the
original Google R package. It implements BSTS and exposes the posterior columns
used below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0013-p000

~~~~~~markdown
### The Analysis Window

Compute pre/post periods and filter data for the analysis window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Running BSTS with [[ML4T_A3_0001]]

Bayesian BSTS engine faithful to the original Google R package. Provides
posterior credible intervals - a probability statement about the parameter -
rather than frequentist confidence intervals.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
#### Extracting the Posterior Effect

Normalize column naming differences across [[ML4T_A3_0001]] versions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
#### The BSTS Runner

Execute BSTS inference and normalize outputs for downstream validation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
### The Event Study Dispatcher
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
## 3. Spillover Validation

The counterfactual is built from the controls, so a control that responds to the
announcement carries part of the effect into the thing the effect is measured against.
This section runs the same BSTS specification with each control as the target and the
remaining controls as its predictors, and flags a control whose own post-period interval
excludes zero.

**What the test can and cannot see.** A control is judged against the other controls, so
the flag fires on a control that moves *differently* from them. A Fed announcement that
moves all three through the same dollar and global-risk channel moves each one's
predictors with it, and none of the three is flagged - which is the contamination that
matters most for the target's counterfactual. Read a clean result as "no differential
response among the controls", not as "the controls were unaffected". The design that
would answer the stronger question needs a control set with no plausible exposure to US
policy rates at all, and the caveat under Control Selection Rationale says what that
would cost.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0028-p000

~~~~~~markdown
## 4. Analyze Key FOMC Events

We analyze the response to selected Fed announcements in bond ETFs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0031-p000

~~~~~~markdown
The chart reports the estimand in log-return units. Intervals that cross zero
do not distinguish the event response from posterior uncertainty; intervals
that exclude zero remain conditional on the no-spillover assumption.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
**Interpretation**: The FOMC event results above show whether the target ETF
(IEF by default) moved significantly after rate decisions, after constructing a
counterfactual from its controls. The causal impact estimates capture the *additional*
movement attributable to the announcement beyond what correlated assets predicted.
The uncertainty intervals, rather than a macro narrative about each date, determine
whether the model distinguishes an event response from market-wide risk.
Credible intervals that include zero indicate the model cannot distinguish the
event effect from noise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
## 5. Placebo Test Validation

Run the same analysis on 12 dates with no Fed announcement. A
"significant" cumulative impact on any of these dates means the model
is misspecified. With so few placebo dates the empirical rate is a
coarse diagnostic rather than a precise Type I estimate: a single
flagged window moves it by a large step, and its denominator is not the
twelve dates listed but however many of them survive the FOMC screen
applied below, which is the count printed beside the rate. We therefore
report it as a *placebo false-positive rate*, not a multiple-testing FDR.

**Caveat - macro contamination of placebo dates**: "No FOMC announcement"
is necessary but not sufficient. A clean placebo date for a Fed/bond
event study should also avoid CPI prints, payrolls, Treasury refunding
announcements, FOMC minutes, banking stress headlines, and other
macro releases that move the rates curve. The 12 dates below are not
screened for these - they are illustrative, and a publication-grade
placebo test would filter against a macro-calendar exclusion list
before computing the rate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
A placebo date is only a placebo if its post-window is clear of the announcements this
notebook is studying. The windows are twenty trading days long and the FOMC meets every
six to eight weeks, so a date chosen for being on no announcement can still sit a fortnight
ahead of one, and its "false positive" would then be a true effect measured from the wrong
origin. The screen below is against [[ML4T_A3_0001]], the four dates this notebook treats as
events; the wider macro calendar in the caveat above is not screened, so a window this
check calls clear is clear of those four dates and nothing more.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
A valid design should rarely produce credible intervals excluding zero on
dates without an FOMC announcement. This chart makes both the false-positive
count and the uncertainty behind each placebo estimate visible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
## 6. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>
