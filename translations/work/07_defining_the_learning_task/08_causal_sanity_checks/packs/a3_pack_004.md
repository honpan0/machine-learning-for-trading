# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/08_causal_sanity_checks.ipynb；A3 Pack 004；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0045-p000

~~~~~~markdown
12-1 momentum IC is strongest at lag 0 and decays only gradually out to the longest lag
tested, as the figure shows. The persistence is partly mechanical: with a lookback of
roughly a year, a shifted feature shares most of its input data with the original.
The key diagnostic is that IC peaks at lag 0 - the most recent version of the
feature is the most informative - and even the fully stale version (lag 252d,
beyond the lookback) retains some residual predictability. Reversal IC is near
zero at all lags - there is no timely information to decay.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0046-p000

~~~~~~markdown
### Shared-Driver Check Results

We test whether each feature's cross-sectional mean predicts Treasury (IEF)
21-day forward returns. For 12-1 momentum, Treasury co-movement through
risk-on/risk-off dynamics is plausible, so a non-zero Treasury IC would flag
a shared-driver concern rather than strictly falsify the mechanism.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0048-p000

~~~~~~markdown
The reading for this row is the **Treasury** column, and only that column. Neither
feature's cross-sectional mean predicts Treasury forward returns, so neither shows the
shared-driver confound this check exists to detect.

The permutation column is reported beside it but does not decide the outcome, because it
answers a different question - *is there any signal here at all?* - and the timing check
already reports that. Gating the shared-driver reading on it would mark a feature as
having a confound when its actual problem is having nothing to confound.

Two things to read off the permutation column. First, the p-value is computed as
[[ML4T_A3_0001]] and printed beside the finest value [[ML4T_A3_0002]] permutations can resolve; a
permutation p-value is never exactly zero, because the observed assignment is
itself one of the arrangements under the null. Second, the null is **block**
permuted at the label horizon, so its spread reflects how persistent this data actually
is. An independent within-date shuffle would produce a far narrower null and would
reject nearly anything - [[ML4T_A3_0003]] measures that gap on its own panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0049-p000

~~~~~~markdown
### Regime Heterogeneity (VIX Regimes)

A sign flip is only flagged as STOP if the opposite-sign partition has
HAC [[ML4T_A3_0001]] **and** the unconditional IC is itself not significant. In
low-power subsamples, small ICs with the wrong sign may reflect noise rather
than genuine heterogeneity. This criterion is stated here as an a priori
design choice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0050-p000

~~~~~~markdown
The regime cutoffs below are terciles. The reading is qualitatively the same under a
median split or quartiles, because the diagnostic is sign stability rather than the
exact boundary.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0053-p000

~~~~~~markdown
The two panels fail the same check in opposite directions. Momentum's unconditional IC
is an average over regimes in which it behaves very differently, so the single number
understates it in calm markets and overstates it in turbulent ones. Reversal's
unconditional IC is near zero not because the feature does nothing but because its sign
flips across regimes and the halves cancel. In both cases the headline IC is an artifact
of mixing, and a model trained on the pooled sample is being asked to fit two different
relationships with one coefficient.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0054-p000

~~~~~~markdown
### Publication Figure Artifact

The book scorecard figure reads this compact artifact so formatting changes do
not rerun ETF/VIX preparation or permutation checks.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0056-p000

~~~~~~markdown
12-1 momentum keeps a positive IC in all three VIX regimes, but the magnitude varies by
several times between the calmest and the most turbulent, and only the calm-regime
estimate is significant - the figures are printed above. This is consistent with the
well-documented "momentum crash": momentum strategies suffer in high-volatility
environments (Daniel and Moskowitz 2016). The sign is stable across regimes, so this
earns CAUTION for magnitude variation rather than STOP.

Reversal shows a significant sign flip: its IC is negative in the low-VIX regime and
positive in the high-VIX one, both at t-statistics past two in their respective
directions, and the two halves cancel into a near-zero unconditional IC. That is a
textbook aggregation artifact - the feature encodes opposite information depending on
the volatility state - and earns STOP.

**Important**: this check cannot distinguish confounding from genuine effect
modification. A feature whose IC varies by regime may be confounded *or* may
have a mechanism that operates differently across states. Chapter 15 provides
multivariate sensitivity analysis to separate these cases.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0057-p000

~~~~~~markdown
## Collider Bias: A Synthetic Demonstration

We place this simulation here - after the three main checks - because its
purpose is different: it illustrates a DAG concept from Section 2 rather
than diagnosing a specific feature. Readers who want to reinforce the DAG
vocabulary before running the checks can read this section first.

The text defines **collider bias**: conditioning on a common *effect* of feature
and label creates a spurious association between them. This short simulation
makes the concept concrete.

**Setup**: Momentum ([[ML4T_A3_0001]]) and forward returns ([[ML4T_A3_0002]]) are independent. Fund flows
([[ML4T_A3_0003]]) are a function of both: [[ML4T_A3_0004]]. Because
[[ML4T_A3_0005]] is a collider, conditioning on it opens a path between [[ML4T_A3_0006]] and [[ML4T_A3_0007]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0059-p000

~~~~~~markdown
Conditioning on high fund flows (the collider) induces a negative correlation
between momentum and returns: among high-flow funds, strong momentum implies
weaker returns and vice versa. This is an artifact of the conditioning, not a
real effect. The practical lesson: never condition on a variable that is
*caused by* both the feature and the label.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0060-p000

~~~~~~markdown
## Plausibility Scorecard

Aggregate results into a dual-feature scorecard aligned with the
proceed / revise / stop framework from Section 7.3.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>
