# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/04_dml_crypto_regime.ipynb；A3 Pack 002；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Volatility → 波動率
- Covariance → 共變異數

## 待翻譯英文單元

### c0020-p000

~~~~~~markdown
### A Subgroup Is Episodes, So Its Standard Error Needs the Whole Grid

The two fits below re-fit everything inside a regime, nuisance models included, which is a
different estimator from the full-sample one rather than the same estimator on fewer rows.
That is what makes them worth having, and it is also what breaks their time grid.

A regime is a set of **episodes**, not an interval: the market moves in and out of high
volatility repeatedly, and the cell below prints how many episodes each regime has and how
long they run. Handed only its own timestamps, the covariance estimator numbers them
consecutively, so the last bar of one episode and the first bar of the next become
neighbours however much calendar time separates them. A bandwidth of [[ML4T_A3_0001]] bars then
counts *retained* bars and can reach across weeks that the regime was not active for.

So the cross-fitting happens inside the regime and the standard error is taken on the full
grid. The residualized outcome and treatment go back to their own bars and every other bar
carries a zero. A zero contributes nothing to that bar's aggregated score, which is what an
inactive bar contributes, and it leaves the slope untouched - a zero row moves neither
[[ML4T_A3_0002]] nor [[ML4T_A3_0003]] - so what changes is only the thing that was wrong. Each fit prints what
the filtered grid would have reported beside what the full grid does.

The regime **difference** still comes from the interaction model further down, which is
fitted on the full sample in one regression and needs none of this.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0023-p000

~~~~~~markdown
The difference above adds the two subgroup variances as if the estimates were independent
draws. Disjoint subsets are not independent estimates: both come from the same market and
the residuals they are built from share the nuisance models that produced them.

The interaction model is the better answer. It fits one regression on the residualized
full sample with the treatment, the regime and their product, so the coefficient on the
product is the regime difference and its standard error comes from the joint fit. The
regime main effect is in the design so the interaction is identified against
regime-specific intercepts rather than absorbing a level shift between regimes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## 8. EconML Comparison

[[ML4T_A3_0001]] cross-fits on whatever folds it is handed. [[ML4T_A3_0002]] counts its
[[ML4T_A3_0003]] and embargo in the positions it receives, so fed the panel's rows it would
purge a fraction of one bar and let a fold boundary cut through a cross-section. The folds
below are built over the ordered bars and expanded back to rows by membership, which is
what [[ML4T_A3_0004]] does internally once it is given [[ML4T_A3_0005]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## 9. Refutation Tests

**Block permutation** breaks the alignment between treatment and outcome while leaving the
treatment's own persistence intact. A plain random shuffle removes the persistence too,
which makes the placebo distribution too narrow and the effect too easy to distinguish
from it.

The blocks are permuted **within symbol**, along that symbol's own ordered bars. Passed a
bare array, [[ML4T_A3_0001]] would count [[ML4T_A3_0002]] in panel rows, and nineteen
consecutive rows here are one 8-hour bar - so a 21-row "seven-day block" would be a
handful of perpetuals in a single bar, which is the random shuffle the test exists to
avoid. With [[ML4T_A3_0003]] and [[ML4T_A3_0004]] the sweep below spans one, seven and fourteen days of a
symbol's own history, which is what makes the comparison across block lengths mean
anything.

The treatment is a 14-day premium z-score and several controls use multi-day windows, so
the fourteen-day block is the one that covers the treatment's whole input window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0027-p001

~~~~~~markdown

**The comparison is made on t-statistics, not on effect sizes.** The controls explain most
of this treatment's variance - section 5 prints the share left over - and a
permuted treatment is no longer explained by them at all. Its residual is therefore far
larger, and since that residual is the second stage's denominator, a placebo effect is
mechanically smaller than the observed one whether or not there is anything to find. A
placebo distribution of raw effects is narrow for that reason alone, and reading the
observed effect against it would report significance that the standard error does not
support. Each permutation's t-statistic divides by its own standard error, so the scale
cancels and what is left is the question the refutation is for: is the alignment between
treatment and outcome stronger than the alignment a shuffle produces?

Each placebo also runs the estimator being tested, with the same fold count and embargo. A
placebo fitted on fewer folds is a different estimator on a different number of cross-fitted
rows, and the null would then be centred wherever that difference puts it rather than where
the absence of an effect does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p001>>>
<<<ML4T-ZH-END:c0027-p001>>>

### c0027-p002

~~~~~~markdown

**What cancelling the scale does not buy.** It removes one known bias and does not make the
test calibrated. A permutation test is valid when the permuted labels are exchangeable under
the null; a treatment that persistent confounders predict is not, because the shuffle breaks
the confounding along with the effect. An estimate that is itself biased then sits far from
its own permutation null and the test reports that distance. Measured on twelve synthetic
panels with a true effect of exactly zero, the studentized comparison still rejects at the
conventional five percent level on five of the twelve. The sweep
below compares block lengths against a shuffle; it does not certify a significance level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p002>>>
<<<ML4T-ZH-END:c0027-p002>>>

### c0029-p000

~~~~~~markdown
## 10. Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0033-p000

~~~~~~markdown
No ratio of the two regime estimates appears here. Both are small relative to their own
standard errors, so a quotient of them divides two numbers whose signs the data does not
pin down, and it moves for reasons that carry no information. The interaction answers the
same question and arrives with a standard error.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>
