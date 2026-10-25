# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/03_sec_form4_insider_transactions.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# SEC Form 4: Insider Transaction Analysis

**Chapter 4: Fundamental and Alternative Data**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 4.1 (The Point-in-Time Pipeline)

## Purpose

A Form 4 is filed when a company's officer, director or ten-percent shareholder trades its
stock, and it is due within two business days of the trade. That deadline is short enough
that the filing arrives while the information is still current, which is what makes the form
worth parsing at all. The previous notebook read Form 4s through a library that had already
parsed them. This one works from the XML the SEC publishes, because a feature built on
insider activity is only as trustworthy as the reader that produced it, and the failure modes
live in the parsing.

## Learning Objectives

After completing this notebook, you will be able to:

- Read a Form 4 XML document and name the elements that carry the issuer, the reporting
  insider and each individual trade.
- Extract one row per trade with its transaction code, date, share count, price and
  direction, keeping every field attached to the trade it came from.
- Reconcile the rows you extracted against the trades present in the raw files, and account
  for every one you did not keep.
- Separate trades that reflect a decision to buy or sell from the compensation events that
  make up most of the volume, using the transaction code.
- Aggregate priced trades into a per-insider dollar total without letting an unpriced row
  silently enter it.

## Prerequisites

This notebook reads Form 4 filings downloaded by:
[[ML4T_A3_0002]]

## Cross-References
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- **Download Script**: [[ML4T_A3_0001]]
- **Related**: [[[ML4T_A3_0002]]](02_sec_filing_explorer.ipynb) (edgartools for interactive exploration)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0003-p000

~~~~~~markdown
---
## Part 1: What is on disk

The download script writes one XML file per filing, under a directory named for the issuer's
ticker. Reading the file count and the file sizes first is worth the two lines: a Form 4 is a
small document, and a file of a few hundred bytes is an error page rather than a filing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0005-p000

~~~~~~markdown
---
## Part 2: Reading the XML

Each filing holds a [[ML4T_A3_0001]] for common stock and a [[ML4T_A3_0002]] for
options and other derivatives, and each table holds one transaction block per trade. Those
blocks are the reason to use an XML parser rather than a regular expression over the document
text: a regex has no notion of where one block ends, so it will pair the transaction code
from one trade with the price from the next, and read straight across the boundary from
common stock into options. Walking the tree keeps every field anchored to its own trade.

### The elements this notebook reads

| Element | Description |
|---------|-------------|
| [[ML4T_A3_0003]] | The company whose stock was traded |
| [[ML4T_A3_0004]] | One block per insider filing the report |
| [[ML4T_A3_0005]] | The insider's name |
| [[ML4T_A3_0006]] | The insider's position, where they hold one |
| [[ML4T_A3_0007]] | One common-stock trade |
| [[ML4T_A3_0008]] | What kind of trade it was |
| [[ML4T_A3_0009]] | Number of shares |
| [[ML4T_A3_0010]] | Price per share, absent on some transaction types |
| [[ML4T_A3_0011]] | A for acquired, D for disposed |

Derivative transactions are read separately below only to be counted, so that the rows this
notebook keeps can be reconciled against everything the files contain.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
### One filing, one function

A Form 4 may be filed jointly by more than one insider, in which case the document carries
several [[ML4T_A3_0001]] blocks and reports the trades on behalf of all of them. Reading the first
name found anywhere in the document would attach a joint filing's trades to whichever owner
happened to be listed first, so the owners are collected as a list and their count is carried
on every row.

Two categories of trade are deliberately not returned: derivative transactions, which are a
different instrument, and any block missing the code, the date or the share count, without
which the row cannot be interpreted. Both are counted rather than dropped in silence, so that
the reconciliation in Part 3 can account for them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
Running it on one filing before the whole set is the cheap way to see whether the element
paths are right: a wrong path returns [[ML4T_A3_0001]] rather than raising, so a parser that reads
nothing looks exactly like a parser that read an empty filing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### What the transaction codes mean

The code is the field that decides whether a row carries information. An open-market purchase
or sale is a decision the insider made with their own money. A grant, an option exercise, a
share withholding to cover tax, or a gift is compensation machinery running on a schedule
fixed months earlier, and it says nothing about what the insider thinks the stock is worth.

| Code | Description |
|------|-------------|
| P | Open market purchase |
| S | Open market sale |
| A | Grant or award |
| M | Exercise of a derivative security |
| X | Exercise of an in-the-money option |
| G | Gift |
| D | Disposition to the issuer |
| F | Shares withheld to pay tax |
| C | Conversion of a derivative security |
| I | Discretionary transaction |
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
---
## Part 3: Every filing, and an account of every trade

Parsing the whole set produces one row per common-stock trade. What matters more than the row
count is that the row count can be explained: a parser that quietly drops a tenth of its
input produces a panel that looks complete and is not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### Reconciling against the raw files

The check that a parser is complete cannot come from the parser. Counting the opening tags in
the file text uses no part of the code above: it does not know the element paths, the schema
or which blocks were skipped, so agreement between the two counts is evidence rather than
self-confirmation. Every trade in the files then falls into exactly one of three buckets:
extracted, excluded as a derivative, or excluded as incomplete.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
### The panel

Before anything is computed from it, the panel is worth looking at directly: which issuer it
covers, which insiders appear, over what dates, and whether any filing reported more than one
owner.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>
