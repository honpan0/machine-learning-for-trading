# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/03_fractional_differencing.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Fractional Differencing

**Chapter 9 | Section 9.1**

**Docker image**: [[ML4T_A3_0001]]

Differencing a price series once makes it stationary and throws away the level. That is
a real loss: whether a price is near the top or the bottom of its recent range is
information, and a return series has none of it. **Fractional differencing** takes the
difference a fractional number of times, which is enough to make the series stationary
while leaving part of the level intact.

**Learning objectives**

- Explain what differencing a series a fractional number of times means, and read the
  weights that do it.
- Apply the transform across a range of the fractional order and read the trade it makes:
  how much of the original level is left against how strongly the result tests
  stationary.
- Say how many observations at the start of a sample the transform costs, and why the
  answer depends on a convention you choose rather than on the data.
- Pick the fractional order without searching the sample you will be tested on.

**Book reference**

Chapter 9, Section 9.1 (Diagnostics and stationarity features).

**Prerequisites**

[[ML4T_A3_0002]] for the ADF test and what stationarity means.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## What a fractional difference is

Differencing once replaces [[ML4T_A3_0001]] with [[ML4T_A3_0002]]. Write that as a weighted sum of
the history, [[ML4T_A3_0003]], and the weights are [[ML4T_A3_0004]].
Differencing twice gives [[ML4T_A3_0005]]. The **fractional** difference of order
[[ML4T_A3_0006]] uses the weights the binomial expansion of [[ML4T_A3_0007]] produces for a
non-integer [[ML4T_A3_0008]], where [[ML4T_A3_0009]] is the operator that shifts a series back one period:

[[ML4T_A3_0010]]

For [[ML4T_A3_0011]] this terminates after two terms and reproduces the ordinary difference. For
[[ML4T_A3_0012]] between zero and one it never terminates. After [[ML4T_A3_0013]] every weight is negative
and decays towards zero, so the transform is today's value minus a decaying weighted
average of the entire past. At [[ML4T_A3_0014]] that average reduces to yesterday alone,
which is the ordinary difference; below one it spreads over hundreds of sessions, and
that spread is the memory ordinary differencing discards.

In practice the tail is cut where the weights become negligible. [[ML4T_A3_0015]] is
where: a weight smaller than this in magnitude is dropped, and the number of weights
left is the width of the fixed window the transform applies. The threshold therefore
decides both how faithful the transform is and how much history each output value
needs, which is the subject of two sections below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## The series

One ETF panel, nine years of daily closes, and the transform is applied to **log**
prices throughout. Logs matter because the filter is linear: on log prices its output is
a weighted combination of log returns plus a small multiple of the log level, where a
multiple of the *price* would scale with the price itself. The residual level term does
not vanish, and it is the subject of the weight-sum section below: multiplying every
price by a constant shifts every output by the weight sum times the log of that
constant. Reduced dependence on the price scale, not independence from it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## The weights, and what the truncation leaves behind

Every weight sequence starts at [[ML4T_A3_0001]], so the differences between orders are all in
the tail. Plotting the magnitude of the weights on a log scale, with the first one
omitted because it is the same for every order, shows the decay rate directly.

Read it in two parts. At lag one the weight is exactly [[ML4T_A3_0002]], so a higher order applies
the larger immediate correction and starts above the others. Every pair of lines then
crosses, because a lower order decays more slowly and its weights end up larger at
distant lags, but they cross at very different places: widely separated orders swap
within the first ten or twenty lags, while two neighbouring low orders stay close and
swap only after hundreds. The end of each line is where its window closes, and that
ordering does not reverse anywhere.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The two columns below are what the truncation costs. The window width is how many
sessions of history each output value needs. The weight sum is what a constant input
would come out as: for an untruncated fractional difference of any positive order the
weights sum to zero, so a constant maps to zero and the level is removed entirely.
Truncation leaves a small positive remainder, and the transformed series therefore
carries that fraction of the level on top of the differenced fluctuation. At a low order
the remainder is large, which is the same fact as "a low order preserves memory", seen
from the other side.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## The boundary convention, and the observations it costs

[[ML4T_A3_0001]] is **boundary-partial**: near the start of the sample, where the full window of
history does not exist yet, it applies whatever weights it can and returns a value
anyway. Nothing is null and the row count is preserved, which is convenient and means
the earliest values were produced by a shorter filter than the later ones.

The **full-window** convention (Lopez de Prado, 2018) treats those rows as unavailable.
It is the one to use for a feature, because a column whose first few hundred values were
computed a different way is a column with a silent regime change at its start.

Imposing it is one line: the first [[ML4T_A3_0002]] rows, where [[ML4T_A3_0003]] is the number of
weights, do not have a full window and are set to null. The count of those rows is the
**sample loss**, and it is reported everywhere below because it is the price of the
order chosen.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## Reading the trade across the grid

Each row applies one order to the SPY log price and reports three things: how many
observations the warmup cost, how strongly the result rejects a unit root, and how much
of the original level survived, measured as the correlation between the transformed
series and the log price it came from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
