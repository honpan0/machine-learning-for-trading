# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/04_model_based_features.ipynb；A3 Pack 005；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Cross-sectional → 橫斷面
- Volatility → 波動率

## 待翻譯英文單元

### c0037-p000

~~~~~~markdown
The figure below is what a filtered regime probability looks like, drawn against the
series it was inferred from so the two can be read together. The top panel is the
cross-sectional funding the model observes; the bottom is the probability it assigns
to the stressed state, on validation settlements only, so every value shown comes from
a model fitted on earlier bars. Read the bottom panel for how the probability behaves,
not for where it happens to be high: it moves between its bounds within a day rather
than drifting, which is the signature of a filter that revises hard on each new
observation and is what makes the feature a state indicator rather than a trend.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0040-p000

~~~~~~markdown
## D. Do the fitted parameters move as the window rolls?

Both models are re-estimated on a schedule that runs the length of the history, and that
choice is only worth its cost if the estimates actually move. Parameters that come back
identical from one refit to the next would say the schedule bought nothing and a single
early fit would have done. Parameters that drift say something more useful and more
uncomfortable: the feature means a slightly different thing at different points in the
sample, and a model pooling the whole series is pooling quantities calibrated differently.

This is the question the old per-fold design could only answer at fold resolution - three
estimates, one per fold, with no way to tell a genuine drift from the difference between
two overlapping ten-year windows. The schedule gives one estimate every
[[ML4T_A3_0001]] settlements, so the coefficient path is a series and can be read as
one.

The two models get a chart each, because their units do not compare: a recursion
coefficient is dimensionless and a regime duration is counted in settlements.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0040-p001

~~~~~~markdown

What is plotted for the volatility model is **persistence**, [[ML4T_A3_0001]] - the fraction of a variance shock still present one settlement later, with
the asymmetry term at half weight because it is active on the half of settlements that
fall. Persistence is the quantity to read rather than any single coefficient, because
the coefficients trade off against each other: one can rise while another falls and
leave the decay rate unchanged, so a claim of stability read off [[ML4T_A3_0002]] alone can be
wrong in either direction. The model is fitted per perpetual, so the median across
symbols is drawn with the interquartile range behind it. For the regime model the
quantity is the expected run length of each state, in settlements.

Each perpetual is refit on its own settlements, because its walk starts from its own
listing, so the refit dates do not line up across symbols. Taking the cross-section at
each date a fit happened would therefore compare a changing subset of perpetuals - and a
date where one symbol refit would show a median of one model and an interquartile range
of zero, which reads as agreement rather than as a group of one. Each symbol's most
recent estimate is carried forward onto a common timeline instead, so every point is the
cross-section of every perpetual that had a fitted model by then.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p001>>>
<<<ML4T-ZH-END:c0040-p001>>>

### c0044-p000

~~~~~~markdown
**What to read off the two charts.** Three things, in order.

Whether the **median persistence path touches the dashed line at one**. A fit at that
boundary is censored there: it cannot distinguish "extremely persistent" from
"integrated", and while it sits on the line the individual coefficients are not
separately identified. This is why persistence is plotted rather than [[ML4T_A3_0001]] or
[[ML4T_A3_0002]] alone - either can move a long way while the decay rate does not.

Whether the **interquartile band is wide or narrow**. A wide band means the perpetuals
disagree about how persistent variance is, which is what makes a per-symbol fit worth
its cost. A band that collapses would say a single pooled fit would serve.

Whether the **paths move at all**. If they are flat, the refit schedule bought nothing
and its only remaining justification is that a schedule is what makes the feature causal
in the first place - which is reason enough, but worth knowing. If they drift, the
feature is calibrated differently at different points in the sample, and a model pooling
the history should know that.

The vertical line on both charts is where re-estimation stops. Every settlement to the
right of it carries the last estimate made to its left, which is what keeps the holdout
out of the parameters while still giving it values.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0045-p000

~~~~~~markdown
## E. Combine and emit

The two models produce differently shaped output. The volatility model gives one row per
perpetual and settlement; the regime model gives one row per settlement, because it
describes the market rather than any single contract. Combining them means broadcasting
the market-level probabilities across the symbols quoting at each settlement.

**The key is [[ML4T_A3_0001]] and nothing else.** Under the previous design it was
[[ML4T_A3_0002]], because the same settlement carried a different value in
every fold - which is what a fold-frozen fit produces and what made the file several
times larger than the panel it describes. A settlement now has one value, computed once,
and whichever fold a model notebook later assigns that row to does not change it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>
