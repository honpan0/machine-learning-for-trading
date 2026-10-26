# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/10_uncertainty.ipynb；A3 Pack 003；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤
- Validation set → 驗證集
- Test set → 測試集
- Standard deviation → 標準差

## 待翻譯英文單元

### c0047-p000

~~~~~~markdown
---
## Part C: MC Dropout vs Deep Ensembles

We now compare both uncertainty methods head-to-head on the same test set,
alongside the Ridge baseline which provides no uncertainty estimate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
### Side-by-Side Calibration
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
### Coverage Probability

A complementary calibration diagnostic: what fraction of actual values fall
within the predicted confidence intervals? We compute empirical coverage at
the [[ML4T_A3_0001]] below for both methods, using the Gaussian assumption
([[ML4T_A3_0002]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0053-p000

~~~~~~markdown
**Interpretation**: both methods severely underestimate uncertainty under the
Gaussian assumption. The dropout-spread is tiny in absolute terms, so MC
Dropout's intervals are essentially zero-width and capture almost none of
the actual returns. The ensemble does better - its members genuinely
disagree - but the resulting intervals are still far too narrow at every
nominal level. The pattern is consistent across reruns: raw LSTM
uncertainty estimates are **not usable for risk management without
post-hoc calibration**. The next section uses split-conformal prediction to
convert these raw spreads into intervals with controlled empirical coverage.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0054-p000

~~~~~~markdown
### Split-Conformal Calibration

Split-conformal prediction (Vovk et al.) turns any point predictor into a
distribution-free interval estimator: under exchangeability of validation
and test residuals, the resulting test intervals have at least [[ML4T_A3_0001]]
marginal coverage in finite samples.

We implement two variants on the held-out validation set:

- **Plain conformal**: [[ML4T_A3_0002]],
  test interval [[ML4T_A3_0003]].
  Width is constant across test points.
- **Normalized (locally adaptive) conformal**: [[ML4T_A3_0004]],
  test interval [[ML4T_A3_0005]].
  Width scales with the model's own uncertainty estimate, so well-calibrated
  [[ML4T_A3_0006]] yields tighter intervals where the model is confident.

We need validation predictions from MC Dropout and the ensemble. We re-run
inference on the val split.

**Two reasons the guarantee does not strictly hold here.** Both are about
exchangeability, which is the one assumption split-conformal makes.

First, the calibration set is the early-stopping set. The quantiles below come from
the same [[ML4T_A3_0007]] split [[ML4T_A3_0008]] stopped on, so the models were selected to make
these exact residuals small. That biases [[ML4T_A3_0009]]
downward and makes the intervals mildly optimistic. A production pipeline carves a
third, dedicated calibration split before training; this notebook reuses the
validation split to stay on one train/validation/test partition.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0054-p001

~~~~~~markdown

Second, the labels overlap. A [[ML4T_A3_0001]]-session forward return shares days
with its neighbours, so residuals within a split are strongly dependent rather than
exchangeable draws, and the effective sample size behind each quantile is far below
the row count. The split above purges the boundary, which stops calibration
residuals from resolving inside the test period; it does nothing about the
dependence within each split.

So read the coverage below as what these intervals achieved on this test set, not as
a finite-sample guarantee that they will.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p001>>>
<<<ML4T-ZH-END:c0054-p001>>>

### c0056-p000

~~~~~~markdown
#### Calibration: plain and normalized conformal quantiles

[[ML4T_A3_0001]] guards the normalized variant against division by zero where the model
reports near-zero predicted std on the validation set.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0058-p000

~~~~~~markdown
**Reading the table.** Compare the empirical coverage column against the nominal
level, and the two variants against each other at the same level.

The plain variant uses no [[ML4T_A3_0001]] at all: it takes a quantile of the held-out
absolute residuals and gives every test point that same half-width. So its coverage
is a statement about the calibration procedure, not about either uncertainty method.
The normalized variant divides each residual by the model's own [[ML4T_A3_0002]] before
taking the quantile, then multiplies back at test time - which is the only place in
this notebook where MC Dropout's or the ensemble's spread does any work.

A small [[ML4T_A3_0003]] is not itself a problem. Multiplying every [[ML4T_A3_0004]] by a
constant divides the quantile by that constant and multiplies the width back by it,
leaving the intervals unchanged - so the normalized variant is scale-invariant, and a
method reporting standard deviations of [[ML4T_A3_0005]] is on the same footing as one
reporting [[ML4T_A3_0006]]. A [[ML4T_A3_0007]] that is exactly constant reproduces the plain
widths.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0058-p001

~~~~~~markdown

What decides the outcome is how much [[ML4T_A3_0001]] varies, and whether it varies
where the errors are. The coefficients of variation printed above are the first thing
to read. A [[ML4T_A3_0002]] that barely varies leaves the normalized variant doing what
plain conformal already does. A [[ML4T_A3_0003]] that varies without tracking error
still redistributes width - some test points get a narrower interval and some a wider
one - but it allocates that width by something unrelated to where the model is
actually wrong. Marginal coverage still holds, because the quantile is chosen to make
it hold; what degrades is coverage *per point*, which is the property a position
sizer built on these intervals would rely on. The widths and coverage in the table
are the evidence, not the size of [[ML4T_A3_0004]].

The scale invariance does break at the bottom, where [[ML4T_A3_0005]] approaches [[ML4T_A3_0006]].
The printed minima say whether that is in play.

The marginal coverage guarantee is distribution-free (Vovk et al. 2005), but it is
not assumption-free: it needs calibration and test residuals to be exchangeable,
which the two paragraphs above the calibration set out is not the case here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p001>>>
<<<ML4T-ZH-END:c0058-p001>>>

### c0059-p000

~~~~~~markdown
### Uncertainty-Based Prediction Filtering

The practical payoff: does removing the most uncertain predictions improve
forecast quality? We exclude the highest-uncertainty quartile and compare IC
on the filtered subset against the full test set.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>
