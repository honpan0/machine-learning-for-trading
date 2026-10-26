# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/13_model_analysis.ipynb；A3 Pack 004；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Market regime → 市場狀態
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Covariance → 共變異數

## 待翻譯英文單元

### c0054-p000

~~~~~~markdown
## 6. Heterogeneity: Labels, Horizons, and Regimes

This section answers two questions: does the signal strengthen or
weaken at shorter horizons? And does model ranking depend on the
market regime? Both matter for strategy design.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
### The same families at a shorter horizon

Two label horizons are declared: [[ML4T_A3_0001]] at the monthly rebalancing cadence and
[[ML4T_A3_0002]] at the weekly one. The panels below put each family's highest-IC configuration for
each horizon side by side with its HAC interval, and a tile marked "no run" is a family that was
never fitted at that horizon rather than one that was fitted and produced nothing.

Two questions come out of the comparison: whether the cross-sectional signal is stronger at one
horizon than the other, and whether the ordering among families is the same at both. A family
that leads at one horizon and not at the other is a family whose advantage is about the horizon
rather than about the model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0058-p000

~~~~~~markdown
**Coverage is the first thing the panel above says, before any comparison.** A family with no
tile at a horizon was never fitted there, which is a fact about what was run rather than a result
about the horizon - and reading an absence as a weak result is the mistake this layout exists to
prevent.

Where a family spans both horizons, the comparison is worth making carefully, because the two
panels do not have the same amount of evidence behind them. A five-day label produces more
scoreable validation dates than a twenty-one-day one over the same window, so its intervals are
tighter for reasons that have nothing to do with signal. A family that looks more credible at the
shorter horizon may simply have been measured more times there, and the point estimates are what
to compare on strength while the intervals are what to compare on confidence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0059-p000

~~~~~~markdown
### Regime Conditioning

Models do not have one universal performance level. The ETF cross-section
is driven by macro regimes: risk-on/risk-off rotations, volatility spikes,
and trend reversals can all shift which model family extracts signal. We
condition performance on a volatility regime derived from cross-sectional
return dispersion, which is a usable proxy for macro uncertainty.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0061-p000

~~~~~~markdown
### Figure 8: Conditional Performance by Volatility Regime
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0063-p000

~~~~~~markdown
Regime sensitivity is critical for ETF rotation strategies because the
universe itself is a macro instrument. During high-volatility periods
(risk-off), the cross-section separates more sharply, with bonds rallying
while commodities and emerging markets sell off, creating larger
cross-sectional spreads for models to exploit. During low-volatility
periods (risk-on), ETF returns converge, and cross-sectional
dispersion shrinks, making ranking harder.

If one model family achieves the highest IC in high-vol but fails in
low-vol, a regime-conditional strategy that switches models (or adjusts
position sizing) based on realized volatility may produce a higher
net IC than a static choice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0064-p000

~~~~~~markdown
## 7. Structural and Causal Evidence

Not all model chapters produce comparable predictive scores. Ch14
(latent factors) extracts structure; Ch15 (causal DML) estimates
treatment effects. These require separate evidence blocks.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0065-p000

~~~~~~markdown
### Latent Factors (Ch14)

ETFs is one of the five case studies in scope for the latent-factor
pipeline. Five estimators were fitted on this cross-section: principal components, instrumented
PCA, the conditional autoencoder, the stochastic discount factor and the supervised
autoencoder. [[[ML4T_A3_0001]]](11_latent_factors.ipynb) sets out what separates them. The
diagnostics below read each one's persisted fold extras to look inside the fit rather than at
its score.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0066-p000

~~~~~~markdown
The per-fold diagnostics are stored under the **training hash** of the run that produced them -
[[ML4T_A3_0001]] - so the configuration name from the metrics
table has to be resolved to that hash first. Passing the name straight through returns [[ML4T_A3_0002]] for
every estimator, and because the loader answers [[ML4T_A3_0003]] for "no file" rather than raising, the
figures below silently render nothing while the prose beside them describes what they show. The
estimators that wrote no extras are named rather than left out, so an empty panel is
distinguishable from a panel that was never asked for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0068-p000

~~~~~~markdown
#### How concentrated is the return panel's variance?

PCA's loadings come from the covariance of the training returns, so how much of that covariance
the leading components carry decides how much structure there is to load on. A steep drop after
one or two components means the panel is dominated by a few common movements; a flat profile
means the variance is spread thinly and a low-rank model has little to work with.

Both panels average over the folds, because each fold refits the decomposition on its own
training window and a single fold's profile is one draw of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0070-p000

~~~~~~markdown
**What the decomposition does and does not settle.** A concentrated variance profile says the
funds move together, which is what makes a factor model the right shape for this panel. It says
nothing about whether those factors carry a **premium** - whether loading on them is rewarded.
That is a separate question, and it is the one the latent-factor IC table above answers.

The estimators in that table differ in exactly one thing: how much the fit is allowed to know
about returns. PCA reads the return panel alone; IPCA lets the features set the exposures; the
conditional autoencoder does the same with a network in place of a linear map; the stochastic
discount factor and the supervised autoencoder each drop the two-stage split, one by pricing the
cross-section directly and one by predicting the return directly. Where the ordering in the table
sorts them by that axis rather than by model complexity, the panel is telling you that what
helps is supervision, not capacity. [[[ML4T_A3_0001]]](11_latent_factors.ipynb) sets out the
family, and each member's own notebook reports its fit.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0071-p000

~~~~~~markdown
#### Did the autoencoders converge, and did they converge to the same place?

One line per fold, per model. What matters is not the level - the loss scales with the fold's own
training window - but the shape: a curve that descends and flattens has converged, and a set of
curves that flatten at similar rates is a model finding reproducible structure. Curves that
diverge from each other say the representation is a property of the fold rather than of the
panel, which is a reason to distrust it downstream whatever its IC.
~~~~~~

<<<ML4T-ZH-BEGIN:c0071-p000>>>
<<<ML4T-ZH-END:c0071-p000>>>
