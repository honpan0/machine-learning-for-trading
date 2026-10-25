# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/03_structural_cross_instrument_features.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Feature engineering → 特徵工程
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Structural and Cross-Instrument Features

**Chapter 8: Feature Engineering**
**Section Reference**: 8.3 - Structural and Cross-Instrument Features
**Docker image**: [[ML4T_A3_0001]]

## Purpose

This notebook demonstrates features that require **data beyond a single asset's
price series**: term structures, cross-instrument relationships, and
derivatives-implied quantities. These encode information invisible in any
individual price history.

## Learning Objectives

1. Compute carry (roll yield) from futures term structure data
2. Build cross-asset beta and lead-lag correlation features
3. Extract options-implied features: ATM IV, risk reversal, IV term structure, VRP
4. Understand surface stability requirements for options features

## Feature Families Covered

| Family | Representative Features | Data Source |
|--------|------------------------|-------------|
| **Carry & Term Structure** | Roll yield, curve slope/curvature | CME futures |
| **Cross-Asset Structure** | Rolling beta, lead-lag, relative value | ETFs |
| **Options-Implied** | ATM IV, risk reversal, VRP, term slope | S&P 500 options |

## Data Policy

All examples use **real data**: CME futures, ETFs, and S&P 500 options.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
---

# Part 1: Carry and Term Structure

Carry features encode **risk compensation**: the return from holding a position
absent price change. Roll yield from futures is the canonical example.

Key formula:

[[ML4T_A3_0001]]

- Positive carry (backwardation): near > far, so a holder earns by rolling
- Negative carry (contango): near < far, so a holder pays to roll
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
## Load Futures Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## Roll Yield (Manual Implementation)

Roll yield is the annualized price difference between near and far contracts.
We pivot tenors to compute the spread.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## Term Structure Slope and Curvature

With three tenors we can also extract slope and curvature:

- **Slope**: [[ML4T_A3_0001]], the overall term structure direction
- **Curvature**: [[ML4T_A3_0002]], the butterfly shape
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Visualize Carry Across Products
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
The four panels carry very different magnitudes, so each has its own vertical scale and
only the sign is comparable across them. Count the signs rather than reading them off
the panel heights.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
**Interpretation**: read the shares printed above rather than the panel heights, which
are on four different scales. Backwardation means the front contract trades above the
deferred one, so a holder who rolls earns the difference; contango is the reverse and
the holder pays. The table says how often each product sat on each side of that line
over this sample.

The received explanations are worth holding next to the numbers rather than in place of
them. Backwardation in an energy contract like CL is usually read as physical tightness,
a market paying up for a barrel today. Gold is the standard contango example, because
storage and financing dominate and there is no convenience yield to offset them. A
note like ZN carries the coupon against a financing rate, so its sign follows that
spread. ES sits on the cost-of-carry relation between dividends and financing. Whether
this sample agrees with each of those is what the table is for, and a sample this short
settles none of them.

**Crypto funding rates** operate on a distinct clock (8-hour settlements) with
much higher volatility. See the [[ML4T_A3_0001]] case study for the
full treatment.

**Full pipeline**: The [[ML4T_A3_0002]] case study applies these features to all
30 CME products with proper roll handling and cross-sectional ranks.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
### Book Figure: Cross-Sectional Roll Yield Snapshot

Load all CME products and plot a single-date snapshot of annualized roll yield
sorted by magnitude, which is the canonical carry signal of this section.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
The bars, the regime annotations and the sector legend are built in one cell because the
inline backend flushes a figure at the end of the cell that created it; splitting the
legend into a later cell would display the bars before it is attached.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
---

# Part 2: Cross-Asset Structure and Relative Value

Cross-asset features model relationships *between* instruments:
- **Rolling beta**: Sensitivity to a common factor (market, sector)
- **Lead-lag**: Temporal structure across markets
- **Relative value**: Deviation from peer mean (z-scored)
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
## Load ETF Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
## Rolling Beta to Market

Rolling beta measures time-varying sensitivity to the market factor:

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
## Beta-Adjusted Residual Momentum

Isolate stock-specific momentum by subtracting market contribution:

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
