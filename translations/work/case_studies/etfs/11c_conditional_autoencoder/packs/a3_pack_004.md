# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11c_conditional_autoencoder.ipynb；A3 Pack 004；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Factor returns → 因子報酬率
- Label → 標籤

## 待翻譯英文單元

### c0023-p002

~~~~~~markdown

**Known limitations.** The architecture, the bottleneck width and the schedule are declared in
[[ML4T_A3_0001]] rather than searched, so nothing here says this network is the
right one - only what this one did. Fifty epochs is where training stops, not where anything
established it should stop. Two of the eight folds are negative on the primary label and one on
the five-day, and the fold-to-fold dispersion is essentially unchanged from IPCA's
(0.092 against 0.099), so the improvement is in the average rather than in how much any
single fold can be relied on. The panel narrows from 96 funds in the
first fold to 90 in the last. The published result is a CUDA result, and a reader who refits on
CPU gets a different identity registered beside it rather than the same numbers. And every number
here is measured on validation folds that have been read many times over by the time a case study
reaches this notebook.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p002>>>
<<<ML4T-ZH-END:c0023-p002>>>

### c0024-p000

~~~~~~markdown
**Next**: [[[ML4T_A3_0001]]](11d_stochastic_discount_factor.ipynb) leaves the
two-stage shape behind entirely - it prices the cross-section rather than splitting the problem
into exposures and factor returns - and
[[[ML4T_A3_0002]]](11e_supervised_autoencoder.ipynb) drops the factor
interpretation altogether and predicts the return from its bottleneck directly, which makes it
the one member fitted without the family's central assumption. Its network is not this one's -
it is deeper and wider, at a tenth of this learning rate - so the pair is not a controlled
comparison and that notebook does not read it as one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>
