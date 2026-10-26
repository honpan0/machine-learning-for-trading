# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/03_econml_dml.ipynb；A3 Pack 003；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Label → 標籤
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0025-p001

~~~~~~markdown

**What cancelling the scale does not buy.** It removes one known bias and does not make the
test calibrated. A permutation test is valid when the permuted labels are exchangeable under
the null, and a treatment that persistent confounders predict is not: the shuffle breaks the
confounding along with the effect, so an estimate that is itself biased sits far from its own
permutation null and the test reports that distance. Measured on twelve synthetic panels with
a true effect of exactly zero and persistent AR(1) confounders, the studentized comparison
still rejects at the conventional five percent level on five of the twelve, against eleven for
the raw-effect comparison. [[ML4T_A3_0001]] carries that measurement. Read the count below as a comparison against a shuffle
rather than as a significance level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p001>>>
<<<ML4T-ZH-END:c0025-p001>>>

### c0027-p000

~~~~~~markdown
**The z-score and the p-value can disagree, and the count is the one that holds.** The
z-score measures how far the observed t-statistic sits from the placebo *mean* in placebo
standard deviations, which is a statement about a normal distribution centred where the
placebos are. The permutation p-value counts how many placebo draws reach its magnitude.
When the placebo distribution is not centred near zero the two answer different questions,
and only the count is a statement about the null the test actually built. Read the count
printed above, and the mean and standard deviation beside it, before reading the z-score.

**This null is not centred at zero, and that is worth looking at rather than reporting.**
A permutation that implemented "no association" would put the placebo statistics around
zero. Two obvious explanations do not survive a check: demeaning the fitted residuals by
symbol leaves the placebo estimates positive, and so does demeaning them by date, so
neither a preserved between-symbol nor a preserved between-date component accounts for it.
What does is not settled here. Until it is, the count is the statistic to read - it asks
how often a permuted treatment reaches the observed statistic, which stays a fair question
whatever the distribution's centre - and the z-score, which measures distance from that
centre in placebo standard deviations, is a statement about a distribution the test has not
explained.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0028-p000

~~~~~~markdown
The two halves are cut at a decision time rather than at a row, so neither holds a
fragment of a cross-section. That is the same reason the subsample near the top keeps
whole dates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
## 6. Nuisance Model Sensitivity

DML results depend on the quality of nuisance models. Let's compare different choices.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
## 7. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
## Key Methodological Points

### The four choices that decide whether the estimate means anything
1. **Cross-fitting with purging and embargo**, over decision times rather than rows.
   Purging drops training rows whose labels overlap the test window; the embargo adds a
   buffer after it (Chernozhukov et al. 2017, de Prado 2018).
2. **Driscoll-Kraay standard errors**, so the serial-correlation correction is applied
   along time and the cross-sectional dependence within a date is absorbed rather than
   counted as extra observations.
3. **Block permutation within entity**, so the placebo distribution is built from a
   treatment that keeps its persistence.
4. **A nuisance-model sweep**, because the point estimate depends on the first stage and
   the spread across specifications is the honest width of the finding.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0035-p000

~~~~~~markdown
### Three Intervals on One Effect

The notebook produces three statements of uncertainty about the same quantity, and they do
not agree. EconML's [[ML4T_A3_0001]] treats the residualized observations as independent
draws. The manual DML path reports a Driscoll-Kraay standard error, which aggregates by
decision time and absorbs whatever the ETFs share on a day. The permutation test compares
the estimate against a null built by shuffling the treatment within each ETF.

The spread between them is not a defect in any one of them. It is the price of the panel:
an interval is only as good as its account of what is independent, and 52,000 ETF-days are
not 52,000 independent observations.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
## Key Takeaways

1. **DML is an adjusted estimate, not a free lunch**. The orthogonalized
   coefficient is interpretable as a causal effect only under the maintained
   assumptions: pre-treatment controls are sufficient, positivity holds, no
   interference, and the specified DAG is correct.

2. **The robust standard error has to match the data's axis.** Overlapping 21-day labels
   make the iid standard error too small, and on a stacked panel the ordinary Newey-West
   correction fixes that along the wrong axis: its lags run across the cross-section.
   Driscoll-Kraay aggregates by decision time first, which is what the SE inflation
   printed above measures.

3. **Manual DML matches EconML conceptually and differs numerically.** The point estimate
   moves with nuisance-model flexibility, and the sweep in section 6 shows by how much.
   Neyman orthogonality is a guarantee about first-order sensitivity to nuisance error,
   not about agreement across nuisance choices.

4. **A refutation counts in the units its name claims.** Block permutation preserves
   autocorrelation only when the blocks run along an entity's own trading days; on a
   flattened panel the same call permutes a slice of one day's cross-section, which is
   the iid shuffle the test exists to avoid. The same is true of the walk-forward folds
   and of the temporal halves.

5. **The sign of the confounding bias is a result, not a rule.** Here the controls change
   the momentum slope in one direction; on the crypto funding premium in
   [[ML4T_A3_0001]] they change it in the other. The comparison printed above says
   which happened on this data, and it is the printed numbers, not this sentence, that
   settle it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>
