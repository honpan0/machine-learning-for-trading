# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/08_causal_sanity_checks.ipynb；A3 Pack 003；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0027-p000

~~~~~~markdown
### Feature selection for diagnostic deep-dive

We select two features for the mechanism plausibility checks, chosen to
illustrate contrasting triage outcomes:

- **12-1 Momentum**, the largest IC in the scan at the 21-day horizon. Follows the
  Jegadeesh-Titman convention of skipping the most recent month to separate momentum
  from short-term reversal. The question: does it hold up under the mechanism checks,
  or is the signal driven by a confound?
- **1-day Reversal**, whose IC at the same horizon is indistinguishable from zero and
  which also flips sign across VIX regimes. Its one significant cell, at the five-day
  horizon, is the one the shifted-label check above takes apart. We
  expect the mechanism checks to return STOP - and the useful part is *which* check
  catches it, since neither a timing placebo nor a shared-driver control was
  designed to detect how a feature and its label are constructed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## Mechanism Hypotheses

Before running diagnostics, we state the assumed causal mechanism for each
feature. This structures the interpretation of the checks.

### Feature A: 12-1 Momentum

The 12-1 momentum signal (return from [[ML4T_A3_0001]] to [[ML4T_A3_0002]]) is attributed to
behavioral underreaction: investors are slow to incorporate information, so past
risers keep rising. The alternative: momentum proxies a
risk-on/risk-off regime rather than encoding timely cross-sectional information.

[[ML4T_A3_0003]]

### Feature B: 1-day Reversal

Negated 1-day return. The hypothesized mechanism is microstructure-driven mean
reversion: temporary price dislocations reverse within days. At a 21-day
horizon, this mechanism should have no power - the effect decays too quickly.

[[ML4T_A3_0004]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0030-p000

~~~~~~markdown
### Why run these checks?

These checks cost minutes; building a full model pipeline costs chapters.
Their primary value is **catching dead features early** (reversal correctly
gets STOP) and **generating actionable diagnostics** (momentum's regime
concentration informs Ch12+ modeling choices).

**REVISE is the expected outcome, not failure.** In efficient markets cross-sectional
ICs are small - the magnitudes the scan above produced are typical - and HAC-adjusted
significance is conservative. Few single features will cleanly pass all three bivariate
checks. The diagnostic information - *where* and *when* a feature works -
matters more than the triage label.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0031-p000

~~~~~~markdown
## Baseline IC (HAC-Adjusted)

The grid-wide BH decision for these same two cells is carried alongside the raw
p-value. Reporting a raw p here without it is what let this section call a cell
"significant" that the scan's own correction had already rejected.

The lookup joins on the feature column rather than the display label: the scan and the
deep-dive spell the same feature differently, so a label join silently returns nothing
for one of the two features - exactly the kind of quiet miss this table exists to
prevent.

We report the HAC-adjusted IC for both features at the 21-day horizon. This
establishes the baseline that the diagnostic checks will probe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
12-1 momentum has the largest IC in the grid and the smaller raw p-value of the two
features here, and it **does not clear the grid-wide BH correction** - the column
recording that decision says so, and the scan said so about the same cell. The raw [[ML4T_A3_0001]] is a
post-selection number: this feature and this horizon were chosen by looking at the scan,
so every comparison that produced the choice has to be paid for, and BH is the bill.
Reversal IC is indistinguishable from zero on any reading.

The naive t-statistic for momentum is higher than the HAC one because it ignores
autocorrelation in the IC series. That correction and the multiplicity correction are
separate, and both apply: HAC widens the interval for one test, BH sets the threshold
that test has to clear given all the others.

The deep-dive continues on 12-1 momentum regardless, because the chapter needs a
worked example and this is the strongest candidate the scan produced. What it is
an example of is a **large effect at borderline significance** - which is the
ordinary situation in cross-sectional equity work, and a more useful thing to
demonstrate the diagnostics on than an unambiguous result would be.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
## Reusable Diagnostic Functions

We extract each falsification test into a reusable function so we can apply
the same checks to both features systematically.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
### Shared-Driver Check

The check below builds its IC series from a rolling rank correlation over a quarterly
window. Consecutive windows share all but one day of their data, so the effective sample
is much smaller than the number of windows. The HAC adjustment on the resulting series
accounts for part of that, and a borderline t-statistic should still be read with care.
Test whether a common exogenous factor (Treasury returns) or permutation
control explains the observed feature-outcome correlation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
The outcome of the shared-driver check is about the shared driver, and only the Treasury
arm speaks to it. The permutation control answers a different question - *is there any
signal at all?* - so it is reported beside the outcome and does not enter it. An earlier
version of this function said exactly that and then gated on the permutation anyway,
which marked a feature as carrying a shared-driver confound when its real problem was
having no signal to confound.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000

~~~~~~markdown
### Regime Heterogeneity
Partition by VIX regime and test whether signal effectiveness varies
across market states.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
## Run All Checks on Both Features

We apply each plausibility check to 12-1 momentum and 1-day reversal, collecting
results for the comparison scorecard. All t-statistics use Newey-West (HAC)
standard errors to account for serial dependence in overlapping IC series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
### Timing Placebo

For a rolling-window feature with lookback [[ML4T_A3_0001]], a [[ML4T_A3_0002]]-shifted version
shares roughly [[ML4T_A3_0003]] of its inputs with the original. This creates
a mechanical floor on IC persistence. We therefore treat the IC-lag profile as
a **diagnostic** (how does IC behave as information ages?) rather than applying
a hard decay threshold. More weight should be placed on lags beyond the lookback
window.

For 12-1 momentum (lookback ~231 trading days), we extend the lag grid to
252d so the furthest lag reaches beyond the lookback window entirely.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>
