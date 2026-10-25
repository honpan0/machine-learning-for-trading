# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/08_garch_volatility.ipynb；A3 Pack 003；單元 3 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Clustering → 分群
- Volatility → 波動率

## 待翻譯英文單元

### c0031-p000

~~~~~~markdown
## The features this notebook produces

| Column | What it is | Where the timing guarantee holds |
|---|---|---|
| filtered conditional volatility | the recursion run forward under parameters fitted on the training block | on the held-out block only |
| standardized residual | the return divided by that session's estimate | wherever the estimate dividing it does |
| volatility percentile rank | where the current estimate sits in a trailing window | throughout |
| volatility of volatility | how unstable the estimate itself has been | throughout |
| persistence | a fitted parameter, one per symbol, not a per-session column | on a block after the one it was fitted on |

The right-hand column is the one to read, because "causal" is a property of a value's
position rather than of the construction that produced it. The filtered series carries the
guarantee only where its parameters preceded it, which is the block after the training
split; inside the training block the same values were produced by parameters estimated
partly from them. The standardized residuals plotted earlier come from the whole-sample
fit and are a diagnostic rather than a feature, and the panel's persistence is estimated
over each symbol's entire history and is descriptive for the same reason. The cell below
marks the part of the filtered series that carries the guarantee.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## Key takeaways

1. **Volatility is the part of a return series that is predictable**, and a GARCH fit is
   the standard way to turn that into one number per session. The mean is not, which is
   the previous notebook's finding.
2. **The two parameters are the model.** How much a new move moves the estimate, and how
   much of the old estimate carries into the next one. Their sum decides how long a shock
   takes to decay, and it sits just below one for essentially every liquid asset.
3. **Check the standardized residuals, and expect two different answers.** The clustering
   goes away, which says the variance model worked; the tails do not, which says the
   innovation distribution is wrong and is a separate repair.
4. **A risk number is a claim that can be counted.** Applying the value-at-risk rule at
   every session and counting the exceedances is the check, and under a normal assumption
   on fat-tailed data it comes out short.
5. **A feature has to be filtered, not fitted in place.** Estimating parameters on a
   training block and running the recursion forward gives a column no later return
   touched, and on this data it agrees closely with the in-sample version anyway.

**Known limitations.** Every fit here uses a normal innovation distribution, which the
residual diagnostics reject; a Student-t fit would change the value-at-risk numbers and
little else. The exceedance counts are in-sample for the whole-sample fit. The panel's
symbols overlap heavily, so its distribution of persistence is not a hundred independent
draws. And nothing here forecasts more than one session ahead, where the mean-reversion
of the variance towards its long-run level starts to dominate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0033-p001

~~~~~~markdown

**Previous**: [[ML4T_A3_0001]], which modelled the mean.
**Next**: [[ML4T_A3_0002]] for volatility models built on longer memory than a
single decay rate can express.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p001>>>
<<<ML4T-ZH-END:c0033-p001>>>
