# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/04_model_based_features.ipynb；A3 Pack 003；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤
- Standard deviation → 標準差

## 待翻譯英文單元

### c0013-p000

~~~~~~markdown
The figure draws the five evaluation windows and the gap in front of each. Read it as a
picture of what section F screens over, not of what bounds a fit - nothing here bounds a
fit any more. The gap between each pair of bars is the purge, sized to the label horizon
so that no training session's outcome reaches into the window a model is scored on, and
no bar crosses into the shaded holdout.

The estimation schedule is drawn separately, once the series each model reads has been
built: ARIMA at the end of C.1 and the regime chain at the end of C.3, each against its
own series, because their burn-ins are paid on series that begin at different dates.

**The file this notebook writes carries rows dated inside the holdout, and that is
deliberate.** A holdout evaluation downstream needs a feature value on those sessions.
What must not reach into the holdout is an estimate, and neither model makes one there:
both stop re-estimating at the last session before the boundary and carry that estimate
across frozen. Section E prints, column by column, what is populated where.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
## The input all three models read: carry

Carry is how far the front-month contract settles above the next one along, as a
fraction of the front price, scaled by twelve:

[[ML4T_A3_0001]]

where the superscript is the contract position. A trader holding the front month has to
replace it with the next contract before it expires, and that gap is what the
replacement earns or costs. It is positive in **backwardation**, where the nearer
contract is the dearer one, and negative in **contango**, where it is the cheaper one.

**The twelve is a scale factor, not an annual rate.** It would turn a one-month spread
into a yearly one, and the four energy curves in this universe do list a contract every
month. The other twenty-six are on quarterly or irregular cycles, so for them twelve is
the wrong multiple for an annual rate and the number is not one. It is the same constant
for every product on every date, so it changes no ranking and no z-score; what it does
not deliver is a level that means the same thing on a Treasury curve as on a crude one.

Two derived series come out of it. **Smoothed carry** is carry averaged over
[[ML4T_A3_0002]] sessions, which removes the daily settlement noise the models would
otherwise fit. **The carry z-score** expresses that smoothed level as the number of
standard deviations it sits from its own average over the previous
[[ML4T_A3_0003]] sessions, so that gold in dollars and corn in cents can be
compared on one scale.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0015-p001

~~~~~~markdown

[[[ML4T_A3_0001]]](03_financial_features.ipynb) writes the same z-score under the
name [[ML4T_A3_0002]], but with one row per contract rather than one per product. The
models here need one series per product, so the same definition is recomputed in that
shape from the raw prices - both windows read from the same configuration - rather than
reshaped out of that file. This is why the file this notebook writes records the raw
prices as its input and no other feature file.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p001>>>
<<<ML4T-ZH-END:c0015-p001>>>

### c0017-p000

~~~~~~markdown
---

## C. The three models

Each subsection below states what the model infers, where its parameters are allowed to
come from, and ends with an assertion that runs - not a comment claiming the
window held, but a check that fails the notebook if it did not.

### C.1 ARIMA: what carry does next

Term structure changes gradually, so today's carry z-score carries information about
tomorrow's. ARIMA is the standard model for that kind of series: it writes the next
value as a weighted sum of recent values and of recent forecast errors, and estimates
the weights. Its three orders say how many of each go in - [[ML4T_A3_0001]] past values, [[ML4T_A3_0002]] past
errors, and [[ML4T_A3_0003]] differences taken first if the series drifts rather than reverting.

The orders are declared in [[ML4T_A3_0004]] rather than searched for at each refit, and the
cell below sets out the measurement behind that. Only the weights are re-estimated on the
schedule; [[ML4T_A3_0005]], [[ML4T_A3_0006]] and [[ML4T_A3_0007]] stay put, so the forecast means the same thing in every block.
Seasonal terms play no part here, because the seasonality this case study cares about is
measured directly in C.2.

**Why every value it emits is a forecast and not a fit.** One call walks each product's
whole history a session at a time: at each step the model sees the history up to that
session and predicts the next one. What is emitted for a session is therefore the
prediction made before the session happened, and the weights behind it are re-estimated
every [[ML4T_A3_0008]] steps. There are no fitted-in-place values anywhere in the
output. The walk cannot begin until there is enough history to estimate from, so the
first [[ML4T_A3_0009]] sessions of each product's history get no value.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0017-p001

~~~~~~markdown

The two features are the forecast itself, [[ML4T_A3_0001]], and what it missed,
[[ML4T_A3_0002]] - the realised z-score minus the forecast. A large residual says
carry moved in a way its own recent path did not imply.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p001>>>
<<<ML4T-ZH-END:c0017-p001>>>

### c0018-p000

~~~~~~markdown
Every product with enough history goes into one call, as a long frame keyed by product
and date. The library walks those series together, spread across cores. It is the same
walk-forward routine as
[[[ML4T_A3_0001]]](../../09_model_based_features/10_uncertainty_features.ipynb),
and the two settings that govern it - the burn-in and the refit cadence - are the ones
[[ML4T_A3_0002]] declares under [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
The carry frame carries [[ML4T_A3_0001]], so a bound written as a Python date is cast to the
column's own dtype; that is what makes an inclusive upper bound cover the last session.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
