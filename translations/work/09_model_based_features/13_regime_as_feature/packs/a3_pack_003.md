# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/13_regime_as_feature.ipynb；A3 Pack 003；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Clustering → 分群
- Volatility → 波動率

## 待翻譯英文單元

### c0029-p000

~~~~~~markdown
## Takeaways

1. **A regime feature has to be refit inside the fold that uses it.** Fitting the hidden
   Markov model once on the whole sample and then splitting the folds puts every fold's test
   block into the parameters of its own feature. The cost of doing it correctly is one fit per
   fold and a feature that disagrees with itself across folds on the sessions they share.
2. **Filtered probabilities, not smoothed ones.** [[ML4T_A3_0001]] and Viterbi decoding both
   condition on the whole sequence. The forward recursion conditions on the past, which is
   what a value computed on the day can know.
3. **Read the spread across folds before the mean.** The error moves more between folds than
   between designs here, and an averaged number with no spread beside it would have hidden
   that. Five nested folds cannot support a significance claim about the difference, however
   the pairing is done.
4. **The mixture of experts pays for its sharpness in sample size.** Each expert sees only its
   own regime's training rows, and a misrouted test session reaches a model that never saw its
   kind. The single model with a regime column degrades instead of switching.
5. **A low impurity importance on a regime column is a statement about the other columns.**
   Where [[ML4T_A3_0002]] is already a feature, a probability fitted on volatility adds little that
   a tree cannot reach directly. The same column ranks higher where the base features carry no
   volatility of their own.
6. **Check what each library expression consumes.** Half of the catalog above reads prices and
   differences them internally; handing those a return column produces a plausible number and
   no error.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0029-p001

~~~~~~markdown

**Previous**: [[ML4T_A3_0001]] fits the model whose probabilities this notebook spends, and
[[ML4T_A3_0002]] the clustering alternative. **Next**: [[ML4T_A3_0003]] moves from
one series to a cross-section.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p001>>>
<<<ML4T-ZH-END:c0029-p001>>>
