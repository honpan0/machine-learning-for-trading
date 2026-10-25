# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/13_algoseek_minute_bars_eda.ipynb；A3 Pack 003；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Label → 標籤

## 待翻譯英文單元

### c0045-p000

~~~~~~markdown
## 10. Volume: Exchange vs Off-Exchange (FINRA)

Volume is split between lit exchanges and off-exchange venues:

| Field | Source | Description |
|-------|--------|-------------|
| [[ML4T_A3_0001]] | Lit exchanges | NYSE, NASDAQ, BATS, etc. |
| [[ML4T_A3_0002]] | Off-exchange | Dark pools, internalizers, OTC |
| [[ML4T_A3_0003]] | All | Number of trades in the bar |

**Total Volume = volume + finra_volume**

> **Data Contract**: FINRA Trade Reporting Facility (TRF) collects reports of
> off-exchange trades (dark pools, internalizers, OTC). These trades are included
> in the consolidated tape but execute away from lit exchanges.

### Why This Matters

The reporting-facility share is the part of a bar's volume that did not print on a lit
exchange. Two quite different flows land there and the share alone cannot separate
them: institutional orders routed to a dark pool to avoid showing size, and retail
orders internalised by a wholesaler. Both raise the share, for opposite reasons.

What the series is good for is noticing when it moves. A bar whose off-exchange share
departs sharply from its own recent level is a bar in which the routing changed, and
that is worth conditioning on even without knowing which of the two flows caused it.
Attaching an institutional or retail label to a level, rather than to a change, asks
more of the number than it carries.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0047-p000

~~~~~~markdown
## 11. Spread: Liquidity Conditions

Spread fields capture bid-ask spread dynamics:

| Field | Meaning | Note |
|-------|---------|------|
| [[ML4T_A3_0001]] | Minimum spread during bar | **0 = locked/crossed market** |
| [[ML4T_A3_0002]] | Maximum spread during bar | Widening indicates stress |

**min_spread = 0 is an anomaly indicator**, not "free liquidity." It signals
market stress where bid ≥ ask (locked or crossed market).
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
## 12. VWAP and Time-Weighted Prices

| Field | Meaning |
|-------|---------|
| [[ML4T_A3_0001]] | Volume-weighted average price (exchange trades) |
| [[ML4T_A3_0002]] | VWAP of off-exchange trades |
| [[ML4T_A3_0003]] | Time-weighted average bid |
| [[ML4T_A3_0004]] | Time-weighted average ask |
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
## 13. Visualizations: Single Day Deep Dive
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0054-p000

~~~~~~markdown
## 14. Intraday Patterns

Key microstructure metrics show distinct patterns across the trading day.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0057-p000

~~~~~~markdown
## 15. Trading Mechanism Menu: Connecting Fields to Strategies

The microstructure fields in TAQ minute bars connect to specific trading mechanisms:

### What each family of fields is evidence about

The dataset's value is that several independent views of the same minute arrive
pre-computed. What follows is what each view can support, and what it cannot.

**Aggressor direction** ([[ML4T_A3_0001]], [[ML4T_A3_0002]], and the imbalance built from
them) says which side crossed the spread. It is evidence about who was demanding
liquidity, and it is the input both the momentum and the reversal reading start from -
which is why it cannot by itself distinguish them.

**Tick direction** ([[ML4T_A3_0003]], [[ML4T_A3_0004]]) says how the price moved between
consecutive trades. It agrees with aggressor direction most of the time and diverges when
a large order is filled at one price rather than walking the book, which makes the
divergence more informative than either series alone.

**Pressure** says how far from the midpoint the average trade printed.
[[ML4T_A3_0005]] is that distance in dollars; [[ML4T_A3_0006]]
divides it by the spread, and it is the second one that compares across stocks.
Direction and intensity are different questions, and this is the intensity one.

**Spread and quote count** ([[ML4T_A3_0007]], [[ML4T_A3_0008]], [[ML4T_A3_0009]]) describe the
conditions rather than the flow. A widening spread with a falling quote count is market
makers stepping back; [[ML4T_A3_0010]] at zero is a locked or crossed market, which is a data
condition worth knowing about before reading anything else in that bar.

**Off-exchange share** ([[ML4T_A3_0011]]) says how much of the bar did not print on a lit
venue, which is a routing fact rather than a directional one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0057-p001

~~~~~~markdown

None of these is a strategy, and turning any of them into one requires the two things
this notebook does not do: a forward-looking test with the signal lagged behind the
return it is supposed to predict, and a comparison against what trading it would cost.
Chapters 7 onwards do both.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p001>>>
<<<ML4T-ZH-END:c0057-p001>>>

### c0058-p000

~~~~~~markdown
## Key Takeaways

### Dataset Structure

1. **61 columns** organized into 7 families: identifiers, quote OHLC, trade OHLC,
   spread, volume, trade buckets, and pressure indicators
2. **Continuous bars**: Rows exist for every minute 04:00-20:00 ET, even without trades
3. **Null semantics**: Trade fields null = no trades (normal), quote fields never null

### Quote vs Trade Fields

| Aspect | Quote Fields | Trade Fields |
|--------|--------------|--------------|
| Source | NBBO updates | Actual executions |
| Null when | Never (carried forward) | No trades in bar |
| Examples | open_bid_price, close_ask_price | first_trade_price, vwap |

### TAQ Field Families and Trading Mechanisms

| Family | Key Fields | Trading Mechanism |
|--------|------------|-------------------|
| **Trade Buckets** | trade_at_bid/ask | Aggressor direction → OFI |
| **Tick Direction** | uptick/downtick_volume | Trade-level momentum |
| **Pressure** | trade_to_mid_vol_weight | Directional intensity |
| **FINRA** | finra_volume | Institutional activity |
| **Spread** | min/max_spread | Liquidity conditions |

### Key Microstructure Insights
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>
