# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/13_backtest.ipynb；A3 Pack 001；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Label → 標籤

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto perpetuals: the baseline that turns a ranking into a book

The model notebooks produced rankings. At each eight-hour funding timestamp, each configuration
scores the contracts it can see and orders them. A ranking is not a portfolio, and nothing so
far says what a reader would have earned holding one.

This notebook builds the crudest portfolio that a ranking supports and runs it. An **entry
rule** turns the scores at one timestamp into a set of positions - take the five highest-scored
contracts long and the five lowest short, say - and every position gets the same weight. Equal
weight is deliberate. It is the one sizing choice that contributes no information of its own, so
a difference between two configurations here is a difference between their rankings and nothing
else. [[[ML4T_A3_0001]]](14_portfolio_management.ipynb) is where sizing starts to vary.

**Funding is the reason this case study exists, and it is settled inside the run.** A perpetual
future never expires, so no delivery date forces its price towards spot. The exchange applies a
**funding rate** instead: every eight hours, whoever is long pays whoever is short an amount
proportional to the gap between the perpetual and the index, and when the gap is negative the
payment runs the other way. That is a cash flow the holder receives or pays whatever the price
does. A position can pay while its price prediction is wrong, and a price-only equity curve is
therefore not the return on a perpetual position - it is a different quantity. The backtest
boundary settles the official rate against the position carried into each timestamp, before any
fill at that same timestamp, and the rates it used are part of what identifies the result.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

**Nothing is selected here.** Every declared configuration gets a baseline, the results are
registered, and the ranking of one against another is read in
[[[ML4T_A3_0001]]](19_strategy_analysis.ipynb).

**Learning objectives.** By the end of this notebook you will be able to:

- State, for one strategy, the moment the decision is taken, the moment it is filled, how long
  the position is held, and when the next decision is allowed, and check that the four agree
  with the horizon the label was built on.
- Say why a long-short rule that asks for ten contracts a side cannot be run on a universe of
  nineteen, and read which members of a declared grid the shared selector dropped.
- Run every member of a frozen prediction population through one entry rule and have each
  result registered with the funding settlements that produced it.
- Recognise an equal-weight backtest as the reference every later sizing, cost and risk variant
  is measured against, rather than as a candidate in its own right.

**Book reference**: Chapter 16 (Strategy Simulation).

**Prerequisites**: the model notebooks [[[ML4T_A3_0002]]](06_linear.ipynb) through
[[[ML4T_A3_0003]]](10_dl_tcn.ipynb) have registered their complete validation prediction populations.

**What it writes**: one [[ML4T_A3_0004]] backtest per prediction set and entry rule, in
[[ML4T_A3_0005]], grouped into one immutable population per entry rule and one candidate
set per label. [[[ML4T_A3_0006]]](14_portfolio_management.ipynb) reads those candidate
sets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0004-p000

~~~~~~markdown
## 1. The population this notebook backtests

A **population** is a named, immutable list of results, written down before the work that
produces them starts. The model notebooks each published one; the call below re-derives the
complete case-wide list from the training menus and records it under one name, so that what
follows is measured against a declaration rather than against whatever the registry happens to
contain. If a configuration is declared and missing, or present and incomplete, the check two
cells down fails here rather than producing a baseline over a silently smaller set.

Freezing is a canonical-run step. A preview run against a private workspace backtests the
predictions its own model notebooks wrote there; it does not read the released population and
does not redeclare it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The catalog is what gets backtested, and on a canonical run it is **the declared population
read back**, not the registry filtered down to it. The distinction is the whole point of
freezing: a query returns whatever is registered under a set of predicates, and the registry
is immutable, so a superseded generation's rows are still there and still [[ML4T_A3_0001]]. Filtering
by [[ML4T_A3_0002]], [[ML4T_A3_0003]] and [[ML4T_A3_0004]] therefore returns both generations, and a sweep over both
ranks a retired identity against a live one and carries whichever wins into every stage
downstream. Reading the population back cannot do that: it is a fixed list of hashes, declared
before this notebook ran.

The membership check is the other half. A declared member with no registry row means the
population names something the model notebooks never produced, and that has to fail here rather
than produce a baseline over a silently smaller set.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>
