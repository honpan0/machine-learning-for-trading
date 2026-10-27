# 06_strategy_definition｜A2 翻譯工作清單

- Pack 總數：4；待翻譯：4；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| B | 待翻譯 | `01_where_ideas_come_from` | 001 | 0/13 | 9080 | [pack_001.md](../work/06_strategy_definition/01_where_ideas_come_from/packs/pack_001.md) |
| A | 待翻譯 | `02_cv_foundations` | 001 | 0/29 | 9601 | [pack_001.md](../work/06_strategy_definition/02_cv_foundations/packs/pack_001.md) |
| A | 待翻譯 | `02_cv_foundations` | 002 | 0/9 | 4745 | [pack_002.md](../work/06_strategy_definition/02_cv_foundations/packs/pack_002.md) |
| B | 待翻譯 | `03_case_study_overview` | 001 | 0/24 | 7209 | [pack_001.md](../work/06_strategy_definition/03_case_study_overview/packs/pack_001.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 06_strategy_definition --report-only
```
