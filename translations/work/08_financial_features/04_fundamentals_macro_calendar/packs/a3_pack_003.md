# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/04_fundamentals_macro_calendar.ipynb；A3 Pack 003；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵
- Label → 標籤

## 待翻譯英文單元

### c0050-p000

~~~~~~markdown
**Interpretation**: Time-to-event serves as a **state variable**: a label
that partitions trading days into discrete proximity windows
(pre-2d, pre-5d, normal, far). These windows feed downstream signal × state
interactions (see [[ML4T_A3_0001]] for the IC-conditioning
pattern); this notebook covers only the encoding step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
## Summary

### Fundamentals
- **Value**: Book-to-market, earnings yield, CF yield
- **Quality**: ROE, ROA, accruals ratio
- **Alignment**: ASOF join with both frames sorted by [[ML4T_A3_0001]]
- **Scaffolding**: Market cap approximation is for teaching only

### Macro
- **Publication lag**: Add 30-day lag for monthly data
- **Forward-fill**: Use filled version for YoY/3m changes
- **Naming**: Rolling median [[ML4T_A3_0002]] percentile rank (be precise)
- **Risk regimes**: VIX thresholds, credit regime from spread levels

### Calendar
- **Cyclical encoding**: sin/cos for month, day-of-week, time-to-event
- **Phase, not outcome**: Encode timing, not post-event realized moves

### Key Patterns

| Feature Type | Update Freq | Alignment | Use Case |
|--------------|-------------|-----------|----------|
| Fundamentals | Quarterly | ASOF by announcement | Factor signals |
| Macro | Daily/Monthly | Forward-fill + lag | Context, regime |
| Calendar | Deterministic | Direct encoding | Seasonality |

### Next Notebooks

- [[ML4T_A3_0003]]: feature selection and deduplication (§8.6)
- [[ML4T_A3_0004]]: regime conditioning and interactions (§8.6)
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>
