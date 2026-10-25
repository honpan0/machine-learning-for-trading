# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/07_multiple_testing.ipynb；A3 Pack 003；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Sharpe ratio → 夏普比率
- Feature → 特徵
- Out-of-sample → 樣本外
- Cross-validation → 交叉驗證
- Overfitting → 過度擬合
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0043-p000

~~~~~~markdown
The Rademacher ratio printed above is well below one, reflecting the high correlation
among the momentum variants - testing six lookbacks is not six independent trials. Even
with that milder effective penalty, the features do not clear BH-FDR correction after
HAC inference.

Across the correlated momentum, reversal, volatility and volume features in this scan,
and with HAC inference, no feature clears BH-FDR at the level set above.
Univariate bivariate-IC screening is one filter; Chapters 11-12
evaluate the same features in a multivariate setting where the relevant
question is conditional contribution to a fitted model, not single-feature
significance. The corrections here ensure that features *selected* for
that pipeline have not been promoted purely by selection bias.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
## Output: Discovery Report

The JSON structure below is a template for production logging. Recording
the search-set size, correction method, and per-method discovery counts
alongside the Rademacher analysis makes the report self-contained and
auditable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0048-p000

~~~~~~markdown
## Deflated Sharpe Ratio (DSR)

When the outcome is a strategy Sharpe ratio (not factor IC), the **Deflated Sharpe
Ratio** (Bailey & López de Prado, 2014) adjusts for selection bias among
multiple strategies tested.

DSR answers: "Given that I tested N strategies and kept the highest Sharpe, what is the
probability that this Sharpe is genuinely positive?"

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
**Every row above is on the annualized scale.** That matters more than it sounds: the
library returns [[ML4T_A3_0001]], [[ML4T_A3_0002]] and [[ML4T_A3_0003]] per period
and [[ML4T_A3_0004]] already annualized, so printing them in one column without
converting puts a factor of the square root of the trading year between two adjacent
rows. The comparison the table invites - the highest Sharpe against the null's expected
maximum - is only meaningful once they are on the same scale.

Read that way, the table above is stark. The highest-scoring of the pure-noise
strategies posts a respectable annualized Sharpe, and the expected maximum *under the
null* is barely below it. Almost the entire apparent performance is selection. What is
left after deflation is a small excess, and the DSR probability falls well short of any
conventional confidence level. [[ML4T_A3_0005]] is the number that makes this
legible: it says how good the highest-scoring strategy would look *even if none of them
had any skill at all*.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
## Probability of Backtest Overfitting (PBO)

PBO (Bailey et al., 2017) estimates the probability that the strategy ranked first in
sample lands in the bottom half out of sample. A PBO above one half is conventionally
read as severe overfitting - with a caveat this notebook measures rather than states.

The method uses combinatorial purged cross-validation (CPCV): split the data
into S groups, choose half as in-sample, the rest as out-of-sample, and
repeat across all [[ML4T_A3_0001]] combinations.

Full implementation with CPCV splitting is covered in Chapter 16. Here we
demonstrate the [[ML4T_A3_0002]] function on pre-computed IS/OOS performance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0053-p000

~~~~~~markdown
The number to compare against here is **one half, not zero**. Strategy 0 was handed a
large in-sample advantage and nothing else - out of sample it is the same standard normal
as the other nineteen. So the strategy selected in sample is selected on noise, and its
out-of-sample rank is uniform: it lands below the median about half the time. A PBO near
one half is the *correct* reading of a selection that carries no real edge, and the
median out-of-sample rank printed above - dead centre of the field - says the same thing
a second way.

This is why the "PBO above one half means severe overfitting" rule of thumb needs care.
It is not a pass mark with a comfortable margin below it. A strategy whose edge is
entirely an artifact of selection sits *at* one half, and the sampling error on a PBO
estimated from this many combinations is wide enough that a point estimate somewhat
below it is fully consistent with a strategy that has no edge at all. What would
actually be reassuring is a PBO close to zero, together with a strategy that ranks
first in sample and stays near the top of the out-of-sample ranking.

PBO is a powerful complement to DSR. While DSR focuses on Sharpe inflation,
PBO directly measures whether the in-sample best-performing configuration *degrades* out-of-sample.
See Chapter 16 for applying PBO with actual CPCV backtest splits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0054-p000

~~~~~~markdown
The FWER adjustment in the table below is driven by how much the trial Sharpes disagree
with each other: if every candidate scored identically, searching more of them would
tell you nothing new. Setting the trial variance to zero therefore switches the
correction off and every column would print the single-test answer. The dispersion used
is the one the Deflated Sharpe search above actually exhibited, so the table reports the
cost of that search rather than of a hypothetical one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
## Minimum Track Record Length (MinTRL)

How long must a track record be before we trust a Sharpe ratio?
[[ML4T_A3_0001]] gives the minimum number of observations needed for
statistical significance, adjusted for non-normal returns (skewness, kurtosis,
autocorrelation). [[ML4T_A3_0002]] additionally adjusts for the number of
strategies tested.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
**Interpretation**: read across a row, not down a column. Every row lengthens as the
search widens, and the rows do not lengthen at the same rate.

The lowest-Sharpe row already needs more than a decade of daily data with no search at
all, and once even a handful of candidates have been tried it cannot be confirmed at any
length - which is what [[ML4T_A3_0001]] in the table means, the required record growing faster
than the evidence a longer record supplies. The next higher Sharpe is confirmable in a
couple of years unsearched, needs longer than a career after a handful of candidates,
and reaches [[ML4T_A3_0002]] after a hundred. Only the highest-Sharpe row stays inside a working
career all the way across.

The columns differ only because the trial Sharpes differ. That is the whole mechanism:
the FWER correction prices the *search*, so a search over candidates that all score
alike costs nothing while a search over dispersed candidates is expensive. A higher
Sharpe buys back room, but the ordering across a row never reverses.

This connects to NB06's track record planning for IC: both IC and Sharpe
require longer records than practitioners typically assume.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>
