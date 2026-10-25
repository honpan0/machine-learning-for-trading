# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/08_futures_positioning.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Futures Positioning: CFTC Commitment of Traders Analysis

**Chapter 4: Fundamental and Alternative Data**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 4.3 (Fundamentals Across the Asset-Class Spectrum)

## Purpose

In a futures market every long position is somebody's short, so the aggregate is always zero
and tells you nothing. What is informative is *who* is on each side. The Commodity Futures
Trading Commission requires any trader holding more than a reporting threshold to disclose
their positions weekly, sorts them into categories by what kind of firm they are, and publishes
the totals for free in the Commitment of Traders report.

That gives a weekly picture of how each kind of participant is positioned: which way the hedge
funds lean, whether the physical producers are hedged more than usual, and where the dealers
are absorbing the other side. This notebook loads those reports, turns raw contract counts into
a comparable measure of how unusual the current positioning is, attaches the date the report
became public, and joins it onto futures prices at that date rather than at the date it
describes.

## Learning Objectives

After completing this notebook, you will be able to:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Name the trader categories in each of the two report formats and say which kind of firm
  each one holds.
- Load a product's report history and resolve the several CFTC contract markets that share one
  product code down to the one that carries the position.
- Turn a net contract count into a rolling z-score, and say what window it is measured against.
- Compute the date a report became public and join it onto a daily price series at that date,
  so that every session reads only reports already published.
- Build a contrarian signal from extreme positioning and a change signal from a weekly move,
  with the threshold for the change measured on prior weeks only.
- Compare positioning extremes across asset classes and say whether they arrive together.

## Prerequisites

Two free downloads, neither of which needs a key or a subscription. The first is the COT
archive; the second is the S&P 500 ETF, whose sessions Part 4 joins the reports onto.

[[ML4T_A3_0001]]

## Cross-References

- **Upstream**: [[ML4T_A3_0002]] (CFTC COT reports, weekly, free)
- **Downstream**: [[ML4T_A3_0003]] (sentiment features)
- **Related**: [[[ML4T_A3_0004]]](07_macro_data_alignment.ipynb) (the same publication-date correction on macro series)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0002-p000

~~~~~~markdown
Four settings decide what the notebook measures. The z-score window is the one that changes an
answer: at fifty-two weekly reports it asks how unusual today's positioning is against the
past year, which is short enough to adapt to a changed regime and long enough that a single
quarter cannot move the mean far.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## 1. What is in a COT report

Positions are recorded as of the close on **Tuesday** and published on **Friday afternoon**.
The report gives, for each trader category, the number of contracts held long and the number
held short. The difference is the category's **net position**: positive means the category is
collectively long.

The CFTC publishes two formats, and which one a product gets depends on what it is.

| Format | Products | Categories |
|--------|----------|------------|
| Traders in Financial Futures | Equity index, rates, currencies | Dealers, asset managers, leveraged money, other reportables, non-reportables |
| Disaggregated | Physical commodities | Producers and merchants, swap dealers, managed money, other reportables |

The category names differ but the roles line up. **Dealers** and **swap dealers** are
intermediaries: they take the other side of what their clients want and hedge the residue.
**Asset managers** are long-only institutions whose positions move with allocation decisions
rather than with views on the next few weeks. **Leveraged money** and **managed money** are
hedge funds and commodity trading advisors, the participants who take directional risk
deliberately and who unwind it quickly. **Producers and merchants** hedge physical inventory,
which is why a commodity's commercial category is read as informed about that commodity.

The reading that follows from this is that an extreme in the speculative category is worth
attention: hedge funds crowded on one side have no one left to buy from, and the position has
to be unwound eventually.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Loading a product, and the duplicate rows

The CFTC reports on **contract markets**, not on the ticker a trader thinks in. Several
distinct contract markets map to one product code: the E-mini S&P 500 shares its code with a
smaller related contract, and crude oil with more than one delivery specification. The
downloader writes them all, so a product's history has more than one row on many report dates.

Leaving them in would double-count the position and make any statistic over the series
meaningless. The rule used here is to keep, on each date, the row with the largest open
interest, which is the market that actually carries the position. What makes that safe rather
than convenient is that the choice has to be *stable*: if the largest market changed from week
to week, the resulting series would be jumping between contracts and its week-over-week changes
would be fiction.

The loader carries no contract-market identifier, so stability cannot be read off directly.
What can be measured is the margin: how many times larger the kept market is than the one
dropped beside it. A margin that never narrows toward one makes a change of rank implausible,
which is evidence and not proof.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0010-p000

~~~~~~markdown
### The columns

The loader derives a net column for each category, which is the only column most analysis uses.

| Column | What it holds |
|--------|---------------|
| [[ML4T_A3_0001]] | Contracts outstanding across all traders |
| [[ML4T_A3_0002]], [[ML4T_A3_0003]] | Hedge fund positions, gross |
| [[ML4T_A3_0004]] | Hedge funds long minus short |
| [[ML4T_A3_0005]] | Asset managers long minus short |
| [[ML4T_A3_0006]] | Dealers long minus short |

A commodity's report uses [[ML4T_A3_0007]] for the speculative category rather than
[[ML4T_A3_0008]], which is a naming difference and not a difference in what is measured, so the
comparison in Part 6 renames it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>
