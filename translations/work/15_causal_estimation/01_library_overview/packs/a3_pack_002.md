# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/01_library_overview.ipynb；A3 Pack 002；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Time series → 時間序列
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0013-p000

~~~~~~markdown
## 2. DoWhy (Microsoft/Amazon)

DoWhy asks for the causal graph up front, derives an estimand from it, and only then
estimates. Writing the graph down is the point: it makes the adjustment set a consequence
of stated assumptions rather than a choice, and it gives the refutation tests something to
perturb.

Use it when the assumptions have to be visible and testable, which is most of the time in
a research setting.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Estimand vs. estimator

The **estimand** is the quantity being targeted; the **estimator** is the procedure that
produces a number for it. Two libraries can report different numbers because they use
different estimators for the same estimand, or because they target different estimands
altogether, and only the first of those is a question about accuracy.

| Estimand | Description | Libraries |
|---|---|---|
| [[ML4T_A3_0001]] | Marginal effect of a continuous treatment | EconML, DoWhy |
| [[ML4T_A3_0002]] | Binary treatment effect, high group against low | CausalML |

If the estimand is not identified from the data at hand, no estimator recovers it. A
flexible model fitted to a confounded comparison returns a precise answer to the wrong
question.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
## 3. Other Libraries Referenced in the Chapter

**CausalML** (Uber) targets uplift with S-, T-, X- and R-learners, and its support is
strongest for the binary or discrete interventions typical of experiments and marketing.
Continuous treatments are possible but are not where the library is aimed. Chapter 15
works with continuous treatments and event studies, so CausalML appears in the selection
guide without a worked example; the
[CausalML documentation]([[ML4T_A3_0001]]) covers the uplift setting.

**tfp-causalimpact** fits a Bayesian structural time-series model and needs a pre-period
of the outcome series to build a counterfactual, which the cross-sectional sample here
does not provide. [[ML4T_A3_0002]] runs it on a Fed announcement.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
## 4. Library Comparison Summary

The table lists every library the chapter references and where each one is used.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
Tigramite and causal-learn learn a graph; EconML and DoWhy quantify an effect once a
graph or an adjustment set is settled. Discovery therefore comes before estimation rather
than replacing it, and its output is a set of hypotheses to test rather than a structure
to trust.

Two of the chapter's discovery methods are not library calls. NOTEARS, which learns a
contemporaneous graph by continuous optimization under a differentiable acyclicity
constraint, is implemented directly in [[ML4T_A3_0001]] following Zheng et al.
(2018); causal-learn does not ship it. Granger causality serves there as a predictive
baseline. causal-learn supplies the VAR-LiNGAM fit, which recovers lagged and
contemporaneous structure from non-Gaussian residuals.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
## 5. Selection Guide

Section 15.1 arranges the choice as a table, reproduced here. The first question is
whether the causal graph is known, because that decides whether the problem is estimation
or discovery.

| Graph known? | Treatment type | Method | Library |
|---|---|---|---|
| Yes | Binary or continuous | Backdoor adjustment | DoWhy |
| Yes | Continuous | DML | EconML |
| Yes | Binary, at a point in time | BSTS | tfp-causalimpact |
| Yes | Binary or discrete, uplift | Metalearners | CausalML |
| No | Not applicable | PCMCI | Tigramite |
| No | Not applicable | VAR-LiNGAM | causal-learn |
| No | Not applicable | NOTEARS | implemented in [[ML4T_A3_0001]] |

Reading the top half: DoWhy and EconML both need an adjustment set that identifies the
effect, and they differ in how it is supplied. DoWhy takes a graph and derives the
adjustment set from it; EconML takes the controls directly and fits them with machine
learning models. Neither escapes the identification assumption, so "no graph" is a reason to
run discovery first, not a reason to prefer one estimator over the other.

Reading the bottom half: the split is contemporaneous against lagged structure, not
cross-sectional against time series. PCMCI and VAR-LiNGAM both read time-lagged
dependence, and [[ML4T_A3_0002]] runs them on the same universe; NOTEARS
targets structure within a single cross-section.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
## 6. Effect Estimates, and What They Support

EconML and DoWhy target the same estimand here, so their estimates are comparable with
each other and with the known true ATE. Each is reported with a confidence interval, and
the last column records whether that interval covers the true value.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
Read the coverage column before the error column. The absolute error mixes sampling noise
with bias and a single estimate cannot separate the two, so a gap between the estimate and
the true ATE is not by itself evidence that the adjustment failed. The interval is what the
estimator says about its own precision: an estimate whose interval covers the true value is
consistent with it, however far the point estimate sits away. Non-coverage is not the
mirror image of that. An interval built to cover in nineteen samples out of twenty misses
in the twentieth even when the adjustment is exactly right, so a single miss establishes
nothing on its own. Whether these intervals are calibrated at all is a question about
repeated samples, and this notebook draws one.

Coverage on one sample is also the most these two rows can support. They are fitted to the
same 1,000 observations, so their errors move together, and a single draw ranks nothing.
CausalML would answer a different question on a binarized treatment, so its number is not
comparable and the table leaves it out.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>
