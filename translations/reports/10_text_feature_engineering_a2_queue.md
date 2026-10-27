# 10_text_feature_engineering｜A2 翻譯工作清單

- Pack 總數：15；待翻譯：15；回覆待匯入：0；已匯入：0
- 指派 A/B 為**建議分工**（以英文原文字元平衡負載），可自由交換。
- 中文翻譯品質仍需人工抽查；結構 PASS 不等於語意已驗收。
- 原始 AI 回覆請依指定路徑存成 UTF-8 `.txt`。

| 帳號 | 狀態 | Notebook | Pack | 翻譯單元 | 英文字元 | 任務檔 |
|---|---|---|---:|---:|---:|---|
| A | 待翻譯 | `01_word2vec_training` | 001 | 0/13 | 8998 | [pack_001.md](../work/10_text_feature_engineering/01_word2vec_training/packs/pack_001.md) |
| B | 待翻譯 | `01_word2vec_training` | 002 | 0/4 | 4955 | [pack_002.md](../work/10_text_feature_engineering/01_word2vec_training/packs/pack_002.md) |
| A | 待翻譯 | `02_asset_embeddings` | 001 | 0/18 | 9646 | [pack_001.md](../work/10_text_feature_engineering/02_asset_embeddings/packs/pack_001.md) |
| B | 待翻譯 | `02_asset_embeddings` | 002 | 0/6 | 4329 | [pack_002.md](../work/10_text_feature_engineering/02_asset_embeddings/packs/pack_002.md) |
| A | 待翻譯 | `03_sentiment_evolution` | 001 | 0/15 | 7973 | [pack_001.md](../work/10_text_feature_engineering/03_sentiment_evolution/packs/pack_001.md) |
| A | 待翻譯 | `03_sentiment_evolution` | 002 | 0/2 | 1877 | [pack_002.md](../work/10_text_feature_engineering/03_sentiment_evolution/packs/pack_002.md) |
| B | 待翻譯 | `04_bert_finetuning` | 001 | 0/15 | 8158 | [pack_001.md](../work/10_text_feature_engineering/04_bert_finetuning/packs/pack_001.md) |
| B | 待翻譯 | `04_bert_finetuning` | 002 | 0/2 | 2600 | [pack_002.md](../work/10_text_feature_engineering/04_bert_finetuning/packs/pack_002.md) |
| B | 待翻譯 | `05_financial_ner_finetuning` | 001 | 0/13 | 9457 | [pack_001.md](../work/10_text_feature_engineering/05_financial_ner_finetuning/packs/pack_001.md) |
| A | 待翻譯 | `06_finbert_cross_dataset` | 001 | 0/11 | 8702 | [pack_001.md](../work/10_text_feature_engineering/06_finbert_cross_dataset/packs/pack_001.md) |
| A | 待翻譯 | `07_news_return_signals` | 001 | 0/24 | 8217 | [pack_001.md](../work/10_text_feature_engineering/07_news_return_signals/packs/pack_001.md) |
| A | 待翻譯 | `07_news_return_signals` | 002 | 0/4 | 3554 | [pack_002.md](../work/10_text_feature_engineering/07_news_return_signals/packs/pack_002.md) |
| B | 待翻譯 | `08_text_feature_evaluation` | 001 | 0/16 | 8561 | [pack_001.md](../work/10_text_feature_engineering/08_text_feature_evaluation/packs/pack_001.md) |
| B | 待翻譯 | `09_filing_text_signals` | 001 | 0/21 | 9527 | [pack_001.md](../work/10_text_feature_engineering/09_filing_text_signals/packs/pack_001.md) |
| B | 待翻譯 | `09_filing_text_signals` | 002 | 0/1 | 1434 | [pack_002.md](../work/10_text_feature_engineering/09_filing_text_signals/packs/pack_002.md) |

## 收件與匯入

請將每份 GPT 回覆存到 `reply` 欄指定路徑（詳見同名 CSV）。
逐份 Notebook 可用：

```bash
python3 translation_tools/collect_translation.py <來源.ipynb> --all
```

上面 `<來源.ipynb>` 是占位符；請替換為完整的英文 Notebook 相對路徑。
收件後重新產生工作清單：

```bash
python3 translation_tools/prepare_chapter.py 10_text_feature_engineering --report-only
```
