# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/04_model_based_features.ipynb；A3 Pack 004；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0040-p000

~~~~~~markdown
The moving average [[ML4T_A3_0001]] measures the level against is a fixed-weight backward
window with nothing estimated in it, so it is computed once over each pair's whole
history rather than inside the walk. Taking the same window [[ML4T_A3_0002]] gives
[[ML4T_A3_0003]] means the two columns measure price against one reference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
**The three checks this section rests on, executed.** Each stops the notebook rather than
leaving plausible numbers behind.

*Every value's parameters end before it.* This is the property the section exists for and
the one the old fold-frozen arrangement broke. [[ML4T_A3_0001]] returns the same
[[ML4T_A3_0002]] pairs the walk used, and every emitted index has to fall at or after
the [[ML4T_A3_0003]] of the block it belongs to. Checking the schedule rather than the values is
what makes this an assertion about the estimation channel rather than about the recursion.

*Burn-in coverage, reported rather than hidden.* Each pair's first [[ML4T_A3_0004]]
sessions carry no value, and the cell says which sessions those are and what share of the
oldest window's training rows they cost.

*Forward only.* [[ML4T_A3_0005]] is a recursion, so the value it reports for session
[[ML4T_A3_0006]] must not move when the observations after [[ML4T_A3_0007]] are deleted. This is the distinction
section 2 named as invisible in the emitted numbers: a backward pass would produce a
column of the same shape and range. The truncation runs on the pre-holdout series, the
same boundary every other cell reads its data through.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0045-p000

~~~~~~markdown
## 5. When the Dollar Is Calm and When It Is Turbulent

The second model answers a question about the market as a whole rather than about one
pair. Currency volatility arrives in stretches: months where dollar moves are small and
orderly, then a period where they are not, then back. A **hidden Markov model** is the
standard way to describe that. It assumes the market is always in one of a small number
of unobservable states, that each state produces observations with its own mean and
variance, and that the state persists from one session to the next with a fixed
probability. Two states are configured here, and after fitting they are ordered so that
the one with the larger variance is the turbulent one - a naming rule the fit itself does
not supply, since the two states come back in an arbitrary order every time.

What is emitted is not which state the market was in but how likely each session is to
have been in the turbulent one, computed from the sessions up to that day. A probability
carries the model's uncertainty; a hard label discards it.

The larger-variance state is described as turbulent and nothing more. Variance says how
far the dollar travelled, not which way, so it does not identify the state where
investors are retreating from risk - that would need the direction of the move as well,
and this model is not given it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0046-p000

~~~~~~markdown
The model reads one series: an average dollar return across the seven pairs that have
the dollar on one side of the quote. Those seven are the dollar pairs from the universe
table, and the sign has to be fixed before averaging, because [[ML4T_A3_0001]] rising and
[[ML4T_A3_0002]] rising are opposite moves in the dollar. Both sides are derived from the
declared universe rather than listed here, so a universe change cannot silently drop a
leg of the average.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0048-p000

~~~~~~markdown
The model is given two numbers per session rather than one: the average dollar return
and a rolling standard deviation of it over the window bound above. The return alone
would let the model separate the states only through how far individual sessions
scatter, and the rolling figure states the recent scale directly, which is the quantity
the two states differ in.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
### Reading the Model Forward

The library's own [[ML4T_A3_0001]] answers the question section 2 named as unusable: it
returns the probability of each state given the *whole* series, later sessions included.
The probability given only the sessions up to and including the one being scored comes
from the forward recursion, which [[ML4T_A3_0002]]
implements. It is imported rather than written out here because six notebooks in this
book need the same recursion, and it reaches one library method that is not part of the
public interface - a detail worth carrying in one place rather than six.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
Expectation-maximisation climbs to whichever optimum is nearest its starting point, so
the fit is repeated from several starting points and the highest-likelihood result is
kept. A run whose final step *lowers* the likelihood has not converged, and is discarded
rather than quietly used.

Fixing the starting points is not by itself enough to make this fit reproducible, and
the difference matters because the feature file is identified by a digest of its values.
The initial state means come from a k-means partition of the training sample, and
k-means sums over that sample in parallel. Floating-point addition is not associative,
so the sums depend on how the work happened to be divided across processor threads, and
expectation-maximisation carries that difference forward into the transition matrix and
into every probability the model reports. A seed fixes which starting points are drawn,
not how the arithmetic is scheduled. Holding the fit to a single thread fixes the
schedule too, and it costs seconds here because the series is one column of daily
figures. Measured over three separate runs of this notebook's fit: with the default
thread pool the transition matrix came back different every time; held to one thread it
came back identical every time. The other two models were checked the same way and are
already reproducible across runs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>
