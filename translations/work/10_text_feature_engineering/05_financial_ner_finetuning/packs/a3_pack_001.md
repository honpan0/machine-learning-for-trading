# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/05_financial_ner_finetuning.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Training set → 訓練集
- Test set → 測試集

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Financial Named Entity Recognition (NER) Fine-Tuning

**Chapter 10: From Text to Features - The Transformer Breakthrough**
**Section Reference**: See Section 10.4 for Transformers and token classification

**Docker image**: [[ML4T_A3_0001]]

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 10_text_feature_engineering/05_financial_ner_finetuning.py
> ```


## What this notebook is for

Named entity recognition turns a sentence into structured fields: which spans are
organizations, which are amounts, which are dates. That is what makes a filing or an
earnings call queryable, and it is the step between having text and having a table.

The task differs from the sentiment classification in [[ML4T_A3_0002]] in a way that
causes most of the difficulty: a tag marks part of a sentence rather than the whole of it,
and a transformer works in subword pieces that do not line up with words. So
most of the work below is alignment, and the piece worth reading closely is the function
that maps word-level tags onto subword tokens.

The span is the unit here: a tag names where an entity starts and where it ends, not what
the sentence as a whole is about.

The data here is generated from templates rather than annotated by hand. That keeps the
notebook runnable, and it has a consequence the notebook measures rather than glosses: the
generator repeats itself, so much of the test set is also in the training set and the
scores are near the ceiling for that reason.

## Learning objectives

After working through this notebook you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Read and write BIO tags, and say what goes wrong if a multi-word entity opens with [[ML4T_A3_0001]].
- Align word-level labels to a transformer's subword tokens, and explain which subwords get
  a label and which get ignored by the loss.
- Fine-tune a transformer for token classification and score it entity by entity rather
  than token by token.
- Check whether a held-out split of generated data is actually held out.

## Prerequisites

- Section 10.4 of the chapter.
- [[ML4T_A3_0002]] for the Trainer mechanics, which are not re-explained here.

## Related notebooks

- [[ML4T_A3_0003]] - the same Trainer applied to whole-sentence classification
- [[ML4T_A3_0004]] - extracting features from filings at scale
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
[[ML4T_A3_0001]] covers Python, NumPy and Torch. The Trainer draws from its own generator
for shuffling and dropout, which needs seeding separately or the run is not reproducible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
## The data, and why it is generated

Annotated NER corpora are expensive because a person has to mark every span, so this
notebook generates its sentences from templates instead. The tradeoff is explicit: the
pipeline that follows is exactly what you would run on CoNLL-2003 or FiNER-139 or your own
annotations, and the scores it produces on this data are not.

The generator fills five sentence templates from five options per entity slot, tagging as
it goes so the labels are correct by construction rather than by annotation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
The tag vocabulary is fixed here rather than inferred from the data, so a label id means
the same thing on every run and a class absent from one sample does not renumber the rest.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
### How much of the test set is already in training

The generator can produce a few hundred distinct sentences: four of its templates have
three entity slots and one has two, with five options each. Every draw is independent and
with replacement, so long before the sample count approaches that ceiling the same
sentences come up repeatedly - the collision argument is the birthday problem, not a
shortage of possibilities.

The consequence is what matters here. A random split of a sample containing duplicates puts
copies of the same sentence on both sides, so the model is scored partly on sentences it
was trained on. That is worth counting rather than assuming, because it is the reason the
scores below look the way they do. The count is over exact token sequences.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
One example, with the tag on each token. [[ML4T_A3_0001]] opens an entity, [[ML4T_A3_0002]] continues the one
before it, and [[ML4T_A3_0003]] is everything outside an entity. A two-word company name is therefore
[[ML4T_A3_0004]] followed by [[ML4T_A3_0005]], which is what lets the scheme mark where one entity ends and
the next begins.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Aligning labels to subwords

The labels are one per word; the model reads one token per subword, and "JPMorgan" may
arrive as three of them. Something has to decide which subword carries the word's label.

The convention below gives the label to the first subword of each word and marks the rest
-100, which is the value PyTorch's cross-entropy ignores. So the loss is computed once per
word rather than once per subword, and a word that happens to split into many pieces does
not outweigh a word that does not. Getting this wrong is the most common way an NER
pipeline trains without error and scores badly.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0020-p000

~~~~~~markdown
### What these scores are measuring

The scores are near the ceiling, and the count printed after the split says why: most of
the distinct test sentences appear verbatim in the training set. The model is being asked
to reproduce sentences it has already seen, which it can do, and the metric is reporting
that it did.

So read this number as a plumbing check. It says the tokenizer, the subword-to-word label
alignment, the collator and the training loop are wired up correctly, which is genuinely
worth confirming and is the thing most likely to be silently wrong in an NER pipeline. It
says nothing about whether the model can find an entity it has not seen before.

On a real annotated corpus - CoNLL-2003, FiNER-139, or your own filings - the interesting
errors appear: boundaries in the wrong place, a ticker read as an ordinary word, an
organization the model has never encountered. The pipeline below is unchanged for those;
only the data is.

There is a second thing to check before trusting an NER number anywhere. The canonical
metric is entity-level, meaning a span counts only when both its full extent and its type
match, and [[ML4T_A3_0001]] computes it. Without [[ML4T_A3_0002]] installed this notebook falls back to a
token-level score from [[ML4T_A3_0003]], which is more lenient because a span with one token wrong
still earns credit for the rest. On data this saturated the two agree; on real data they do
not, and the entity-level one is the number to quote.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
