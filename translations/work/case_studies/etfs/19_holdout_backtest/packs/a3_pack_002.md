# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/19_holdout_backtest.ipynb；A3 Pack 002；單元 1 個。


## 待翻譯英文單元

### c0012-p000

~~~~~~markdown
## What this notebook establishes, and what it does not

It establishes a return series for the selected configuration over a period no choice in this
case study was made on. That is the only thing a holdout can give, and it is worth less than
it looks: the window is short beside the validation span it is being compared with, which is
too few observations to separate a strategy that decayed from one that had an ordinary year.

It does not establish that this configuration was the right one to carry here. The selection
that brought it was made on validation, over a pool large enough that its maximum is
optimistic by construction, and this notebook inherits that pool without correcting for it.
The deflation is [[[ML4T_A3_0001]]](20_strategy_analysis.ipynb)'s.

Re-running this notebook against the same configuration is free and idempotent - the backtest hash
is unchanged and the registered run is served back. A different configuration is refused, for the
reason 18 gives.

**Next:** [[[ML4T_A3_0002]]](20_strategy_analysis.ipynb).
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>
