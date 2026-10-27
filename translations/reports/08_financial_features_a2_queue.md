# 08_financial_features｜A2 翻譯工作清單

- Pack 總數：15；待翻譯：15；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| A | 待翻譯 | `01_price_volume_features` | 001 | 0/23 | 8721 | [pack_001.md](../work/08_financial_features/01_price_volume_features/packs/pack_001.md) |
| B | 待翻譯 | `01_price_volume_features` | 002 | 0/22 | 9485 | [pack_002.md](../work/08_financial_features/01_price_volume_features/packs/pack_002.md) |
| A | 待翻譯 | `01_price_volume_features` | 003 | 0/6 | 3228 | [pack_003.md](../work/08_financial_features/01_price_volume_features/packs/pack_003.md) |
| A | 待翻譯 | `02_microstructure_features` | 001 | 0/14 | 8489 | [pack_001.md](../work/08_financial_features/02_microstructure_features/packs/pack_001.md) |
| B | 待翻譯 | `02_microstructure_features` | 002 | 0/7 | 5951 | [pack_002.md](../work/08_financial_features/02_microstructure_features/packs/pack_002.md) |
| A | 待翻譯 | `03_structural_cross_instrument_features` | 001 | 0/27 | 9470 | [pack_001.md](../work/08_financial_features/03_structural_cross_instrument_features/packs/pack_001.md) |
| B | 待翻譯 | `03_structural_cross_instrument_features` | 002 | 0/5 | 3557 | [pack_002.md](../work/08_financial_features/03_structural_cross_instrument_features/packs/pack_002.md) |
| B | 待翻譯 | `04_fundamentals_macro_calendar` | 001 | 0/24 | 9716 | [pack_001.md](../work/08_financial_features/04_fundamentals_macro_calendar/packs/pack_001.md) |
| A | 待翻譯 | `04_fundamentals_macro_calendar` | 002 | 0/6 | 2887 | [pack_002.md](../work/08_financial_features/04_fundamentals_macro_calendar/packs/pack_002.md) |
| B | 待翻譯 | `05_feature_selection` | 001 | 0/22 | 9177 | [pack_001.md](../work/08_financial_features/05_feature_selection/packs/pack_001.md) |
| B | 待翻譯 | `05_feature_selection` | 002 | 0/1 | 1312 | [pack_002.md](../work/08_financial_features/05_feature_selection/packs/pack_002.md) |
| B | 待翻譯 | `06_robustness_sensitivity` | 001 | 0/19 | 8132 | [pack_001.md](../work/08_financial_features/06_robustness_sensitivity/packs/pack_001.md) |
| A | 待翻譯 | `07_event_studies` | 001 | 0/21 | 9806 | [pack_001.md](../work/08_financial_features/07_event_studies/packs/pack_001.md) |
| B | 待翻譯 | `07_event_studies` | 002 | 0/1 | 833 | [pack_002.md](../work/08_financial_features/07_event_studies/packs/pack_002.md) |
| A | 待翻譯 | `case_study_feature_summary` | 001 | 0/9 | 6228 | [pack_001.md](../work/08_financial_features/case_study_feature_summary/packs/pack_001.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 08_financial_features --report-only
```
