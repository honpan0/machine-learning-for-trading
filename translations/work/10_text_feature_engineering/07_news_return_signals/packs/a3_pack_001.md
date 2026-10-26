# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/07_news_return_signals.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Feature engineering → 特徵工程
- Look-ahead bias → 前瞻偏誤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# News-Based Alpha Signals: From Text to Factors

**Chapter 10: Text Feature Engineering**

**Docker image**: [[ML4T_A3_0001]]

**Section Reference**: See Section 10.5 for practitioner workflow and alpha factor design

## Purpose
This notebook demonstrates how to construct alpha factors from financial news text.
We move beyond sentiment classification to build systematic signals that can be
evaluated using standard factor analysis techniques.

The "news surprise" concept follows Bhargava, Lou, Ozik, Sadka & Whitmore (2023)
"Quantifying Narratives and their impact on Financial Markets," which shows that
semantic deviation from recent narrative patterns predicts abnormal returns.

## Learning Objectives
After completing this notebook, you will be able to:
- Process large-scale financial news data from FNSPID dataset
- Compute news embeddings using sentence transformers
- Construct a "news surprise" factor measuring semantic deviation
- Aggregate signals by stock and date for factor evaluation
- Handle look-ahead bias in text-based factor construction
- Evaluate factor information coefficients (IC) against actual returns
- Analyze quintile spreads for practical signal assessment

## Cross-References
- **Foundation**: Section 10.4 covers Transformer embeddings
- **Factor Evaluation**: Chapter 9 covers IC analysis and factor evaluation
- **Application**: Chapter 16 shows how factors integrate into trading strategies
- **Academic**: Bhargava et al. (2023) for narrative impact on markets
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
[[ML4T_A3_0001]] covers Python, NumPy and Torch. The transformers pipelines draw from
their own generator, which needs seeding separately.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0006-p000

~~~~~~markdown
## The news corpus

FNSPID pairs financial news articles with the tickers they mention and the dates they ran,
over more than two decades. The download defaults to a sample rather than the whole thing,
which is enough for the construction shown here and small enough to embed in reasonable
time.

[[ML4T_A3_0001]]

Reference: [FNSPID on HuggingFace]([[ML4T_A3_0002]])
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0009-p000

~~~~~~markdown
## Data Preparation

Clean and structure the news data for factor construction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0010-p000

~~~~~~markdown
FNSPID's column names have changed between releases, so the text, date and ticker columns
are identified by looking for known names in priority order rather than assumed. Headline
is preferred over any summary field, because a generated summary is not what a reader saw.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0014-p000

~~~~~~markdown
## Text-to-Signal Pipeline Checklist

The chapter introduces a critical checklist for converting text to tradeable signals.
This section demonstrates each step with concrete implementations.

| Checklist Item | Implementation |
|----------------|----------------|
| Availability timestamp | Use publication date, lag signal by 1 day |
| Wire deduplication | Exact + 50-char prefix hash within (ticker, date) |
| Entity resolution | Normalize tickers to canonical symbols |
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Wire Deduplication
Remove near-duplicate articles using hash-based deduplication within each (ticker, date) group.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
### Optional: TF-IDF near-duplicate comparison

The hash pass above is fast (O(n)) and removes exact and shared-prefix copies —
the bulk of wire-service duplication. It does not catch *paraphrased*
near-duplicates, where an editor rewords a headline enough to change its prefix.
A TF-IDF cosine-similarity pass within each (ticker, date) group catches those,
at O(n²) per group; here the groups are small, so the added cost is modest.

The two methods are complementary. The pipeline keeps the fast hash result as its
default; the comparison below runs the fuzzy pass on the same raw corpus and
reports what it would additionally remove, so you can weigh the trade-off and tune
the [[ML4T_A3_0001]] cosine cutoff.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
The two deduplication strategies run side by side on the same corpus so their disagreement
is visible. The pipeline keeps the hash result; this comparison exists so the cosine cutoff
can be set by looking at what it removes rather than by taste.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
### Ticker Normalization
Map ticker aliases to canonical symbols.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## Compute News Embeddings

We use a pre-trained Transformer to convert headlines into dense vector representations.
These embeddings capture semantic meaning beyond keyword matching.

**Mean Pooling**: We average the token embeddings (weighted by attention mask) to get
a single fixed-size vector per headline. This is the standard approach for sentence embeddings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
### Mean Pooling
Average token embeddings weighted by attention mask to get a single sentence vector.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
### Encode Texts to Embeddings
Batch-encode texts using the Transformer model with mean pooling and L2 normalization.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
### Sentiment Scoring with FinBERT
Score headlines using FinBERT-tone for polarity (-1=Negative, 0=Neutral, +1=Positive).
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>
