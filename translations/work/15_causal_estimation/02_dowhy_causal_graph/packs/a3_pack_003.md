# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/02_dowhy_causal_graph.ipynb；A3 Pack 003；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0041-p000

~~~~~~markdown
## 7. Analysis B: Premium Reversion as Outcome

Now we test whether extreme high premium causes premium *reversion*. The
mechanism here is direct: high premium triggers arbitrage trades
(sell perp, buy spot) that mechanically push the premium back toward zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0046-p000

~~~~~~markdown
A larger robustness value does not make the reversion claim safe. Liquidity, funding
congestion, exchange credit risk and market-wide leverage can all move both the
extreme-premium state and the speed at which it decays, and none of them is in the
adjustment set. What the robustness value bounds is how weak such a confounder could be
and still overturn the estimate, which is a floor on the argument rather than a defence
of it. The reversion outcome is also mechanically close to the treatment, since both are
built from the same premium series, so part of the measured decay is ordinary mean
reversion after an extreme reading.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0047-p000

~~~~~~markdown
## 8. Side-by-Side Comparison
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
### How Fast Each Estimate Decays Under Omitted Confounding

Each curve traces what an omitted confounder of a given strength would leave of the
estimate, as a fraction of the estimate the notebook actually reports. Both start at one,
because a confounder of zero strength changes nothing, and each crosses zero at its own
robustness value. Plotting the fraction rather than the level is what puts the two
outcomes on one axis: the ATEs themselves differ by a factor of five and are measured in
different units.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
## 9. Additional Validation: Placebo Date and Negative Control

Section 15.3 describes two validation tests beyond the sensitivity analysis above. A
**placebo-date test** shifts the treatment assignment by several days, and a credible
effect should vanish once the treatment lands at the wrong time. A **negative-control
outcome** is a pre-treatment variable the treatment cannot cause, so any association the
adjustment leaves there is confounding or leakage rather than an effect.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0052-p000

~~~~~~markdown
### Placebo-Date Test

We shift the treatment ([[ML4T_A3_0001]]) forward by 21 bars
(7 days at 8h frequency). At each row, the treatment value now comes
from a week earlier -- well outside the 24h mechanism window. If the
original effect is causal, the placebo effect should be near zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
A credible causal effect shrinks toward zero under the placebo, because a treatment
measured a week early has no mechanism by which to reach the outcome. A placebo ATE that
stays close to the original says the association follows something persistent in the
series rather than the treatment arriving when it did. The ratio is the readable form,
since the two outcomes are on different scales.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
### Negative-Control Outcomes

Each headline outcome gets its own same-scale negative control:
[[ML4T_A3_0001]] (24h return ending 48h before treatment) for the
returns ATE, and [[ML4T_A3_0002]] (24h premium change ending
48h before treatment) for the reversion ATE.

Because the negative-control DAGs (correctly) omit any
[[ML4T_A3_0003]] edge, DoWhy's backdoor identification
refuses to attribute a causal effect - the *graph structure itself*
rules the path out, and [[ML4T_A3_0004]] returns zero by construction.
That is the right behavior for an identifiability check, but it gives
us no numeric diagnostic of *residual association* in the data.

To recover the diagnostic, we run an OLS regression of each past
outcome on the treatment and confounders, with HAC standard errors. If
the coefficient on treatment is non-trivial, the backdoor adjustment is
not blocking all confounding paths - even though no real causal effect
can exist on a pre-treatment outcome.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
Each residual association should be negligible relative to its
corresponding headline effect. A large ratio on one outcome but not the
other signals that the headline claim on the affected outcome inherits
residual confounding the backdoor adjustment did not block. Treat this
as a placebo diagnostic - not an identifiable causal effect - because
the DAG structurally forbids the path.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0058-p000

~~~~~~markdown
## 10. What Separates the Two Outcomes

The estimator, the adjustment set and the sample are identical across the two analyses.
What differs is how much of the market sits between the treatment and the outcome, and
that is what the diagnostics are picking up.

### Forward returns
[[ML4T_A3_0001]]
Speculative demand, leverage and risk appetite move both the funding premium and
subsequent returns, which is a backdoor path the adjustment set has to block.
[[ML4T_A3_0002]] and [[ML4T_A3_0003]] proxy for part of it and not for the rest, so the path
stays partly open. The residual association the negative control finds on a pre-treatment
return is the direct evidence of it.

### Premium reversion
[[ML4T_A3_0004]]
Funding makes the long side of the perpetual expensive while the premium is high, which
creates an incentive to sell the perpetual and buy spot, which compresses the premium.
The path is short enough that the same unmeasured sentiment has less room to act on the
outcome independently of the treatment. It is also short enough to be partly mechanical,
since the treatment and the outcome are built from the same premium series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0059-p000

~~~~~~markdown
## 11. Practical Implications

- **Choose the outcome before choosing the estimator.** The outcome decides which
  backdoor paths exist, and therefore whether the available controls can block them while
  leaving the treatment's own mechanism intact. A broad market outcome opens paths through
  everything the adjustment set omits, and no estimator repairs that.
- **Run the checks that fail for different reasons.** The placebo-date shift catches an
  effect that does not depend on timing, the negative control catches adjustment that
  leaves residual association, out-of-sample drift catches a fit to one period, and the
  robustness value says how weak an unseen confounder could be and still erase the
  estimate. Each is blind to what the others see.
- **Read out-of-sample drift on the estimate's own scale.** A large relative drift on a
  small estimate can sit well inside its standard error, so read the drift beside the HAC
  standard error rather than against a fixed cutoff.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0060-p000

~~~~~~markdown
## 12. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0062-p000

~~~~~~markdown
### Reading the four diagnostics together

No single diagnostic settles the comparison, and they are not independent of one another.
The cell below reports each of the four side by side, computed from the values above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0062-p000>>>
<<<ML4T-ZH-END:c0062-p000>>>
