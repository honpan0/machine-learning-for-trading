# 11_ml_pipeline｜A2 翻譯工作清單

- Pack 總數：17；待翻譯：17；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| B | 待翻譯 | `01_ols_inference` | 001 | 0/16 | 9494 | [pack_001.md](../work/11_ml_pipeline/01_ols_inference/packs/pack_001.md) |
| B | 待翻譯 | `01_ols_inference` | 002 | 0/11 | 9313 | [pack_002.md](../work/11_ml_pipeline/01_ols_inference/packs/pack_002.md) |
| A | 待翻譯 | `01_ols_inference` | 003 | 0/1 | 1793 | [pack_003.md](../work/11_ml_pipeline/01_ols_inference/packs/pack_003.md) |
| A | 待翻譯 | `02_regularization_paths` | 001 | 0/20 | 9322 | [pack_001.md](../work/11_ml_pipeline/02_regularization_paths/packs/pack_001.md) |
| A | 待翻譯 | `02_regularization_paths` | 002 | 0/16 | 7505 | [pack_002.md](../work/11_ml_pipeline/02_regularization_paths/packs/pack_002.md) |
| B | 待翻譯 | `03_logistic_classification` | 001 | 0/35 | 9531 | [pack_001.md](../work/11_ml_pipeline/03_logistic_classification/packs/pack_001.md) |
| B | 待翻譯 | `03_logistic_classification` | 002 | 0/12 | 4384 | [pack_002.md](../work/11_ml_pipeline/03_logistic_classification/packs/pack_002.md) |
| B | 待翻譯 | `04_nested_cv_hpo` | 001 | 0/26 | 8796 | [pack_001.md](../work/11_ml_pipeline/04_nested_cv_hpo/packs/pack_001.md) |
| B | 待翻譯 | `04_nested_cv_hpo` | 002 | 0/1 | 1527 | [pack_002.md](../work/11_ml_pipeline/04_nested_cv_hpo/packs/pack_002.md) |
| A | 待翻譯 | `05_shap_analysis` | 001 | 0/25 | 9570 | [pack_001.md](../work/11_ml_pipeline/05_shap_analysis/packs/pack_001.md) |
| B | 待翻譯 | `05_shap_analysis` | 002 | 0/9 | 5750 | [pack_002.md](../work/11_ml_pipeline/05_shap_analysis/packs/pack_002.md) |
| B | 待翻譯 | `06_conformal_prediction` | 001 | 0/12 | 7932 | [pack_001.md](../work/11_ml_pipeline/06_conformal_prediction/packs/pack_001.md) |
| A | 待翻譯 | `06_conformal_prediction` | 002 | 0/17 | 9130 | [pack_002.md](../work/11_ml_pipeline/06_conformal_prediction/packs/pack_002.md) |
| A | 待翻譯 | `06_conformal_prediction` | 003 | 0/1 | 1272 | [pack_003.md](../work/11_ml_pipeline/06_conformal_prediction/packs/pack_003.md) |
| A | 待翻譯 | `07_case_study_insights` | 001 | 0/24 | 9378 | [pack_001.md](../work/11_ml_pipeline/07_case_study_insights/packs/pack_001.md) |
| A | 待翻譯 | `07_case_study_insights` | 002 | 0/6 | 2977 | [pack_002.md](../work/11_ml_pipeline/07_case_study_insights/packs/pack_002.md) |
| A | 待翻譯 | `08_ml_backtest_intro` | 001 | 0/11 | 6360 | [pack_001.md](../work/11_ml_pipeline/08_ml_backtest_intro/packs/pack_001.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 11_ml_pipeline --report-only
```
