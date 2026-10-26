# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/04_model_based_features.ipynb；A3 Pack 002；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Cross-sectional → 橫斷面
- Volatility → 波動率

## 待翻譯英文單元

### c0006-p000

~~~~~~markdown
### The data these models run on

Before fitting anything, look at the panel. The universe is a hundred exchange-traded funds
assembled to cover the asset classes a diversified investor can reach through them, and the
download configuration that defines it groups them into nine categories. The table below is
that grouping, with the history each category actually has on disk.

Two things in it decide what happens further down. The panel is **unbalanced**: several of
these funds launched well after the sample begins, so the number quoting on a session grows
through the history. A fund also has to pay the volatility model's burn-in out of its own
history, so the late arrivals carry no conditional volatility for their first two years. And
the categories are **not equally sized**: a cross-sectional ranking over this universe is
dominated by equities, because more than half the names are equity funds of one kind or
another.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## B. What the schedule has to respect

The schedule replaces the fold as the thing that bounds an estimate, and only two boundaries
are left for it to respect.

The first is the **holdout**. A coefficient re-estimated on holdout sessions is a parameter
estimated on the holdout however causal the recursion around it looks, so past the holdout
boundary each walk stops refitting and keeps applying the last estimate it made before the
holdout opened. The holdout still gets values - it has to, or the final notebook would have no
features to score - and they are computed from holdout returns through pre-holdout parameters.
That is the [[ML4T_A3_0001]] argument below.

The second is the **burn-in**. The first sessions of the history pay for the first estimate and
carry no value. The market-level regime model pays it once at the start of the panel; the
per-ETF volatility model has each fund pay it out of its own history, so a fund that launched
in 2018 carries no conditional volatility until 2020. The cell after the folds measures what
the first costs and the write-out measures the second.

The folds themselves are still resolved here, for two reasons that no longer include deciding
which parameters a row gets. They fix which sessions the evaluation at the end may read, and
they are what the burn-in is measured against.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### What the burn-in costs the earliest folds

The regime and differenced-price features are one series each, so their burn-in is paid once,
at the very start of the price history. Where that lands relative to the folds is not a free
choice: the folds roll a ten-year training window back one year at a time, so the oldest of
them begins on the second session of the panel, and no burn-in at all fits before it.

Two different things follow, and only one of them is a defect. A **validation** session with no
feature value is one the evaluation scores against a column that is silently filled with the
feature's mean, so it has to be impossible - and it is, by a wide margin, because the earliest
validation window opens roughly seven years into the sample. A **training** session with no
value is the burn-in itself, showing up as fewer usable rows at the far left of the oldest
folds; that is what a burn-in costs and it is reported rather than asserted away. The count is
printed below, per fold.

The volatility model is not covered by either statement and cannot be: its burn-in is per ETF,
and a fund that launched inside a fold window has no way to pay it earlier. What that costs is
reported against the written table in section E.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The folds themselves, for reference: the windows a later notebook selects rows by, and the
windows the evaluation at the end of this notebook is allowed to read.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## C. One section per model

Three models are fitted, and each of the three sections below answers the same three questions
in the same order: what does this model infer, on what schedule were its parameters estimated,
and what stops the inference from reading forward.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
### C.1 Regime states from a hidden Markov model

A **hidden Markov model** assumes the series is generated by a small number of unobserved
states, that the state on one session depends only on the state on the one before, and that
each state emits observations from its own distribution. Fitting it means recovering those
distributions and the probabilities of moving between states; using it means asking, for each
session, how likely each state is.

Two states are used here, and the observation on each session is a pair: that session's log
return and the realized volatility of the recent past. Two states is a modelling choice, not
a fitted one - the model is not asked how many regimes there are, it is asked to split the
market into a calm state and a stressed one and to say which is more likely on each day.

The model is fitted on the broad market rather than on each ETF. A regime in this sense is a
property of the market as a whole, not of one fund, so one hundred separately fitted models
would be one hundred noisy estimates of the same thing; and a state that means "stressed"
for one ETF and "stressed" for another only supports a cross-sectional comparison if the two
were defined identically. Every ETF therefore inherits the same regime probability on a given
session, which also means this feature can only help a model by interacting with something
that does vary across assets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>
