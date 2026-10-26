# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/02_dowhy_causal_graph.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Training set → 訓練集
- Volatility → 波動率

## 待翻譯英文單元

### c0016-p000

~~~~~~markdown
## 3. Descriptive Statistics: Is There Anything to Explain?

Before any causal question, the association has to exist. An AR(1) regression of the
forward premium change on the premium z-score, fitted on the training set, measures it,
and the two reversion rates below count how often an extreme reading in either direction
is followed by a move back toward the mean within 24 hours.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
The association is there, and it is not subtle. Everything that follows is about whether
it reflects an effect of the premium state on what comes next, or the same forces showing
up in both, and about how far the answer depends on which outcome is asked about.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## 4. Causal Graph Specification

We specify a DAG encoding our domain knowledge. The treatment
[[ML4T_A3_0001]] is a directional indicator: premium z-score
above the threshold. Using a directional treatment avoids the
cancellation that arises from combining extreme high and low premiums.

[[ML4T_A3_0002]]

Both confounders (recent returns and volatility) affect the treatment
and the outcome, creating backdoor paths that the adjustment set must
block. The sensitivity analysis below quantifies how much *additional*
unobserved confounding would change our conclusions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
There is deliberately no DAG for the two negative-control outcomes. Both precede the
treatment, so a correct graph omits any edge from [[ML4T_A3_0001]] into them, and
DoWhy's backdoor identification then returns zero by construction: the graph rules the
path out and reports nothing about the data. Section 9 measures the residual association
directly instead, with an OLS regression on the same adjustment set, which is a placebo
diagnostic rather than an identifiable causal effect.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
### Identifying the Adjustment Set

DoWhy's [[ML4T_A3_0001]] applies the backdoor criterion to our DAG and
determines which variables must be conditioned on to block confounding paths.
The estimand below shows the identified adjustment set.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
The backdoor adjustment set consists of [[ML4T_A3_0001]] --
these are the observed confounders that lie on non-causal paths between
treatment and outcome. By conditioning on them, we block spurious
associations while leaving the causal path
[[ML4T_A3_0002]] [[ML4T_A3_0003]] [[ML4T_A3_0004]] open.
Both graphs share the same adjustment set because the confounding structure
is identical; only the outcome variable differs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
## 5. Causal Analysis Helper Functions

We split the analysis pipeline into three reusable stages:
estimation, refutation, and sensitivity analysis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0026-p000

~~~~~~markdown
### Fit and Estimate

Build a [[ML4T_A3_0001]], identify the estimand via the backdoor criterion,
and estimate the average treatment effect (ATE) using linear regression.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
### HAC Standard Errors

DoWhy's [[ML4T_A3_0001]] estimator reports iid standard errors. For
8-hour crypto series the residuals are autocorrelated by construction -
rolling-window confounders and overlapping forward outcomes both carry
persistence. We complement each DoWhy estimate with an OLS regression
that uses the same adjustment set and Newey-West HAC standard errors,
keeping the pedagogy of DoWhy while giving readers inference that matches
the data structure.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
### Refutation Tests

Two of DoWhy's refuters run on each estimate. The **placebo-treatment** refuter permutes
the treatment column, which destroys any real treatment-outcome link while leaving the
marginal distributions intact: an estimate that stays large under permutation is being
produced by something other than the treatment. The **random-common-cause** refuter adds
an independent draw to the adjustment set, which cannot confound anything: an estimate
that moves is unstable to the adjustment set itself.

Both are reported as ratios to the original estimate rather than as pass or fail, because
what counts as small depends on the estimate's own standard error, which the ratio does
not carry.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
### Sensitivity Analysis

Section 15.3 poses the sensitivity question as *how strong would an omitted confounder
have to be to overturn the result*. For a linear backdoor estimate that question has a
closed-form answer: the **robustness value** is the partial [[ML4T_A3_0001]] an unobserved confounder
would need with both the treatment and the outcome, after the observed controls, to drive
the estimate to zero (Cinelli and Hazlett, 2020). DoWhy computes it through
[[ML4T_A3_0002]].

The partial [[ML4T_A3_0003]] parameterization is what makes the two outcomes comparable. It is a
share of residual variance, so it does not inherit the scale of the outcome, and a
forward return measured in percent and a premium change measured in index points land on
the same axis. Passing the observed controls as [[ML4T_A3_0004]] additionally
expresses a hypothetical confounder as a multiple of the ones already in the model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
## 6. Analysis A: Returns as Outcome

We first test whether extreme high premium *causes* forward BTC returns.
The mechanism here is indirect: high premium reflects bullish sentiment,
which may also drive returns through other channels.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0037-p000

~~~~~~markdown
DoWhy's refuters draw from numpy's legacy global stream, so it is reseeded before each
refutation block. Without that, the second outcome's draws would depend on how many the
first one consumed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0040-p000

~~~~~~markdown
The robustness value answers a question the reader can weigh against what they know about
crypto markets: an omitted confounder explaining that share of the residual variance of
both the treatment and the outcome would move the estimate to zero.

It is a statement about the fit's algebra rather than about its sampling uncertainty. The
robustness value is a function of the partial [[ML4T_A3_0001]] of the treatment with the outcome,
which the OLS fit fixes through the identity [[ML4T_A3_0002]].
Replacing the iid standard error with a HAC one changes what the estimate claims about its
own precision; it changes neither the fitted coefficient nor the residual variances the
omitted-variable bias formula operates on, so it leaves the robustness value where it is.

That split is why DoWhy's robustness value *at a significance level* is omitted here.
That one asks how much confounding would make the estimate statistically indistinguishable
from zero, which is a question about standard errors, and the OLS+HAC regression above
shows the iid standard error is not the right one for overlapping 24-hour outcomes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>
