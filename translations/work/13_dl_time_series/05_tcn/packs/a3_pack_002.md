# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/05_tcn.ipynb；A3 Pack 002；單元 3 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Walk-forward validation → 滾動向前驗證
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0029-p000

~~~~~~markdown
The left panel measures cross-sectional ranking, while the right panel asks
whether either fitted model improves squared error over predicting zero. These
are distinct questions. This purged single split demonstrates the architecture;
it does not establish a stable model ranking. Section 13.9 supplies the
walk-forward comparison across datasets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0030-p000

~~~~~~markdown
## Key takeaways

1. **Causality is a property of the trim, and it is checkable.** [[ML4T_A3_0001]] pads
   both ends, so dropping the last [[ML4T_A3_0002]] outputs is what leaves the output at day
   [[ML4T_A3_0003]] a function of days up to [[ML4T_A3_0004]] and no later; differentiate an output position
   with respect to the inputs to confirm that, rather than trusting the argument
   name. It is not what keeps the target out of the input - the window does that,
   because every day in the window precedes the target date and the head reads only
   the final position. Causality is what would make each intermediate position a
   forecast for its own date, and this notebook uses only the last.
2. **Doubling the dilation each layer buys reach geometrically.** Stacking blocks
   whose dilation doubles makes the receptive field grow like [[ML4T_A3_0005]]
   rather than linearly, which is how four blocks reach across the whole window.
   The arithmetic is printed above rather than restated here, so it follows
   [[ML4T_A3_0006]] and the dilation schedule if either changes.
3. **Fully parallelizable**: Unlike LSTMs, all timesteps are processed
   simultaneously during both training and inference
4. **Fixed receptive field**: The maximum lookback is determined at design
   time by the dilation schedule -- unlike attention, which adapts dynamically
5. **Reference architecture matters**: Weight normalization, channel-wise
   dropout, and the final causal state preserve the TCN block's intended
   inductive bias without mixing batch statistics
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0030-p001

~~~~~~markdown

**Known limitations.** One chronological split of one ETF panel, one label horizon,
one seed, and a single dilation schedule - the receptive field was designed to cover
the window rather than searched for. The comparison is against one baseline, and a
single split cannot rank architectures; [[ML4T_A3_0001]] is where these
families are compared across case studies under walk-forward validation. The TCN
fitted there is a different block from this one: batch normalisation after each
convolution, plain dropout, and a mean over the whole window instead of the final
causal state ([[ML4T_A3_0002]]). Repeated
execution reproduces on the same software and GPU; another environment will differ in
the final decimals.

**Next**: [[ML4T_A3_0003]] drops convolution too, and gets at the same structure with
nothing but fully connected layers applied along one axis at a time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p001>>>
<<<ML4T-ZH-END:c0030-p001>>>
