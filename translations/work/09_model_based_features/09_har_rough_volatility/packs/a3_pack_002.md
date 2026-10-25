# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/09_har_rough_volatility.ipynb；A3 Pack 002；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0013-p000

~~~~~~markdown
The identity closes to the last digit, which it must; what it buys is the size of each
term. The overnight square is a large fraction of the daily square for a symbol whose
market is open six and a half hours out of twenty-four, and the cross-product is small
beside the other two, so the two components are close to uncorrelated.

The last ratio is the separate question. Summing squared minute returns and squaring the
aggregate open-to-close return are two estimates of the same session's variance and they
do not agree: the minute-by-minute sum picks up movement that reverses before the close
and the aggregate does not. Neither is wrong, and which one a model wants depends on
whether reversals inside a session are risk it is exposed to. A position held through the
session sees the aggregate; one traded inside it sees the sum.

Either way, a comparison between an intraday measurement and a daily estimator has to
account for the overnight term, and a strategy holding overnight is exposed to a risk no
intraday measurement sees.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
## Which daily estimator to use

Ranking estimators by accuracy needs a target measured the same way, and the section
above is the reason there is not one here: the intraday measurement covers the session
and every daily estimator covers something else.

What is measured below instead is each estimator's **dispersion around its own trailing
average**, session by session on the ETF panel's adjusted daily bars. Be clear about what
that is and is not. It is not the estimator's sampling error: the underlying volatility
genuinely moves within twenty sessions, so real movement is in the number, and the
trailing average in the denominator carries the estimator's own noise as well. Nor are
the four measuring the same interval, since the close-to-close estimator spans a session
boundary and the other three do not.

What it does show is how jagged each column would be if a model read it, which is a
property of the column rather than of the estimator, and is the thing that decides
whether a feature needs smoothing before use.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
The close-to-close column is the one that separates from the rest, on both of the
quantities reported. It is the most dispersed around its own average, and it is the only
one that puts a non-trivial number of sessions at zero: a session that closed where it
opened has no close-to-close movement to read, whatever happened in between. Reading the
high and the low is what removes that failure, and Chapter 8 is where the efficiency of
each formula is derived rather than measured.

The mean column ranks them on level, and there the ordering says nothing about which is
right. Each formula assumes something about the process, they cover different parts of
the day, and this notebook has no target to check any of them against. Read the level as
a scale each estimator carries, and never mix two of them in one feature without
rescaling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## The library's versions, and the one that sees the gap

[[ML4T_A3_0001]] supplies all five as Polars expressions. They take a
window rather than working session by session, and they average variances before taking
the square root where the cells above take the square root first, so the two do not agree
exactly even where they implement the same formula. The difference is the usual one
between a mean of roots and a root of means, and it is small next to the difference
between estimators.

The fifth estimator is the reason to run this: **Yang-Zhang** adds an overnight component
to an intraday one, so it is the only one of the five whose target is the whole day that
Part 1 decomposed. Its level should sit above the others for exactly that reason.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
Yang-Zhang and the close-to-close estimator are the two that cross a session boundary,
and they are the two whose target is the day rather than the session. The three purely
intraday estimators are measuring something smaller and should not be compared against
them on level, which is the same point Part 1 made with the decomposition and is the
reason a feature set should not mix them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
# Part 2: three horizons instead of one

The **heterogeneous autoregressive** model (Corsi, 2009) predicts tomorrow's volatility
from three averages of today's: yesterday's, the last week's, and the last month's.

[[ML4T_A3_0001]]

The argument for that shape is economic rather than statistical. Traders operating at
different frequencies watch volatility at different horizons and act on what they watch,
so the volatility a market produces is a superposition of their responses rather than a
single decay. The model is a linear regression, which makes it far easier to fit than
GARCH and far easier to read: each coefficient is the weight one horizon carries.

The regressors are built from a range-based estimator for the reason Part 1 established,
and each is lagged so that nothing on the right-hand side of the regression is known
later than the session it predicts from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>
