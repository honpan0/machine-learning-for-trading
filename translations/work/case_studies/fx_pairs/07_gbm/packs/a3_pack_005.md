# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/fx_pairs/07_gbm.ipynb；A3 Pack 005；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Correlation → 相關性

## 待翻譯英文單元

### c0032-p004

~~~~~~markdown

**A near-zero negative is a weaker statement than a large negative.** In a case study where the
model reliably ranks the cross-section backwards, that is a relationship with the sign fitted the
wrong way, and it is informative. Here the magnitudes are small enough that the honest summary is
that this family does not rank this cross-section, in either direction, rather than that it
reliably gets it wrong.

**None of this selects anything.** IC measures whether predictions rank pairs correctly, not
whether a strategy trading them makes money after costs. Selection is on validation backtest
Sharpe over the population just published, in [[[ML4T_A3_0001]]](13_backtest.ipynb), where the
checkpoint is part of what is selected. A family that does not clear zero on IC enters that
comparison without a ranking advantage to defend, which is a fact about this notebook and not a
conclusion about the backtest.

**Known limitations.** The IC is an average of daily rank correlations with no adjustment for the
dependence between pairs that share a currency, which is exactly the structure described above -
so the effective number of independent observations behind each daily correlation is smaller than
the number of pairs. The five-day and 21-day labels add a second dependence the one-day label
does not have: consecutive decision dates share most of their forward window, so their daily
correlations are not independent draws. The grid varies capacity and loss at a fixed learning
rate, and five configurations per objective is a thin base for the objective comparison. And
every number is measured on validation folds already read many times by the time a case study
reaches this notebook.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p004>>>
<<<ML4T-ZH-END:c0032-p004>>>

### c0032-p005

~~~~~~markdown

**Next**: [[[ML4T_A3_0001]]](08_tabular_dl.ipynb) asks the same question of a neural network built
for tabular data. Two model classes have now been fitted to this cross-section, and the useful
thing to watch is whether a third fails in the direction the tree ensemble did, which would point
at the cross-section rather than at any one model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p005>>>
<<<ML4T-ZH-END:c0032-p005>>>
