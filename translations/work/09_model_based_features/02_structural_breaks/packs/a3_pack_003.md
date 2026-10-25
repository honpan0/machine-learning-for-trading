# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/02_structural_breaks.ipynb；A3 Pack 003；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Cluster → 群集
- Volatility → 波動率

## 待翻譯英文單元

### c0022-p000

~~~~~~markdown
The two panels show the trade the choice is between. CUSUM keeps every deviation, so a
shift moves the statistic permanently and a second shift is then read against a baseline
the first one moved; the excursions in 2008 and 2020 never come back. MOSUM holds only
what is inside its window, so a shift it has fully absorbed stops adding to it and the
statistic stays readable for the next event, at the cost of being blind to a drift too
gradual to register across [[ML4T_A3_0001]] observations. It
comes back to zero here because the average return after each crisis is close to the
burn-in average again, not because the statistic forgets a permanent shift.

The bandwidth is the same trade at a smaller scale: a short window reacts sooner and
crosses a threshold more often on noise alone, a long one is steadier and later. Neither
is a default. Set it from how long a shift has to persist before you would want to act
on it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
# Part 2: break detection as a classification problem

The ADIA Lab structural break challenge poses the problem in a third form. Given a
series and a candidate boundary date, decide whether the process changed at that
boundary. The input is one series and one date; the output is a probability. That
framing makes the problem supervised, so the detector is learned from labelled examples
rather than derived from a null hypothesis, and it accepts evidence of any kind that
separates the two sides of the boundary.

The work is then in the features. Each one summarises a comparison between the window
before the boundary and the window after it, and the families below cover the four ways
two samples can differ: where they sit, how spread out they are, what shape they have,
and how each observation depends on the one before it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0024-p000

~~~~~~markdown
## Labelled examples

Real breaks are scarce and their dates are arguable, so the detector is trained on
series whose construction is known. Each example is 500 steps with a candidate boundary
at the midpoint. Half have nothing at the boundary; the other half have one of four
changes, each of which a different family of features is built to see.

The figure below draws three of the four. The fourth, a change in how strongly each
value depends on the one before it, is left out because neither panel would show it: it
alters no level, no spread and no distribution, only the order the same values arrive
in. That is exactly why one of the five families measures dependence and none of the
other four would catch it.

Holding the spread fixed while the dependence changes takes care in the generator, in
three places. A first-order autoregressive series with coefficient [[ML4T_A3_0001]] and
unit-variance innovations has marginal variance [[ML4T_A3_0002]], so raising [[ML4T_A3_0003]] would
raise the spread too: scaling the innovations by [[ML4T_A3_0004]] fixes the marginal
variance at one on both sides. Keeping [[ML4T_A3_0005]] below one keeps both halves stationary.
And the recursion runs once through the whole series, starting from a draw with the
stationary variance rather than from zero, because a series restarted at zero has
variance [[ML4T_A3_0006]] at step [[ML4T_A3_0007]]: starting each half separately would put a variance
transient at exactly the boundary being tested, which is the thing the example is
supposed not to contain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0027-p000

~~~~~~markdown
## Family 1: where the two windows sit

**Welch's t-test** compares two means without assuming the two samples have the same
variance, which matters here because a break often moves both. It is run on the raw
values, and again on absolute values at three window widths: taking absolute values
converts a change in spread into a change in level, so the same test picks up a
variance shift that the raw comparison would miss.

The three widths are then combined by **Fisher's method**, which turns independent
p-values into a single one by summing their logs. It is the standard way to ask whether
a set of weak signals is jointly stronger than chance. The windows here overlap, so
their p-values are not independent and the combined value is not a calibrated
probability; it is used as a feature, where being monotone in the evidence is what is
required of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
## Family 2: how spread out they are

Three tests of the same question, differing in what they assume. The **F-test** on the
ratio of variances is exact when both samples are normal and unreliable when they are
not, which for financial returns they never are. **Levene's** test compares mean
absolute deviations from the group centre, which stays accurate on non-normal samples.
**Fligner-Killeen** ranks the deviations before comparing them, so the size of the
largest observation cannot drive the answer at all. On financial data the last two are
the ones to read; all three are kept because the classifier can learn where they
disagree.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
## Family 3: what shape they are

A break can leave the mean and the variance where they were and still change the
distribution, so this family compares the two samples whole. The
**Kolmogorov-Smirnov** statistic is the largest gap between their cumulative
distributions. The **Jensen-Shannon divergence** and the **Hellinger distance** both
measure how far apart two histograms are, the first through the information lost by
treating one as the other and the second geometrically; both are bounded, which keeps
them comparable across series. The **Wasserstein distance** is the cost of moving one
distribution onto the other, so unlike the other three it grows with how far the
probability has to travel and carries the units of the data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## Family 4: how each observation depends on the last

Two windows can agree on every distributional summary above and still differ in
ordering, because a distribution says nothing about sequence. Lag-one autocorrelation
captures the ordering of the values themselves; the same statistic on squared values
captures whether large moves cluster, which is the dependence that changes when a
volatility regime does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
## Family 5: does the data agree on where the boundary is

The four families above take the boundary as given and ask what changed there. This one
asks the boundary itself: run a change point detector that is free to pick any date,
and measure how far its answer lands from the candidate. A break at the candidate date
should attract both detectors to it; a series with no break puts them anywhere.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>
