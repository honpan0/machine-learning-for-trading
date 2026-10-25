# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/03_label_methods.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Machine learning → 機器學習
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0032-p000

~~~~~~markdown
The two figures make the same point from opposite sides. Class proportions are fixed by
construction, so the first figure is flat by design and carries no information about the
market; the small steps in it are changes in the number of ETFs, not changes in returns.
Everything that varies has been pushed into the second figure: the return a fund needs
to reach the top quintile is a few percent in a quiet month and tens of percent in a
dislocation. A model trained on these labels sees a constant class balance and a target
whose economic meaning changes underneath it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
## Triple-Barrier Labels

Path-dependent labeling that captures realistic trade outcomes:
- **Upper barrier**: Take profit hit → +1
- **Lower barrier**: Stop loss hit → -1
- **Time barrier**: Neither hit → label based on final return

This method is from De Prado's *Advances in Financial Machine Learning*.

**What the barriers are tested against.** [[ML4T_A3_0001]] takes [[ML4T_A3_0002]],
[[ML4T_A3_0003]] and [[ML4T_A3_0004]] alongside [[ML4T_A3_0005]]. Supplied, it detects a touch on the bar's
range and executes a gap-through at the open. Omitted - as here, to keep the mechanics
visible on a single series - the bar reduces to its close: a barrier is touched only if
a *close* crosses it, and the trade is then booked at the barrier price rather than at the
close that crossed it. Both simplifications flatter the label set, and the section below
measures by how much.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
### Triple-Barrier Path Visualization

Each figure below is one trade. The navy segment is the window in which the position was
open, the copper cross is the bar the label resolves on and the price it books, and the
dotted grey continuation is the rest of the twenty-day window - drawn because a reader
needs to see what the label deliberately ignores. The lower-barrier example is the one to
study: the label records a one percent loss on a path that went on to fall twenty-eight
percent, which is the whole point of a stop and the whole risk of trusting the label as a
description of the market rather than of the trade.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
### ATR-Based Barriers

Volatility-adjusted barriers adapt to market conditions:
- Low volatility → Tighter barriers (capture smaller moves)
- High volatility → Wider barriers (avoid whipsaws)
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0040-p000

~~~~~~markdown
### Sample Weights from Uniqueness

Overlapping labels create mechanical dependence: high-concurrency periods
dominate training loss. Weighting by uniqueness prevents these periods
from overwhelming the model. De Prado introduces **uniqueness-based
sample weights** where more unique samples (less overlap) get higher weights.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
### Rich Triple-Barrier Output

Unlike simple forward-return labels, triple-barrier output includes the **full
trade outcome**. This is critical for MFE/MAE analysis (NB04) and position
sizing (Ch20).
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0046-p000

~~~~~~markdown
The two spikes sit exactly on the barriers because a close-only test books the barrier
price, not the close that crossed it. That is an assumption, and it is measurable: the
cell below compares what each trade was booked at against the close that actually
triggered it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0048-p000

~~~~~~markdown
The gap runs the wrong way on both sides, and further on the lower side than the upper
one. An upper-barrier exit is booked at the take-profit when the close that triggered it
was already above it, so the label gives away part of the gain; a lower-barrier exit is
booked at the stop when the close that triggered it was well below, so the label hides
part of the loss. Averaged over every barrier exit the label set is better than what
those closes would have paid, and the bias is asymmetric rather than a wash.

Read that as barrier-price against trigger-close accounting on a fixed set of exits, and
nothing more. It is **not** a measurement of what OHLC detection is worth: supplying
[[ML4T_A3_0001]], [[ML4T_A3_0002]] and [[ML4T_A3_0003]] changes which bar exits and which barrier is hit, not
only the price each exit is booked at, and an intrabar touch that does not gap still
executes at the barrier there too. Sizing that setting needs a second labeling run to
compare against, not a repricing of this one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0049-p000

~~~~~~markdown
### Sequential Bootstrap

Overlapping labels create sample dependence. The **sequential bootstrap**
(De Prado, AFML Ch4) generates bootstrap indices that respect label
uniqueness - favoring samples with less concurrent overlap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0052-p000

~~~~~~markdown
Overlaid on one axis with one binning. Side-by-side panels rescale independently, which
would let two nearly identical distributions look like a finding.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
The two histograms are nearly the same shape, and the printed comparison above says how
far apart their means are. The shift is real and it is small: the sequential draw tilts
toward less-overlapped labels, it does not select them. What it cannot do is manufacture
independent observations that the sampling scheme never generated - the overlap is a
property of labelling every bar over a horizon of many bars, and the next section
measures what that leaves.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
### Effective Sample Size

The section text defines [[ML4T_A3_0001]] and notes that
for fixed-horizon labels sampled at every bar, [[ML4T_A3_0002]].

That is an approximation. Below we *measure* [[ML4T_A3_0003]] by computing each
label's average uniqueness [[ML4T_A3_0004]] directly - per symbol, since concurrency
accumulates along the time axis, not across the cross-section - and compare it
to the [[ML4T_A3_0005]] shortcut. We report both the single-asset (SPY) and the full-panel
figures, because they answer different questions: how many independent
observations does *one* series carry, and how many does the *panel* carry.
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0056-p000

~~~~~~markdown
Uniqueness depends only on the index geometry of the labels, not on prices: label [[ML4T_A3_0001]] is
alive over bars [[ML4T_A3_0002]], and [[ML4T_A3_0003]] averages [[ML4T_A3_0004]] over that span. Concurrency is a
per-symbol quantity, because two different ETFs' labels do not overlap each other in the
sense the weight measures, so the panel figure is a sum over symbols rather than one
calculation on the stacked frame.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0058-p000

~~~~~~markdown
## Trend Scanning Labels

De Prado's adaptive approach that identifies trends using t-statistics.
The method scans forward with varying windows and selects the one
with the highest statistical significance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>
