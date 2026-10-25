# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/07_multiple_testing.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0021-p000

~~~~~~markdown
[[ML4T_A3_0001]] is the bound the concentration (Hoeffding) term needs, and it bounds the
*per-period* IC observations that get averaged - not the averaged IC. That is the same
units confusion as the complexity term above, one term to the right, and it is easy to
make because the averaged ICs are tiny: their magnitudes invite a small kappa, while a
per-period Spearman IC is supported on the whole interval from minus one to one.

**The reported bound uses the full Spearman support.** Hoeffding needs a bound fixed
*before* the data is seen. The observed sample maximum is a function of the same sample
the bound is being computed on, so substituting it does not give a conservative bound
with a smaller constant - it gives no valid coverage guarantee at all, and the
"significant" flag downstream would then mean nothing.

The empirical maximum is computed too and shown beside it as a **sensitivity calculation
only**: the size of the estimation term if one were willing to assume the observed range
persists. No significance claim is read off that row. It is here because the gap between
the two is the honest cost of a distribution-free bound on one year of data, and that
cost is invisible if only one value is shown.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
All 100 factors are pure noise, and the RAS lower bound reflects that: no factor's
conservative lower bound clears zero, though a good many show a positive raw IC by
chance. The penalty is an absolute deduction in IC units, not a percentage haircut
on each IC, and it has two parts. The data-snooping term [[ML4T_A3_0001]] is the price of
having searched the candidate set at all; the estimation term
[[ML4T_A3_0002]] is the price of a finite sample.

Both terms are now on the IC scale, so their sizes can be compared and the
comparison means something - read them off the table above rather than from here,
because which one dominates is not a fixed fact about the method. It moves with
[[ML4T_A3_0003]], with [[ML4T_A3_0004]] and with [[ML4T_A3_0005]]: the search term scales with the number and
correlation of the candidates, the estimation term with [[ML4T_A3_0006]]. On this
panel - a distribution-free [[ML4T_A3_0007]] and a single year of data - the finite sample
is much the more expensive of the two. Lengthen the sample or widen the candidate
set and that ordering changes.

This paragraph has now been written wrong twice, in both directions, which is the
argument for printing the components instead of narrating them: an ordering asserted in
prose outlives the re-run that invalidates it.

Read against the largest observed IC, the total deduction is many times that IC -
enough to sink every candidate, which is correct, because every candidate here is noise
by construction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0023-p001

~~~~~~markdown

The point of putting the complexity in IC units is that the comparison becomes a
statement about the data at all. On the standardized scale the search penalty alone was
an order of magnitude larger than the largest IC in the set, printed above, and it would
have rejected everything whatever the ICs were. A bound that returns the same answer for
every input is not measuring anything.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p001>>>
<<<ML4T-ZH-END:c0023-p001>>>

### c0024-p000

~~~~~~markdown
## Harvey et al. (2016) Thresholds

Based on the factor zoo of several hundred published factors, Harvey et al. recommend
stricter t-statistic thresholds for declaring a new factor than the one a single test
would use. They are declared and printed below rather than typed into prose, because the
cells that follow apply them and the two should not be able to drift apart.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0030-p000

~~~~~~markdown
## Practical Pipeline

The recommended workflow for evaluating many factors:

1. **Compute HAC-adjusted p-values** for each factor
2. **Apply BH-FDR** to control false discovery rate
3. **Report adjusted p-values** alongside discoveries
4. **Consider RAS** if factors are correlated (e.g., parameter variants)
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
### Exploration vs. Confirmation Pass

The chapter's *Separate exploration from confirmation* section recommends splitting
evaluation into two passes:

1. **Exploration**: screen all candidates on the first portion of data,
   promote based on fold stability rather than peak performance.
2. **Confirmation**: re-evaluate only promoted candidates on held-out data
   with a reduced comparison set.

The confirmation pass controls FDR more tightly because the search set
shrinks to only the promoted candidates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0035-p000

~~~~~~markdown
The confirmation pass operates on a smaller search set (only the promoted
candidates), so BH corrections are less aggressive. At the same time, using
held-out data prevents the double-dipping that inflates exploration-pass
discovery rates. This two-pass workflow is the practical implementation of
the "separate exploration from confirmation" principle the chapter sets out.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
### Applied Example: ETF Feature Search

The HAC call in the search below passes [[ML4T_A3_0001]], because the forward return is
sampled daily over a multi-day window and this IC series is therefore overlapping.
Without it the library picks the truncation from the sample size alone, which is the
defect [[ML4T_A3_0002]] corrects. The synthetic factor zoos earlier in this notebook
draw their periods independently, so the automatic rule is right for those and only for
those.

The synthetic simulations above use known ground truth to verify the
corrections work. Now we apply the same pipeline to real features on
the ETF universe - the same data used in notebooks 05, 06, and 08.

We compute 13 candidate features (momentum at 6 lookbacks, reversal
at 3 horizons, realized volatility, and volume ratios) and test each
for IC significance with HAC inference. After BH-FDR correction for
13 simultaneous tests, how many survive?
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0042-p000

~~~~~~markdown
Every bar is drawn in the same colour because nothing cleared the threshold: the search
found no feature it could call a discovery at this false-discovery rate. The two largest
ICs are realized-volatility features and are not small in absolute terms, which is the
point worth sitting with - a respectable-looking IC on a searched set is not evidence,
and the correction is what says so.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>
