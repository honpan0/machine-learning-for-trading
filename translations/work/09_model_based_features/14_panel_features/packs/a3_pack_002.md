# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/14_panel_features.ipynb；A3 Pack 002；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Transaction costs → 交易成本
- Slippage → 滑價
- Drawdown → 回撤
- Feature → 特徵
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0014-p000

~~~~~~markdown
## From spread to position

The signal is the spread measured against its own recent history: subtract a rolling mean,
divide by a rolling standard deviation, and the result is in units of its own variability. A
spread [[ML4T_A3_0001]] standard deviations below its recent mean is an entry on the long
side, meaning long the dependent series and short [[ML4T_A3_0002]] units of the other, and the
position is held until the spread crosses back through the mean.

Both the mean and the standard deviation are rolling and both use the window chosen above, so
every value is available on its own session. The position is stepped forward one session at a
time rather than computed with a vector operation, because it depends on its own previous
value: an entry that has not yet reverted stays open.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
## What the position would have returned

What was held over session [[ML4T_A3_0001]] is one share of the dependent fund against [[ML4T_A3_0002]] shares
of the other, because [[ML4T_A3_0003]] is the ratio the filter had produced by the previous close.
Its profit in dollars is the two price changes weighted by those holdings:

[[ML4T_A3_0004]]

and to express it as a return it is divided by what holding both legs committed, which is the
value of one share of the first plus [[ML4T_A3_0005]] shares of the second.

That is deliberately not the first difference of the [[ML4T_A3_0006]] column. The spread at [[ML4T_A3_0007]] is
defined with [[ML4T_A3_0008]], so differencing it mixes the session's price moves with the change in
the ratio itself, and a holder cannot rebalance at a ratio they only learn at that session's
close. The two agree only where the filtered ratio is flat.

It is also not the difference of the two funds' returns. That quantity is the profit of equal
dollar amounts in the two legs, which is a hedge in money rather than in shares, and it uses no
estimated ratio at all. Which of the two a strategy wants is a choice; reporting one while
having estimated the other is not.

Three limits, all structural rather than fixable here. No transaction costs and no slippage are
charged, and a spread strategy trades often enough to be sensitive to both. The short leg is
assumed available at no borrowing cost. And the pair was chosen by looking at the same history,
which the screening section takes up.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
The entry count is the number to read, and it is the section's conclusion. A half-life of
months sets a window of about a year, a band that wide is crossed rarely, and the result is a
position that opens a couple of times across the evaluated years and is then held for more than
half of their sessions. That is not
a mean-reversion strategy; it is a slow directional bet on a spread, which is what the
cointegration tests said would happen when they declined to find a stationary combination.

The return is therefore not evidence about the method. It is one draw from as many trades as the
entry count reports. The
drawdown is the one figure here worth carrying: it is what a position of that duration exposed
a holder to while waiting for a reversion the spread had no mechanism to deliver.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
## Screening, and what a screen costs

Six candidate pairs, each with a stated reason to be related, run through the same two tests.
The table is the point of the section: a reason is not evidence, and the two tests do not
always agree.

The screen also carries a cost that the table cannot show. Testing six pairs at the same
level and reporting whichever passes makes the reported level wrong, because the chance that
at least one of six independent tests rejects a true null is far above the level of any one of
them. What follows from that is not a correction to apply here but a rule for reading: a pair
that passes a screen has cleared a lower bar than a pair tested on its own, and its spread
needs to hold up on data the screen did not see.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
Read the two counts printed under the table first. Over this sample no pair clears the
Engle-Granger test at the stated level, and one pair is called cointegrated by Johansen alone.
Six pairs with a stated reason, one weak signal: that is the result, and it is more useful than
a table of successes would have been, because the reasons were not bad ones.

The half-life column decides something different from whether the relationship exists. A
half-life of a few sessions leaves room to enter and exit inside the reversion. Every half-life
here is measured in months, and the shortest of them still holds a position through a quarter in
which the relationship may have changed for reasons no test on past data can see. A pair needs
both: a spread that reverts, and reversion fast enough to trade.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
## The same features as library expressions

The pairwise work above is written out with statsmodels and numpy, one pair at a time.
[[ML4T_A3_0001]] supplies the rolling versions as Polars expressions, which is the form a
pipeline over many pairs wants: [[ML4T_A3_0002]] and [[ML4T_A3_0003]] read return
columns, [[ML4T_A3_0004]] reads price columns, and [[ML4T_A3_0005]] reads
a correlation column and emits flags for its level.

What these are not is a replacement for the tests above. A rolling score computed over a
window is a description of that window, and cointegration is a statement about a relationship
holding over a long sample. The two answer different questions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## A level replaced by a position

The second half of the notebook changes what a feature is computed over. Nothing here is a
rolling window: the operation reads one date across many assets and returns each asset's
standing among them on that date.

Three versions of the same idea, and they are not interchangeable. A **rank** is an integer
position and is bounded by the number of assets, so it says nothing about how far apart the
assets are. A **percentile** divides the rank by the count, which makes a universe of ten
comparable with one of five hundred. A **z-score** subtracts the cross-sectional mean and
divides by the cross-sectional standard deviation, which keeps the distances and therefore
keeps the outliers, and on a date when one asset moved five times as far as the rest it is the
only one of the three that says so.

None of the three uses a future date. That is worth stating because the causality question
looks the same as everywhere else in the chapter and has a different answer: a cross-sectional
operation reads across assets at one date, so it cannot look forward in time whatever else it
does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>
