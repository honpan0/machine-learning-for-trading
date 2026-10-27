# 05_synthetic_data｜A2 翻譯工作清單

- Pack 總數：19；待翻譯：19；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| B | 待翻譯 | `00_classical_simulation` | 001 | 0/15 | 8780 | [pack_001.md](../work/05_synthetic_data/00_classical_simulation/packs/pack_001.md) |
| B | 待翻譯 | `00_classical_simulation` | 002 | 0/16 | 9452 | [pack_002.md](../work/05_synthetic_data/00_classical_simulation/packs/pack_002.md) |
| A | 待翻譯 | `00_classical_simulation` | 003 | 0/19 | 8966 | [pack_003.md](../work/05_synthetic_data/00_classical_simulation/packs/pack_003.md) |
| B | 待翻譯 | `01_timegan` | 001 | 0/23 | 9018 | [pack_001.md](../work/05_synthetic_data/01_timegan/packs/pack_001.md) |
| B | 待翻譯 | `01_timegan` | 002 | 0/3 | 3826 | [pack_002.md](../work/05_synthetic_data/01_timegan/packs/pack_002.md) |
| B | 待翻譯 | `02_tailgan_tail_risk` | 001 | 0/28 | 9120 | [pack_001.md](../work/05_synthetic_data/02_tailgan_tail_risk/packs/pack_001.md) |
| A | 待翻譯 | `03_sigcwgan_signatures` | 001 | 0/11 | 8402 | [pack_001.md](../work/05_synthetic_data/03_sigcwgan_signatures/packs/pack_001.md) |
| B | 待翻譯 | `03_sigcwgan_signatures` | 002 | 0/33 | 9550 | [pack_002.md](../work/05_synthetic_data/03_sigcwgan_signatures/packs/pack_002.md) |
| B | 待翻譯 | `03_sigcwgan_signatures` | 003 | 0/4 | 3636 | [pack_003.md](../work/05_synthetic_data/03_sigcwgan_signatures/packs/pack_003.md) |
| A | 待翻譯 | `04_gtgan_irregular` | 001 | 0/16 | 8263 | [pack_001.md](../work/05_synthetic_data/04_gtgan_irregular/packs/pack_001.md) |
| B | 待翻譯 | `04_gtgan_irregular` | 002 | 0/23 | 8910 | [pack_002.md](../work/05_synthetic_data/04_gtgan_irregular/packs/pack_002.md) |
| B | 待翻譯 | `04_gtgan_irregular` | 003 | 0/1 | 1013 | [pack_003.md](../work/05_synthetic_data/04_gtgan_irregular/packs/pack_003.md) |
| A | 待翻譯 | `05_diffusion_ts` | 001 | 0/24 | 9933 | [pack_001.md](../work/05_synthetic_data/05_diffusion_ts/packs/pack_001.md) |
| A | 待翻譯 | `05_diffusion_ts` | 002 | 0/16 | 9387 | [pack_002.md](../work/05_synthetic_data/05_diffusion_ts/packs/pack_002.md) |
| A | 待翻譯 | `05_diffusion_ts` | 003 | 0/5 | 3639 | [pack_003.md](../work/05_synthetic_data/05_diffusion_ts/packs/pack_003.md) |
| A | 待翻譯 | `06_llm_tabular_great` | 001 | 0/18 | 8836 | [pack_001.md](../work/05_synthetic_data/06_llm_tabular_great/packs/pack_001.md) |
| B | 待翻譯 | `06_llm_tabular_great` | 002 | 0/5 | 4433 | [pack_002.md](../work/05_synthetic_data/06_llm_tabular_great/packs/pack_002.md) |
| A | 待翻譯 | `07_dp_gan` | 001 | 0/22 | 9057 | [pack_001.md](../work/05_synthetic_data/07_dp_gan/packs/pack_001.md) |
| A | 待翻譯 | `07_dp_gan` | 002 | 0/3 | 3157 | [pack_002.md](../work/05_synthetic_data/07_dp_gan/packs/pack_002.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 05_synthetic_data --report-only
```
