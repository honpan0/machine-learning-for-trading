# 07_defining_the_learning_task｜A2 翻譯工作清單

- Pack 總數：22；待翻譯：22；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| B | 待翻譯 | `01_data_quality_diagnostics` | 001 | 0/25 | 9183 | [pack_001.md](../work/07_defining_the_learning_task/01_data_quality_diagnostics/packs/pack_001.md) |
| B | 待翻譯 | `01_data_quality_diagnostics` | 002 | 0/10 | 4640 | [pack_002.md](../work/07_defining_the_learning_task/01_data_quality_diagnostics/packs/pack_002.md) |
| A | 待翻譯 | `02_preprocessing_pipeline` | 001 | 0/36 | 9764 | [pack_001.md](../work/07_defining_the_learning_task/02_preprocessing_pipeline/packs/pack_001.md) |
| B | 待翻譯 | `02_preprocessing_pipeline` | 002 | 0/4 | 1286 | [pack_002.md](../work/07_defining_the_learning_task/02_preprocessing_pipeline/packs/pack_002.md) |
| B | 待翻譯 | `03_label_methods` | 001 | 0/25 | 9562 | [pack_001.md](../work/07_defining_the_learning_task/03_label_methods/packs/pack_001.md) |
| A | 待翻譯 | `03_label_methods` | 002 | 0/14 | 8458 | [pack_002.md](../work/07_defining_the_learning_task/03_label_methods/packs/pack_002.md) |
| A | 待翻譯 | `03_label_methods` | 003 | 0/1 | 1753 | [pack_003.md](../work/07_defining_the_learning_task/03_label_methods/packs/pack_003.md) |
| B | 待翻譯 | `04_maximum_favorable_adverse_excursion` | 001 | 0/22 | 9419 | [pack_001.md](../work/07_defining_the_learning_task/04_maximum_favorable_adverse_excursion/packs/pack_001.md) |
| B | 待翻譯 | `04_maximum_favorable_adverse_excursion` | 002 | 0/6 | 3840 | [pack_002.md](../work/07_defining_the_learning_task/04_maximum_favorable_adverse_excursion/packs/pack_002.md) |
| A | 待翻譯 | `05_signal_evaluation` | 001 | 0/20 | 8822 | [pack_001.md](../work/07_defining_the_learning_task/05_signal_evaluation/packs/pack_001.md) |
| B | 待翻譯 | `05_signal_evaluation` | 002 | 0/12 | 6952 | [pack_002.md](../work/07_defining_the_learning_task/05_signal_evaluation/packs/pack_002.md) |
| A | 待翻譯 | `05_signal_evaluation` | 003 | 0/10 | 6870 | [pack_003.md](../work/07_defining_the_learning_task/05_signal_evaluation/packs/pack_003.md) |
| B | 待翻譯 | `06_ic_inference` | 001 | 0/15 | 8948 | [pack_001.md](../work/07_defining_the_learning_task/06_ic_inference/packs/pack_001.md) |
| A | 待翻譯 | `06_ic_inference` | 002 | 0/1 | 1427 | [pack_002.md](../work/07_defining_the_learning_task/06_ic_inference/packs/pack_002.md) |
| A | 待翻譯 | `07_multiple_testing` | 001 | 0/13 | 9130 | [pack_001.md](../work/07_defining_the_learning_task/07_multiple_testing/packs/pack_001.md) |
| B | 待翻譯 | `07_multiple_testing` | 002 | 0/14 | 8224 | [pack_002.md](../work/07_defining_the_learning_task/07_multiple_testing/packs/pack_002.md) |
| B | 待翻譯 | `07_multiple_testing` | 003 | 0/3 | 2615 | [pack_003.md](../work/07_defining_the_learning_task/07_multiple_testing/packs/pack_003.md) |
| B | 待翻譯 | `08_causal_sanity_checks` | 001 | 0/11 | 7959 | [pack_001.md](../work/07_defining_the_learning_task/08_causal_sanity_checks/packs/pack_001.md) |
| A | 待翻譯 | `08_causal_sanity_checks` | 002 | 0/12 | 9276 | [pack_002.md](../work/07_defining_the_learning_task/08_causal_sanity_checks/packs/pack_002.md) |
| A | 待翻譯 | `08_causal_sanity_checks` | 003 | 0/15 | 7910 | [pack_003.md](../work/07_defining_the_learning_task/08_causal_sanity_checks/packs/pack_003.md) |
| A | 待翻譯 | `08_causal_sanity_checks` | 004 | 0/2 | 2771 | [pack_004.md](../work/07_defining_the_learning_task/08_causal_sanity_checks/packs/pack_004.md) |
| A | 待翻譯 | `10_ml4t_library_ecosystem` | 001 | 0/20 | 6216 | [pack_001.md](../work/07_defining_the_learning_task/10_ml4t_library_ecosystem/packs/pack_001.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 07_defining_the_learning_task --report-only
```
