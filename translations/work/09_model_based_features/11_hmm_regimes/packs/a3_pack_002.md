# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/11_hmm_regimes.ipynb；A3 Pack 002；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Clustering → 分群
- Volatility → 波動率
- Covariance → 共變異數

## 待翻譯英文單元

### c0020-p000

~~~~~~markdown
The spread across random starts is the size of the problem: it is how much of the fitted
log-likelihood is decided by where the optimizer happened to begin rather than by the
data. A seeded start reaches its answer once, which is not the same as reaching a better
one, and the two numbers beside each other say which happened here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
## How many states

The **Bayesian information criterion** charges each parameter a penalty that grows with
the sample size, and the smallest value picks the model. For a Gaussian model with [[ML4T_A3_0001]]
states over [[ML4T_A3_0002]] series the parameter count is the initial distribution, the transition
matrix, the means and the covariances.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
The criterion's answer and the choice made here are not the same, and the reason is worth
stating rather than hiding. A criterion computed in sample rewards any structure the model
can fit, and on a long return series more states always find more volatility clustering to
describe. Whether those extra states are regimes a person could act on is a different
question that the criterion does not ask.

The rest of this notebook uses two states, on the grounds that calm and stressed is the
distinction the features are for and that a two-state fit is the one whose labels stay
interpretable when the model is refitted. That is a judgement about what the feature is
for, and it is stated so a reader can disagree with it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
Sorting by variance is what makes the table above readable, and it is the step most
easily skipped. Without it the row labeled zero would be whichever state the optimizer
happened to number first, so the same column computed in two windows could carry opposite
meanings and a model reading it across a refit would learn nothing.

The hard state above is the argmax of the **filtered** probabilities rather than the
model's own [[ML4T_A3_0001]], which runs the Viterbi algorithm over the whole sequence and
therefore reads the future. Two ways of labeling the same sessions, one of which is a
feature.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0026-p000

~~~~~~markdown
## The same difference, on real data
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0029-p000

~~~~~~markdown
The two agree for most of the sample and disagree exactly where a feature would be used:
at the edges of a stressed period, where the smoothed reading has already turned and the
filtered one has not. The last line is the number to carry: on that share of sessions the
two readings would put the market in different states, and a backtest built on the
smoothed column gets those sessions right for free.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0030-p000

~~~~~~markdown
# Part 4: the columns

Four features come out of a fitted model, and they are different kinds of thing. The
probability changes every session. The transition probabilities and the expected duration
they imply are properties of the fit, so they change only when the model is refitted. The
entropy of the state distribution is the model's own statement about how sure it is,
which is the uncertainty feature [[ML4T_A3_0001]] is about, available here for
free.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0033-p000

~~~~~~markdown
The expected duration follows from the diagonal of the transition matrix and nothing
else: a state the model leaves with probability [[ML4T_A3_0001]] each session lasts [[ML4T_A3_0002]] sessions on
average. It takes exactly as many distinct values as there are states, so as a column it
is the state label wearing a unit, and it is worth carrying only where the model is
refitted often enough for the diagonal to move.

The entropy is the column with the most to say. It is near zero when the filtered
probability is close to zero or one and at its maximum when the model cannot tell, so it
marks the sessions on which the regime feature should not be trusted. A model given both
the probability and its entropy can learn to ignore the first when the second is high.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
# Part 5: a second model of the same idea

**Markov switching autoregression** describes the same picture with a different mechanism.
Instead of a state that emits observations, it fits an autoregression whose variance, and
optionally whose coefficients, switch between regimes. It is estimated by maximum
likelihood rather than by expectation-maximization, and it produces the same two readings.

Fitting both is worth the cell it costs, because agreement between two differently
specified models is much better evidence that a regime is in the data than either one's
own confidence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
## Where the four readings agree

Four statements about the same sessions: the two rules from Part 1, the hidden Markov
model's filtered probability, and the switching model's. They are not measuring the same
thing. The index threshold reads an option market's expectation, the moving average reads
a trend, and the two fitted models read the size of recent moves. Agreement between them
is informative and disagreement is not an error in any of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
# Part 6: regime without a model

[[ML4T_A3_0001]] supplies indicators that classify a regime from price
structure alone, by fixed rules. They are deterministic, need no fitting, and are
available the same session. What they classify is a trend regime rather than a volatility
regime, so they answer a different question from the models above and the overlap between
them is a measurement rather than a validation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0042-p000

~~~~~~markdown
The agreement rate is the number to ignore. The two labels flag very different shares of
the sample, so most of their agreement is both saying no, and a rate above a half here
means almost nothing.

The last three lines are the ones with content, and they are worth reading twice. The two
labels co-occur *less* often than they would if they were unrelated.

The classifier's -1 is worth naming precisely before that number is read: it is the
range-bound class, fired when the ADX and choppiness rules agree that price is not
trending. It says nothing about direction and nothing about the size of the moves, and a
choppy market can have large ones. The two labels therefore measure different properties,
and how far their overlap falls short of independence is a result about this sample
rather than something the definitions require. On another sample it could go the other
way.

That is a reason to carry both rather than either. One says how large the moves are and
the other says whether they are trending; a conditioning rule usually wants each
separately, and a single label that has collapsed them into one is the thing to avoid.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>
