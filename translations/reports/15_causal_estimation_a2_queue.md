# 15_causal_estimation｜A2 翻譯工作清單

- Pack 總數：18；待翻譯：18；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| A | 待翻譯 | `01_library_overview` | 001 | 0/14 | 8928 | [pack_001.md](../work/15_causal_estimation/01_library_overview/packs/pack_001.md) |
| B | 待翻譯 | `01_library_overview` | 002 | 0/4 | 4460 | [pack_002.md](../work/15_causal_estimation/01_library_overview/packs/pack_002.md) |
| B | 待翻譯 | `02_dowhy_causal_graph` | 001 | 0/15 | 9503 | [pack_001.md](../work/15_causal_estimation/02_dowhy_causal_graph/packs/pack_001.md) |
| A | 待翻譯 | `02_dowhy_causal_graph` | 002 | 0/18 | 8383 | [pack_002.md](../work/15_causal_estimation/02_dowhy_causal_graph/packs/pack_002.md) |
| A | 待翻譯 | `02_dowhy_causal_graph` | 003 | 0/6 | 5272 | [pack_003.md](../work/15_causal_estimation/02_dowhy_causal_graph/packs/pack_003.md) |
| A | 待翻譯 | `03_econml_dml` | 001 | 0/15 | 9692 | [pack_001.md](../work/15_causal_estimation/03_econml_dml/packs/pack_001.md) |
| B | 待翻譯 | `03_econml_dml` | 002 | 0/10 | 8038 | [pack_002.md](../work/15_causal_estimation/03_econml_dml/packs/pack_002.md) |
| B | 待翻譯 | `04_dml_crypto_regime` | 001 | 0/15 | 8627 | [pack_001.md](../work/15_causal_estimation/04_dml_crypto_regime/packs/pack_001.md) |
| A | 待翻譯 | `04_dml_crypto_regime` | 002 | 0/9 | 6288 | [pack_002.md](../work/15_causal_estimation/04_dml_crypto_regime/packs/pack_002.md) |
| B | 待翻譯 | `05_momentum_causal_trading` | 001 | 0/25 | 8565 | [pack_001.md](../work/15_causal_estimation/05_momentum_causal_trading/packs/pack_001.md) |
| B | 待翻譯 | `06_fed_announcement_bsts` | 001 | 0/18 | 9332 | [pack_001.md](../work/15_causal_estimation/06_fed_announcement_bsts/packs/pack_001.md) |
| B | 待翻譯 | `06_fed_announcement_bsts` | 002 | 0/5 | 3051 | [pack_002.md](../work/15_causal_estimation/06_fed_announcement_bsts/packs/pack_002.md) |
| B | 待翻譯 | `07_tigramite_time_series` | 001 | 0/17 | 5926 | [pack_001.md](../work/15_causal_estimation/07_tigramite_time_series/packs/pack_001.md) |
| A | 待翻譯 | `08_neural_causal_discovery` | 001 | 0/28 | 8418 | [pack_001.md](../work/15_causal_estimation/08_neural_causal_discovery/packs/pack_001.md) |
| A | 待翻譯 | `09_adia_causal_benchmark` | 001 | 0/18 | 8845 | [pack_001.md](../work/15_causal_estimation/09_adia_causal_benchmark/packs/pack_001.md) |
| A | 待翻譯 | `09_adia_causal_benchmark` | 002 | 0/8 | 2713 | [pack_002.md](../work/15_causal_estimation/09_adia_causal_benchmark/packs/pack_002.md) |
| B | 待翻譯 | `10_case_study_insights` | 001 | 0/14 | 7627 | [pack_001.md](../work/15_causal_estimation/10_case_study_insights/packs/pack_001.md) |
| A | 待翻譯 | `11_factor_zoo_validation` | 001 | 0/16 | 6449 | [pack_001.md](../work/15_causal_estimation/11_factor_zoo_validation/packs/pack_001.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 15_causal_estimation --report-only
```
