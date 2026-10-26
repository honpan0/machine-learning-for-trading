# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/09_xai_limitations.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# XAI Limitations: Explanation Instability

**Chapter 12, Section 12.5**: Model Explainability with SHAP

## Purpose
This notebook demonstrates critical limitations of model explanations
that practitioners must understand before relying on SHAP for
downstream decisions (feature pruning, risk allocation, reporting).

## Learning Objectives
- Identify explanation instability: similar predictions with different SHAP profiles
- Demonstrate the Rashomon effect across model families (GBM vs Random Forest)
- Understand when SHAP attributions reflect model-specific fitting, not data truth

## Cross-References
- **Section 12.5**: Rashomon effect, explanation multiplicity
- **Related**: [[ML4T_A3_0001]] (SHAP fundamentals), [[ML4T_A3_0002]] (UQ)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## 2. Load Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## 3. Demonstration 1: Similar Predictions, Different Explanations

Two samples with nearly identical predictions can have entirely
different SHAP profiles: the model arrived at the same answer
through different reasoning paths.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0011-p000

~~~~~~markdown
**Interpretation**: SHAP explanations are not unique. The same prediction
can be reached through different feature contribution paths. When instability
pairs are found, the top-three SHAP contributors can differ completely even
when predictions agree to within fractions of a percent. For production
deployment, report confidence intervals on feature importance rather than
point estimates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
## 4. Demonstration 2: Rashomon Effect Across Model Families

Models with similar predictive performance can attribute predictions
to different features. We compare three LightGBM seeds plus a
Random Forest to demonstrate cross-architecture disagreement.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0016-p000

~~~~~~markdown
Read the table by the spread rather than by any single value. The three
LightGBM seeds differ only in their random seed, and they span a wider range
than separates any of them from the Random Forest, which lands inside that
span. Changing the seed therefore moves validation IC by more than changing
the model family does here. The Rashomon point holds in either direction:
similar predictive performance, different feature attributions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
**Interpretation**: Features that rank highly across all four models
(both GBM and Random Forest) are more likely to reflect genuine data
structure. Features that only one family highlights may reflect
architecture-specific fitting patterns. When SHAP attributions
drive downstream decisions, validate across model specifications.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
## 5. Stakeholder Guidance

| Audience | Recommended Explanation | Key Caveat |
|----------|------------------------|------------|
| Risk Manager | SHAP summary plot | Correlation [[ML4T_A3_0001]] causation |
| Trader | Feature importance rank | May vary with retraining |
| Regulator | Model documentation | Include confidence intervals |
| Quant Researcher | Full SHAP + interactions | Check stability across seeds |
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
## 6. Key Takeaways

1. **Explanation instability**: Samples with similar predictions can have
   different top SHAP contributors: the same output is reachable through
   different feature-contribution paths.

2. **Rashomon effect**: Models with different architectures or random seeds
   attribute predictions to different features, so SHAP explanations reflect
   model-specific fitting patterns, not ground truth about the data.

3. **Best practices**: Report confidence intervals on feature importance,
   check stability across random seeds and model architectures, and never
   claim SHAP proves causation.

**Next**: See [[ML4T_A3_0001]] for SHAP fundamentals and drift detection,
or Section 12.5 in the chapter text for the theoretical framework.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>
