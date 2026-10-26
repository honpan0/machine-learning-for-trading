# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/09_dl_lstm.ipynb；A3 Pack 002；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Overfitting → 過度擬合
- Correlation → 相關性

## 待翻譯英文單元

### c0012-p000

~~~~~~markdown
## 4. Fitting the population

[[ML4T_A3_0001]] fits every resolved request: for one request it walks the folds, saves a
checkpoint at each declared epoch interval, scores each checkpoint on that fold's validation
dates, and registers every checkpoint as its own prediction set. What the call publishes is a
**population** - a named, immutable list of the prediction sets it produced - which is what
[[[ML4T_A3_0002]]](14_backtest.ipynb) resolves rather than a query it composes itself.

**There is one identity builder, and the runner owns it.** A notebook that built its own lookup
specification to decide whether a configuration was already fitted would have to agree with the
runner's field for field, and a field the runner later makes identity-bearing - the device, say -
would break that agreement silently: the model trains, registers under the fuller identity, and
the notebook reports its own checkpoints incomplete. Nothing here derives an identity, so nothing
here can disagree.

**A second run fits nothing.** Every identity is re-derived from the inputs, the registry already
holds the matching rows and the saved weights, and [[ML4T_A3_0003]] in the line below counts what came
back from store rather than from a GPU.

[[ML4T_A3_0004]] names the population snapshot this run replaces, which the registry
refuses the write without once a name has been published before. The declaration below retires
the generation fitted while the sequence runner's identity was a hash of its source file, before
that became a declared version.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0012-p001

~~~~~~markdown

The hash is committed source, so it is wrong for every reader: [[ML4T_A3_0001]] is gitignored and a
clean clone has no [[ML4T_A3_0002]] table to hold it. [[ML4T_A3_0003]] resolves the
declaration against the registry in hand and withholds it where there is nothing to retire, so
one committed value is right for the author's refit and the reader's first run alike.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p001>>>
<<<ML4T-ZH-END:c0012-p001>>>

### c0014-p000

~~~~~~markdown
## 5. What came out, and which checkpoints are comparable

One row per epoch checkpoint. The **information coefficient** is the daily one: on each
validation date, rank the funds by the model's prediction, rank them by the return they went on
to earn, correlate the two rankings, and average that daily correlation over the validation
period. Zero is no relationship.

**The daily IC is read from [[ML4T_A3_0001]] rather than from the catalog, and that is not a
stylistic choice.** The research catalog exposes [[ML4T_A3_0002]] and [[ML4T_A3_0003]] side by side, but they
do not describe the same quantity: [[ML4T_A3_0004]] is the mean over folds, while [[ML4T_A3_0005]] counts the
dates behind [[ML4T_A3_0006]], which the catalog does not carry. Pairing the two that the catalog
offers reports a coverage count for a statistic it was not computed from. Until the catalog
carries the daily IC, this cell reads it where it lives.

[[ML4T_A3_0007]] is how many validation dates produced a defined correlation, and it decides which
rows are comparable with each other. A network that has settled into predicting nearly the same
value for every fund on a date gives that date no spread to rank, and the date drops out of the
average - which makes a collapsed checkpoint look better by being scored on fewer, easier days.
[[ML4T_A3_0008]] marks the checkpoints measured on every date the label offers, and selection
happens only among those.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
Every full-coverage checkpoint is published as a candidate; this notebook chooses none of them.
Scanning the grid for the highest validation IC is the sequence-model analogue of early
stopping, and it is read here as a diagnostic - it says where in training the signal peaked, and
it anchors the learning curve and the per-fold table below. It is not the pipeline's selection:
IC ranks nothing anywhere in this pipeline, and a configuration is chosen on validation backtest
Sharpe in the evaluation stage, from the whole grid published here. The holdout is not touched.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## 6. The learning curve

Validation IC at each epoch checkpoint. The peak is amber; any checkpoint left unpublished
for partial coverage is copper. A curve that rises and then falls is the model fitting and then
overfitting the validation folds; a flat one says the epoch count was never the binding choice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## 7. Against the flat-feature baselines

The peak checkpoint against the linear and gradient-boosting leaders. This is the comparison the
notebook exists to make: whether reading the history as a sequence adds anything over handing
the same history to a model as columns.

The comparison only means anything if the three numbers describe the same rows, and section 2
explained why that is not guaranteed. Matching date counts would not be enough: sequence
eligibility drops the warm-up rows a flat model keeps, so the same date can carry a different
cross-section in each family, and each family's stored IC is computed over its own sample.

So the stored numbers are not what the chart plots. The three prediction sets are intersected
on their exact [[ML4T_A3_0001]] keys and the daily rank IC is recomputed on the rows all
three share. That is a different and smaller sample than any family's own, which is the point:
it is the only sample on which the three are one comparison rather than three.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## 8. Is the average stable across time?

The reported IC is an average over folds, and an average can be positive while most of its terms
are not. The per-fold breakdown is what separates a model with a weak but consistent edge from
one whose mean is carried by a single fold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## 9. What to notice
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>
