# 12_gradient_boosting｜A2 翻譯工作清單

- Pack 總數：16；待翻譯：16；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| B | 待翻譯 | `01_ensemble_foundations` | 001 | 0/14 | 6689 | [pack_001.md](../work/12_gradient_boosting/01_ensemble_foundations/packs/pack_001.md) |
| B | 待翻譯 | `02_gbm_comparison` | 001 | 0/21 | 8962 | [pack_001.md](../work/12_gradient_boosting/02_gbm_comparison/packs/pack_001.md) |
| A | 待翻譯 | `02_gbm_comparison` | 002 | 0/3 | 3293 | [pack_002.md](../work/12_gradient_boosting/02_gbm_comparison/packs/pack_002.md) |
| A | 待翻譯 | `03_dl_vs_gbm` | 001 | 0/19 | 9519 | [pack_001.md](../work/12_gradient_boosting/03_dl_vs_gbm/packs/pack_001.md) |
| B | 待翻譯 | `04_optuna_tuning` | 001 | 0/19 | 9631 | [pack_001.md](../work/12_gradient_boosting/04_optuna_tuning/packs/pack_001.md) |
| B | 待翻譯 | `04_optuna_tuning` | 002 | 0/1 | 483 | [pack_002.md](../work/12_gradient_boosting/04_optuna_tuning/packs/pack_002.md) |
| B | 待翻譯 | `05_cross_library_hpo` | 001 | 0/22 | 6470 | [pack_001.md](../work/12_gradient_boosting/05_cross_library_hpo/packs/pack_001.md) |
| A | 待翻譯 | `06_optuna_multi_asset` | 001 | 0/16 | 5044 | [pack_001.md](../work/12_gradient_boosting/06_optuna_multi_asset/packs/pack_001.md) |
| A | 待翻譯 | `07_hpo_comparison` | 001 | 0/19 | 8328 | [pack_001.md](../work/12_gradient_boosting/07_hpo_comparison/packs/pack_001.md) |
| A | 待翻譯 | `08_shap_analysis` | 001 | 0/26 | 8835 | [pack_001.md](../work/12_gradient_boosting/08_shap_analysis/packs/pack_001.md) |
| A | 待翻譯 | `09_xai_limitations` | 001 | 0/10 | 3578 | [pack_001.md](../work/12_gradient_boosting/09_xai_limitations/packs/pack_001.md) |
| B | 待翻譯 | `10_shap_nlp_sentiment` | 001 | 0/10 | 4709 | [pack_001.md](../work/12_gradient_boosting/10_shap_nlp_sentiment/packs/pack_001.md) |
| B | 待翻譯 | `11_conformal_gbm` | 001 | 0/32 | 9733 | [pack_001.md](../work/12_gradient_boosting/11_conformal_gbm/packs/pack_001.md) |
| A | 待翻譯 | `11_conformal_gbm` | 002 | 0/1 | 1190 | [pack_002.md](../work/12_gradient_boosting/11_conformal_gbm/packs/pack_002.md) |
| A | 待翻譯 | `12_case_study_insights` | 001 | 0/34 | 9911 | [pack_001.md](../work/12_gradient_boosting/12_case_study_insights/packs/pack_001.md) |
| B | 待翻譯 | `12_case_study_insights` | 002 | 0/11 | 2740 | [pack_002.md](../work/12_gradient_boosting/12_case_study_insights/packs/pack_002.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 12_gradient_boosting --report-only
```
