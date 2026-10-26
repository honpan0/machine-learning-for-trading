# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/03_yield_curve_decomposition.ipynb；A3 Pack 002；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Transaction costs → 交易成本
- Time series → 時間序列
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0034-p000

~~~~~~markdown
**PC1 (Level)**: Approximately equal positive loadings across all maturities,
a near-parallel shift of the entire curve. This is the dominant mode of yield
variation, driven by changes in inflation expectations and the overall level
of interest rates.

**PC2 (Slope)**: Monotonically increasing loadings from short to long
maturities (negative at the short end, positive at the long end). Positive
PC2 corresponds to *steepening* (long rates rise more than short rates).
Slope variation reflects business-cycle dynamics: the curve typically flattens
during tightening cycles and steepens during easing.

**PC3 (Curvature)**: Opposite signs on the middle of the curve versus the
ends, a "butterfly" twist where intermediate maturities move differently
from the short and long ends. This factor reflects nuances in term-premium
pricing and convexity effects.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0035-p000

~~~~~~markdown
## 7. Scree Plot
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
The first component dominates, three components capture essentially all of
the variance, and components beyond PC3 add negligible explanatory power.
The yield curve's effective dimension is three, exactly the Level / Slope /
Curvature structure documented in Litterman & Scheinkman (1991) for the US
Treasury market.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0038-p000

~~~~~~markdown
## 8. Factor-Shock Time Series

PCA was fitted to yield *changes*, so its scores are daily shocks rather than
yield levels. Dividing each score by its fitted standard deviation places the
three components on a comparable scale. A 63-observation rolling mean reveals
sustained directions in recent curve changes without relabeling those changes
as the level or inversion state of the curve.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0041-p000

~~~~~~markdown
The rolling Level shock turns strongly negative during rapid easing and positive
during tightening episodes. The Slope and Curvature series isolate recent
steepening/flattening and butterfly directions. These are descriptive changes,
not recession signals or estimates of the current curve level; interpreting the
economic cause of any episode requires information outside this PCA.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
## 9. Reconstruction Quality

The reconstructed yield changes use the first [[ML4T_A3_0001]] components:

[[ML4T_A3_0002]]

where [[ML4T_A3_0003]] is the [[ML4T_A3_0004]] score matrix and [[ML4T_A3_0005]] the [[ML4T_A3_0006]] loading matrix.
With three factors explaining essentially all of the variance, reconstructed
changes should closely track actuals across every maturity.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0046-p000

~~~~~~markdown
**Reading it**: the right panel's bars are the question - each is a maturity's
reconstruction error as a share of how much that maturity actually moves, so a low bar
means the three factors carry most of that maturity's variation and a high one means
they do not. Comparing bars across maturities is what the normalisation makes possible;
comparing raw RMSE would just rank maturities by volatility.

The left panel is the same fact at daily resolution, and it is worth looking at
alongside the bars: a maturity can have a respectable aggregate error and still miss
individual days badly. Whatever is left over is variation the three-factor basis does
not represent, and PCA on its own says nothing about what causes it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0047-p000

~~~~~~markdown
## 10. Practical Application: Generalized Duration

The low-dimensional structure enables efficient hedging. Rather than managing
exposure to dozens of individual bonds, a portfolio manager neutralizes three
factor exposures: level, slope, and curvature sensitivity:

1. **Level Duration**: Sensitivity to parallel shifts (traditional DV01)
2. **Slope Duration**: Sensitivity to curve steepening/flattening
3. **Curvature Duration**: Sensitivity to butterfly twists

This "generalized duration" framework enables more precise hedging using
liquid instruments (Treasury futures, interest rate swaps) that target
specific yield curve movements. See Chapter 14, Section 14.4 for the full
hedging discussion.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0048-p000

~~~~~~markdown
Each loading is in standardized-yield space, which is the wrong unit for a hedge. The
conversion below puts it back into basis points, which is what a key-rate DV01 profile
is quoted in, so the two can be multiplied to get an exposure per unit of factor score.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0052-p000

~~~~~~markdown
**Finding**: In this local linear example, positions in three independent
key-rate instruments reduce all three fitted factor exposures to numerical
zero. This is an algebraic exposure match, not a backtest. A production hedge
must map the target weights to actual futures or swaps and account for
convexity, carry, basis risk, liquidity, and transaction costs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0053-p000

~~~~~~markdown
## Key Takeaways

1. **Eight maturities, three directions that matter.** The cumulative variance figure
   is where that claim is checked, and the printed shares say how the total splits
   across the three. The loading shapes are the Level, Slope and Curvature structure
   Litterman and Scheinkman documented in 1991, and the moving-block bootstrap says how
   much of each shape is pinned down by this sample rather than by the resampling.

2. **Low-dimensional macro drivers**: The yield curve's compressibility
   reflects that its underlying drivers (inflation expectations, business
   cycle, term premium) are themselves low-dimensional, in sharp contrast
   to equities, where thousands of idiosyncratic factors operate alongside
   a smaller systematic core.

3. **Practical hedging**: The illustrative key-rate example shows how three
   independent hedge directions can neutralize fitted Level, Slope, and
   Curvature exposure. It is a local sensitivity calculation, not evidence of
   realized hedge performance.

**Next**: See [[[ML4T_A3_0001]]](04_ipca.ipynb) for time-varying factor models that extend PCA
by conditioning on observable characteristics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>
