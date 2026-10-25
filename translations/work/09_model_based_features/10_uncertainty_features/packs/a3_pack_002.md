# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/10_uncertainty_features.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0018-p000

~~~~~~markdown
Read the last column before using either parameter as a feature. A ratio that is a
meaningful fraction of one says the sampler alone could move the column by an amount
comparable to what it moves between quarters, which is enough to make the
quarter-to-quarter path unreliable at that resolution. It does not say what share of the
path is sampling error; establishing that means rerunning the fits with more draws and
watching whether the spread stays where it was. The draws needed scale with the square of
how much further the error has to fall.

This is a property of the model rather than of the data, and it is worth knowing which
models have it. A likelihood with a narrow curved region takes many draws to explore
whichever way it is sampled, and the standard responses are a non-centered
parameterization of the latent path, far longer chains, or a sampler built for
state-space models rather than a general-purpose one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
The bottom panel is the argument of the section above, drawn. The level steps once a
quarter and holds, so within a quarter it says nothing about which sessions were volatile.
What does carry information at that cadence is the width of the interval relative to the
level, and how the parameters move between fits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## The parameter posteriors

The four histograms are the model's statement about how well each parameter is pinned
down. A narrow posterior is a parameter the data determined; a wide one spanning most of
its prior is a parameter the data had little to say about, and reading its mean as an
estimate would be reading the prior back.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
The degrees-of-freedom posterior is the one to read carefully. It is bounded below by two
and unbounded above, and a large value means the Student-t has become a normal. A broad
right tail therefore says the data does not rule out a normal rather than that the tails
are thick, and the parameter's mean is a poor summary of a distribution shaped like that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
## Forecast intervals as a feature

The second source of uncertainty in this notebook is cheaper and different in kind. An
ARIMA forecast comes with a prediction interval, and that interval widens when the model
fits the recent past badly. It is available at every session at negligible cost, which is
the opposite trade from the sampler above.

The model is fitted to the **logarithm** of volatility, for two reasons. A forecast on
the log scale exponentiates to something positive, which a volatility has to be. And the
residuals of a log-volatility model are much closer to normal than those of a
volatility model, which is what the interval's construction assumes.

The back-transform is exact rather than approximate, and it is worth being precise about
what it gives. If the forecast on the log scale is normal with mean [[ML4T_A3_0001]] and standard
deviation [[ML4T_A3_0002]], then on the original scale [[ML4T_A3_0003]] is the **median** and
[[ML4T_A3_0004]] is the mean, and exponentiating the endpoints of the interval on the
log scale gives an interval on the original scale with exactly the stated coverage. The interval is asymmetric around the median, wider
above than below, which is right for a quantity with a floor at zero and no ceiling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
The three tests do not agree, which is the useful outcome here rather than an obstacle.
The differencing order is exactly what they disagree about, so rather than picking one
test's answer the order is chosen by an information criterion over the first training
window and then held fixed, and the selected order is printed below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0030-p000

~~~~~~markdown
The coverage line is the check the interval exists to pass, and it is the one number in
this section that says whether the uncertainty estimate is any good. An interval that
contains the outcome far more often than it claims is too wide and one that contains it
less often is too narrow; either way the width is not the quantity it says it is.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0033-p000

~~~~~~markdown
The three columns are not three features. On a log-normal interval the ratio of the
endpoints is the exponential of twice the z-score times the forecast standard deviation,
a function of that standard deviation and nothing else, so it carries exactly the
information the middle panel does and adds none.
The width in the original units is that same quantity multiplied by the level, so it is
mostly a volatility feature wearing an uncertainty label.

The describe table says how little room the ratio has: its spread across the whole sample
is a small fraction of its mean, because the forecast standard deviation of a fixed-order
model barely moves. **The uncertainty of this model is nearly constant.** Its interval
widens in volatile periods because the level widens, not because the model becomes less
sure, and a feature built from the width would be a volatility feature.

That is the useful negative result of this half of the notebook, and it separates the two
sources cleanly. The sampler's posterior width above changes because the data changes what
is knowable; a fixed-order ARIMA's interval width changes almost entirely with the level
it is centered on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
## The features this notebook produces

| Column | What it is | Cadence |
|---|---|---|
| [[ML4T_A3_0001]], [[ML4T_A3_0002]] | posterior means of the two volatility-process parameters | one value per refit, and only where the Monte Carlo error is small beside their spread |
| [[ML4T_A3_0003]], [[ML4T_A3_0004]] | how wide the posterior over the filtered volatility is | one value per refit |
| [[ML4T_A3_0005]] | that width over the level, so it is comparable across refits | one value per refit |
| [[ML4T_A3_0006]] | the forecast standard deviation on the log scale | every session |
| [[ML4T_A3_0007]] | the back-transformed point forecast | every session |

[[ML4T_A3_0008]] and the original-scale [[ML4T_A3_0009]] are deliberately absent. The
first is a function of [[ML4T_A3_0010]] alone and the second is that function times the
level, so a model given either alongside the columns above is given nothing new.

The posterior columns are causal: each is the posterior at the last session of a training
window that ended before the sessions it is stamped on. The level column is causal in the
same sense and stale for the reason the section above gives.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>
