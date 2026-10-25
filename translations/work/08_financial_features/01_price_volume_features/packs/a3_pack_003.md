# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/01_price_volume_features.ipynb；A3 Pack 003；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market regime → 市場狀態
- Momentum → 動能
- Sharpe ratio → 夏普比率
- Feature → 特徵
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0053-p000

~~~~~~markdown
### Volatility State Features

Volatility state features transform continuous vol into conditioning variables:

- **Vol ratio** (short/long): Detects expansion/contraction
- **Vol percentile**: Where current vol sits in its 252-day history
- **Vol decile**: Binned version for evaluation slicing
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0055-p000

~~~~~~markdown
### Price-Derived Regime Indicators

[[ML4T_A3_0001]] provides rolling statistical tests that detect market regime
changes without relying on parametric models (HMM, GARCH are in Chapter 9):

| Indicator | Test/Signal | Interpretation |
|-----------|-------------|----------------|
| **Variance Ratio** | Lo-MacKinlay RW test | >1 trending, <1 mean-reverting |
| **Fractal Efficiency** | Mandelbrot efficiency | 1=trending, 0=noise |
| **Trend Intensity** | ADX-like directional | High=strong trend |
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0057-p000

~~~~~~markdown
**Variance Ratio**: Values above 1 indicate positive autocorrelation (trending);
below 1 indicates mean-reversion. This is the Lo-MacKinlay (1988) test as a
rolling feature.

**Fractal Efficiency**: Measures path efficiency. One means price moves in a
straight line (trend), zero means random wandering.

**Note**: These are *rolling-window* regime indicators derived purely from price.
Parametric regime models (HMM, Markov-switching GARCH) appear in Chapter 9.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0058-p000

~~~~~~markdown
## Volume and Liquidity Features

Volume features proxy for:
- **Attention**: High volume = information event
- **Liquidity**: Capacity to trade
- **Conviction**: Volume confirms price moves
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0059-p000

~~~~~~markdown
### Dollar Volume

Raw volume is not comparable across assets. Dollar volume normalizes.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0061-p000

~~~~~~markdown
### Relative Volume

Volume relative to its recent average. >1 means above-average activity.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0064-p000

~~~~~~markdown
The two lower panels are different transformations, so the same numeric cut does not select
the same days. Measure that disagreement rather than assume it away.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0066-p000

~~~~~~markdown
The two lower panels are not one quantity in two units. Relative volume divides raw volume
by its own rolling mean; the z-score standardizes the **logarithm** of volume, which pulls
in the long right tail that volume always has. The counts printed above are what that costs:
the same numeric cut applied to each selects overlapping but different sets of days, and the
relative-volume level corresponding to a z-score at the cut is a range rather than a number.

The z-score is the one worth writing a rule against. A cut expressed in standard deviations
of log volume means the same thing on an instrument whose volume is more dispersed, while a
ratio threshold does not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0067-p000

~~~~~~markdown
### VWAP Distance

How far price has moved from the volume-weighted average price.
Useful for intraday strategies and execution.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p000>>>
<<<ML4T-ZH-END:c0067-p000>>>

### c0069-p000

~~~~~~markdown
**Interpretation**: Positive VWAP distance means the close is above the
volume-weighted average, so buying pressure exceeded selling pressure over the
lookback. Negative indicates the opposite. For intraday strategies this is a
key mean-reversion anchor; for daily data it proxies volume-weighted trend.
~~~~~~

<<<ML4T-ZH-BEGIN:c0069-p000>>>
<<<ML4T-ZH-END:c0069-p000>>>

### c0070-p000

~~~~~~markdown
## Cross-Sectional Normalization

For multi-asset strategies, raw features are not comparable. Normalization
creates standardized signals across the universe.

**Warning**: Cross-sectional operations can introduce leakage if not careful
about timing. Always use point-in-time data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0071-p000

~~~~~~markdown
### Cross-Sectional Ranks

Rank-based features are robust to outliers.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0071-p000>>>
<<<ML4T-ZH-END:c0071-p000>>>

### c0073-p000

~~~~~~markdown
### Vol-Scaled Cross-Sectional Momentum

The text's spec-table formula: cumulative return divided by realized volatility,
then cross-sectional percentile rank. Vol-scaling penalizes momentum driven by
high volatility: two assets that rose by the same amount are not equally interesting if
one of them did it with several times the dispersion of the other.

[[ML4T_A3_0001]] here is the annualized volatility estimated on a 21-day window, which is
what the [[ML4T_A3_0002]] column below holds and what a [[ML4T_A3_0003]] column means throughout this
repository: the standard deviation of daily returns over [[ML4T_A3_0004]] days, times [[ML4T_A3_0005]].
Writing the annualization into the formula is the point - without it the expression and
the [[ML4T_A3_0006]] column do not agree:

[[ML4T_A3_0007]]

The numerator is a 21-day cumulative return and the denominator is an annual rate, so
the ratio is not a standardized return and does not compare across horizons. The
feature pipelines build the same quantity and call it [[ML4T_A3_0008]]
([[ML4T_A3_0009]]), which is the convention
this cell follows. Scaling the denominator by any positive constant leaves the
cross-sectional percentile rank below unchanged, so [[ML4T_A3_0010]] is the same
either way; [[ML4T_A3_0011]] itself is not.
~~~~~~

<<<ML4T-ZH-BEGIN:c0073-p000>>>
<<<ML4T-ZH-END:c0073-p000>>>

### c0075-p000

~~~~~~markdown
**Interpretation**: Vol-scaling reshuffles the ranking. High-momentum assets
with elevated volatility drop, while steady trending assets rise. This is the
same intuition as the Sharpe ratio applied cross-sectionally.
~~~~~~

<<<ML4T-ZH-BEGIN:c0075-p000>>>
<<<ML4T-ZH-END:c0075-p000>>>
