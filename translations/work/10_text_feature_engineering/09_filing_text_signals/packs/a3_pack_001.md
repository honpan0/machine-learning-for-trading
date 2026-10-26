# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/09_filing_text_signals.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Feature engineering → 特徵工程

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# SEC Filing Signals: From 10-Q Text to Alpha Factors

**Chapter 10: Text Feature Engineering**

**Docker image**: [[ML4T_A3_0001]]

**Section Reference**: See Section 10.5 for practitioner workflow and signal validation protocol

> **GPU recommended**: this notebook runs FinBERT and sentence-transformer
> inference over thousands of MD&A passages (no training). On a GPU the
> MAX_SYMBOLS=50 default lands in ~5 minutes; CPU is 5–10× slower. For GPU:
> ```bash
> docker compose run --rm ml4t-gpu python 10_text_feature_engineering/09_filing_text_signals.py
> ```


## Purpose

This notebook demonstrates how to construct alpha factors from SEC 10-Q filings.
Unlike headline-based signals (NB07), corporate filings provide dense, structured text
that reflects management's assessment of financial condition. We extract two complementary
signal types from MD&A sections:

1. **Sentiment signals** via FinBERT (directional bias in management language)
2. **Semantic change signals** via sentence-transformer embeddings (quarter-over-quarter narrative shifts)

The filing date provides a natural point-in-time anchor: the signal becomes available
when the SEC accepts the filing, not when the quarter ends.

## Learning Objectives

After completing this notebook, you will be able to:
- Load and explore SEC 10-Q MD&A text at scale
- Apply FinBERT sentiment scoring to long-form corporate text
- Compute document embeddings using sentence-transformers
- Construct a "narrative change" signal from sequential filing embeddings
- Join text signals to market data with point-in-time correctness
- Evaluate signal quality using IC, ICIR, and quintile analysis
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

## Prerequisites
- Section 10.5 of the chapter (alpha-factor evaluation, point-in-time joins).
- SEC 10-Q MD&A panel produced by [[ML4T_A3_0001]].

## Related Notebooks
- [[ML4T_A3_0002]] / [[ML4T_A3_0003]] — FinBERT model details.
- [[ML4T_A3_0004]] — analogous workflow on headlines instead of filings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0002-p000

~~~~~~markdown
Zero means every symbol. FinBERT scores one filing at a time, so runtime is close to linear
in the number of filings and the default trades coverage for a notebook that finishes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0005-p000

~~~~~~markdown
## 1. Load SEC 10-Q MD&A Data

The MD&A (Management's Discussion and Analysis) section is the most valuable narrative
section of quarterly filings. Unlike boilerplate Risk Factors that change slowly,
MD&A discusses current quarter performance and forward-looking outlook.

Data comes from our SEC EDGAR download script
([[ML4T_A3_0001]]),
which extracts MD&A sections from S&P 500 10-Q filings (2017-2021).
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### One signal per filing date

A catch-up filer can submit several quarters' 10-Qs on one date. The investable event is
the date, so only the most recent period is kept. Left in, the duplicates give the sentiment
and narrative tables repeated keys, the later join fans out on both sides, and those firms
are counted several times in every information coefficient below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
The gap in the right panel is a property of the forms, not of the sample. A company files
three 10-Qs a year and a 10-K for the fourth quarter, and the 10-K is the form that lands
in the first calendar quarter for most filers. So the quarter that looks empty is the one
whose disclosure went into an annual report this notebook does not read.

Anything read seasonally from these signals has to account for that: one quarter in four is
a different and much smaller sample of companies, not a quiet period.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0011-p000

~~~~~~markdown
## 2. FinBERT Sentiment Scoring

FinBERT processes text at the sentence level (max 512 tokens). For long MD&A sections
(median ~7,800 words), we use a chunking strategy:

1. Split MD&A into sentences
2. Score each sentence with FinBERT (positive/negative/neutral probabilities)
3. Aggregate sentence scores to document-level sentiment

This mirrors how analysts read filings: extracting overall tone from many paragraphs.
The aggregation captures both the **average sentiment** (management tone) and
**sentiment dispersion** (mixed signals within the same filing).
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Chunking Strategy

MD&A sections average ~9,500 words but FinBERT accepts only 512 tokens (~380 words).
We split into paragraphs and score each one, then aggregate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0018-p000

~~~~~~markdown
The middle panel is the one to read before using the left one. Sentiment averaged over a
filing is a mean of chunk scores whose spread is substantial, so two filings with the same
mean can differ in whether the document was uniformly mild or a mix of strongly positive
and strongly negative passages. That is why [[ML4T_A3_0001]] is carried as its own signal
rather than discarded as noise around the mean.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## 3. Document Embeddings and Narrative Change

Beyond sentiment polarity, we capture **semantic content** using sentence-transformer
embeddings. The key signal is **narrative change**: how much the MD&A text shifts
from one quarter to the next.

Intuition: a large semantic shift between consecutive filings suggests material
new information that the market may not have fully priced. This is analogous to
the "news surprise" factor in NB07, but applied to corporate disclosures.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
### Document Embedding Strategy

Full MD&A texts are too long for a single embedding pass. We use **mean pooling
over chunk embeddings**: embed each paragraph/chunk, then average. This captures
the overall semantic content while respecting model token limits.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0026-p000

~~~~~~markdown
Most consecutive filings are close together, which is what boilerplate does: an MD&A is
largely carried forward and edited, so the base rate of change is low and the tail is where
something was rewritten. The signal is the distance relative to that base rate, not the
distance itself.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0027-p000

~~~~~~markdown
## 4. Combine Signals and Join to Market Data

Two signal families are available:
- **Sentiment signals**: mean, std, positive/negative fractions
- **Narrative change**: cosine distance between consecutive filings

We join these to AlgoSeek S&P 500 daily prices using the **filing_date** as the
point-in-time anchor. The signal becomes investable on the filing date itself
(SEC filings are public immediately upon acceptance).
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0030-p000

~~~~~~markdown
### The point-in-time join

Each filing date is matched forward to the first trading day on or after it. Forward, not
backward: a backward match would attach the signal to a session that closed before the
filing existed, which is the look-ahead this whole construction is arranged to avoid. An
SEC filing is public on acceptance, so the filing date itself is investable when it is a
trading day.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>
