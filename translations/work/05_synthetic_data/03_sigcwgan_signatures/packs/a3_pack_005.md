# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/03_sigcwgan_signatures.ipynb；A3 Pack 005；單元 1 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Clustering → 分群
- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0094-p001

~~~~~~markdown

The reference values are declared as [[ML4T_A3_0001]] in the configuration cell
and printed next to this run's Sig-W1 and TSTR figures in the evaluation cells.

The Sig-W1 scale depends on signature depth, augmentation choices, and the
magnitude of the input series, so direct numeric comparison to the paper is
only meaningful when those settings match. The values printed above in the
evaluation cell are the achieved metrics on the run in this notebook.

**Limitations**:

1. **Signature Cost**: O(d^depth) where d = path dimension after augmentations
2. **Small Universe**: 1-5 assets max at depth 4 (exponential scaling)
3. **Single Asset**: Paper only demonstrates on single-asset time series
4. **Higher-moment fidelity**: matching low-order expected signatures reproduces
   the marginal mean and variance but, in this unconditional depth-4 setup,
   under-produces fat tails, skewness, and volatility clustering (see the
   stylized-facts comparison in Section 13b)
~~~~~~

<<<ML4T-ZH-BEGIN:c0094-p001>>>
<<<ML4T-ZH-END:c0094-p001>>>
