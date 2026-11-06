# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/04_model_based_features.ipynb；A3 Pack 008；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0075-p000

~~~~~~markdown
---

## E. Combining the three and writing the file

The three models produce values at three different levels of detail. ARIMA gives one
value per product and session. The spectral features give one per product and session
too. The regime features give one per session, shared by every product because the model
reads the book as a whole.

They are brought onto one grid: every combination of session, product and contract
position that the price file contains, up to the last session the holdout covers. A left
join then attaches each family where it has a value and leaves an empty cell where it does
not, so nothing is invented and no row is dropped for lack of a feature.

The grid is written once and keyed [[ML4T_A3_0001]]. Repeating it once per
period, with the period number in the key, would hand a model training on one period the
features estimated on that period's training sessions. Every fitted value here is bounded by
its own estimation block instead, and it is the same value whichever period later selects the
row.

**The upper bound has to be stated, and a per-period grid would not need it.** A period bounds
its own rows, so such an artifact reaches no further than the last period's evaluation window
whatever the price file holds. The walks run over each entity's whole history instead, so the
grid would otherwise extend to the end of the price file - and a session
past [[ML4T_A3_0002]] is one no stage in this case study evaluates, carrying a feature value
from an estimate frozen before the holdout opened. On this panel the two dates coincide
and the filter removes nothing, which is exactly why it is a filter and an assertion
rather than a sentence: a price file refreshed past the holdout would otherwise widen the
artifact silently.
~~~~~~

<<<ML4T-ZH-BEGIN:c0075-p000>>>
<<<ML4T-ZH-END:c0075-p000>>>

### c0080-p000

~~~~~~markdown
How much of the grid each feature actually fills. The share is taken over the whole grid,
which spans every session of the price calendar and is far larger than any one model's
reach, so these are not quality scores - they are a check that each family landed where it
was supposed to and nowhere else.

ARIMA's share is the lowest of the three, for two reasons that are both by construction:
the burn-in at the front of each product's history, which no forecast can cover, and the
products excluded for having too little history before the holdout. **This table
understates what the models downstream receive**, because most of the grid it counts over
is outside any evaluation window. The count printed under section C.1 is the one to read
for that: it is taken against the product-sessions each window quotes.

The spectral features fill nearly everything, since they run over the full history. The
regime features fill every session from the end of their burn-in on, one value repeated
across that session's products.
~~~~~~

<<<ML4T-ZH-BEGIN:c0080-p000>>>
<<<ML4T-ZH-END:c0080-p000>>>

### c0082-p000

~~~~~~markdown
### What is written, and what the checks before the write are for

[[ML4T_A3_0001]] and [[ML4T_A3_0002]] are two separate files
and neither reads the other. The model notebooks in Chapter 11 onward read both and join
them on [[ML4T_A3_0003]].

Three properties are asserted before the file is written. The key is unique, so no join
downstream can silently multiply rows. There is no period column, because a value here is
bounded by its own estimation block and a period id would have nothing to record. And the
columns carrying a value on a holdout-dated row are exactly the ones allowed to.

That last check is the one worth reading closely. ARIMA and the hidden Markov model
estimate parameters, and their holdout-dated cells have to be **filled**: a holdout
evaluation downstream reads them, and both models reach them the same way, by carrying
the last pre-boundary estimate across the window frozen. An empty holdout is the failure
this check exists to catch, and asserting "no fitted column has a holdout-dated value"
would be satisfied perfectly by a run that emitted nothing there.

The other direction is not checkable from the frame and never was: the weights are not in
it. What bounds them is the shape of the call, plus [[ML4T_A3_0004]] and the holdout cut on
[[ML4T_A3_0005]]'s input, both asserted where they are applied in C.1 and C.3.

The spectral features estimate nothing and read a backward-looking window, so their
holdout-dated cells are filled too, and there is nothing about them that could have come
from the future.
~~~~~~

<<<ML4T-ZH-BEGIN:c0082-p000>>>
<<<ML4T-ZH-END:c0082-p000>>>

### c0084-p000

~~~~~~markdown
### The file, and the fingerprint written beside it

The file is written with a small companion file recording four things: a **content
fingerprint** of the feature values, the number of rows, the columns that form the key,
and the fingerprint of the prices these features were built from.

The fingerprint is what makes the record useful rather than decorative. A registry that
notes only which feature *names* a model was trained on cannot tell two training runs
apart when the names are identical and the values are not - which is exactly the
situation after the code that computes them changes. Two runs whose values differ get
different fingerprints even when the row count and the column names match, so a
training run downstream can record which version of the features it read.

The upstream fingerprint is taken over the raw settlement prices, because section C
recomputes carry from them. This notebook reads no other case study file for a feature
value, and the record says so.

What goes in beside it is the estimation schedule, which is what a reader needs in order to
know what an emitted value means. A fold geometry in its place would answer "which window is
period 3", a question this file does not pose.
~~~~~~

<<<ML4T-ZH-BEGIN:c0084-p000>>>
<<<ML4T-ZH-END:c0084-p000>>>
