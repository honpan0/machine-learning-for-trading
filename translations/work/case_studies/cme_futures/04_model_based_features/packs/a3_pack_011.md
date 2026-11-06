# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/04_model_based_features.ipynb；A3 Pack 011；單元 1 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0104-p002

~~~~~~markdown

**Known limitations.** The average carry the regime model reads is taken over whichever
products settled, with a two-session hold for the rest, so it is not a fixed basket;
section C.3 measures how much of the gap that hold covers and how much it does not. The
screen in section F cannot measure the two regime features at all, because they do not
vary across products within a session, so what those features are worth is not settled
here. Each estimate is held fixed until the next refit, so a break occurring inside a
block is read by parameters estimated before it - at worst a quarter for the regime chain
and a month for ARIMA. Across the holdout both are frozen at their last pre-boundary
estimate, which is the price of not estimating anything on it. And the burn-in prefix
carries no value at all: the oldest period trains from the first session of the panel, so
C.3 prints how many of that period's training sessions the regime chain's 504-session
burn-in costs.

**Writes**: [[ML4T_A3_0001]], keyed on [[ML4T_A3_0002]],
with its fingerprint recorded alongside.

**Next**: [[[ML4T_A3_0003]]](05_evaluation.ipynb) weighs these features against the ones
from [[[ML4T_A3_0004]]](03_financial_features.ipynb); the model notebooks from
Chapter 11 onward read both files together.
~~~~~~

<<<ML4T-ZH-BEGIN:c0104-p002>>>
<<<ML4T-ZH-END:c0104-p002>>>
