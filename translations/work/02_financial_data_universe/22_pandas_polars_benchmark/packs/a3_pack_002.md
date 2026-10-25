# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/22_pandas_polars_benchmark.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Sharpe ratio → 夏普比率
- Feature → 特徵
- Cross-sectional → 橫斷面
- Standard deviation → 標準差

## 待翻譯英文單元

### c0025-p000

~~~~~~markdown
### A4: Rolling Sharpe Ratio

A compound calculation: a rolling mean divided by a rolling standard deviation,
annualized. It tests chained window operations, and it is where the two sides had
drifted apart. The pandas side took [[ML4T_A3_0001]] per symbol and then rolled the
resulting flat Series, so its window ran across the boundary between one symbol and
the next and averaged the two together; Polars had [[ML4T_A3_0002]] on both windows
and did not. The result was a chart comparing a per-symbol Sharpe against a Sharpe
that mixed symbols, and nothing in the notebook could have told you.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0028-p000

~~~~~~markdown
### A5: Exponential Moving Average

An exponentially weighted mean over [[ML4T_A3_0001]], the smoothing most trend-following
signals are built on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0031-p000

~~~~~~markdown
## Category B: GroupBy Aggregations

GroupBy operations are essential for cross-sectional analysis and resampling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
### B1: OHLCV Resampling (1-min to daily)

Aggregate minute bars to daily bars - common in bar construction pipelines.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0036-p000

~~~~~~markdown
### B2: Cross-Sectional Statistics by Date

Compute market-wide statistics for each timestamp.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
### B3: Symbol-Level Statistics

Per-symbol summary statistics across all time periods.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0042-p000

~~~~~~markdown
## Category C: Window Functions

Window functions compute values relative to other rows in a group.
These are essential for cross-sectional normalization.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0044-p000

~~~~~~markdown
### C1: Cross-Sectional Z-Score

Normalize returns relative to cross-section at each timestamp.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0047-p000

~~~~~~markdown
### C2: Percentile Rank

Rank each symbol's return within the cross-section at its timestamp, as a fraction.
The denominator is the count of ranked observations, which is what pandas'
[[ML4T_A3_0001]] uses. Dividing by the largest rank instead, which is what this used
to do on the Polars side, agrees only while nothing is tied at the top: average
ranking pulls the top rank below the count as soon as anything is, and the two
columns then differ everywhere in the group rather than only at the tie.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0050-p000

~~~~~~markdown
### C3: Lagged Values

One column per entry in [[ML4T_A3_0001]], the usual shape of an autoregressive feature set.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0053-p000

~~~~~~markdown
## Category D: Filtering

Filter operations select subsets of data based on conditions.
Complex predicates are common in options chain processing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0055-p000

~~~~~~markdown
### D1: Simple Price Filter
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0058-p000

~~~~~~markdown
### D2: Multi-Condition Filter

Combine price, volume, and symbol conditions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0061-p000

~~~~~~markdown
### D3: Range Filter (Options-Style)

Simulate filtering an options chain by moneyness and expiry.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>
