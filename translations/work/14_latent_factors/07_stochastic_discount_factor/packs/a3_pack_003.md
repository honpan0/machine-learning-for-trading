# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/07_stochastic_discount_factor.ipynb；A3 Pack 003；單元 2 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子

## 待翻譯英文單元

### c0063-p000

~~~~~~markdown
Validation MSE below train MSE in the upper panel does not mean the network
generalizes better than it fits. The two curves measure the same loss on
different samples of the beta target, the return-factor product, whose scale
is not constant across windows. Only movement along the validation curve
supports the checkpoint comparison.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0064-p000

~~~~~~markdown
## 8. Takeaways

1. **Timing defines the SDF.** Current ranked characteristics and delayed
   market state determine weights for the next trading day's excess returns.
2. **The sign matters.** The paper's factor is [[ML4T_A3_0001]];
   reversing it would reverse the economic interpretation of beta signals.
3. **Selection stops before test.** Validation chooses the SDF and beta
   checkpoints. Test enters only after both networks are frozen.
4. **Pricing and prediction differ.** Factor Sharpe and pricing errors assess
   the kernel; daily rank IC assesses the beta network's asset ordering.
5. **This remains an adaptation.** Daily data, a fixed training-defined liquid
   universe, current-snapshot FRED data, and gross-normalized weights make the
   mechanics inspectable but do not reproduce the paper's monthly experiment.

The next notebook,
[[[ML4T_A3_0002]]](08_supervised_autoencoder.ipynb), returns to a
supervised representation whose bottleneck is trained directly for prediction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>
