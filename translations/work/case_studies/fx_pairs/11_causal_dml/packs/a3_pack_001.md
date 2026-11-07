# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/11_causal_dml.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Machine learning → 機器學習
- Out-of-sample → 樣本外
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Causal DML - FX Momentum

Double machine learning estimates the effect associated with a specified momentum treatment after
flexible adjustment for the configured volatility and price-state variables. It is a causal
estimand, not a predictive model configuration, so its result remains separate from prediction
catalogs and backtest selection.

The shared request verifies that the treatment and every confounder exist, excludes outcomes whose
horizon reaches the holdout, keeps complete timestamp panels when applying a sample cap, cross-fits
nuisance models with an embargo, and records the block-placebo design in the causal identity.

**Learning objectives**

- Inspect the treatment, confounders, timing, and refutation design before estimation.
- Run the same causal request used by direct Python callers.
- Keep causal evidence separate from predictive-family comparison and selection.

**Book reference**: Chapter 15, Section 15.4

**Prerequisites**: [[ML4T_A3_0001]], [[ML4T_A3_0002]], and [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## The question this asks, and why it is not the question the rest of the case study asks

Every other modelling notebook here asks a predictive question: given what is observable now,
what is the best guess at next period's return? A model that answers it well is useful even if
every variable in it is a proxy for something else, because prediction does not require knowing
why a relationship holds - only that it keeps holding.

This notebook asks a different question. It asks what would happen to the outcome **if the
treatment were different and nothing else changed**. That is a claim about intervention rather
than association, and it is not answered by a better fit. A model can predict returns from
momentum superbly because both are driven by a third thing, and be completely wrong about what
changing momentum would do.

The distinction matters for what may be done with the answer. A predictive result earns its
place by out-of-sample performance and is selected against other configurations on validation
Sharpe. A causal estimate is not a candidate for that comparison at all - it does not compete
with the gradient boosting configurations, it is not eligible for a backtest, and it never
enters the selection funnel. It answers a question about the market's structure that the
chapter's narrative rests on, and the value of getting it right is that the narrative is true.

### What double machine learning does about confounding

The obstacle is that momentum is not assigned at random. Periods of strong momentum differ
systematically from periods of weak momentum in volatility, in trend state, in liquidity - and
those differences also move returns. Regressing the outcome on the treatment attributes all of
that to the treatment.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

The classical fix is to include the confounders as controls, which works only if their
relationship to the outcome is the shape the model assumes. Double machine learning removes that
requirement in two steps. First it predicts the outcome from the confounders alone, and the
treatment from the confounders alone, using flexible models that need not be linear in anything.
Then it estimates the effect from what is left over in each - the parts of the outcome and the
treatment that the confounders could not explain. Whatever the confounders drive has been taken
out of both sides before the effect is estimated.

The nuisance predictions are **cross-fitted**: the model that residualizes an observation is
never fitted on that observation. Without that, a flexible model overfits its own training rows,
the residuals are too small there, and the effect estimate inherits a bias that grows with how
flexible the nuisance models were. The embargo extends the same idea across time, because a
financial panel's neighbouring rows are not independent the way a cross-section's are.

### What the refutation is for

A causal estimate cannot be validated the way a prediction can, because the counterfactual is
never observed - there is no held-out truth to score against. What can be done is to run the
same estimator against data where the answer is known in advance to be nothing, and check that
nothing is what comes back.

That is the block placebo. The treatment is shuffled so that any genuine relationship to the
outcome is destroyed, the whole estimation is re-run, and the effect it reports is recorded. Do
that many times and the result is a distribution of effects under the null hypothesis that the
treatment does nothing, which is what the reported p-value is computed against.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

The shuffling is done in **blocks** rather than row by row, and the block size is part of the
causal identity for a reason worth stating: a row-by-row shuffle would destroy the series'
autocorrelation along with its relationship to the outcome, and an estimator tested against
implausibly clean data will pass a test that means nothing. The blocks are sized to preserve the
dependence that makes the real series hard, so the placebo is a fair opponent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>

### c0004-p000

~~~~~~markdown
## Resolve the estimand and analysis population

Nonzero fold, sample, symbol, or placebo limits declare a preview. They are recorded in identity
and excluded from canonical evidence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>
