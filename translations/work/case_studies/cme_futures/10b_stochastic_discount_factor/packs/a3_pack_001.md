# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/10b_stochastic_discount_factor.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Risk premium → 風險溢酬
- Momentum → 動能
- Feature → 特徵
- Overfitting → 過度擬合
- Volatility → 波動率
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Stochastic Discount-Factor Features

The stochastic discount-factor model learns fold-scoped latent factors from the product panel and
maps them to each declared forward-return horizon. Training rows determine the representation;
validation rows are transformed without refitting. The fitted model, fold identity, prediction
shard, and eligible validation keys are persisted together.

The notebook executes the declared SDF configurations and publishes their catalog rows. IC remains
diagnostic. The equal-weight validation backtest in [[ML4T_A3_0001]] selects configurations.

One framing to carry through the rest: this is the most theoretically motivated model in the
case study and it is given no special standing because of that. Its rows enter the same funnel
as the linear model's, are selected on the same statistic, and can lose to a gradient-boosting
configuration that rests on no asset-pricing argument at all. A better story about why a model
should work is not evidence that it does.

Prerequisites: [[ML4T_A3_0002]], [[ML4T_A3_0003]], and [[ML4T_A3_0004]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What a stochastic discount factor is

Asset pricing has one central result worth stating plainly, because everything this notebook
does follows from it. If prices admit no arbitrage, then there exists a single random variable
- call it [[ML4T_A3_0001]] - such that for every asset, the expected product of [[ML4T_A3_0002]] and that asset's return
is the same constant. One object prices everything: equities, bonds, corn futures, all of it.
That object is the **stochastic discount factor**.

Its usefulness is that it converts "which assets earn more, and why" into a question about one
quantity. An asset earns a premium when its return covaries negatively with [[ML4T_A3_0003]] - when it pays
badly in the states [[ML4T_A3_0004]] says are expensive, which are the states investors care most about
being protected in. Under that view a risk premium is not compensation for variance; it is
compensation for failing to pay off when payment matters.

[[ML4T_A3_0005]] is not observable. But it is a well-defined thing to estimate, and estimating it with a
neural network means not having to assume in advance what functional form it takes - which
matters, because the classical models that assume one (a market factor, a small set of
characteristics entering linearly) have a long record of being rejected on the data.

## How this differs from [[ML4T_A3_0006]], on two axes rather than one

The index for this stage frames the two configurations as differing in objective. That is true
and it is not the whole difference - they also see different data, which is worth being exact
about because it changes what each is capable of finding.

**PCA sees returns only.** [[ML4T_A3_0007]] takes the characteristics panel and discards it with
[[ML4T_A3_0008]] before fitting; it is handed a matrix of product returns and nothing else.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

**The SDF sees returns and characteristics.** [[ML4T_A3_0001]] passes [[ML4T_A3_0002]] through to
[[ML4T_A3_0003]], and the number of instruments it
builds is derived from the characteristics' width. So carry, momentum and volatility are
inputs here in a way they are not in [[ML4T_A3_0004]].

The two differences compound. PCA asks which directions explain the most variation in returns,
using returns alone. The SDF asks which combination of assets, weighted by their observable
characteristics, best explains the cross-section of returns - so it can express "products with
high carry and low volatility load on this factor" in a way PCA structurally cannot, because
PCA never sees carry.

That is why the comparison between them is informative rather than decorative. A win for the
SDF is evidence that the characteristics carry pricing information beyond what the return
covariance already encodes. A win for PCA is evidence that they do not, and that the extra
freedom bought overfitting.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0004-p000

~~~~~~markdown
## Declared requests

Both return horizons use the named stochastic discount-factor configuration. The resolved plan
shows the eligible rows, folds, feature count, checkpoint schedule, and identity before fitting.

**This model publishes on [[ML4T_A3_0001]], declared in [[ML4T_A3_0002]] rather than detected.** The device
enters both [[ML4T_A3_0003]] and [[ML4T_A3_0004]] inside the hashed computation, so leaving it to
[[ML4T_A3_0005]] would resolve one training identity on a GPU host and a different one
on a CPU host, both publishing under this population's name. [[ML4T_A3_0006]] overrides the same
declaration to [[ML4T_A3_0007]], because PCA has no GPU implementation to record.

**Nothing here fails on a fit that did not converge.** The shared runner enforces convergence for
IPCA only, and this case study does not declare IPCA; for the stochastic discount factor it
records the training history and the terminal Sharpe as fold extras and checks neither. That is a
gap in shared code rather than in this notebook, so what is claimed below is that every declared
checkpoint was produced and registered - not that the objective had settled when it was.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>
