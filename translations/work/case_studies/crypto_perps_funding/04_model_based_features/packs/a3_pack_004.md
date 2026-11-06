# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/04_model_based_features.ipynb；A3 Pack 004；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0027-p000

~~~~~~markdown
One derived column follows. The conditional volatility is a level, and a level is hard
to compare across perpetuals whose typical volatility differs by a factor of three, so
a z-score against each symbol's own trailing window says whether *this* symbol is
currently agitated relative to its own recent norm. It is computed within [[ML4T_A3_0001]],
over the one continuous conditional-volatility series each perpetual now has. Under the
previous design it had to be computed within [[ML4T_A3_0002]], and the trailing window
restarted at every fold boundary; there are no boundaries left for it to restart at.
Its own warm-up - [[ML4T_A3_0003]] settlements after the model's burn-in - stays
null rather than being filled.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
### C.2 Funding regimes, market-wide

The second model asks a question about the market rather than about a symbol. Funding
on a perpetual is the periodic payment between long and short holders that keeps the
contract near spot; when the whole universe is paying heavily in one direction, and
disagreeing about how much, the market is in a different state from a quiet week. A
**hidden Markov model** formalizes exactly that: it assumes an unobserved state that
switches between a small number of values, with a probability of switching estimated
from the data, and it assumes what you observe is drawn from a distribution that
depends on which state you are in.

The observation here is two-dimensional per settlement: the cross-sectional mean of
realized funding across the perpetuals quoting at that settlement, and its
cross-sectional standard deviation, both in basis points. Mean gives the direction the
market is paying, dispersion gives how much the contracts disagree. Two states is what
the notebook fits, and the state with the larger fitted dispersion is named the
stressed one - the naming has to be a property of the fit and not an accident of
labelling, because the algorithm returns the states in an arbitrary order and the same
regime can come back as state 0 in one fold and state 1 in the next.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
Two shared helpers do the work that must be identical everywhere it is used.
[[ML4T_A3_0001]] runs the forward recursion that gives [[ML4T_A3_0002]]
rather than the smoothed posterior a library returns by default, and
[[ML4T_A3_0003]] puts the states in dispersion order so state 0 means the same
thing at every refit. That second helper matters more under a schedule than it did under
a fold, not less: expectation-maximization labels its states arbitrarily, so without a
fixed ordering the feature would swap meaning several hundred times across the history
instead of twice. They live in [[ML4T_A3_0004]] because a regime feature
is only comparable across estimates if every notebook orders its states the same way, and
because the forward recursion reaches a private method of the modelling library that
should be named in one place rather than several.

[[ML4T_A3_0005]] is the third, and it is the search. Expectation-maximization reaches
a local optimum, so this notebook has always fitted from ten starting points at every
refit and kept the one with the highest training likelihood. That loop used to live here;
it now lives in the shared module, because [[ML4T_A3_0006]] and [[ML4T_A3_0007]] each wrote the same loop
for themselves and three copies of a selection rule is three places for it to drift.

What changed underneath it is where a restart begins. The fits are now initialized from a
k-means partition of the training window rather than by the modelling library's own
scheme, which is a starting point the data chose rather than one the seed did. The
restarts stay: measured on [[ML4T_A3_0008]]' panel through this same estimator, ten of them give ten
distinct log-likelihoods, so the better start does not make the search redundant.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0031-p001

~~~~~~markdown

The fit is also held to a single compute thread, inside the shared helper rather than
here. The k-means partial sums are reduced across threads and floating-point addition is
not associative, so the starting means depend on how the work happened to be split and
expectation-maximization carries that into the transition matrix. Measured on that helper,
five thread counts gave five log-likelihoods and five transition matrices, and this
notebook's stage-04 artifact was one of three that hashed differently run to run because
of it. A seed fixes the draw and not the schedule; pinning the pool fixes both.

The convergence threshold is declared in [[ML4T_A3_0001]] rather than left to the
library. This notebook fits at [[ML4T_A3_0002]], a hundred times tighter than hmmlearn's default,
and so does [[ML4T_A3_0003]]; [[ML4T_A3_0004]] and [[ML4T_A3_0005]] take the default. That difference was
measured on the [[ML4T_A3_0006]] panel through this same estimator rather than argued about: across
twelve refit blocks the two thresholds move the emitted state probability by about
[[ML4T_A3_0007]] on average, by [[ML4T_A3_0008]] at the single worst row, and **change none of 756 emitted
state assignments** at the one-half threshold. Zero flips is the decision result, not a
claim that the columns are identical - this probability is read as a continuous feature
as well as through a threshold, so the small differences are real even where no
classification moves. The declaration is there because two case studies chose the
tighter value deliberately, not because the looser one was shown to be wrong.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p001>>>
<<<ML4T-ZH-END:c0031-p001>>>

### c0032-p000

~~~~~~markdown
The extraction below fits on the fold's training settlements, then runs the forward
recursion over training and validation settlements together. Running it over the
joined stretch is not a shortcut: the filter needs the training observations to arrive
at the state distribution it holds when the validation window opens, and because the
recursion only ever looks backwards, a validation settlement's probability depends on
nothing after it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0035-p000

~~~~~~markdown
The same seal as the volatility model, recomputed from the settlements each regime fit
consumed. There is one series here rather than nineteen, so the schedule is checked
exactly rather than as a bound, and the last estimation window is displayed beside the
holdout boundary it has to precede.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>
