# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/04_dml_crypto_regime.ipynb；A3 Pack 003；單元 4 個。


## 待翻譯英文單元

### c0035-p000

~~~~~~markdown
## Key Takeaways

1. **The treatment has a mechanism.** A stretched premium makes the long side of the
   perpetual expensive through funding, which is a reason to expect the premium to
   compress and, less directly, a reason to expect something of the return. The first of
   those is what [[ML4T_A3_0001]] estimates; this notebook takes the second.

2. **The standard error decides what the estimate can support**, more than the estimator
   does. The inflation printed above is the ratio between the iid standard error and one
   that treats each 8-hour bar as a single period rather than nineteen, and the interval
   it produces is what the effect has to clear.

3. **A regime difference needs one model, not two.** Adding the two subgroup variances
   assumes the estimates are independent draws, which disjoint subsets of one market are
   not; and a subgroup fitted on its own episodes has no unbroken time grid for its
   standard error to count on. The interaction on the residualized full sample avoids both
   problems, giving the difference and its standard error from a single fit on every bar.

4. **A block permutation is only a block permutation if the blocks run along time.** On
   this panel a bare [[ML4T_A3_0002]] would shuffle within a bar. The sweep over one, seven
   and fourteen days is worth reading precisely because the blocks now differ.

5. **A placebo is only comparable to the estimate on a common scale.** Permuting the
   treatment also frees it from the controls, so the placebo estimator has a much larger
   denominator than the one being tested. Comparing t-statistics puts both on the scale
   their own standard errors define; comparing effect sizes compares two different
   estimators and reports the difference as evidence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0035-p001

~~~~~~markdown

**Next**: [[[ML4T_A3_0001]]](05_momentum_causal_trading.ipynb) turns
regime-conditional effects into position sizes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p001>>>
<<<ML4T-ZH-END:c0035-p001>>>

### c0036-p000

~~~~~~markdown
## 11. Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
**Reading the table.** The "Bias vs DML" column is how far the unadjusted slope sits from
the adjusted one, as a share of the adjusted estimate; it measures what the six controls
were carrying, not how much of the remaining estimate is causal. The regime rows and the
interaction below them answer whether the effect differs between calm and volatile
markets, and the interaction is the one with a standard error that accounts for both rows
coming from the same market.

The block permutation builds the null the estimate is compared against. Permuting within
symbol along each symbol's own bars keeps the treatment as persistent as it really is,
which widens that null; a shuffle that destroys the persistence would narrow it and make
the estimate easier to distinguish from a placebo than the data warrants. The null is a
null of t-statistics for the reason given in section 9: a permuted treatment is no longer
absorbed by the controls, so its residual variance - the second stage's denominator - is
an order of magnitude larger than the observed treatment's, and raw placebo effects are
smaller than the observed effect for arithmetic that has nothing to do with causality.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>
