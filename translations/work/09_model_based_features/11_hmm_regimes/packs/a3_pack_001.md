# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/11_hmm_regimes.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Clustering → 分群
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Regime Detection with Hidden Markov Models

**Chapter 9 | Section 9.5**

**Docker image**: [[ML4T_A3_0001]]

A **regime** is a period during which the market behaves one way rather than another:
calm or stressed, trending or reverting. Nobody observes it. What a regime model does is
infer, from what is observable, which of a small number of unobserved states the market is
probably in now, and how likely it is to be in a different one tomorrow.

The distinction that matters more than the model is between an inference that uses only
what had happened by a given session and one that uses the whole sample. The second is
better in every way except the one that counts.

**Learning objectives**

- Build two regime indicators from observable quantities alone, and treat them as the bar
  any estimated model has to clear.
- Work through the recursion that infers a hidden state from observations one at a time,
  on an example small enough to check by hand.
- Say what separates that recursion's answer from the one that reads the whole sample, and
  measure the difference on real data.
- Fit the model to returns, handle the three things that go wrong when you do, and turn
  the result into columns.

**Book reference**

Chapter 9, Section 9.5 (Regime features).

**Prerequisites**

[[ML4T_A3_0002]] for stationarity. Probability and matrix multiplication.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## The data

SPY daily bars with three derived series: the log return, a rolling standard deviation of
it, and a long moving average of the price. The first two are what the model reads; the
moving average is one of the two rules in Part 1.

A Gaussian model reading returns alone can already separate states that differ only in
variance, because two emissions with the same mean and different variances are two
different distributions. So that is not why the volatility column is here. It is here for
what it is: a summary of the last month rather than of one session, which makes the state
inferred at each session a statement about recent history and not about the latest return.

The frame keeps only sessions where all three are defined, which puts the first session
one moving-average window after the data begins. That window is the price of the rule in
Part 1: over those sessions the moving average is missing, and a comparison against a
missing value is false rather than missing, so a frame that kept them would report them as
sessions the price was not below its average.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
# Part 1: what a rule can do without estimating anything

Two indicators, both computable by hand, both available the moment the data is. They are
not a warm-up: an estimated model that does not beat them is not worth its estimation
risk, and stating them first is what makes the rest of the notebook a comparison rather
than a demonstration.

The **volatility index** at a level is the classic stress rule. The index is the option
market's expectation of near-term volatility, so it is a forward-looking quantity nobody
has to fit, and a level around twenty has been the conventional line between calm and
stressed for decades.

A price against its own **long moving average** is the classic trend rule. Above the
average is an uptrend, below it a downtrend, and the only choice is the length.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
# Part 2: inferring a state you cannot see

A **hidden Markov model** has three parts. A small number of hidden states; a **transition
matrix** giving the probability of moving from each state to each other one; and an
**emission** distribution per state saying what observations that state tends to produce.
The states are never observed. What is observed is a sequence of numbers, and the model's
job is to say which state each of them probably came from.

The **forward algorithm** does that one observation at a time. It carries a probability
over states, advances it through the transition matrix, multiplies by how likely the new
observation is under each state, and renormalizes. What comes out at each step is
[[ML4T_A3_0001]], which is called the **filtered**
probability and is the quantity a feature has to be.

The example below is ten observations from a two-state model whose parameters are known,
small enough to read off the printed table and check.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The recursion in two lines. Start with the initial distribution weighted by how likely
the first observation is under each state:

[[ML4T_A3_0001]]

then advance:

[[ML4T_A3_0002]]

Normalizing [[ML4T_A3_0003]] across states gives the filtered probability. Nothing after step
[[ML4T_A3_0004]] enters it, which is the whole point.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Filtered against smoothed

The **smoothed** probability [[ML4T_A3_0001]] answers a
different question: given everything that eventually happened, what state was the market
in at [[ML4T_A3_0002]]? It is the better estimate of the past and it is unusable as a feature, because
at time [[ML4T_A3_0003]] the observations it conditions on had not happened.

The difference between the two is not a technicality. A smoothed probability rises before
a transition, because the observations after the transition tell it the transition was
coming. A model trained on that column learns to predict an event from a feature that
already knows the event happened.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
# Part 3: fitting it to returns

Three things go wrong when this model is estimated rather than given, and each has a
standard answer.

**The optimizer finds a local maximum.** Expectation-maximization climbs from wherever it
starts and stops at the first peak it reaches, so different starts give different models.
The answers are to start from several places and keep whichever reached the highest
likelihood, or to start somewhere sensible: a clustering of the observations puts the initial emission parameters near
where they will end up.

**The number of states is a choice.** More states always fit better, so the criterion has
to charge for them.

**The states have no order.** Nothing in the model says which state is which, so the same
fit run twice can return them swapped, and a feature built from a state label means
different things in different windows. The answer is to sort them by something the model
does define, here the size of each state's variance.

All four helpers below live in [[ML4T_A3_0001]] rather than in this
notebook, because filtered inference in particular needs a private hmmlearn call that is
worth having in one place: [[ML4T_A3_0002]] returns the smoothed posterior and there is no
public method that returns the emission term the forward recursion needs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>
