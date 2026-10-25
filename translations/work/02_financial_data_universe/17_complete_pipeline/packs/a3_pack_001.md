# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/17_complete_pipeline.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Complete Data Pipeline: Multi-Source Acquisition to ML-Ready Data

**Docker image**: [[ML4T_A3_0001]]

## Purpose
Wire together the chapter's components — multi-provider acquisition,
OHLC validation, source attribution, and efficient storage — into two
end-to-end pipelines: an equity pipeline that stitches WikiPrices
(1990-2018) with Yahoo (2018-now), and a crypto pipeline that consumes
the local Binance hourly perpetuals panel. The notebook then shows how
[[ML4T_A3_0002]] does the same job in a fraction of the code.

## Learning Objectives
- Build a multi-source equity pipeline and validate at every boundary.
- Detect 24/7 coverage gaps and add session features for crypto data.
- Tag every row with its source so multi-source data is auditable.
- Replace the explicit pipeline with the [[ML4T_A3_0003]] + [[ML4T_A3_0004]] +
  [[ML4T_A3_0005]] higher-level API that ships with [[ML4T_A3_0006]].

## Book reference
Chapter 2, §2.3 (multi-source stitching + production pipelines). The
pipeline outputs feed the ETF and crypto-perps case studies.

## Prerequisites
- WikiPrices parquet under
  [[ML4T_A3_0007]].
- Crypto-perps hourly parquet loadable via [[ML4T_A3_0008]].
- Live YahooFinance access (the equity pipeline calls it for the
  2018-now leg — same convention as [[ML4T_A3_0009]]).

## Note on universe choice
WikiPrices covers individual US stocks (~3,200 tickers, 1962-2018) but
**not** index ETFs. For the equity pipeline below the demo universe
uses three large-caps (AAPL, MSFT, JPM) so the WikiPrices-Yahoo stitch
is non-trivial; the ETF rotation case study itself uses Yahoo-only
from 2008 onwards (see [[ML4T_A3_0010]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] fixes the right-hand end of every window so the outputs are stable between
book editions rather than moving with the wall clock.

[[ML4T_A3_0002]] is the seam. The WikiPrices feed stopped on that date, so it is the
boundary the stitch filters on and the line the figure draws. It appears once here rather
than in each of the three places that need it.

The two gap thresholds encode a difference in kind rather than degree: an equity calendar
closes for weekends and holidays, and a perpetual futures market does not close at all, so
the same gap means an ordinary weekend on one panel and an outage on the other.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0005-p000

~~~~~~markdown
---

## 1. Pipeline Architecture

A production pipeline has three stages:

| Stage | Inputs | Outputs |
|-------|--------|---------|
| **Acquire** | Yahoo Finance, WikiPrices, Binance | raw OHLCV per source |
| **Process** | raw OHLCV | validated, normalized, tagged frames |
| **Store** | tagged frames | partitioned Parquet keyed by symbol/date |

Four design principles drive the rest of the notebook:

1. **Provider independence** — the orchestrator shouldn't care which
   source each row came from.
2. **Validate at boundaries** — every entry/exit point checks OHLC
   invariants, gap thresholds, and duplicate timestamps.
3. **Source attribution** — every row carries a [[ML4T_A3_0001]] column so
   downstream debugging stays sane.
4. **Incremental updates** — re-runs fetch only what is new (the
   [[ML4T_A3_0002]] API in §5 handles this transparently).
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0006-p000

~~~~~~markdown
---

## 2. Equity Pipeline

### The seam needs a rescale, not just a filter

Two things have to be reconciled at the boundary, and the first is mechanical. The two
providers disagree about time zones - one stamps its timestamps naive and the other stamps
them UTC-aware - so concatenating the legs raises rather than silently mixing two clocks.
That refusal is right, and it still has to be resolved: both are daily bars in UTC, so
converting to UTC and dropping the zone puts them on one clock without moving anything.

Both feeds publish adjusted prices, and they are adjusted for different sets of events.
WikiPrices back-adjusts only the splits that happened inside its own coverage window,
which ends in 2018. Yahoo back-adjusts every split up to today, including ones after that
date - Apple's four-for-one in 2020 among them. Filtering the two legs at the seam and
concatenating them therefore produces a series with a step in it, and the step is a
corporate action rather than a price move.

The fix is one number, and where it is measured matters more than it looks. Both legs are
already dividend-adjusted, so on any day *both* feeds quote, the ratio of their two closes
is the difference in adjustment basis and nothing else. Taking the ratio across the seam
instead - the last historical close against the first recent one - divides two different
days' prices, so the intervening market move rides along in the factor. That forces the
return across the seam to zero and pushes the same move into the rescaled volume.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0006-p001

~~~~~~markdown

So the recent leg is fetched from [[ML4T_A3_0001]], before the seam rather than after it,
purely so the two legs share dates to measure on; the factor comes from the last day they
both quote, and the overlapping rows are then dropped from the historical side when the
legs are joined. Volume scales the other way - a four-for-one split quarters the price and
quadruples the share count - so the historical volume is divided by the same number.

The combine step asserts that the overlap was non-empty, because a fetch window that does
not overlap leaves the factor unset and the rescale silently skipped, which looks exactly
like a stitch that needed no rescale.

### Requirements

- **Universe**: AAPL, MSFT, JPM (chosen because they have full
  WikiPrices coverage; pure ETFs like SPY only have Yahoo data here).
- **History**: 1990-present (~35 years).
- **Frequency**: Daily.
- **Adjustments**: Split + dividend (total return).
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p001>>>
<<<ML4T-ZH-END:c0006-p001>>>

### c0007-p000

~~~~~~markdown
### Combine Multi-Source Data

Wiki Prices ends at 2018-03-27; Yahoo Finance continues from there.
This function stitches the two sources at the boundary, tagging each
row with its origin for downstream auditability.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Validate Pipeline Data

Check OHLC invariants, detect zero/negative prices, flag date gaps
beyond five calendar days, and catch duplicate timestamps.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### Fetch Historical Data from Wiki Prices

Reads adjusted OHLCV from the Wiki Prices parquet, adapting to whichever
column-naming schema the on-disk file uses ([[ML4T_A3_0001]]/[[ML4T_A3_0002]]/[[ML4T_A3_0003]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Process a Single ETF Symbol

Drives one symbol through fetch, combine, validate, and tag. Returns
a result dict with the data and validation report.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
