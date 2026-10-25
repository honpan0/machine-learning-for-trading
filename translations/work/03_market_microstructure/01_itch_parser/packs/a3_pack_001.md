# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/01_itch_parser.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構
- Feature → 特徵

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# NASDAQ TotalView-ITCH: Order Book Data Parsing

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

This notebook demonstrates how to parse NASDAQ's TotalView-ITCH binary protocol.
Understanding MBO (message-by-order) data is foundational for microstructure-based ML features.

## Learning Objectives

After completing this notebook, you will be able to:
- Read one ITCH v5.0 message out of a binary file: find where it starts, how long it is,
  and which of the twenty-odd message types it is.
- Unpack a message's fields with Python's [[ML4T_A3_0002]] module, and convert the two encodings
  ITCH uses - a nanosecond offset from midnight, and a price held as an integer with four
  implied decimal places.
- Run the parse over a full trading day, writing each message type to its own Parquet
  partition so that a day that does not fit in memory still lands on disk.
- Load an already-parsed day and check that every message type reads back.
- Say when the Python parser is the right tool and when the Rust one is.

## Book reference

Section §3.3, *From raw messages to the limit order book* - the binary-parsing-at-scale
subsection and Table 3.1. §3.2 places ITCH among the other feeds.

## Cross-References

- **Downstream**: [[ML4T_A3_0003]] (builds order book from these messages)
- **Related**: [[ML4T_A3_0004]] (alternative MBO data source)

## Data Requirements

ITCH sample data can be downloaded using:
[[ML4T_A3_0005]]

Files are ~5GB compressed from: [[ML4T_A3_0006]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## ITCH Message Types

The [ITCH v5.0 specification]([[ML4T_A3_0001]]) defines 20+ message types:

| Type | Name | Description |
|------|------|-------------|
| **S** | System Event | Market open/close events |
| **R** | Stock Directory | Ticker information and characteristics |
| **H** | Trading Action | Trading halts, pauses, and resumptions |
| **Y** | Reg SHO Restriction | Short sale price test restrictions |
| **L** | Market Participant | Market maker positions |
| **V** | MWCB Decline Level | Market-wide circuit breaker levels |
| **W** | MWCB Status | Circuit breaker breach status |
| **A** | Add Order | New limit order enters the book |
| **F** | Add Order (MPID) | Same as A, with market participant ID |
| **E** | Order Executed | Partial/full execution against standing order |
| **C** | Order Executed w/Price | Execution at different price (hidden orders) |
| **X** | Order Cancel | Partial cancellation |
| **D** | Order Delete | Full removal from book |
| **U** | Order Replace | Modify price/size (cancel + add) |
| **P** | Trade | Non-displayed execution |
| **Q** | Cross Trade | Opening/closing cross |
| **B** | Broken Trade | Trade cancellation |
| **I** | NOII | Net Order Imbalance Indicator (auction) |
| **J** | LULD Auction Collar | Limit up-limit down price bands |
| **K** | IPO Quoting Period | IPO quotation timing |

By combining these messages chronologically, we can reconstruct the order book at any point in time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
The parse reads one directory and writes another. [[ML4T_A3_0001]]
resolves the parsed-message root from the repository's data configuration rather than a
path typed here, so the same notebook runs against a local checkout and inside the Docker
image. The raw binary sits in a [[ML4T_A3_0002]] directory beside it, which is where the download
script puts it.

[[ML4T_A3_0003]] is what makes a clean start work. For every other notebook in this
chapter an absent [[ML4T_A3_0004]] directory is the download instruction and the loader is
right to refuse; this notebook is the one that creates it, and it has to be told where
before there is anything there. The directory itself is created in Section 4, where the
parse is about to write: creating it here would leave an empty one behind on a machine
with no raw feed, and an empty directory is exactly what stops the loader refusing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 1. Message Specifications

Each ITCH message has a fixed binary structure. The format is defined in [[ML4T_A3_0001]]
using Python's [[ML4T_A3_0002]] module. Format codes:
- [[ML4T_A3_0003]] = unsigned short (2 bytes)
- [[ML4T_A3_0004]] = unsigned int (4 bytes)
- [[ML4T_A3_0005]] = unsigned long long (8 bytes)
- [[ML4T_A3_0006]] = char (1 byte), [[ML4T_A3_0007]] = N chars
- [[ML4T_A3_0008]] = big-endian byte order
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 2. Binary Parsing Example

Let's demonstrate how binary parsing works by creating and parsing a sample Add Order message.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
Packing a message by hand is the quickest way to see the layout. An Add Order carries the
format [[ML4T_A3_0001]]: big-endian, two unsigned shorts, a six-byte timestamp, an eight-byte
order reference, a one-character side, the share count, an eight-character padded ticker
and the price. Unpacking it below returns exactly these fields.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0013-p000

~~~~~~markdown
## 3. What the Pipeline Holds Right Now

Before parsing anything, take stock: the raw binary is the input, the per-message-type
Parquet directories are the output, and either can be absent. On a first run the parsed
side is empty, and it stays empty until Section 4 writes it. The parsed messages are
loaded in Section 5, after there is something to load.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
## 4. Full Parser Implementation

The parser below is written to be read. It processes one message at a time in Python, which
is what makes each step visible and also what makes a full trading day take about twenty
minutes. Section 6 covers the Rust parser, which emits the same Parquet schema and is what
you would run over many days.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
### Parser Helpers

The parse splits into three functions. [[ML4T_A3_0001]] takes the next message off the file
and hands back its type and its raw bytes; [[ML4T_A3_0002]] turns those bytes into a
dictionary of Python values; and [[ML4T_A3_0003]] runs the loop, buffering decoded
messages and writing them out in batches.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
Decode binary payload into a Python dict, converting raw timestamp bytes
to nanosecond integers and byte strings to stripped ASCII.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
The main parser reads the binary file sequentially, buffering decoded messages
and flushing to Parquet periodically to bound memory usage.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
