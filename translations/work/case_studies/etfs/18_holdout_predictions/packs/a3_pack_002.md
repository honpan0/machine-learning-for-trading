# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/18_holdout_predictions.ipynb；A3 Pack 002；單元 1 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Out-of-sample → 樣本外

## 待翻譯英文單元

### c0017-p000

~~~~~~markdown
## What this notebook establishes, and what it does not

It establishes one thing: a prediction set over the holdout window, produced by the
configuration this case study selected, fitted on data that ends a full label horizon before
the window opens. That is a precondition for an out-of-sample claim, not the claim itself.
Nothing here says whether the predictions are any good - they have not been scored, sized or
traded.

It does not make the holdout a fresh test in the strict sense. The configuration reached this
notebook through a selection made on the validation folds, and this window is being used once
per configuration that gets here. What it does remove is the specific circularity of scoring
a validation-fitted model on the period meant to judge it.

Re-running this notebook is free: the same configuration re-derives the same training identity and
the fit is served from the registry. Evaluating a DIFFERENT configuration is not, and is
refused here. If a later pass finds the selection was wrong, that is a question for the
registry's lifecycle, which records that a second look was taken - not something to settle by
deleting rows until the registry agrees.

**Next:** [[[ML4T_A3_0001]]](19_holdout_backtest.ipynb).
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>
