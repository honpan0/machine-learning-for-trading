# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/10_uncertainty.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0023-p000

~~~~~~markdown
### Calibration Helper

Both MC Dropout and Deep Ensembles need the same calibration diagnostic:
bin predictions by uncertainty quartile and check whether error tracks
uncertainty. We extract this into a reusable function.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
### Calibration Analysis

Well-calibrated uncertainty means: when the model says "I'm uncertain about
this prediction," the actual error should be proportionally larger. We bin
predictions by uncertainty quartile and check whether error tracks uncertainty.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
**Interpretation**: the Spearman correlation printed above is the headline
calibration diagnostic - it asks whether the model's predicted std orders
absolute errors. The quartile table makes the same question concrete: does
mean |error| rise monotonically as you move from the low-std quartile (Q1) to
the high-std quartile (Q4)? With dropout active on only two LSTM layers, the
std spread is small in absolute terms; a near-zero correlation here means
that small spread carries little information about which predictions will be
wrong. The Q1→Q4 |error| gradient in the table is the visual version of the
same diagnostic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0028-p000

~~~~~~markdown
### MC Dropout Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
---
## Part B: Deep Ensembles

Deep Ensembles train [[ML4T_A3_0001]] independently initialized models and use their
disagreement as an uncertainty estimate. Unlike MC Dropout (which approximates
weight uncertainty within a single model), ensembles capture **functional
diversity** arising from different loss landscape minima.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0031-p000

~~~~~~markdown
### Ensemble Member Architecture

Each member is a simpler LSTM than the MC Dropout version: dropout only within
the LSTM layers (no extra dropout head). The diversity comes from random
initialization, not from stochastic regularization.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
### Training Ensemble Members

Each member receives a different random seed for weight initialization.
The training procedure is identical; only the starting point differs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0036-p000

~~~~~~markdown
### Ensemble Predictions

Each member produces an independent point prediction. The ensemble mean is
the forecast; the ensemble standard deviation is the uncertainty estimate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
**Interpretation**: the member ICs printed above compare how well each member ranks
funds, and the ensemble mean's IC against their range says how much averaging
helped - it helps when members make errors that partly cancel.

Note that this says nothing about the uncertainty estimate. An IC is a rank
statistic, so two members can score identically while predicting quite different
magnitudes, and the ensemble's uncertainty is [[ML4T_A3_0001]]: the per-example standard
deviation across members, printed above as a mean and plotted as a histogram below.
Whether that quantity is informative is the calibration question, and it is answered
by the uncertainty-error diagnostics, not by the IC spread.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000

~~~~~~markdown
### Calibration Analysis
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
**Interpretation**: the two correlations are printed together above, so read them
side by side. The argument for expecting the ensemble's to be larger is that its
members are separate optimisations that can land in different places, where MC
Dropout samples subnetworks of one trained model - a narrower kind of variation. The
run either bears that out or does not.

What neither number can be is a calibration guarantee. A rank correlation between
predicted spread and absolute error says the ordering carries some information; it
says nothing about whether an interval of a given width contains the outcome as
often as it claims. That is what the coverage table measures, and what the
split-conformal section is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000

~~~~~~markdown
### Epistemic vs Aleatoric Decomposition

Deep ensembles naturally decompose total predictive uncertainty into two components:

[[ML4T_A3_0001]]

- **Epistemic uncertainty** (model uncertainty): variance of the ensemble means.
  Reducible with more data -- members disagree because they learned different
  functions from finite data.
- **Aleatoric uncertainty** (data uncertainty): average variance within each
  member. Irreducible -- inherent noise in the data generating process.

For regression with MSE loss (no per-member variance head), we approximate
epistemic uncertainty as ensemble disagreement and note that aleatoric
uncertainty would require heteroscedastic outputs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0044-p000

~~~~~~markdown
**Note**: Without heteroscedastic output heads (where each member predicts both
[[ML4T_A3_0001]] and [[ML4T_A3_0002]]), total variance equals epistemic variance. A production
model would add per-member variance heads to separate aleatoric noise - the
irreducible uncertainty inherent in the data generating process. See section
13.8 for the full variance decomposition equation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0045-p000

~~~~~~markdown
### Ensemble Member Agreement Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>
