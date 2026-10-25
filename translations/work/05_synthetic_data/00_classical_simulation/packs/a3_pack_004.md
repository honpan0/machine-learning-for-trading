# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/00_classical_simulation.ipynb；A3 Pack 004；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Out-of-sample → 樣本外
- Cross-validation → 交叉驗證
- Clustering → 分群
- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0059-p000

~~~~~~markdown
---
# Part 3: Bootstrap Methods

Bootstrap methods resample historical data rather than assuming a parametric
model. They preserve the **empirical distribution** exactly, including fat tails.

| Method | Block Size | Preserves Autocorrelation | Best For |
|--------|-----------|--------------------------|----------|
| **IID Bootstrap** | 1 | No | i.i.d. assumption OK |
| **Block Bootstrap** | Fixed | Yes (within blocks) | Time series |
| **Stationary Bootstrap** | Random | Yes (smoother) | Financial returns |

### Key Trade-off

- **Parametric**: Can generate scenarios *beyond* historical range
- **Bootstrap**: Preserves empirical distribution *exactly* but limited to observed extremes

### Consistency Note

We bootstrap **log-returns** to match the parametric models above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0060-p000

~~~~~~markdown
## Load Real Data for Bootstrap
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0062-p000

~~~~~~markdown
## IID Bootstrap

The simplest resampling method: draw individual returns **with replacement**.

### Algorithm

[[ML4T_A3_0001]]

### Properties

- **Preserves marginal distribution**: Same histogram as original
- **Destroys autocorrelation**: Each draw is independent
- **Fast and simple**: No tuning parameters
~~~~~~

<<<ML4T-ZH-BEGIN:c0062-p000>>>
<<<ML4T-ZH-END:c0062-p000>>>

### c0064-p000

~~~~~~markdown
Draw one IID bootstrap sample the same length as the original series and
compare its moments with the original's.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0066-p000

~~~~~~markdown
### Library Usage: IID Bootstrap
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0068-p000

~~~~~~markdown
## Block Bootstrap

Resample **contiguous blocks** of fixed length to preserve local dependence.

### Algorithm (Moving Block Bootstrap)

[[ML4T_A3_0001]]

### Block Length Selection

- Rule of thumb: [[ML4T_A3_0002]]
- Financial: ~22 days (one month) is common
- Optimal: Cross-validation on out-of-sample statistics
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0070-p000

~~~~~~markdown
Use 22-day blocks, roughly one trading month.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0072-p000

~~~~~~markdown
### Library Usage: Block Bootstrap
~~~~~~

<<<ML4T-ZH-BEGIN:c0072-p000>>>
<<<ML4T-ZH-END:c0072-p000>>>

### c0074-p000

~~~~~~markdown
## Stationary Bootstrap

Uses **random block lengths** from a geometric distribution, eliminating
artificial block boundaries.

### Algorithm (Politis & Romano 1994)

[[ML4T_A3_0001]]

### Why "Stationary"?

With random block lengths, the bootstrap distribution is **stationary** -
each position in the sample has the same marginal distribution.
~~~~~~

<<<ML4T-ZH-BEGIN:c0074-p000>>>
<<<ML4T-ZH-END:c0074-p000>>>

### c0076-p000

~~~~~~markdown
Use the same expected block length so the two block methods differ only in
whether the length is fixed or random.
~~~~~~

<<<ML4T-ZH-BEGIN:c0076-p000>>>
<<<ML4T-ZH-END:c0076-p000>>>

### c0078-p000

~~~~~~markdown
### Library Usage: Stationary Bootstrap
~~~~~~

<<<ML4T-ZH-BEGIN:c0078-p000>>>
<<<ML4T-ZH-END:c0078-p000>>>

### c0080-p000

~~~~~~markdown
## Bootstrap Method Comparison
~~~~~~

<<<ML4T-ZH-BEGIN:c0080-p000>>>
<<<ML4T-ZH-END:c0080-p000>>>

### c0082-p000

~~~~~~markdown
## Autocorrelation Preservation

The key difference between bootstrap methods is how they handle **temporal
dependence**. We measure this via autocorrelation of **squared returns**
(signature of volatility clustering).
~~~~~~

<<<ML4T-ZH-BEGIN:c0082-p000>>>
<<<ML4T-ZH-END:c0082-p000>>>

### c0084-p000

~~~~~~markdown
### How Much Dependence Each Method Retains

The ACF curves above come from one resample each, and one resample cannot rank
two methods that differ only in whether the block length is fixed or random.
Summarize each resample by the sum of its squared-return autocorrelations over
the first [[ML4T_A3_0001]] lags, divided by the same sum for the original series, and
repeat it [[ML4T_A3_0002]] times per method. A value of one means the
resample carries as much volatility clustering as SPY; zero means none.
~~~~~~

<<<ML4T-ZH-BEGIN:c0084-p000>>>
<<<ML4T-ZH-END:c0084-p000>>>
