# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/02_asset_embeddings.ipynb；A3 Pack 003；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Covariance → 共變異數

## 待翻譯英文單元

### c0044-p000

~~~~~~markdown
## Applications

Asset embeddings enable practical applications:

### 1. Stock Substitution
Find replacement stocks when constraints prevent trading the original.

### 2. Portfolio Diversification
Measure true diversification: positions far apart in embedding space
are more diversified than those close together.

### 3. Crowding Detection
Track how embeddings evolve; stocks moving toward dense regions
may face crowding-related headwinds.

### 4. Risk Modeling
Embedding similarity captures relationships not visible in returns covariance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0046-p000

~~~~~~markdown
## Key Takeaways

1. **Word2Vec applies beyond text**: Portfolios as sentences, stocks as words.

2. **Skip-gram learns from position ordering**: Stocks at similar portfolio
   positions (by weight) get similar embeddings.

3. **Gabaix et al. (2025) frame holdings as informationally sufficient** for
   asset pricing. This notebook does not reproduce that proof; it
   implements one of the paper's embedding methods (Skip-gram on portfolio
   sentences) and reproduces the masked-asset benchmark protocol on a
   single-quarter 13F snapshot of ~500 portfolios. The notebook's own
   measurements are the Hits@k and MRR values printed above, with
   bootstrap CIs and the vs-random improvement multiple.

4. **Keep the paper's numbers and the notebook's apart.** Gabaix et al. report results on
   valuation variance and a comparison against text-only embeddings that nothing here
   measures. This notebook's own measurements are the per-bucket recovery rates, the pooled
   rate and its bootstrap interval, and the improvement multiple over the random baseline.
   Read the paper for the rest rather than inferring it from these.

5. **Practical applications**: Stock substitution, diversification,
   crowding detection, and enhanced risk models.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>
