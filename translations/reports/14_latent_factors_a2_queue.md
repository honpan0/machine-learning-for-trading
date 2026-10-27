# 14_latent_factors｜A2 翻譯工作清單

- Pack 總數：12；待翻譯：12；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| A | 待翻譯 | `01_pca_equity_sectors` | 001 | 0/27 | 9469 | [pack_001.md](../work/14_latent_factors/01_pca_equity_sectors/packs/pack_001.md) |
| A | 待翻譯 | `01_pca_equity_sectors` | 002 | 0/2 | 2461 | [pack_002.md](../work/14_latent_factors/01_pca_equity_sectors/packs/pack_002.md) |
| B | 待翻譯 | `02_eigenportfolios` | 001 | 0/29 | 9099 | [pack_001.md](../work/14_latent_factors/02_eigenportfolios/packs/pack_001.md) |
| A | 待翻譯 | `02_eigenportfolios` | 002 | 0/10 | 5660 | [pack_002.md](../work/14_latent_factors/02_eigenportfolios/packs/pack_002.md) |
| B | 待翻譯 | `03_yield_curve_decomposition` | 001 | 0/21 | 9124 | [pack_001.md](../work/14_latent_factors/03_yield_curve_decomposition/packs/pack_001.md) |
| B | 待翻譯 | `03_yield_curve_decomposition` | 002 | 0/4 | 2487 | [pack_002.md](../work/14_latent_factors/03_yield_curve_decomposition/packs/pack_002.md) |
| A | 待翻譯 | `04_ipca` | 001 | 0/15 | 5269 | [pack_001.md](../work/14_latent_factors/04_ipca/packs/pack_001.md) |
| B | 待翻譯 | `05_rp_pca` | 001 | 0/13 | 5890 | [pack_001.md](../work/14_latent_factors/05_rp_pca/packs/pack_001.md) |
| A | 待翻譯 | `06_conditional_autoencoder` | 001 | 0/29 | 7771 | [pack_001.md](../work/14_latent_factors/06_conditional_autoencoder/packs/pack_001.md) |
| A | 待翻譯 | `07_stochastic_discount_factor` | 001 | 0/30 | 8103 | [pack_001.md](../work/14_latent_factors/07_stochastic_discount_factor/packs/pack_001.md) |
| B | 待翻譯 | `08_supervised_autoencoder` | 001 | 0/19 | 5302 | [pack_001.md](../work/14_latent_factors/08_supervised_autoencoder/packs/pack_001.md) |
| B | 待翻譯 | `09_case_study_insights` | 001 | 0/19 | 6271 | [pack_001.md](../work/14_latent_factors/09_case_study_insights/packs/pack_001.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 14_latent_factors --report-only
```
