# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/01_data_quality_diagnostics.ipynb；A3 Pack 003；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Time series → 時間序列

## 待翻譯英文單元

### c0057-p000

~~~~~~markdown
## Normality Testing

The **Jarque-Bera test** jointly tests whether skewness and kurtosis match
a normal distribution. Financial returns almost always reject normality
due to fat tails and asymmetric distributions.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0059-p000

~~~~~~markdown
SPY daily returns strongly reject normality ([[ML4T_A3_0001]]), driven by
excess kurtosis (fat tails). This confirms that robust scaling and
winsorization - not standard z-scoring - are appropriate for financial
returns. See [[ML4T_A3_0002]] for winsorization in practice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0060-p000

~~~~~~markdown
### Stationarity Quick Check

Prices are non-stationary (they trend); returns are typically stationary.
This validates using returns, not prices, as ML features and labels.
Stationarity testing is covered formally in Chapter 9.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0062-p000

~~~~~~markdown
Prices carry a unit root and returns do not, which is what the standard practice of
feeding models returns (or differences) rather than levels rests on. Chapter 9 covers
formal time series analysis including ADF, KPSS, and Phillips-Perron tests.

KPSS reports its p-value from a lookup table, and a statistic outside that table's
range gets the nearest tabulated bound rather than an interpolated value. The cell
above silences the resulting [[ML4T_A3_0001]] for this one module: the consensus
label turns on which side of the critical value the statistic falls, not on the
p-value's fourth digit, so the clipping changes nothing that is read here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0062-p000>>>
<<<ML4T-ZH-END:c0062-p000>>>

### c0063-p000

~~~~~~markdown
## Key Findings

Based on the diagnostic survey, the datasets fall into two groups:

**Ready for direct use** (no structural cleaning needed):
- **ETFs** - complete OHLCV coverage; outlier flags reflect Yahoo adjustment artifacts.
- **Crypto perpetuals and premium** - complete coverage, 8-hour-aligned timestamps.
- **CME futures** - session-aligned bars across every product, with no null closes.
- **Firm Characteristics** - column-level coverage is complete by construction;
  downstream models inherit the source paper's coverage rule.

**Require active preprocessing** (see [[ML4T_A3_0001]]):
1. **US Equities** - a penny-stock filter, extreme-return handling, and price-spike
   review. Every row the return threshold flags is an *upward* move, so corporate
   actions should be taken from [[ML4T_A3_0002]] rather than inferred from return size;
   see the split analysis under **US Equities** above.
2. **FX Pairs** - almost every weekend timestamp is a Sunday reopen bar at or after
   the reopen hour and stays in the panel. Only the Saturday and Sunday-daytime bars
   are anomalies to filter before the spot-vs-forward analytics in Section 7.2.

The two lists above are qualitative on purpose. The cell below sizes them from the
stored diagnostics, so the figures move with the run instead of ageing inside a
sentence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0065-p000

~~~~~~markdown
The next notebook applies these cleaning steps and demonstrates split-aware
preprocessing to prevent information leakage.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0066-p000

~~~~~~markdown
## Key Takeaways

1. **Index integrity** is fundamental - time monotonicity and uniqueness must pass,
   and the check has to be capable of failing: sorting a frame before asking whether
   it is sorted returns True for every input
2. **Column coverage is not panel coverage** - a dataset can report complete columns
   while whole rows are absent, because a null count only sees rows that exist
3. **Domain violations** (negative prices/volume) indicate data quality issues
4. **Detect events from the column that records them** - [[ML4T_A3_0001]] identifies
   splits directly, while a [[ML4T_A3_0002]] threshold is one-sided by construction and
   misses nearly every forward split
5. **Calendar alignment** matters for FX (weekends) and crypto (24/7)

**Next**: See [[ML4T_A3_0003]] for cleaning and split-aware preprocessing.
**Book**: Section 7.1 discusses why data quality determines model quality.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>
