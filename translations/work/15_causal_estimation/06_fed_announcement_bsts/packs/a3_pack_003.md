# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/06_fed_announcement_bsts.ipynb；A3 Pack 003；單元 1 個。


## 待翻譯英文單元

### c0044-p000

~~~~~~markdown
## Key Takeaways

1. **BSTS constructs a counterfactual** from pre-event target-control
   relationships and reports the post-event gap with posterior uncertainty.
2. **The cumulative estimand has return units** because the model uses daily log
   returns; summing post-period point effects yields cumulative abnormal log return.
3. **Placebo and control-as-target tests are diagnostics, not proofs**. Passing
   their interval rules does not establish that global controls are unaffected.
4. **Daily timing remains a limitation**. A close-to-close event-day return mixes
   trading before and after the afternoon announcement.
5. **A placebo date is only a placebo if its window is one.** The dates here are screened
   against the four announcements this notebook studies, and against nothing else; CPI
   prints, payrolls and refunding announcements still sit inside some of these windows,
   and window length remains untested at a single pre and post setting.

Continue with [[ML4T_A3_0001]] for time-series causal discovery. See
Section 15.5 for BSTS identification assumptions and event-study interpretation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>
