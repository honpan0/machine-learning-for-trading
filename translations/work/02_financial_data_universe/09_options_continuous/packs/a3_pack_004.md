# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/09_options_continuous.ipynb；A3 Pack 004；單元 1 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Transaction costs → 交易成本
- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0048-p001

~~~~~~markdown

5. **Same-contract returns are the correct label.** Pricing the entry contract in the raw
   chain h days later gives the P&L of a trade someone could have placed. The correlation
   between that and the naive chained return is low enough that a label built from the naive
   series is mostly a record of the selection rule.

6. **Zeroing roll-day returns deletes real P&L.** On a roll day you held yesterday's
   contract, and it moved; that move is a return, not a transaction. The held contract is
   recoverable from the raw chain on every roll day here, and over a single year the two
   reconstructions differ by tens of percentage points of cumulative return from identical
   prices. The discarded returns do not average to zero, so the error is one-sided and it
   compounds over the majority of the sample. The continuous series should take the held
   contract's return.

7. **Roll costs are transaction costs, not returns.** The bid-ask actually crossed to switch
   contracts is execution cost, accounted in Chapter 18 rather than inside the price series.
   That is what a roll-day adjustment is for; it is not a licence to delete the day.

## Next

The S&P 500 options case study
([[[ML4T_A3_0001]]](../case_studies/sp500_options/02_labels.ipynb)) builds its labels with the
same-contract construction from Section 3, priced from the raw chain, across the full
universe and a multi-year sample. It is a label pipeline rather than a backtest, so it has no
continuous mark-to-market series and does not need one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p001>>>
<<<ML4T-ZH-END:c0048-p001>>>
