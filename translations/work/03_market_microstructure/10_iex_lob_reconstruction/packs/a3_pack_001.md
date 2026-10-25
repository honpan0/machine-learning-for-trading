# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/10_iex_lob_reconstruction.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# IEX LOB Reconstruction: Free Market Data Alternative

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Reconstruct a price-level (L2) limit order book from IEX DEEP — the only
free, redistribution-friendly L2 feed at this granularity — and contrast
the resulting book with the order-level (L3) NASDAQ ITCH reconstruction in
[[ML4T_A3_0002]].

## Learning Objectives

After completing this notebook, you will be able to:
- Parse IEX DEEP pcap binary into structured messages and explain the
  feed's 11 message types versus ITCH's ~20.
- Maintain a per-price-level book from [[ML4T_A3_0003]] messages and
  recognize what depth-only feeds cannot tell you (no individual order
  tracking, no per-order cancellation rates).
- Validate the reconstruction (positive spreads, sane depth) and quantify
  what's lost relative to ITCH (queue position, order lifecycles).

## Book reference

Section §3.2 (data-feed taxonomy entry for IEX HIST/DEEP) and §3.3
(notebook is named alongside ITCH and DataBento as a third
reconstruction implementation).

## Prerequisites

- IEX DEEP pcap at
  [[ML4T_A3_0004]]
  (downloaded via [[ML4T_A3_0005]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

> **Data note (important):** [[ML4T_A3_0001]] selects IEX's lowest-volume DEEP file
> to keep the download tiny. On the shipped run that file is a non-trading day
> whose only instruments are IEX's internal **test symbols** (ZIEXT, ZEXIT,
> ZXIET) at flat placeholder prices. So the reconstruction, spread, and depth
> statistics below validate the *parser and L2 algorithm* against IEX's
> synthetic test instruments — they are **not** the microstructure of a traded
> security. To reproduce these analyses on a real name, download a full
> trading-day DEEP file (drop [[ML4T_A3_0002]]) and filter to the symbol of
> interest; the code path is identical.

## IEX vs NASDAQ: Key Differences

| Aspect | NASDAQ ITCH | IEX DEEP |
|--------|-------------|----------|
| LOB granularity | Order-level (L3) | Price-level aggregated (L2) |
| Share of US equity volume | Among the largest single venues | A small single-digit share |
| Speed bump | None | 350μs delay |
| Message types | ~20 | 11 |
| Data access | Licensed | Free public download |

> **Attribution (Required):** Data provided for free by IEX. By accessing or
> using IEX Historical Data, you agree to the
> [IEX Historical Data Terms of Use]([[ML4T_A3_0003]]).
>
> **Note on DEEP**: full depth at each price level but without individual
> order IDs — you see total size at each price, but not how many orders
> comprise it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## 1. Load Raw IEX HIST Data

IEX provides HIST data on a T+1 basis, with 12 months of rolling history.
We use the canonical loader to find downloaded pcap files.

**Available feeds:**
- **TOPS** (Top of Book) - Best bid/ask quotes and trades
- **DEEP** (Depth of Book) - Full price-level depth (required for LOB reconstruction)

To download data, run:
[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Parse IEX-TP Protocol

IEX uses their own binary protocol (IEX-TP) which wraps message payloads.
The [[ML4T_A3_0001]] library handles the low-level decoding.

**DEEP Message Types:**
- [[ML4T_A3_0002]] - LOB depth changes at each price level
- [[ML4T_A3_0003]] - Best bid/ask changes
- [[ML4T_A3_0004]] - Executed trades
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Extract Symbol from IEX Message

Decode the symbol field from raw bytes or string in an IEX message.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Normalize IEX Side Field

IEX encodes the order side in several formats; normalize to "bid" or "ask".
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Dispatch a Single DEEP Message

Route each parsed message to the appropriate buffer based on its type.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Build Result DataFrames

Convert accumulated message buffers into Polars DataFrames for downstream analysis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Parse IEX DEEP Messages

Extract trades, quotes, and price level updates from raw IEX DEEP pcap files.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## 3. Parse DEEP Data

Parse the downloaded DEEP file to extract quotes, trades, and price level updates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
## 4. LOB Reconstruction from Price Level Updates

IEX DEEP provides **price-level aggregated** updates, simplifying reconstruction:
- Each [[ML4T_A3_0001]] tells you the new total size at a price
- Size of 0 means that price level is removed
- No need to track individual order IDs (unlike ITCH)
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
### Capture a Single LOB Snapshot

Record the current book state (best bid/ask, spread, midpoint) at a given timestamp.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
### Reconstruct LOB Snapshots

Build periodic snapshots from price level updates using the IEXOrderBook state machine.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 5. Reconstruct LOB for Active Symbols
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>
