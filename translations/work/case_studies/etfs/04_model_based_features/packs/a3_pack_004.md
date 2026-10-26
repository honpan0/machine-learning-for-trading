# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/04_model_based_features.ipynb；A3 Pack 004；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0026-p001

~~~~~~markdown

Ten reference ETFs are transformed rather than all hundred. These series are shared across the
panel like the regime features - every ETF receives the same ten columns - and they are chosen
to span the asset classes the universe covers, so that a model has a broad-market, a
small-cap, an international, a rates, a credit, a commodity and a property series to read.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p001>>>
<<<ML4T-ZH-END:c0026-p001>>>

### c0029-p000

~~~~~~markdown
### Did the chosen orders reach stationarity?

The claim that these orders leave a usable series is testable, so it is tested rather than
asserted. The augmented Dickey-Fuller test asks whether a series has a unit root - whether it
wanders without returning - and a small p-value is evidence that it does not. The comparison
that matters is against the untransformed log price, which should fail the test comprehensively.

The test runs on the development history only. Reading the holdout to decide whether a
transform works is the use the holdout is held back from, even for a transform that fits
nothing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
### C.3 Conditional volatility from a GARCH(1,1) model

**GARCH(1,1)** models the variance of a return series as evolving rather than fixed: each
session's variance is a weighted blend of a long-run level, the previous session's squared
surprise, and the previous session's variance. The two weights are what get estimated, and the
sum of them says how persistent volatility is - the closer to one, the longer a shock takes to
decay out of the forecast.

Unlike the regime model this one is fitted per ETF, because volatility is exactly the property
that differs across assets on a given session. It is what gives the output table a column that
varies across the cross-section, which is what a model ranking assets needs.

The fit-then-filter pattern is what keeps each value causal, and the schedule is what makes
that true at every position rather than only after a fold's training window. Coefficients are
estimated on the returns up to the start of a block, frozen, and the variance recursion is run
forward over that block; the next block re-estimates on everything up to *its* start. Past the
holdout boundary nothing is re-estimated and the last pre-holdout coefficients carry the rest.

An ETF pays the burn-in out of its own history, so a fund that launched recently carries no
conditional volatility for its first two years and one with less history than the burn-in
carries none at all. Those funds are named rather than counted, because a fund missing from
this feature changes what the column covers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
Each ETF is an independent walk, so they are spread across processes. Within one walk the
blocks are sequential - each refit reads everything before it - and each [[ML4T_A3_0001]] fit is
single-threaded, so parallelising anywhere else buys nothing. A fork context is named rather
than left to the default, because Python 3.14 defaults to forkserver, which re-imports the
parent module and cannot reach a function defined in a notebook kernel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
The same two properties are asserted here, per ETF: nothing was estimated from a session
inside the holdout, and every ETF's first emitted value falls after it had paid its burn-in.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
### The property, tested rather than described

All of section A reduces to one claim: deleting the observations after a session does not move
that session's value. It is checked here on one ETF, by cutting its return series and walking
the shortened one, and the cut lands **inside** a block rather than on a refit boundary. That
is the part worth being careful about. A cut on a boundary leaves every retained block with
exactly the prefix it had, so the two walks agree whatever the recursion inside a block does;
only a cut inside one asks whether an emitted value moves when the rest of its own block
arrives. That is the question [[ML4T_A3_0001]]'s result object answers wrongly, which is why the
recursion is the shared helper's.

The shared driver carries the same check as a unit test over a synthetic series
([[ML4T_A3_0002]]); doing it here as well is what says this notebook's own
configuration of it holds, on real returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000

~~~~~~markdown
### Figure F1: the schedule that was run

Both walks are done, so this draws what they did rather than what they were configured to do.
For each model the pale bar is the burn-in it paid before emitting anything and the dark bar is
where every entity it covers is emitting; the ticks on the regime row are the sessions its
parameters were estimated through, one per estimate that converged. The volatility model is
fitted per ETF and each ETF pays its own burn-in, so its row has a third segment between the
earliest and the latest first emission, where some ETFs are emitting and others are still in
their burn-in.

The dashed line is the holdout boundary. No tick falls to the right of it, which is the freeze:
the holdout is emitted from the last estimate made before it. The thin amber bars underneath
are the fold validation windows a later notebook selects rows by; they no longer decide which
parameters a row carries, which is what one dark bar spanning all of them says.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
## D. What refitting moves

The schedule re-estimates both models many times over the history, on windows that grow rather
than roll, so each estimate differs from the previous one by whatever the newest block of
sessions added. Whether that is much or little is the question the cadence answers to:
parameters that barely move would say a slower schedule would have cost nothing, and
parameters that swing are a warning about any feature depending on them.

The quantity plotted is the persistence of each model, against the session its parameters were
estimated through. These are two different kinds of number and they are not comparable to each
other, which is why they are in separate panels.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>
