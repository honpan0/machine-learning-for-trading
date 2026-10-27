# 13_dl_time_series｜A2 翻譯工作清單

- Pack 總數：25；待翻譯：25；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| A | 待翻譯 | `01_core_architectures` | 001 | 0/9 | 8749 | [pack_001.md](../work/13_dl_time_series/01_core_architectures/packs/pack_001.md) |
| B | 待翻譯 | `01_core_architectures` | 002 | 0/12 | 8658 | [pack_002.md](../work/13_dl_time_series/01_core_architectures/packs/pack_002.md) |
| B | 待翻譯 | `01_core_architectures` | 003 | 0/9 | 8217 | [pack_003.md](../work/13_dl_time_series/01_core_architectures/packs/pack_003.md) |
| B | 待翻譯 | `01_core_architectures` | 004 | 0/1 | 673 | [pack_004.md](../work/13_dl_time_series/01_core_architectures/packs/pack_004.md) |
| B | 待翻譯 | `02_nbeats_interpretable` | 001 | 0/12 | 8897 | [pack_001.md](../work/13_dl_time_series/02_nbeats_interpretable/packs/pack_001.md) |
| A | 待翻譯 | `02_nbeats_interpretable` | 002 | 0/9 | 8073 | [pack_002.md](../work/13_dl_time_series/02_nbeats_interpretable/packs/pack_002.md) |
| B | 待翻譯 | `03_great_debate` | 001 | 0/15 | 9634 | [pack_001.md](../work/13_dl_time_series/03_great_debate/packs/pack_001.md) |
| B | 待翻譯 | `03_great_debate` | 002 | 0/6 | 6919 | [pack_002.md](../work/13_dl_time_series/03_great_debate/packs/pack_002.md) |
| A | 待翻譯 | `04_transformers` | 001 | 0/17 | 8863 | [pack_001.md](../work/13_dl_time_series/04_transformers/packs/pack_001.md) |
| A | 待翻譯 | `04_transformers` | 002 | 0/7 | 5973 | [pack_002.md](../work/13_dl_time_series/04_transformers/packs/pack_002.md) |
| B | 待翻譯 | `05_tcn` | 001 | 0/17 | 8852 | [pack_001.md](../work/13_dl_time_series/05_tcn/packs/pack_001.md) |
| B | 待翻譯 | `06_tsmixer` | 001 | 0/16 | 8178 | [pack_001.md](../work/13_dl_time_series/06_tsmixer/packs/pack_001.md) |
| A | 待翻譯 | `07_mamba_ssm` | 001 | 0/17 | 9020 | [pack_001.md](../work/13_dl_time_series/07_mamba_ssm/packs/pack_001.md) |
| A | 待翻譯 | `07_mamba_ssm` | 002 | 0/3 | 3449 | [pack_002.md](../work/13_dl_time_series/07_mamba_ssm/packs/pack_002.md) |
| B | 待翻譯 | `08_cnn_image_encoding` | 001 | 0/21 | 8762 | [pack_001.md](../work/13_dl_time_series/08_cnn_image_encoding/packs/pack_001.md) |
| B | 待翻譯 | `08_cnn_image_encoding` | 002 | 0/2 | 2461 | [pack_002.md](../work/13_dl_time_series/08_cnn_image_encoding/packs/pack_002.md) |
| A | 待翻譯 | `09_foundation_models` | 001 | 0/14 | 8546 | [pack_001.md](../work/13_dl_time_series/09_foundation_models/packs/pack_001.md) |
| A | 待翻譯 | `09_foundation_models` | 002 | 0/6 | 6501 | [pack_002.md](../work/13_dl_time_series/09_foundation_models/packs/pack_002.md) |
| A | 待翻譯 | `10_uncertainty` | 001 | 0/22 | 9122 | [pack_001.md](../work/13_dl_time_series/10_uncertainty/packs/pack_001.md) |
| A | 待翻譯 | `10_uncertainty` | 002 | 0/15 | 8806 | [pack_002.md](../work/13_dl_time_series/10_uncertainty/packs/pack_002.md) |
| B | 待翻譯 | `10_uncertainty` | 003 | 0/3 | 3822 | [pack_003.md](../work/13_dl_time_series/10_uncertainty/packs/pack_003.md) |
| A | 待翻譯 | `11_library_landscape` | 001 | 0/22 | 9768 | [pack_001.md](../work/13_dl_time_series/11_library_landscape/packs/pack_001.md) |
| B | 待翻譯 | `11_library_landscape` | 002 | 0/5 | 4157 | [pack_002.md](../work/13_dl_time_series/11_library_landscape/packs/pack_002.md) |
| B | 待翻譯 | `12_case_study_insights` | 001 | 0/27 | 9727 | [pack_001.md](../work/13_dl_time_series/12_case_study_insights/packs/pack_001.md) |
| A | 待翻譯 | `12_case_study_insights` | 002 | 0/5 | 2061 | [pack_002.md](../work/13_dl_time_series/12_case_study_insights/packs/pack_002.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 13_dl_time_series --report-only
```
