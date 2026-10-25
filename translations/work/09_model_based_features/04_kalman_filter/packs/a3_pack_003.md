# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/04_kalman_filter.ipynb；A3 Pack 003；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0031-p000

~~~~~~markdown
## A hedge ratio that is allowed to move

A pairs trade holds one asset against a multiple of another, and that multiple is the
**hedge ratio**. Estimating it by regression over a fixed window forces a choice nobody
can make well: a short window is noisy and a long one is slow, and the ratio is not
constant either way.

The same filter estimates it with a different reading of the same equations. The state is
the pair of regression coefficients, the transition says they follow a random walk, and
the observation row carries the explanatory asset's price, so the model is
[[ML4T_A3_0001]] with both coefficients free to drift.

Two settings control it. [[ML4T_A3_0002]] sets how much the coefficients may move per session,
through [[ML4T_A3_0003]]: at the value used here the
coefficients move very little per session and a great deal over a year. [[ML4T_A3_0004]]
is the variance of the pricing error, in squared dollars, and it is set from the residual
a fixed regression leaves rather than assumed. That regression is fitted on a burn-in
period at the start, and the section reports nothing inside it, because a variance read
off the whole pair would put later prices into the gain that produced every earlier
hedge ratio.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0034-p000

~~~~~~markdown
The spread is what is left after the hedge: the price of one asset minus the estimated
multiple of the other. Its band is drawn from an **expanding** standard deviation, so the
band on any session is computed from that session and the ones before it, and a spread
marked as extreme was extreme against the history available at the time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
The two estimates disagree in a way worth naming. The rolling regression jumps whenever a
large observation enters or leaves its window, so it moves for reasons that have nothing
to do with the pair; the filter has no window to leave and moves only when the innovation
says the old ratio is not explaining the new prices. What the filter does not give is a
free lunch on the setting: [[ML4T_A3_0001]] plays the role the window length played, and the
estimate is as responsive as that setting makes it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0037-p000

~~~~~~markdown
## The features this notebook produces

| Column | What it is | What it is read for |
|---|---|---|
| [[ML4T_A3_0001]] | the filtered level of the price | a smoothed price whose smoothing follows the data |
| [[ML4T_A3_0002]] | the filtered rate of change | a trend estimate with no window length |
| [[ML4T_A3_0003]] | the part of each close the prediction missed | how surprising a session was |
| [[ML4T_A3_0004]] | the variance of the level estimate | how much to trust the other three |
| [[ML4T_A3_0005]] | the filtered hedge ratio between two assets | what to hold against what, and its spread |

Every one is **filtered** rather than smoothed: the value at a session uses observations
up to that session and no later. A smoother, which revises earlier states using later
observations, produces better estimates of the past and cannot be used as a feature at
all.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0038-p000

~~~~~~markdown
## Key takeaways

1. **The settings are the model, and their ratio is the behaviour.** How much the state
   may move against how noisily it is observed decides everything the filter does; a
   window length is what a fixed-weight method has instead.
2. **Fitting the settings by maximum likelihood is what makes them an estimate**, and
   fitting them forward on a moving window is what stops the estimate from reading its own
   future. On this sample the fit reverses the hand-set assumption entirely.
3. **A slope with no window still has a horizon**, and it is set by the fitted settings.
   Comparing it against a fixed-window slope compares two horizons unless the horizons are
   fixed first.
4. **Filtered, never smoothed.** Every quantity here uses observations up to its own
   session. The smoothed version of each is a better estimate and is not a feature.
5. **A time-varying hedge ratio moves when the pair moves**, where a rolling regression
   also moves when an old observation leaves the window.

**Known limitations.** The local linear trend model assumes normal noise with constant
variance inside each refit window, and the innovation panel shows the variance is not
constant; a filter with time-varying observation noise, which is what the volatility
models later in the chapter estimate, is the natural repair. The information coefficients
here are single numbers over one symbol and one horizon and carry no confidence interval.
And the uncertainty feature converges to a constant under fixed settings, so it carries
information only across refits.

**Next**: [[ML4T_A3_0001]] for describing a series by its frequencies, and
[[ML4T_A3_0002]] for features of the path rather than of the level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>
