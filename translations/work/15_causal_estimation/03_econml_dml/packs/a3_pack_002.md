# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/03_econml_dml.ipynb；A3 Pack 002；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Machine learning → 機器學習
- Label → 標籤
- Training set → 訓練集
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0013-p000

~~~~~~markdown
## 3. Double Machine Learning Estimate under Observed-Confounder Adjustment

DML uses a three-step orthogonalization process:

1. **Predict outcome from confounders**: [[ML4T_A3_0001]] → residual [[ML4T_A3_0002]]
2. **Predict treatment from confounders**: [[ML4T_A3_0003]] → residual [[ML4T_A3_0004]]
3. **Regress residual outcome on residual treatment**: [[ML4T_A3_0005]]

The coefficient [[ML4T_A3_0006]] is an *orthogonalized* estimate of the treatment
effect under the maintained assumption that the specified controls capture
the relevant pre-treatment confounding variation. DML reduces sensitivity
to nuisance-model errors but does not, by itself, solve unobserved
confounding, simultaneity, interference, or bad-control bias.

The folds come from [[ML4T_A3_0007]] rather than [[ML4T_A3_0008]] or [[ML4T_A3_0009]], because
cross-fitting a forward-looking label needs two things neither of those provides. **Purging**
drops training rows whose 21-day label window overlaps the test window; the **embargo**
leaves a gap after the test window so autocorrelation does not carry back into the next
training set (Chernozhukov et al. 2017, de Prado 2018).
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
The confounders go into EconML's [[ML4T_A3_0001]] slot, which holds controls used for residualization.
The [[ML4T_A3_0002]] slot is for effect modifiers, the variables along which the treatment effect is
allowed to vary. Putting plain confounders in [[ML4T_A3_0003]] still produces a single ATE, so nothing
visibly breaks, but it teaches the wrong habit for [[ML4T_A3_0004]], where the two
slots carry different variables and the distinction decides what the model estimates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
**Interpretation**: The naive OLS estimate captures both the causal momentum effect and
spurious correlation induced by shared confounders (volatility, regime). DML's
orthogonalization removes this confounding by residualizing both treatment and outcome
against the confounders before estimating the final coefficient.

The direction of bias reveals the confounding structure. If the naive effect is
smaller in magnitude than the DML estimate, confounders *mask* the true effect -
for example, high volatility reduces both momentum and returns simultaneously.
If the naive effect is larger, confounders *inflate* the apparent predictive power.

**What it changes downstream**: a position size derived from the raw slope inherits
whatever the confounders contributed to it. The adjusted estimate is the one to size on
when volatility and regime are not separately hedged, and the gap between the two is how
much the raw slope was carrying.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0018-p000

~~~~~~markdown
## 4. The Same Estimate, Assembled by Hand

[[ML4T_A3_0001]] from [[ML4T_A3_0002]] runs the three steps in the
open: cross-fit the two nuisance models over walk-forward folds with an embargo, take the
residuals, regress one on the other. Handed [[ML4T_A3_0003]], it builds those folds over decision
times and reports a Driscoll-Kraay standard error; without them it would do both by row.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## 5. Refutation Tests

**Critical for causal validity**: We validate the DML estimate using refutation tests.

1. **Temporal Placebo**: Regress Y on *lead* of T (should be ~0 if no reverse causality)
2. **Block Permutation**: Shuffle treatment in blocks to preserve autocorrelation
3. **Subset Stability**: Check if effect is stable across temporal subsets
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
**Reading the temporal placebo.** A ratio near one is what this test returns here, and it
is not evidence of reverse causality. The treatment is a momentum signal that barely moves
over 21 trading days, so the horizon-shifted placebo is nearly the same variable as the
real treatment and reproduces a similar effect. For a treatment this persistent, the
shifted-signal placebo cannot refute anything.

The block permutation below is the refuter that can, because it breaks the alignment
between treatment and outcome while keeping the treatment's own persistence intact - but
only if the blocks are built along time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
### Blocks Along Time, Not Along Rows

[[ML4T_A3_0001]] given a bare array counts [[ML4T_A3_0002]] in the positions it is handed. On
this frame that is about a fifth of one day's cross-section, so a "block" is a handful of
ETFs on a single day. Permuting those destroys the serial dependence the test is supposed
to preserve, which is the iid shuffle [[ML4T_A3_0003]]'s own docstring warns makes placebo
tests too easy to pass.

Passing [[ML4T_A3_0004]] and [[ML4T_A3_0005]] makes it permute within each ETF, where [[ML4T_A3_0006]] counts
that ETF's own ordered trading days and a block is the three weeks the name promises.

Each placebo also runs the estimator being tested, with the same fold count and embargo. A
placebo fitted on three folds against an estimate fitted on five is a different estimator
on a different number of cross-fitted rows, and the null would then be centred wherever
that difference puts it rather than where the absence of an effect does. The observed
statistic itself moves between the two settings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
### Compared on t-Statistics, Not on Effect Sizes

Permuting the treatment also frees it from the controls. The second stage regresses the
residualized outcome on the residualized treatment, so whatever the controls explain leaves
the denominator; a permuted treatment is no longer explained by them, its residual variance
is larger, and a placebo effect is mechanically smaller than the observed one whether or not
there is anything to find. Comparing raw effects against that distribution reports
significance the standard error does not support. Each permutation's t-statistic divides by
its own standard error, so the scale cancels and only the alignment between treatment and
outcome is left.

The p-value is the fraction of the placebo distribution at least as extreme as the observed
statistic, and it carries a plus-one correction because the observed statistic is itself one
draw that distribution could produce. Without the correction, a run in which no placebo
reaches it reports zero, which no finite number of permutations can establish. With n draws
the smallest reportable value is 1 / (n + 1), printed beside it as the floor. It is not a
false discovery rate, which is what this quantity used to be called.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>
