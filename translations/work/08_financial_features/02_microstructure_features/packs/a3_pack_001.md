# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/02_microstructure_features.ipynb；A3 Pack 001；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Cross-sectional → 橫斷面
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Microstructure Features

**Chapter 8: Feature Engineering**
**Section Reference**: 8.2 - Price-Derived Features (Microstructure)
**Docker image**: [[ML4T_A3_0001]]

## Purpose

Microstructure features capture market dynamics invisible in daily OHLCV data.
They proxy for **liquidity**, **information flow**, and **execution quality**.

## Learning Objectives

1. Compute trade-based liquidity features (Kyle λ, Amihud, Roll spread)
2. Understand order flow imbalance and its predictive content
3. Distinguish between **flow features** and **state features** (critical!)
4. Know which features are alpha vs feasibility/cost inputs

## Feature Categories

| Category | Features | Data Required |
|----------|----------|---------------|
| **Liquidity** | Kyle λ, Amihud, Roll | OHLCV bars |
| **Order Flow** | OFI, trade intensity | Trade data |
| **Book State** | Spread, depth | LOB snapshots |

## Data Policy

Uses **real NASDAQ ITCH data**. The notebook raises a clear error when ITCH
is missing rather than substituting a synthetic toy panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## Data Loading with Availability Check

Microstructure analysis requires high-frequency data. The loader raises
a clear error if ITCH is missing, with no silent fallback to synthetic data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0005-p000

~~~~~~markdown
The loader fails loudly when ITCH is missing rather than silently substituting a
synthetic toy panel, so a green run of this notebook means it read real trade data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0008-p000

~~~~~~markdown
Read the span printed above before reading any number in this notebook. The ITCH
fixture is a single session, so every statistic below is computed on one day of one
venue's trades. That is enough to show how each feature is built and what it responds
to, and it is not enough to establish anything about how these features behave in
general. Where a number would ordinarily invite a conclusion, the text says what the
sample can and cannot support.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
## Aggregate to Bars

Trade-based features work on aggregated bars (not tick-by-tick).
Common intervals: 1m, 5m, 15m for intraday; daily for cross-sectional.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Trade-Based Liquidity Features

These features require only OHLCV bars (widely available).
They proxy for market liquidity and trading costs.

| Feature | What the library computes here | Interpretation |
|---------|-------------------------------|----------------|
| Kyle λ | mean of \|r\| / (V / V̄), over the window | Return per unit of *relative* volume |
| Amihud | mean of \|r\| / DollarVol × 10⁶, over the window | Return per *million* dollars traded |
| Roll Spread | 2√(-Cov(ΔP_t, ΔP_{t-1})) | Implied bid-ask spread |

The Kyle row is the one to read carefully. [[ML4T_A3_0001]] takes a [[ML4T_A3_0002]] argument that
defaults to [[ML4T_A3_0003]], and [[ML4T_A3_0004]] raises [[ML4T_A3_0005]] in the
installed version, so what this notebook computes is the ratio approximation above and
not the regression slope of Kyle (1985). Both are called Kyle lambda. Only one of them
is a covariance, and it is not the one running here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
**Interpretation**: both measures are an absolute return divided by a volume, averaged
over the window, so neither carries a direction and the difference between them is
entirely in the denominator. Kyle's ratio divides by volume *relative to its own rolling
mean*; Amihud divides by dollar volume in dollars. Naming both "illiquidity" invites the
assumption that they agree, and the correlation printed under the next figure says how
far that holds on this session.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
### Kyle Lambda (Price Impact)

High Kyle λ means prices move a lot per unit of volume: the market is **illiquid**
and trades have high impact.

Kyle (1985) defines λ as the slope of returns on signed order flow, which is a
regression coefficient:

[[ML4T_A3_0001]]

The installed [[ML4T_A3_0002]] does not fit that regression. Its default [[ML4T_A3_0003]]
averages a per-bar ratio over the window instead, with volume normalized by its own
rolling mean:

[[ML4T_A3_0004]]

Read the second formula when reading the figure below, because the second formula is
what produced it. The two agree on the direction of "less liquid" and they are not the
same statistic: the ratio uses the absolute return and so has no sign, while the
regression slope does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
### Amihud Illiquidity

Amihud ratio measures absolute return per dollar traded. Higher = more illiquid.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
Both correlations are negative on this session, which the figure above shows directly:
Kyle lambda falls through the afternoon while Amihud rises to a midday peak before
dropping away. Two measures that a reader would reasonably expect to agree are moving
against each other, and the sign is the thing to notice rather than the magnitude, which
one session of one name does not pin down.

The denominators differ in one respect that is easy to check: what happens if every
volume is multiplied by a constant, returns and prices left alone. Kyle's ratio divides
volume by its own rolling mean, so the constant cancels. Amihud divides by dollar volume
in dollars, so the constant passes through. The cell below runs that substitution and
prints both ratios to the original.

Read it for what it is. It establishes that the two measures answer differently to the
units volume is quoted in, and it does not by itself explain the negative correlation
above, which arises from returns, prices and volumes all moving together across the
session. The cross-stock section later in this notebook does the decomposition that
explains the disagreement.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
What the substitution shows: Kyle's ratio is unchanged and Amihud moves by the
reciprocal of the factor. The measures are not on a common footing, and a threshold
tuned on one says nothing about the other.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
## Order Flow Imbalance (OFI)

OFI measures the buy-sell imbalance within a bar, proxying for **net order
flow**:

[[ML4T_A3_0001]]

**Important**: Without exchange-provided buy/sell labels we estimate the side
of each trade with the **tick rule** (Lee-Ready), classifying it buyer- or
seller-initiated from the sign of the price change. That classification has to
happen at the **trade** level, before aggregation, which is why
[[ML4T_A3_0002]] splits [[ML4T_A3_0003]]/[[ML4T_A3_0004]] there. Applying the tick
rule to a *bar's* single close would collapse OFI to the sign of that bar's
own return (+/-1), a tautology rather than a flow measure. This is the concrete
reason OFI is a **flow** feature that needs trade data, not a bar-OHLCV
feature which is the flow-versus-state distinction this chapter turns on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>
