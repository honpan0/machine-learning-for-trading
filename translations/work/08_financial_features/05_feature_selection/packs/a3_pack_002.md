# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/05_feature_selection.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Cluster → 群集
- Clustering → 分群
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0032-p000

~~~~~~markdown
## Selection Pipeline

Applying the steps in sequence: correlation filtering removes obvious
redundancy, clustering reduces each near-duplicate family to a single
representative, and an IC threshold keeps the representatives with predictive
power.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0035-p000

~~~~~~markdown
## Stability Selection via Bootstrap IC

Stability selection asks whether a feature's IC keeps one sign under resampling, or
rests on a few periods. Each bootstrap sample draws rows with replacement and recomputes
the pooled IC. The table reports, per feature, the mean IC across samples, its standard
deviation, their ratio as an information ratio, the share of samples in which the IC came
out positive, and the share that agreed on whichever sign the feature leans to.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0035-p001

~~~~~~markdown

The last of those carries the rule, and its difference from the one before it matters.
Everything upstream ranks on **absolute** IC: the cluster representative is the member
with the largest |IC|, and the IC filter keeps features on |IC| too. A feature with a
reliable negative edge is a feature, and inverting it costs nothing. A threshold on the
share of positive samples would fail exactly those, contradicting the selection that
produced the list. So the cut is on sign consistency, counting strictly positive and
strictly negative samples separately and taking whichever is larger. The sign the table
reports comes from that same pair of counts rather than from the mean IC: a mean can be
dragged negative by a few large samples while most samples are positive, and reporting
the sign that way would print a feature as negative in most samples when it was negative
in only a handful.
[[ML4T_A3_0001]] is declared in the parameters cell and applied
below, so the notebook prints which features clear it rather than describing a cut it
never makes. Applied means applied: the survivors replace [[ML4T_A3_0002]], so the model
fit, the importance analysis, the correlation check, the summary counts and both exported
parquet files all read the narrowed set. A cut that only changes a printed table is a
decoration, and it leaves the exported selection disagreeing with the notebook that
produced it.

> **Caveat**: The bootstrap below samples individual rows (date × symbol),
> pooling across dates. A more rigorous approach bootstraps by *date*
> (block bootstrap), preserving cross-sectional structure. The pooled
> version here is a quick filter; production systems should use
> time-aware resampling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p001>>>
<<<ML4T-ZH-END:c0035-p001>>>

### c0039-p000

~~~~~~markdown
## ML-Based Feature Importance

Beyond IC ranking, ML models identify features with non-linear predictive
power. We fit a quick LightGBM model and compare its feature importance
with the IC rankings above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
**Interpretation**: MDI (Mean Decrease in Impurity) measures how much each
feature reduces prediction error in the tree ensemble. PFI (Permutation
Feature Importance) measures how much shuffling a feature degrades
predictions. Features ranking high in both IC and ML importance are the
strongest candidates for production.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
## Post-Selection Verification
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
The selection is supposed to leave features that are not near-duplicates of each other.
Whether it did is a number, not an assumption: the heatmap below shows every pairwise
correlation among the selected set and the cell prints the largest of them. Read that
against [[ML4T_A3_0001]], which is the only bar the filtering step actually enforced.
A maximum well below the threshold means the clustering removed more redundancy than the
pairwise filter alone would have; a maximum close to it means the surviving set still
contains a pair the filter was content to keep.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
## Selection Summary and Output
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0048-p000

~~~~~~markdown
## Key Takeaways

1. **Cross-sectional IC** is the correct method for factor evaluation, because
   pooled IC conflates time-series drift with predictive power
2. **Correlation filtering** at [[ML4T_A3_0001]] removes obvious redundancy;
   **clustering** catches subtler near-duplicates within feature families
3. **Use average or complete linkage** (not Ward) for correlation distances, because
   Ward assumes Euclidean geometry
4. **BH-FDR with HAC-adjusted p-values** controls false discovery when
   screening many candidates. The p-values fed into BH-FDR come from the
   Newey-West t-statistic on each feature's daily IC series, not the
   i.i.d. t-stat, because daily ICs are serially correlated. Without a
   multiple-testing correction, a share of null features equal to the chosen level
   appears significant at that level by chance alone, which is what FDR_ALPHA both
   sets and corrects for
5. **Bootstrap stability** separates features whose IC keeps one sign under resampling
   from those that depend on a few periods. The sign it keeps need not be positive:
   the selection ranks on |IC| throughout
6. Features ranking high in both IC and ML importance are the strongest
   production candidates

**Next**: [[ML4T_A3_0002]], on parameter sensitivity and
regime-conditional analysis
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>
