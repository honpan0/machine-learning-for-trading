# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/11_causal_dml.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Machine learning → 機器學習
- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外
- Cluster → 群集
- Cross-sectional → 橫斷面
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Double Machine Learning

This notebook estimates the configured treatment effect for each return horizon. The request
resolves the outcome, treatment, confounders, timing, embargo, nuisance models, and placebo design
before fitting. Missing confounders are an error rather than an invitation to change the estimand.

Nuisance models train on complete timestamp panels before the holdout. HAC uncertainty uses the
declared temporal ordering, and contiguous within-product blocks define the placebo refutation.
[[ML4T_A3_0001]] reports the causal diagnostics. Trading configuration selection uses
validation backtest Sharpe.

Nothing estimated here competes for that selection. A causal result is not a candidate
configuration: it produces no prediction set, is not eligible for a backtest, and never enters
the funnel. A reader looking for it on the leaderboard will not find it, and that absence is
the design rather than an omission - the two stages answer questions that do not compare.

One consequence for how the result is read: a small or insignificant effect here does not
invalidate the trading strategy, and a large one does not endorse it. The strategy stands or
falls on out-of-sample Sharpe either way. What the estimate changes is what the chapter may
claim about *why* it works.

Prerequisites: [[ML4T_A3_0002]], [[ML4T_A3_0003]], and [[ML4T_A3_0004]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## The question, and why this case study in particular has to ask it

The treatment here is [[ML4T_A3_0001]] - the term-structure spread between the front contract and
the next one. That is not an arbitrary choice of variable to interrogate. **Carry is the
signal this entire case study trades.** Every model in stages 06 through 10 is, in one form or
another, learning to predict returns from carry and things built out of carry.

So the question this notebook asks is whether the premise underneath all of that holds: does
carry itself move subsequent returns, or does carry merely travel alongside something else
that does? A predictive model does not care - it profits either way, as long as the
association persists. The chapter's explanation of *why* the strategy works cares a great
deal, because an explanation built on the wrong mechanism is wrong even when the strategy is
profitable.

This is also why the answer cannot come from the backtest. A backtest that earns a positive
Sharpe from carry demonstrates that carry predicted returns over that history. It says nothing
about whether carry was the cause, and no amount of out-of-sample performance converts one
into the other.

### What is being adjusted for, and why each one is a candidate explanation

Double machine learning estimates the effect of the treatment after flexibly removing what the
confounders explain of both the treatment and the outcome. It does this by predicting each
from the confounders alone, using models that need not be linear in anything, and then
estimating the effect from what is left over in each. The predictions are cross-fitted, so the
model that residualizes an observation was never fitted on it.

The three confounders are the three rival explanations worth taking seriously here:
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

- **[[ML4T_A3_0001]].** Contracts in backwardation are frequently contracts under supply stress, and
  stress raises volatility. If volatile contracts earn more simply for being volatile, carry
  would look rewarded without being the reason.
- **[[ML4T_A3_0002]].** Carry and momentum are correlated in futures - a contract in
  sustained backwardation has often been rising. An unadjusted carry effect could be a
  momentum effect wearing carry's label.
- **[[ML4T_A3_0003]].** This is the subtle one, and it is the reason the confounder list is not
  just "the other features". [[ML4T_A3_0004]] is a product's position in the cross-section, while
  [[ML4T_A3_0005]] is its level. Those come apart: a contract can have a high carry level in a
  period when every contract does, and rank in the middle of its peers. Adjusting for the rank
  asks whether the carry *level* carries information beyond where the product sits relative to
  the others - which is precisely what a cross-sectional strategy is already exploiting.

### Why the standard error is HAC

The uncertainty around the effect is computed with a heteroskedasticity- and
autocorrelation-consistent estimator, because the ordinary one assumes the residuals are
independent and identically scattered and neither holds on a futures panel. Volatility
clusters, so the scatter is larger in some periods than others; and overlapping outcomes tie
neighbouring residuals together, so they carry information about each other. Both inflate the
effective information in the sample relative to what an ordinary standard error assumes, and
the result is a confidence interval that is too narrow and a t-statistic that is too large.
The HAC estimator does not fix the estimate - it corrects what may be claimed about it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

### Why the label buffer sizes the placebo block here, and not the treatment

The refutation permutes the treatment in contiguous blocks and re-runs the whole estimation,
building a distribution of effects under the hypothesis that the treatment does nothing. The
block has to be long enough to preserve whatever serial dependence the data has, or the
placebo is a weaker opponent than the truth and every p-value looks significant.

Two separate scales create that dependence, and the block spans the longer of them:
[[ML4T_A3_0001]]. The overlapping labels span the label
horizon, and the treatment's own construction window spans itself.

[[ML4T_A3_0002]] is 1 for this case study, and the reason is a property of the
construction rather than a judgement. [[ML4T_A3_0003]] is
[[ML4T_A3_0004]], computed from two prices at the same timestamp.
Nothing rolls, nothing averages, no window is spanned. The label buffer is therefore the
binding scale here: the registered blocks are 5 periods for [[ML4T_A3_0005]] and 21 for
[[ML4T_A3_0006]], and each row records its own [[ML4T_A3_0007]] beside a [[ML4T_A3_0008]] of
[[ML4T_A3_0009]] saying which of the two set it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>
