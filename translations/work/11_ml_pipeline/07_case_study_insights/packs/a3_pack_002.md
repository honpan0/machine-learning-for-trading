# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/07_case_study_insights.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0036-p000

~~~~~~markdown
### Ridge regularization path

How does mean daily IC change as Ridge [[ML4T_A3_0001]] increases? A flat
path means the conditioning of the feature matrix is already benign;
a pronounced peak indicates an optimal shrinkage strength.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
The confidence bands put the path curvature in context. An apparent optimum
matters only when its change is large relative to uncertainty; across these
panels, most neighboring Ridge settings remain statistically difficult to
distinguish.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0040-p000

~~~~~~markdown
## 4. Persistence and Stability

A positive mean daily IC averaged over the whole validation period can
still come from a few good stretches. The primary persistence view is a
three-month rolling mean of the daily IC, which traces how ranking quality
evolves over time. Because case studies cover different validation windows,
the comparison is clipped to the common validation period for ETFs and FX.
(Figure 11.8 in the chapter.) Per-fold IC and ICIR below are secondary stability
diagnostics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
The rolling view tests whether a full-period average is broadly persistent or
concentrated in a few stretches. Both paths cross zero here, so neither
full-period average describes every validation regime. Both are validation
estimates: the holdout period is untouched by this chapter.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0044-p000

~~~~~~markdown
### Figure: Per-Fold IC Distribution
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0047-p000

~~~~~~markdown
### ICIR cross-CS bar

The information ratio [[ML4T_A3_0001]]
is a stability-adjusted signal-strength summary. With only a handful of folds per
case study it is sample-starved and should be read alongside the
mean daily IC and per-fold distribution, not as a standalone score.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0050-p000

~~~~~~markdown
## 5. Multi-Label Horizon and Metric Symmetry
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
### 5a. Linear IC across regression labels per case study

Several case studies trained the linear pipeline on multiple regression
horizons. For each (case study, label), we take the highest complete
mean daily IC across linear configurations and compare across horizons -
this diagnoses whether the cross-sectional signal strengthens or
weakens with the prediction window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0057-p000

~~~~~~markdown
### 5b. Classification ↔ regression metric symmetry

A linear model trained on a continuous return label has a regression
score; the same modelling apparatus can be trained on the binary
direction label of the same horizon. Across the case studies that
carry binary direction labels, two questions are symmetric:

- **Direction A** - the classification model's score, evaluated as
  IC against the *continuous* return, asks whether the directional
  classifier is also a useful *cross-sectional ranker*. This number
  is on the registry as [[ML4T_A3_0001]] for
  [[ML4T_A3_0002]] rows.
- **Direction B** - the regression model's score, evaluated as mean daily AUC
  against the *binary* direction, asks whether the continuous
  regression score is also a useful *cross-sectional binary classifier*. This number
  is computed on the fly here from raw OOF predictions, since the
  registry stores AUC only for classification training runs.

We restrict to case studies with a binary direction label paired to a
regression label for the same horizon; ternary direction labels (e.g.
NASDAQ-100 [[ML4T_A3_0003]], Crypto [[ML4T_A3_0004]]) need a multi-class
AUC and are out of scope for this brief subsection.
~~~~~~

<<<ML4T-ZH-BEGIN:c0057-p000>>>
<<<ML4T-ZH-END:c0057-p000>>>

### c0065-p000

~~~~~~markdown
### Figure: Direction A and Direction B side by side
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0068-p000

~~~~~~markdown
## 6. Coefficient Analysis

The linear training pipeline stores a fitted pipeline per fold under the
training run's [[ML4T_A3_0001]] directory, so the coefficients below are read out of
those fold models. They are coefficients of the standardized features: the
saved preprocessor imputes and scales and leaves the feature order alone, so
they are comparable across features within a fit.

A stored model was pickled by the scikit-learn that trained it, which is older
than the one running this notebook, so unpickling one raises
[[ML4T_A3_0002]] once per fold. The loader silences that warning and
nothing else, because it reads [[ML4T_A3_0003]] and [[ML4T_A3_0004]] and never calls
[[ML4T_A3_0005]]: an array attribute and a tuple of strings survive the version gap that
the warning is about. A fit whose coefficient count stops matching its feature
names raises instead of being read.
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0070-p000

~~~~~~markdown
### 6a. Sign consistency across folds

For each case study's highest-IC linear configuration on the primary label,
sign consistency is the share of a feature's non-zero folds that agree on its
sign. A regularized fit sets many coefficients to exactly zero, and a zero has
no sign, so the zero folds are excluded from the fraction and a feature that is
zero in every fold is excluded from the statistic altogether. Counting those
zeros as agreement would score a fit that selected almost nothing as the most
stable one in the table; how much a fit zeroes out is section 6b's subject.
[[ML4T_A3_0001]] is how many features the mean is taken over, and
[[ML4T_A3_0002]] is the consistency a feature has to reach to count as
sign-stable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0074-p000

~~~~~~markdown
### 6b. Lasso sparsity

Lasso drives coefficients exactly to zero. The fraction of zero
coefficients per case study summarizes how aggressively Lasso prunes
features at the highest-IC [[ML4T_A3_0001]] for the Lasso family.
~~~~~~

<<<ML4T-ZH-BEGIN:c0074-p000>>>
<<<ML4T-ZH-END:c0074-p000>>>

### c0078-p000

~~~~~~markdown
### 6c. Top-N feature overlap across case studies

Are the same features driving the linear signal across case studies, or does
each case study have its own world? For each case study's highest-IC linear
configuration on the primary label, we rank features by mean absolute fold
coefficient and take the leading [[ML4T_A3_0001]], then measure the pairwise Jaccard
overlap of those sets.

A low overlap has two explanations and the matrix alone cannot separate them:
the panels select different features from a library they share, or their
libraries barely overlap to begin with. The summary under the heatmap reports
how many feature names the most similar pair of panels has in common, which is
what tells the two apart.
~~~~~~

<<<ML4T-ZH-BEGIN:c0078-p000>>>
<<<ML4T-ZH-END:c0078-p000>>>
