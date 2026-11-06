# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/10_latent_factors.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Portfolio → 投資組合
- Volatility → 波動率
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Latent-Factor Requests

The latent-factor stage contains two declared configurations. [[ML4T_A3_0001]] fits principal components
within each training fold. [[ML4T_A3_0002]] estimates the neural stochastic
discount factor within the same fold contract. Neither notebook selects by IC.

This index exposes the complete request population without launching either computation. The two
execution notebooks publish disjoint official populations that [[ML4T_A3_0003]] later combines with
the other predictive families.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## What a latent factor is, and how this stage differs from the ones before it

Every model up to this point was handed named predictors. Carry, momentum, the volatility
estimate, the regime probability - each is a quantity somebody decided to compute, and the
model's job was to weigh them. The choice of what to compute came from the researcher, and a
driver nobody thought to name was a driver no model could use.

A latent factor is inferred instead of specified. The starting observation is that futures
returns move together far more than thirty independent series would: energy contracts rise and
fall as a group, the metals do, the equity indices do, and there are days on which nearly
everything moves the same way. That co-movement is evidence of a small number of underlying
drivers acting on many contracts at once. A latent-factor method estimates those drivers from
the covariance of returns themselves, without being told in advance what they are or how many
there should be.

The appeal is that it can find structure nobody encoded. The cost is that what it finds has no
name and no economic interpretation attached - a factor is a direction in return space that
explains variance, and whether it corresponds to anything a reader would recognise is a
separate question the method does not answer.

## Why two configurations, and what separates them

The two are not variations on one method. They disagree about what a factor is *for*, and
that disagreement is the reason both are here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0001-p001

~~~~~~markdown

**[[ML4T_A3_0001]] maximizes explained variance.** Principal components find the directions along
which returns vary most, in order, each uncorrelated with the ones before it. It is linear,
it has a closed-form solution, and it makes no reference to returns being predictable at all.
Its first component on a futures panel is typically close to "everything moves together"; the
next few usually separate the sectors. It is the standard baseline for exactly the reasons
equal weight is one in the backtest stage: it is well understood, it estimates little, and
anything more elaborate has to beat it to justify itself.

The weakness is that variance and return are different quantities. The direction along which
a panel varies most is not necessarily the direction that pays, and PCA has no mechanism for
preferring one that does - a factor capturing a large, entirely unrewarded common movement is
exactly what it is built to find first.

**[[ML4T_A3_0002]] starts from what prices assets.** Asset pricing theory says
that if markets are free of arbitrage there exists a single random variable - the stochastic
discount factor - whose covariance with any asset's return explains that asset's expected
return. Everything that is priced is priced by the same object. The SDF is not observable, but
it is a well-defined thing to estimate, and estimating it with a neural network means not
having to assume in advance which functional form it takes.

The difference from PCA is the objective and the inputs, not the architecture. PCA asks which
directions explain the most variation; the SDF asks which combination best explains the
cross-section of *returns*. A factor that moves a lot but earns nothing is a success for the
first and a failure for the second.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p001>>>
<<<ML4T-ZH-END:c0001-p001>>>

### c0001-p002

~~~~~~markdown

They also see different data, which is easy to miss and changes what each can find.
[[ML4T_A3_0001]] takes the characteristics panel and discards it with [[ML4T_A3_0002]], so PCA is handed
returns alone. [[ML4T_A3_0003]] passes the characteristics through, and the number of
instruments it builds is derived from their width. So the SDF can express "products with high
carry and low volatility load on this factor" and PCA structurally cannot, because PCA never
sees carry.

So the comparison between the two is not "which fits better". It is a question about this
panel: whether the directions along which futures returns vary most are also the directions
along which they are compensated. The two configurations are run under the same fold contract
and the same universe precisely so the comparison isolates that.

## Why the factors are fitted inside each fold, and why that matters more here

Both configurations estimate their factors within the training portion of each fold, never
once over the whole panel. That is the same discipline every other family follows, but the
consequence of breaking it is worse here and easier to miss.

A supervised model that saw future data would be caught by its own validation score looking
implausible. A latent-factor model fitted on the full sample fails more quietly: the factors
are estimated from the covariance of returns, so a factor fitted over 2011 to 2025 encodes
which contracts moved together across the entire period. Using it to form a position in 2014
means holding a portfolio constructed from the knowledge that those contracts would go on
co-moving. Nothing about the resulting prediction looks impossible. The returns are real, the
weights are finite, and the backtest runs - it just reports a strategy that could not have
been held.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p002>>>
<<<ML4T-ZH-END:c0001-p002>>>
