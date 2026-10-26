# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/07_stochastic_discount_factor.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Volatility → 波動率

## 待翻譯英文單元

### c0030-p000

~~~~~~markdown
With the paper's sign convention, the factor is the portfolio return and the
pricing kernel is one minus that return.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
Pricing moments are averaged through time for each asset and instrument.
Availability weights keep short-lived assets from receiving equal influence
to those observed throughout the segment.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
Validation carries both LSTM states forward from training. Test is deliberately
absent from this helper, so it cannot influence adversarial checkpoints.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
## 4. Three-phase estimation

Phase 1 warm-starts the SDF against constant instruments. Losses are shown in
scientific notation because squared pricing moments are naturally small; a
fixed scale is used only for gradient magnitude.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
Each adversarial round first freezes the SDF and maximizes conditional pricing
errors with respect to the instruments.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
The conditional phase freezes the instruments and updates SDF weights.
Validation factor Sharpe selects a deep-copied checkpoint.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0043-p000

~~~~~~markdown
The training display contains only training and validation information. Test
has not yet been passed through either network.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
## 5. Frozen SDF evaluation

The selected SDF now runs sequentially through train, validation, and test.
This is the first test access. The factor is [[ML4T_A3_0001]], not [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0048-p000

~~~~~~markdown
Test pricing errors summarize [[ML4T_A3_0001]] for each asset. The figure below
plots the mean signed error inside each decile of the per-asset distribution.
Whether a small subset carries the residual moment violations is a question
about magnitude, so it is answered by the printed concentration share rather
than by the signed deciles.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
## 6. Beta-network predictive head

The beta target is the contemporaneously aligned product
[[ML4T_A3_0001]]. Scaling by the training factor volatility improves
optimization but does not change asset ranks.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0052-p000

~~~~~~markdown
Beta checkpoints minimize validation MSE with the LSTM state carried from the
training segment. Test is not read during this second selection step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
This validation helper runs only the training and validation segments and
preserves their chronological LSTM state.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0057-p000

~~~~~~markdown
The frozen beta network now reaches test for the first time. Rank IC is
computed separately for each return date and summarized with a HAC interval.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0060-p000

~~~~~~markdown
## 7. Test diagnostics

Factor Sharpe and pricing errors assess the learned pricing object. Beta rank
IC asks the separate forecasting question. Neither diagnostic substitutes for
the other.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>
