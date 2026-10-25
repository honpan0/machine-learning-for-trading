# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/12_wasserstein_regimes.ipynb；A3 Pack 003；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Slippage → 滑價
- Drawdown → 回撤
- Feature → 特徵
- Label → 標籤
- Cluster → 群集
- Clustering → 分群
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0033-p000

~~~~~~markdown
## What the two clusters were, and what holding through one would have been

The label is known at the close of the session it is stamped on, so the return it can be
earned against is the next session's. Everything below holds each label for one session and
reads the following return, over the block after the split only.

The table reports two different return streams and names each column for the one it belongs
to, because they answer different questions and averaging one into the other is how a
regime study overstates itself.

- The columns marked **in this regime** describe the returns of the sessions the label
  selects, and nothing else. They are conditional statistics of the index.
- The columns marked **holding only here** describe one rule: hold the index while the label
  says this regime, hold cash otherwise, over every session in the evaluated block. Cash
  sessions contribute a zero return and a flat stretch of the equity curve, so the mean is
  pulled toward zero from whichever side it was on, and the drawdown is one someone could have
  taken. No costs and no slippage are charged.

Compounding only the sessions inside a regime, which is the easier thing to write, splices
out the gaps. The deepest drawdown is the same either way: the same returns compound in
the same order and only the flat stretches go. What changes is anything measured per unit
of time. The mean and volatility are annualized over fewer sessions than the rule was
exposed to, and a drawdown that took two years to climb out of is reported as though it
took one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
The conditional volatilities differ by construction, since that is what the clusters were
ordered by, so that row is a check that the ordering did what it claims rather than a
result. The conditional mean return is the result, and it is the asymmetry the chapter's
downstream notebooks use: the two regimes are not two draws from one distribution that
differ only in spread.

The two rules are what a reader would actually be choosing between, and neither is the index.
Each holds it for part of the block and cash for the rest, so each mean is the conditional
mean scaled by the fraction of sessions invested: nearer zero, not necessarily smaller, and a
negative conditional mean comes out higher. The volatility of a rule is not a scaled
conditional volatility at all, because switching between an invested session and a cash one is
itself variation; whichever direction it moves in this table is a fact about this sample.

The difference between the two rules is the only comparison here where the same sessions are
on both sides of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
## The distance between the two clusters' returns

The clustering worked on windows. A separate question is how far apart the two clusters'
individual returns are as distributions, and [[ML4T_A3_0001]] answers it with two measures
built for monitoring a model in production. [[ML4T_A3_0002]] calibrates its
threshold by permutation, so the distance is compared against a null of one distribution
rather than against a fixed number. [[ML4T_A3_0003]] bins both samples and sums a symmetric
relative difference per bin, and its thresholds are conventions rather than tests.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
Both numbers are large, and neither is a surprise: the two samples were separated by a
procedure that reads their distributions. What the permutation threshold adds is a scale,
since a distance is otherwise uninterpretable in the units of a daily log return.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
The middle panel is the one to be suspicious of. The label and a rolling standard deviation
of the same window agree closely, which raises the question of what the clustering bought
over a threshold on that standard deviation. On this series and with two clusters, not much:
the two disagree on the sessions near the boundary and nowhere else, and the disagreement is
what the next notebook has to earn its keep on.

What the clustering does have is a construction that extends. Three clusters, a longer
window, or a distribution that differs in skewness rather than spread are all the same code
with a different argument, and none of them has a threshold to choose.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0041-p000

~~~~~~markdown
## The three columns

The chapter's feature catalog asks for three, and each one is stamped at a window's close
and held, so every value is a function of returns up to and including the session it sits
on.

- [[ML4T_A3_0001]] is the assignment, ordered so the higher number is the more
  volatile cluster.
- [[ML4T_A3_0002]] is the window's distance to the centroid it was assigned to. A window
  is assigned to its nearest centroid whether or not it resembles it, so this column is what
  says whether the assignment means anything: a large value is an environment the fitted
  block did not contain.
- [[ML4T_A3_0003]] is one on the sessions where the Wasserstein assignment and a
  two-moment assignment of the same window disagree. What the two read differs by
  everything a mean and a variance omit, so a disagreement locates a window whose shape and
  whose first two moments point different ways. Which part of the shape did it is not
  something this column records.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
The row count is far short of the session count, and both reasons are deliberate. The
sessions before the first window closed have no value to carry. And the whole fitted block
is dropped, because both sets of centroids and the ordering that numbered them were computed
from those windows: a column over them would be a fit describing its own input, whatever the
stamping does about the window. Fitting chronologically, one refit per block, is what would
recover those years, and it is the construction the case studies use.

The disagreement rate is the number to carry into [[ML4T_A3_0001]]. A rate near zero
would say the column is constant and worthless; a rate near half would say the two methods
have nothing to do with each other and one of them is wrong. The rate here is between them,
which is the only case in which the column can carry anything.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>
