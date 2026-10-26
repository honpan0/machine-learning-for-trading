# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11d_stochastic_discount_factor.ipynb；A3 Pack 002；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤

## 待翻譯英文單元

### c0010-p000

~~~~~~markdown
## 2. Binding the declarations to the data

A menu entry says which estimator to fit. It does not say which fund-date pairs have both a
feature row and a label, or where the walk-forward folds fall. **Resolving** a request goes and
finds that: it reads the label, feature and macro files, computes the fold boundaries from the
walk-forward parameters in [[ML4T_A3_0001]], and works out the exact set of rows each fit is
expected to predict. It fits nothing, so the plan can be read before any training starts.

Four things to check in it:

- **[[ML4T_A3_0002]], [[ML4T_A3_0003]] and [[ML4T_A3_0004]] agree across the rows.** They are
  the width of the networks' input, the number of funds in the cross-section, and the fund-date
  pairs to be predicted. A row that differs is a label measured on a different sample.
- **[[ML4T_A3_0005]] is the same on both rows**, and equals the number of walk-forward splits
  [[[ML4T_A3_0006]]](05_evaluation.ipynb) established.
- **[[ML4T_A3_0007]] and [[ML4T_A3_0008]] bracket the development sample.** The held-out tail
  is scored once, at the end of the case study; any of it visible here would mean it had been
  used to choose something.
- **[[ML4T_A3_0009]]** is the resolved schedule length, and it is the number to multiply by the row
  count to get the candidate models this notebook is about to create.

Each row also carries a [[ML4T_A3_0010]]: the identity of that computation, derived from
everything that can change its result. [[[ML4T_A3_0011]]](../RUN_LOG.md#identity) sets out what goes
into one and what follows from it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
The plan is also where a short population is visible. A run that fitted fewer labels than the
menu declares would still print an IC table and still register its rows; what it would not do is
announce the gap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### The macro contract, read back from what was resolved

The discount factor takes macro context, and the point-in-time question that raises is not
rhetorical: a macro series as it reads today is not what it read on a decision date years ago,
because the agencies that publish these numbers revise them. Training on the revised series would
let the model condition on information nobody had.

The contract below is read out of the resolved specification rather than restated here, so it is
what actually entered the identity:

- **[[ML4T_A3_0001]]** says the values are ALFRED *initial releases* - each series as it was first
  published, not as it now reads.
- **[[ML4T_A3_0002]]** and **[[ML4T_A3_0003]]** say a value dated *t* becomes usable on *t+1*
  and is then carried backward, so a same-day close cannot reach a same-day decision.
- **[[ML4T_A3_0004]]** is where the panel begins, which is set by the last series to start rather
  than the first.
- **[[ML4T_A3_0005]]** is the content of the macro values each fold actually saw. It is
  inside the training identity, so a macro panel that changed underneath would register as a
  different model rather than overwriting this one.

**What this does not buy.** The financial feature matrix still contains yield-curve variables
built from finalized FRED series, so the run as a whole is not a vintage-clean live estimate. The
macro contract covers the macro context and nothing else, and the feature matrix's exact content
is pinned by the modeling-input digest rather than by a release policy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## 3. Fitting the population

[[ML4T_A3_0001]] runs every resolved request. For one request it walks the folds, and on
each one:

1. takes the fund-dates inside that fold's training window, together with the macro values that
   were available on those dates,
2. trains the unconditional stage, then the conditional one that adds the macro context, by
   gradient descent on the pricing errors, writing the weights to disk at each declared save,
3. applies each saved set of weights to the validation dates to get each fund's exposure to the
   discount factor there, and turns that into a predicted return.

Step 3 is what makes one training run produce several results. The fold predictions are
concatenated into one series per checkpoint covering the whole validation period, and each
becomes its own registered prediction set with its own identity.

**What the call publishes is a population**: a named, immutable list of the prediction sets it
will produce, computed from the resolved specifications and written down before the first fit.
Afterwards every member must exist and be complete, which is what makes the downstream comparison
well defined - [[[ML4T_A3_0002]]](14_backtest.ipynb) backtests this population, not whatever
predictions happen to be in the registry - and it is why a configuration that raises fails the
whole call rather than publishing a population one member short.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0016-p001

~~~~~~markdown

[[ML4T_A3_0001]] names the population hash this run replaces. A population is the set of
prediction identities, so anything that moves a training identity - a changed macro panel as
much as a changed epoch schedule - produces a different set under the same name, and the
registry refuses to write it without being told which snapshot it supersedes. It is empty here
because [[ML4T_A3_0002]] has one generation and this run is it: there is no earlier
snapshot to replace. It stays empty on a re-run too, because reproducing a member list already
published under that name is not a replacement. Fill it in when you have changed something that
moves an identity and want the new set to take the name; the error raised on the attempt tells
you which hash to name. A reduced-scale run passes it empty whatever the default is: a
population produced under a reduction is thrown away with the workspace it was written to, so it
has no lineage to extend.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p001>>>
<<<ML4T-ZH-END:c0016-p001>>>
