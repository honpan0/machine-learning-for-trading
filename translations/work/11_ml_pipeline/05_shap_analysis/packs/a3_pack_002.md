# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/05_shap_analysis.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Feature → 特徵

## 待翻譯英文單元

### c0033-p000

~~~~~~markdown
Sign violations are not necessarily wrong - Ridge splits credit across
correlated features, so a feature may flip sign if a correlated partner
absorbs its effect. But persistent violations across folds warrant investigation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
### Feature Dependence

For a linear model, the SHAP dependence plot is linear by construction
([[ML4T_A3_0001]]). We show it here to establish
the pattern - Ch12 extends this to tree models where dependence reveals
threshold effects and non-linear interactions.

The feature plotted is the highest-importance one that actually varies on this
test fold. A feature that is near-constant over the window has near-constant
attribution too, and its dependence plot reduces to a single point.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
## Individual Forecast Explanation

SHAP waterfall plots decompose a *single* prediction into feature contributions.
Starting from the expected value (population mean prediction), each feature
pushes the prediction up (red) or down (blue) by its SHAP value.

We show two examples: one where the model made a large positive prediction
that turned out correct, and one where a large prediction was wrong.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0040-p000

~~~~~~markdown
The waterfall plots show the same model making confident calls for different
reasons. Comparing the feature attributions gives a first hint at what
distinguishes correct from incorrect predictions - the systematic analysis
below makes this rigorous.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0041-p000

~~~~~~markdown
## Decision-Relevant Predictions: Right vs Wrong

Not all predictions are equally important. In a portfolio context, predicted
return magnitude maps directly to position size ([[ML4T_A3_0001]]), so
predictions with large [[ML4T_A3_0002]] are **decision-relevant** - they drive the
biggest bets and have the greatest impact on PnL.

We isolate the highest-conviction predictions, the top band by [[ML4T_A3_0003]] set
in the cell below, and split them into:

- **Right**: [[ML4T_A3_0004]] - the model was
  confidently correct
- **Wrong**: [[ML4T_A3_0005]] - the model was
  confidently incorrect

Comparing their SHAP profiles reveals which features *systematically* mislead
the model at the moments that matter most.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
Read the right/wrong split before reading anything below it. If the model is
wrong on more than half of its largest bets, the SHAP comparison that follows
is a diagnosis of what misleads it, not evidence that it has skill where it is
most confident. Attribution explains what a model did; it says nothing about
whether the model was right, and a confident wrong prediction has just as
clean a decomposition as a confident correct one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
### SHAP Profiles: Right vs Wrong

We compute the mean |SHAP| per feature for each group. Features where the
"wrong" group has disproportionately high SHAP are candidates for improvement:
the model relied on them heavily, but they led it astray.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0046-p000

~~~~~~markdown
A ratio above one means the feature contributed more to the mistakes than to
the successes: the model leaned on it hardest when it was wrong. If volume or
cross-asset features dominate the top of this list,
they may be unreliable as standalone predictors and could benefit from
interaction terms or non-linear modeling in Ch12.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0047-p000

~~~~~~markdown
### Visualizing the Difference

The bar chart compares mean |SHAP| for the top features, side by side for
right (correct) and wrong (incorrect) high-magnitude predictions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
**Interpretation**: Features where the "wrong" bar substantially exceeds the "right"
bar are the model's weak points at high conviction - it relied on them heavily when
making its biggest mistakes. These features are candidates for re-engineering
(e.g., adding interaction terms) or non-linear modeling in Ch12.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0050-p000

~~~~~~markdown
### Signed SHAP: Direction of Influence

Mean |SHAP| shows *magnitude*, but the *sign* matters too. A feature that
consistently pushes predictions in the wrong direction is more problematic
than one that adds noise symmetrically.

We compute mean signed SHAP for each group to see directional bias.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0053-p000

~~~~~~markdown
**Interpretation**: Large positive direction differences mean the feature pushed wrong
predictions upward more than right ones - a systematic directional bias at the moments
that matter most. Features with large negative differences show the opposite pattern.
Both directions suggest the feature's signal is unreliable under high conviction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0054-p000

~~~~~~markdown
### Concentration Risk

When a single feature dominates the total SHAP attribution, the prediction
hinges on one input, which is a fragile basis for a trade. The cell below flags
any prediction where one feature accounts for more than the concentration
threshold it sets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0056-p000

~~~~~~markdown
Read the flagged count against the mean and 95th-percentile shares printed above. A
threshold that flags nothing is telling you the threshold is wrong for this model, not that
the risk is absent: if the largest single feature's share never approaches the cut, the cut
cannot fire whatever the model does.

That is a property of these coefficients on this data rather than something the penalty
guarantees. Ridge shrinks every coefficient and leaves all of them non-zero, which spreads
attribution, but it does not bound any one feature's share of a row - a single large
coefficient can still dominate a prediction.

So where the count comes back empty, the useful moves are to raise the aggregation to the
top few features rather than the top one, or to compare the distribution against another
model rather than against a fixed cut. And check it per fold: in a fold dominated by a
regime change the same diagnostic can flip and flag many predictions, which makes this part
of a standing pipeline rather than a one-time exercise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>
