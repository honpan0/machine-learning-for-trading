# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/14_text_data_extraction.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Text Data Extraction: Structuring Unstructured Financial Documents

**Chapter 4: Fundamental and Alternative Data**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 4.5 (Using Text Data for NLP Features)

## Purpose

An annual report is a quarter of a million characters of which a model wants perhaps a
twentieth. The Securities and Exchange Commission prescribes what a 10-K must contain and
numbers the parts, so the document has a structure; what it does not have is markup that a
parser can rely on, because the numbering appears in the table of contents, in cross-references
inside the narrative, and again as the actual section heading, in whatever typography the filer
chose.

Getting from a filing to a section, reliably, over thousands of documents, is the whole job of
this notebook. Everything downstream in the book - sentiment scoring, topic models, embeddings -
assumes that job was done properly, and the failure mode is silent: an extractor that returns
the table of contents entry instead of the section returns a plausible-looking short string.

## Learning Objectives

After completing this notebook, you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Name the items of a 10-K a research pipeline usually wants, and say where the same content
  sits in a 10-Q.
- Strip HTML from a filing without destroying the paragraph boundaries a later stage needs.
- Locate a section's boundaries when its item number appears many times in the document, and
  explain why the first match is the wrong one.
- Check an extraction for the two failures it can have - returning nothing, and running past
  the section's end - and report the rate rather than assuming success.
- Measure how much of a section changed between two consecutive filings, which is the input to
  the change-detection signals in Chapter 10.

## Prerequisites

This notebook reads live filings from EDGAR, which requires an identifying [[ML4T_A3_0001]]. It is
not an API key and there is nothing to sign up for: put your own name and email on the
[[ML4T_A3_0002]] line of the [[ML4T_A3_0003]] file in the repository root, before you start Jupyter.

[[ML4T_A3_0004]]

## Cross-References

- **Related**: [[[ML4T_A3_0005]]](02_sec_filing_explorer.ipynb) (reaching filings through the library)
- **Downstream**: [[ML4T_A3_0006]] (signals built on filing text)

## Key Concepts
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

- **10-K**: the annual report, filed once a year and the most complete narrative disclosure.
- **10-Q**: the quarterly report, shorter, and with the same content under different item
  numbers.
- **Item 1A, Risk Factors**: the risks management is required to disclose. The largest narrative
  block in a modern filing and the most mined.
- **Item 7, Management's Discussion and Analysis**: management's account of the period's
  results, in its own words.
- **Accession number**: the identifier the SEC assigns to a filing. Unique, permanent, and the
  right primary key for a text dataset.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0002-p000

~~~~~~markdown
The company and form choose which filings are read. Two consecutive filings of the same form
are fetched, because the second is what makes the change measurement in Part 6 possible; one
filing alone can be extracted from but not compared.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0005-p000

~~~~~~markdown
## 1. What a filing is made of

A 10-K is a numbered sequence of items whose meaning is fixed by regulation. Three of them carry
almost all the narrative a research pipeline wants.

| Item | Section | What it holds |
|------|---------|---------------|
| 1 | Business | What the company does, its segments and its markets |
| 1A | Risk Factors | The risks management is required to disclose |
| 7 | Management's Discussion and Analysis | Management's account of the period's results |
| 7A | Quantitative and Qualitative Disclosures | Market risk exposures |
| 8 | Financial Statements | The audited financials |

The numbering is **form-specific**, and this is the single most common source of a silently
empty extraction. In a 10-Q, management's discussion is Item 2 of Part I, not Item 7, and the
risk factors, if updated at all, are Item 1A of Part II. An extractor that hardcodes the 10-K
numbers returns nothing on a 10-Q and says nothing about why.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## 2. The filings

EDGAR requires every request to identify its sender, and rejects placeholder addresses. The
fetch is read-only and rate-limited by the library.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The acceptance timestamp is worth carrying alongside the filing date. A filing accepted after
the close is public that evening and tradeable the next morning, and a strategy that acts on the
filing date alone is a few hours early on every after-hours submission.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0010-p000

~~~~~~markdown
## 3. Cleaning

[[ML4T_A3_0001]] already returns text rather than markup, but a pipeline that fetches documents
directly gets HTML, so the conversion belongs here. The one thing to preserve is the paragraph
boundary: a converter that joins everything with spaces destroys the unit that the change
detection in Part 6 compares.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## 4. Finding a section

The naive approach is to search for the item heading and take everything to the next one. It
fails on the first line of every filing, because the item heading appears in the table of
contents before it appears as a section, and it appears again wherever the narrative
cross-references another item.

Counting the matches in a real document is the quickest way to see the size of the problem.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
Every section matches in more than one place, and only one of those places is the section. What
separates them is **span**: a table of contents entry is followed by the next contents entry a
line or two later, while the real heading is followed by the whole section before the next item
begins. Taking the candidate with the longest span to its own end pattern picks the section
without needing to know where the table of contents ends, and it keeps working on a filer whose
contents page is formatted differently.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## 5. The dataset, and whether the extraction worked

One row per filing and section, keyed on the accession number. The word count is what the
quality check reads: an extraction can fail by returning nothing, by returning a fragment - the
table of contents entry, if the span rule went wrong - or by running past its own end and
swallowing the next item.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
Reporting the rate rather than eyeballing one extraction is the point. Over two filings it is a
formality; over a corpus of thousands it is the only way to know that a formatting change at one
filer has not silently emptied a column, and the same three columns scale unchanged.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>
