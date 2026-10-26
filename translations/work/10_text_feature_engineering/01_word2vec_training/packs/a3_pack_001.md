# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/01_word2vec_training.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Feature → 特徵
- Feature engineering → 特徵工程

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Word2Vec: what a word's neighbors can and cannot tell you

**Chapter 10: Text feature engineering**
**Section reference**: Section 10.2, on the distributional hypothesis and Word2Vec

**Docker image**: [[ML4T_A3_0001]]

> **Docker required**: this notebook uses [[ML4T_A3_0002]], which does not build against the
> Python version the rest of the repository runs on. Run it with:
> ```bash
> docker compose --profile py312 run --rm py312 python 10_text_feature_engineering/01_word2vec_training.py
> ```

## What this notebook is for

Word2Vec turns one idea into a number: a word is described by the words it appears next
to. The idea is worth understanding twice over, because Chapter 10 applies exactly the
same machinery to portfolios, where a stock is described by the stocks held alongside it.

This notebook trains the model on a small corpus of financial sentences and then asks
what the resulting vectors know. The answer is more interesting than a demonstration
that it works: co-occurrence puts words used in the same sentences close together, and
the words a financial writer uses in the same sentence as [[ML4T_A3_0003]] include [[ML4T_A3_0004]]. What
the model learns is topic, and polarity is not topic.

## Learning objectives

After working through this notebook you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Train a Word2Vec model on your own sentences and say what each of its five main
  settings changes about the result.
- Read a nearest-neighbor table as evidence about what the model measures, rather than
  as a list of synonyms.
- Show why a model built from co-occurrence places opposites next to each other, and
  name the cases where that makes it the wrong feature.
- Compare a model trained on a few thousand domain sentences against one trained on
  billions of general ones, and say what each has that the other does not.

## Prerequisites

- Section 10.2 of the chapter.
- A vocabulary is the set of distinct tokens a model keeps; a context window is the
  number of words on each side that count as a word's neighbors. Nothing else is assumed.

## Related notebooks

- [[ML4T_A3_0001]] - the same Skip-gram machinery applied to 13F portfolios
- [[ML4T_A3_0002]] - compares static embeddings to TF-IDF and Transformers
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## The one assumption

"You shall know a word by the company it keeps," in J. R. Firth's 1957 phrasing. Word2Vec
turns that into an optimization: two words that appear beside the same other words are
pushed toward the same vector. There are two ways to set up the prediction and they differ
only in direction. **Skip-gram** is given a word and predicts its neighbors; **CBOW** is
given the neighbors and predicts the word.

The assumption is doing more work than it looks like. It defines similar to mean *used in
the same places*, and that is not the same as *means the same thing*. Where a corpus uses
two opposite words in the same sentence frames, the model has been told they are similar,
and it will say so. The rest of this notebook is largely about that gap.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## The corpus

The Financial PhraseBank is a few thousand sentences from financial news, each labeled for
sentiment by human annotators. The [[ML4T_A3_0001]] subset keeps only the sentences
every annotator scored the same way, which is the cleanest and the smallest of the four.
Its size is the point of the comparison later on: this is a domain corpus, not a large one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
Tokenization here is deliberately the simplest thing that works: lowercase, drop
punctuation, split on whitespace, and discard single characters. Note what it does *not*
do, because it shapes every result below: it keeps numbers. A corpus of earnings sentences
is full of them, and they will compete with words for the model's attention.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The fifteen most frequent tokens, before [[ML4T_A3_0001]] removes anything. Function words lead,
as they do in any corpus. What is worth noticing is how high [[ML4T_A3_0002]] and [[ML4T_A3_0003]] sit: currency
and magnitude markers are among the most common tokens in this corpus, and the numbers they
introduce are in the vocabulary too.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Training

Five settings decide what comes out, and each answers a different question:

- [[ML4T_A3_0001]] is how many numbers describe a word. More capacity needs more text to fill
  it; 100 to 300 is the usual range and this corpus does not justify the top of it.
- [[ML4T_A3_0002]] is how many words on each side count as neighbors. A small window learns which
  words are interchangeable in a phrase; a large one learns which words share a topic.
- [[ML4T_A3_0003]] drops words seen fewer than this many times, because a handful of occurrences
  cannot locate a vector.
- [[ML4T_A3_0004]] picks the direction of the prediction: 1 for Skip-gram, 0 for CBOW.
- [[ML4T_A3_0005]] is how many random words each update pushes *away*, which is what keeps the
  optimization from collapsing every vector onto one point.

[[ML4T_A3_0006]] is not a performance choice. More than one worker means the OS decides the
order updates are applied in, and the result stops being reproducible from the seed.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## What the neighbors actually are

The most direct question to ask a set of embeddings is which words each one sits next to.
Read the table below as evidence about what the model measures, not as a thesaurus.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
Two things in that table are the notebook's whole argument.

**The nearest neighbor of [[ML4T_A3_0001]] is [[ML4T_A3_0002]], and the nearest neighbor of [[ML4T_A3_0003]] is
[[ML4T_A3_0004]].** They are not similar in meaning; they are maximally opposite. But a sentence
reporting one is written almost identically to a sentence reporting the other - "operating
profit rose to EUR ... mn" against "operating loss narrowed to EUR ... mn" - so their
neighbors are the same words and co-occurrence has no way to tell them apart. This is not
a defect in the training run; it is what the distributional hypothesis says, applied
honestly.

**Several neighbors are numbers or currency fragments.** The tokenizer kept digits and
[[ML4T_A3_0005]], [[ML4T_A3_0006]] and bare figures are frequent enough to earn vectors of their own. They
attach to [[ML4T_A3_0007]] because they appear in the same frames it does. A production pipeline
either strips numeric tokens or normalizes them to a placeholder before training; this one
leaves them in so the effect is visible rather than hidden.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>
