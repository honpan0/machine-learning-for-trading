# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/01_academic_characteristics.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Machine learning → 機器學習
- Deep learning → 深度學習
- Feature → 特徵
- Label → 標籤
- Time series → 時間序列
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Chen-Pelger-Zhu Academic Asset Pricing Dataset

**Chapter 4: Fundamental and Alternative Data**
**Docker image**: [[ML4T_A3_0001]]
**Section Reference**: Section 4.1 (The Point-in-Time Pipeline)

## Purpose

Research on machine learning for asset pricing is hard to reproduce because the underlying
firm data usually sits behind a WRDS subscription. Chen, Pelger and Zhu (2021) removed that
barrier by publishing the panel they used: fifty years of monthly US equity observations,
each carrying 46 firm characteristics and the return earned over the following month, with
company names and CRSP identifiers stripped out. This notebook reads that panel, shows what
is in it, and measures how strongly each characteristic lines up with next-month returns.

It is the reference dataset for the [[ML4T_A3_0002]] case study, so the shape,
the split boundaries and the normalization conventions established here are the ones every
model in that case study inherits.

## Learning Objectives

After completing this notebook, you will be able to:

- Load the published panel and report how many stocks it covers in each month of its history.
- Read the 46 characteristics as eight economic groups, and say which quantity each group measures.
- Confirm that a cross-sectional rank normalization has been applied, by checking the range
  each characteristic occupies.
- Measure the information coefficient - the rank correlation between a characteristic and the
  return that follows it - one month at a time, and average it over the training period.
- Correct the significance test on that average for the serial correlation between adjacent
  months, and say how far the correction moves it.
- State what the anonymous identifiers in this panel allow and what they rule out.

## Cross-References
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- **Downstream**: Ch11 [[ML4T_A3_0001]], Ch12 [[ML4T_A3_0002]]
- **Related**: Ch14 [[ML4T_A3_0003]]
- **Synthesis**: [[ML4T_A3_0004]]

## Prerequisites

Download the dataset before running this notebook:
[[ML4T_A3_0005]]

## Data Source

| Attribute | Value |
|-----------|-------|
| **Paper** | "Deep Learning in Asset Pricing" (Chen, Pelger, Zhu, 2021) |
| **Repository** | [[ML4T_A3_0006]] |
| **Features** | 46 firm characteristics, rank-normalized each month |
| **Returns** | Next-month excess returns, left in their original scale |
| **Period** | January 1967 to December 2016 |
| **Identifiers** | Anonymous array positions; each split uses its own numbering |

## Data Construction (from paper Section III.A)

### Stock Universe
- Source: All securities on CRSP
- Only stocks with all 46 characteristics available are included
- That requirement removes predominantly small-cap stocks with missing data
- The released panel covers roughly two thousand stocks in a typical month

### 46 Firm Characteristics
Characteristics are sourced from:
1. Kenneth French Data Library
2. Freyberger, Neuhierl, and Weber (2020)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0000-p002

~~~~~~markdown

**Categories** (cf. Table A.II in paper; this notebook groups them as):
- **Valuation**: BEME, E2P, S2P, CF2P, D2P, A2ME, Q
- **Profitability**: ROA, ROE, PROF, OP, PM, PCM, NI, RNA
- **Investment**: Investment, NOA, OA, AC, AT, D2A
- **Momentum / past returns**: r2_1, r12_2, r12_7, r36_13, ST_REV, LT_Rev, Rel2High
- **Risk**: Beta, MktBeta, IdioVol, Variance, Resid_Var
- **Liquidity / Size**: LME, LTurnover, Spread, SUV
- **Leverage**: Lev, OL, FC2Y, C, CF, DPI2A
- **Other**: ATO, CTO, SGA2S

**Construction**:
- Yearly variables: Updated end of June (Fama-French convention)
- Monthly variables: Updated end of month for use in next month
- All from CRSP/Compustat accounting data or CRSP past returns

### Macroeconomic companion series
The paper pairs the firm panel with 178 macroeconomic time series: 124 from the FRED-MD
database (McCracken and Ng, 2016), 46 cross-sectional medians of the firm characteristics
themselves, and 8 equity-premium predictors from Welch and Goyal (2007). Conditional models
such as the stochastic discount factor GAN of Chapter 14 use them as state variables. They
are distributed separately from the firm panel; assemble them from the paper repository and
join on [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p002>>>
<<<ML4T-ZH-END:c0000-p002>>>

### c0000-p003

~~~~~~markdown

### Cross-Sectional Rank Normalization
Following Kelly, Pruitt, Su (2019) and Kozak, Nagel, Santosh (2020), each characteristic is
ranked across all stocks within a month and the ranks are mapped onto the interval
[[ML4T_A3_0001]]. Two consequences matter for everything below.
Every characteristic then occupies the same range whatever its raw units were, so a
price-to-book ratio and a turnover rate enter a model on equal footing. And because the
ranking keeps only the ordering, an extreme raw value becomes an extreme rank rather than an
extreme number, which bounds the influence any one stock can have on a fitted coefficient.

## Key Concepts

- **Information coefficient (IC)**: the rank correlation, within one month's cross-section,
  between a characteristic and the return realized over the month that follows. It is the
  standard summary of how well a single signal orders stocks.
- **Excess return**: a return measured net of the risk-free rate. The [[ML4T_A3_0002]] column holds the
  excess return of the following month and is the quantity every model here predicts.
- **Anonymous identifier**: the [[ML4T_A3_0003]] column holds a firm's position on the axis of the
  array the authors published, which stands in for the company whose name was removed. It
  links a firm's observations across months within one split, and no further.

---
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p003>>>
<<<ML4T-ZH-END:c0000-p003>>>

### c0004-p000

~~~~~~markdown
---

## Section 1: What is in the panel

The published file holds one row per stock and month. Alongside the 46 characteristics it
carries [[ML4T_A3_0001]], the excess return of the following month, [[ML4T_A3_0002]], the train/validation/test
label assigned by the authors, and [[ML4T_A3_0003]], the anonymous integer identifier.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
The authors split the history by date rather than at random, which is the only split that
respects the arrow of time: a model is fitted on the earliest years, tuned on the middle
ones, and judged on the most recent. The boundaries below are read from the file rather
than assumed, because every figure in this notebook marks them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>
