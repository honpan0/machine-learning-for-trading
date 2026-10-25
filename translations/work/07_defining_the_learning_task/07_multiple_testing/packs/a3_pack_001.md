# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/07_multiple_testing.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Sharpe ratio → 夏普比率
- Label → 標籤
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Multiple Testing and Selection Bias

**Docker image**: [[ML4T_A3_0001]]

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.4 - Search Accounting and Multiple Testing

## Purpose

This notebook addresses the **factor zoo problem**: when testing many signals,
even with proper inference, the "best" will be inflated by selection bias.
We cover FDR control and complexity-aware corrections.

## Learning Objectives

1. Understand why selecting the highest IC inflates the estimate
2. Apply Benjamini-Hochberg FDR for discovery control
3. Use Rademacher complexity (RAS) for correlated factors
4. Build a practical pipeline: HAC p-values → BH → discoveries

## The Factor Zoo Problem

Harvey, Liu and Zhu (2016) counted several hundred factors published in the academic
literature by 2015. Testing that many candidates at a conventional significance level
means a double-digit number of false discoveries is the *expected* outcome even if not
one of the factors is real - the arithmetic is the candidate count times the level, and
it is printed later in this notebook against the parameters used here.

Their recommendation is a materially stricter t-statistic threshold for declaring a new
factor; the thresholds they propose are printed under **Harvey et al. (2016)
Thresholds** below.

## Prerequisites

- [[ML4T_A3_0002]] - provides per-factor HAC inference whose p-values feed
  the BH/Holm/Rademacher corrections here.
- Familiarity with the family-wise error rate (FWER) and false discovery
  rate (FDR), and with the Sharpe ratio's distribution under selection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## The Selection Bias Problem

When testing N factors and keeping the highest-scoring one:
- **Observed IC**: max(IC₁, IC₂, ..., ICₙ)
- **True IC**: Often much lower

Under the null (all factors are noise), the expected maximum is:

[[ML4T_A3_0001]]

This is the "expected best by chance" - the selection bias.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0008-p000

~~~~~~markdown
The distribution is centred on zero because that is the truth about every factor in it.
What the marked line shows is the maximum of a hundred draws from that distribution, and
a maximum is not an estimate of the thing being maximised over. Reporting the selected
factor's IC as its IC is the whole of the selection-bias problem: nothing was
mismeasured, and the number is still wrong, because the selection step is not in it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
### Publication Figure Artifact

The book figure for this section reads a compact NumPy artifact so formatting
changes do not rerun the null simulation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Benjamini-Hochberg FDR Control

**False Discovery Rate (FDR)** controls the expected proportion of false
discoveries among rejections:

[[ML4T_A3_0001]]

The BH procedure:
1. Sort p-values: p₍₁₎ ≤ p₍₂₎ ≤ ... ≤ p₍ₙ₎
2. Find largest k where p₍ₖ₎ ≤ (k/n) × α
3. Reject hypotheses 1, 2, ..., k
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
The p-values below are HAC-adjusted rather than naive. The correction procedures that
follow take p-values as given, so feeding them naive ones would leave the dependence
problem from [[ML4T_A3_0001]] untouched and simply carry it through the correction.

Every HAC call on a synthetic panel passes [[ML4T_A3_0002]], because these panels draw
each period independently and their labels therefore do not overlap. That is a claim
about the data, and it is worth making explicitly: omitting the argument leaves the
library to infer the bandwidth from sample size alone and to warn that it may be
anti-conservative, which is the right warning for real overlapping labels and the wrong
one here. The ETF search later in the notebook passes its actual horizon instead.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0015-p000

~~~~~~markdown
### Holm-Bonferroni FWER Control

BH controls **FDR** (the expected proportion of false discoveries among rejections).
Holm-Bonferroni controls **FWER** (the probability of making *any* false discovery).

Use FWER when even one false positive is unacceptable - e.g., deploying a new
strategy that incurs real capital risk.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## Rademacher Complexity (RAS)

When factors are correlated, Rademacher complexity provides a sharper bound
than assuming independence. The RAS (Rademacher Anti-Serum) adjustment
accounts for the actual complexity of the hypothesis class.

Key insight: Testing 100 variants of the same factor is less risky than
testing 100 truly independent factors.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0018-p000

~~~~~~markdown
### Two scales, and why the distinction matters

Rademacher complexity is estimated from a matrix of per-period performances, and
**it comes out in whatever units that matrix is in**. Two different questions here
need two different scales, and mixing them is a silent error:

- *How correlated is this candidate set?* Compare [[ML4T_A3_0001]] to Massart's bound
  [[ML4T_A3_0002]]. Massart bounds the maximum of [[ML4T_A3_0003]] **standardized** means,
  so this comparison is only meaningful on standardized ICs.
- *How much do I deduct from an observed IC?* The RAS bound
  [[ML4T_A3_0004]]
  subtracts [[ML4T_A3_0005]] from an IC, so here [[ML4T_A3_0006]] must be in **IC units**.

Standardizing divides each factor's column by its own **per-period** IC standard
deviation - the dispersion of that factor's IC across dates, not the dispersion of
the averaged ICs across factors. The two differ by more than an order of magnitude
here, and the cell below prints both so the conversion is checkable rather than
asserted. Feeding the standardized [[ML4T_A3_0007]] into the adjustment would deduct a
penalty many times larger than any IC in the set - the bound would reject
everything, and would do so no matter what the data said.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
A ratio near one means the factors are nearly independent and the full multiple-testing
penalty applies. A ratio well below one signals correlation among the candidates, so the
effective hypothesis count is lower than the nominal count.

The RAS penalty is an absolute deduction - twice the Rademacher average plus the
estimation term - rather than a proportional shrinkage, so the cells below report both
components and the resulting lower bound. Significance follows the library's own
convention: an adjusted IC above zero.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
