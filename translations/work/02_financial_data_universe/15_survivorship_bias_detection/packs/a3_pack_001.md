# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/15_survivorship_bias_detection.ipynb；A3 Pack 001；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Survivorship bias → 存活者偏誤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Survivorship Bias Detection and Quantification

**Docker image**: [[ML4T_A3_0001]]

## Purpose

[[ML4T_A3_0002]] ended on an anomaly: the **US equities panel** records 777 symbols
leaving it, and every single one leaves in 2014 or later. This notebook picks that up and
asks the question a backtest actually depends on:

> For the window where the panel *does* record exits, how much does a portfolio that
> silently drops the leavers overstate its return?

Answering it takes three steps, and the middle one is where the work is:

1. **Read the exit record** and establish what the panel does and does not know about
   the symbols that left.
2. **Repair the return series.** The adjusted prices contain unadjusted corporate actions.
   Left uncorrected they do not merely add noise — they reverse the sign of the answer.
3. **Quantify the bias**, modelling the one quantity the panel cannot observe: what a holder
   received *after* the last quote.

## Learning objectives

- Separate symbols that left the panel from symbols that survived to its final date.
- Distinguish what a price panel observes (a path to a last quote) from what a delisting
  study needs (a terminal outcome), and reason about why the gap forces a modelling step.
- Detect unadjusted splits and reorganisations by their return signature, and see how a
  handful of bad rows propagates into a headline number.
- Build CRSP-calibrated delisting scenarios and put a percentile band around the bias.
- Distinguish *survivorship* completeness from *universe* completeness.

## Book reference

Chapter 2, §2.3 (data-quality framework — survivorship bias).

## Prerequisites

- US equities parquet under [[ML4T_A3_0003]]; loader [[ML4T_A3_0004]].
- Read [[ML4T_A3_0005]] first.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

The Monte Carlo bias estimates the chapter cites are anchored to this seed; overriding it
moves the reported numbers.

[[ML4T_A3_0001]] is the one parameter that carries an argument. §1 shows the panel records no
exit before 2014, so a window opening earlier spends its first years measuring a delisting
rate that is zero by construction. From 2014 to the panel's final date is the only span over
which the panel behaves like a live universe.

[[ML4T_A3_0002]] is one-sided because of what it encodes: a long position cannot lose
more than everything, so an implausible daily return can only be a gain.
[[ML4T_A3_0003]] is the share of the universe a session has to quote before it counts
as a session at all. §3 uses both.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0005-p000

~~~~~~markdown
## 1. The exit record

A symbol has *left* the panel if its last observation predates the panel's final date.
Everything else is still quoted when the feed stops.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0009-p000

~~~~~~markdown
### The exit record starts abruptly
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Reading the chart

The bars occupy the last five calendar years of a fifty-six-year panel — 2014 through the
March 2018 cutoff. The rest of the axis is empty.

That is not a claim about the equity market. Firms were acquired, went private and went
bankrupt throughout the panel's history — Enron was delisted from the NYSE in January 2002,
and it is not in this file's exit record because it is not in this file at all. The chart is a
claim about **the data collection process**: exit information was not being captured, and then
around 2014 it started being captured.

The mechanism is the panel's provenance. It was assembled from the community-maintained
Quandl WIKI feed: the symbols that existed when the project ran, each backfilled to its own
IPO. Symbols that had already died were never added, so their departure was never recorded.
Once the feed was live, symbols leaving it *were* recorded. Then contributor interest decayed,
and in March 2018 the feed stopped.

This is the tax on free public data, and it has a precise consequence: **for the pre-2014 era
the panel cannot tell us what we are missing.** Not "the bias is small" — unknown. The only
window over which the panel behaves like a live universe is 2014 to the final date, so that
is the window this notebook measures.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
## 2. What the panel cannot tell us

Suppose we know exactly which symbols left. Why model their outcomes at all — why not just
read off what happened to them?

Because the panel does not contain it. Fourteen columns: [[ML4T_A3_0001]], [[ML4T_A3_0002]], raw OHLCV,
[[ML4T_A3_0003]], [[ML4T_A3_0004]], and the five [[ML4T_A3_0005]] prices. Nothing else.

| What we need | Where it lives | In this panel? |
|---|---|---|
| The price path while the symbol traded | [[ML4T_A3_0006]] | Yes |
| *Why* the symbol stopped trading | CRSP [[ML4T_A3_0007]] (delisting code) | **No** |
| What a holder received *after* the last quote | CRSP [[ML4T_A3_0008]] (delisting return) | **No** |

A last quote is not a terminal value. When a firm is acquired, holders are paid the deal
consideration after the tape goes quiet. When a firm is liquidated, holders receive a
residual, often near zero, sometimes months later. Neither payment appears in a price file.

It is worse than a missing column. The panel does not even reliably observe the *date* of the
exit. Symbols in §3 sit at stale quotes on zero volume for days before they vanish, and the
feed's coverage was decaying the entire time. A symbol disappearing from this file can mean
"acquired", "liquidated", or "the contributors stopped updating it".

So the terminal return is **unobservable here, and must be modelled**. §4 builds three
scenarios from published CRSP outcome rates. This is a real cost of the free panel, not a
stylistic choice: with CRSP the terminal return is a column, and §4 through §6 collapse into
a [[ML4T_A3_0009]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0013-p000

~~~~~~markdown
## 3. The adjusted prices are not clean

Before measuring anything, one check. The bias is a difference between two compounded return
series, so a single bad daily return propagates into the headline. Look for returns the
market cannot produce.

A long position cannot lose more than everything, so the test is one-sided: only a gain can
be implausibly large, and a daily gain past [[ML4T_A3_0001]] is either a genuinely
extraordinary event or an unadjusted corporate action.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
