# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/09_options_continuous.ipynb；A3 Pack 003；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Backtesting → 回測
- Transaction costs → 交易成本
- Label → 標籤

## 待翻譯英文單元

### c0042-p000

~~~~~~markdown
The short figure is constructed here, by negating each day's held-contract return and
compounding the result over the same year. That is the P&L of a position whose notional is
reset against equity every day, and it has to be named because the convention decides the
answer.

Under *this* convention the short return is not the negation of the long one, and the two
printed numbers show how far from it: both lose money over the year, so a sign flip gets
the direction wrong and not merely the size. Both series reset exposure against their own
equity each day, and two paths that rebalance separately do not stay mirror images.

A different convention gives a different answer, and one of them gives exactly the
negation: holding the opposite quantity of the same contracts every day, never
rebalancing, produces the opposite dollar P&L before costs, which on the same initial
capital is the long return negated. The lesson is not that the negation is wrong in
general. It is that a cumulative short return is undefined until the sizing is stated, and
negating a compounded long return silently assumes one particular sizing that the series
above does not use.

The two roll-convention series part company by tens of percentage points of cumulative
return over a single year, from the same contracts, the same days and the same prices. Only the roll-day
convention separates them. On a series whose stated purpose is to be backtested, that is the
difference between two materially different answers about the same strategy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0042-p001

~~~~~~markdown

Zeroing is the more conservative-looking choice and it is not the safer one. It deletes a
real return on most of the sample, because the contract changes on the majority of days, and
the deleted returns do not average to zero - so it is a one-sided subtraction repeated on the
majority of observations, not noise that cancels. Here it makes the instrument look worse
than it was.

The general form of the error is worth naming, because it is not specific to straddles. A
roll is two facts at once - the instrument changed, and the market moved - and an adjustment
that suppresses the day suppresses both. Futures get away with the crude version because
quarterly rolls make it four days a year. Here it is most of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p001>>>
<<<ML4T-ZH-END:c0042-p001>>>

### c0044-p000

~~~~~~markdown
Both reconstructions remove the sawtooth, which is what the adjustment was for, and they
separate from each other steadily over the year because they disagree on most days. The
zeroed series is the lower of the two and its gap widens monotonically: every roll day
contributes another deleted return.

The held-contract series is the one to backtest. Roll costs, meaning the bid-ask actually
crossed to switch contracts, are a separate deduction and belong with transaction costs in
Chapter 18 rather than inside the price series.

For **labels**, neither reconstruction is the right tool. A label is the return of a trade
someone could have placed and held, which is the same-contract calculation in Section 3.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0045-p000

~~~~~~markdown
## 5. Summary: Three Approaches Compared

| Approach | Mechanism | Suitable For |
|----------|-----------|--------------|
| Naive (chained) | [[ML4T_A3_0001]] on the constant-maturity series | Nothing. It contaminates labels |
| Same-contract | Look up the entry contract h days later | Labels, being per-trade P&L |
| Continuous, held-contract | Roll days take the held contract's return | Backtesting mark-to-market |
| Continuous, roll-zeroed | Roll days take zero | Nothing. It deletes real P&L |

Three of the four need the raw option chain; only roll-zeroing avoids it, and that is the
whole of its appeal. On a series that reselects quarterly the shortcut is defensible. On one
that reselects most days it costs the majority of the sample's return, which the section
above measures rather than argues.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0046-p000

~~~~~~markdown
The final table puts the forward return from each construction side by side over the same
days.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0048-p000

~~~~~~markdown
## Key Takeaways

1. **A constant-maturity series is not an instrument.** The rule picks whichever straddle
   sits closest to the target each day, independently, so the contract identity changes on
   most days of the year. Each change resets time value and prints a price step that no position
   experienced.

2. **The roll contamination is systematic and it is large.** Roll days and non-roll days have
   means of opposite sign, and both are printed above rather than quoted here. The futures
   analogue is roll yield, but a quarterly roll contributes four such days a year and this
   series contributes most of them, which turns a correction into the bulk of the signal.
   Splitting the roll days by what changed is worth doing, and it is worth not over-reading:
   the strike-only group's mean sits beside the do-nothing group's, yet its per-day
   construction error against the held contract averages several percentage points, in the
   opposite direction from the error on expiration days. Agreement between two averages says
   nothing about whether the individual values are right.

3. **A short position's cumulative return is not the long's negation.** Per period and for a
   fixed quantity it is, which is why the notebook prints one convention and states the other.
   Compounding breaks the symmetry: over the demo year the long series and the daily-reset
   short series are both negative, so reading the seller's result off a sign flip gets the
   direction wrong, not merely the magnitude.

4. **The construction error is a per-day quantity.** What the series records minus what the
   contract actually held earned is the thing that reaches a label or a backtest, and it is
   measured day by day in Section 5 rather than inferred from group averages.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>
