# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/02_asset_embeddings.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Feature → 特徵
- Feature engineering → 特徵工程
- Cluster → 群集

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Asset Embeddings: Word2Vec Applied to Portfolios

**Chapter 10: Text Feature Engineering**
**Section Reference**: See Section 10.2 for distributional hypothesis and Word2Vec

**Docker image**: [[ML4T_A3_0001]]

> **Docker required**: this notebook uses [[ML4T_A3_0002]], which does not build against the
> Python version the rest of the repository runs on. Run it with:
> ```bash
> docker compose --profile py312 run --rm py312 python 10_text_feature_engineering/02_asset_embeddings.py
> ```

## Purpose
This notebook demonstrates how Word2Vec - the foundational NLP embedding method -
extends beyond text to financial assets. Just as words appearing in similar
contexts have similar meanings, stocks appearing in similar portfolios may
share fundamental characteristics.

We train Word2Vec on institutional 13F holdings data, treating:
- **Portfolios** as sentences (ordered sequences of words)
- **Stocks** as words (tokens in those sentences)
- **Position ordering** as word order (stocks ranked by holding size)

## Learning Objectives
After completing this notebook, you will be able to:
- Apply Word2Vec (skip-gram) to non-text data
- Create "portfolio sentences" from institutional holdings
- Train asset embeddings using gensim Word2Vec
- Find economically similar stocks using embedding distance
- Understand the bridge between NLP and quantitative finance

## Academic Foundation
- **Gabaix, Koijen, Richmond & Yogo (2025)** "Asset Embeddings"
  NBER WP 33651. They show portfolio holdings contain "all relevant information
  for asset pricing" and demonstrate Word2Vec, BERT, and recommender systems
  on institutional holdings data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Prerequisites
- Section 10.2 of the chapter (distributional hypothesis, Word2Vec).
- [[ML4T_A3_0001]] for the Skip-gram mechanics on text.
- 13F bulk 2024Q3 holdings panel under [[ML4T_A3_0002]]
  (downloaded via [[ML4T_A3_0003]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## The Core Insight: Portfolios as Sentences

In NLP, Word2Vec learns that words appearing in similar contexts have similar
meanings. The **skip-gram** objective predicts context words given a target word.

Gabaix et al. (2025) apply this to portfolios:

| NLP Domain | Finance Domain |
|------------|----------------|
| Sentence | Portfolio (stocks ordered by weight) |
| Word | Stock |
| Context window | Nearby positions (similar weights) |
| Similar meaning | Similar investment characteristics |

**Key insight**: Investors assign similar portfolio weights to stocks with
similar characteristics. If AAPL and MSFT often appear as the 2nd and 3rd
largest positions in tech-focused portfolios, they should have similar embeddings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## Load and Prepare Holdings Data

Every institutional investor managing over [[ML4T_A3_0001]] must file quarterly 13F-HR
disclosures with the SEC. We use the bulk 2024Q3 filing window and select the
largest 500 institutions by number of holdings - enough portfolios to give
Word2Vec a meaningful co-occurrence signal, while keeping training tractable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0008-p000

~~~~~~markdown
## Create Portfolio Sentences

Following Gabaix et al. (2025), we convert each portfolio into a "sentence":
1. Group holdings by institution (CIK)
2. For each institution, order stocks by holding value (descending)
3. The ordered list of stock IDs becomes a "sentence"

This preserves the key insight: stocks with similar portfolio weights
(similar "positions" in the sentence) should have similar embeddings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
One sentence per institution, and the deduplication matters. A single filer can submit
several 13F-HR filings in one quarter - amendments, or separate subsidiaries - so the same
stock appears more than once for the same [[ML4T_A3_0001]]. Left in, those duplicates would put a
stock next to itself in its own sentence and teach the model that it co-occurs with itself.
Collapsing to the largest reported value per pair removes that before the ordering is taken.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
## Train Word2Vec on Portfolios

We use gensim's Word2Vec with the **skip-gram** architecture (sg=1),
following the paper's methodology.

Key parameters:
- [[ML4T_A3_0001]]: Embedding dimension
- [[ML4T_A3_0002]]: Context window (positions within 5 of target)
- [[ML4T_A3_0003]]: Skip-gram (predict context from target word)
- [[ML4T_A3_0004]]: Only stocks appearing in 5+ portfolios
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Why Skip-Gram Works for Portfolios

The skip-gram objective learns embeddings by predicting context words from
a target word. For portfolios:

**Training example**: If Berkshire holds [AAPL, AMEX, KO, BAC, OXY] in order
of position size, and we mask position 3 (KO), we predict KO from its
context (AMEX position 2, BAC position 4).

**Result**: Stocks that appear in similar positions across many portfolios
get similar embeddings-they share investment characteristics valued by
institutional investors.

Gabaix et al. (2025) note: "Investors assign similar portfolio weights to
assets with similar asset embeddings, according to portfolio theory."
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
## Finding Similar Stocks

With embeddings learned, we can find stocks closest in embedding space.
These are stocks that institutional investors treat similarly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
## Visualizing Asset Embeddings

We use t-SNE to project the 100-dimensional embeddings to 2D.
Stocks that cluster together share similar institutional ownership patterns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
### Measuring the claim rather than projecting it

The claim is that stocks held by the same institutions end up close together. That is a
statement about distances in the model's hundred-dimensional space, so measure it there.

A two-dimensional projection is the tempting picture and it does not test this. t-SNE
distorts the points at the edge of a cloud hardest, and the mega-caps here are exactly
those points: run on this subset it presses them all into a single spot against the left
boundary, which looks like strong evidence and is a property of the projection.

So: take the recognizable mega-caps, measure every pair among them, and compare that
against the same stocks' similarity to a random draw from the rest of the widely-held
universe. If co-ownership drives the geometry, the first should exceed the second.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
