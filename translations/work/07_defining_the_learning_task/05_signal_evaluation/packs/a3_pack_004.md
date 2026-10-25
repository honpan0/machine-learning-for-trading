# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/05_signal_evaluation.ipynb；A3 Pack 004；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Out-of-sample → 樣本外
- Walk-forward validation → 滾動向前驗證
- Overfitting → 過度擬合
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0073-p000

~~~~~~markdown
The ROC and precision-recall sweeps below are built by hand rather than taken from
sklearn's curve helpers, for an environment reason recorded in the code comment: the
library path fails under the pin this project carries. The manual sweep is deterministic
and agrees with the library to well inside plotting resolution.
~~~~~~

<<<ML4T-ZH-BEGIN:c0073-p000>>>
<<<ML4T-ZH-END:c0073-p000>>>

### c0077-p000

~~~~~~markdown
### Library Binary Metrics

Point estimates of precision/recall are noisy. [[ML4T_A3_0001]] provides
[[ML4T_A3_0002]] with Wilson confidence intervals and
statistical tests in a single call.
~~~~~~

<<<ML4T-ZH-BEGIN:c0077-p000>>>
<<<ML4T-ZH-END:c0077-p000>>>

### c0080-p000

~~~~~~markdown
### Binary Evaluation Guidelines

| Metric | What It Measures | Trading Interpretation |
|--------|------------------|------------------------|
| **ROC AUC** | Ranking quality | Against the no-skill diagonal, with a confidence interval |
| **PR AUC** | Precision at various recalls | Use when positives are rare |
| **Precision** | % of predicted positives correct | Matters for trade entry |
| **Recall** | % of actual positives found | Matters for opportunity cost |

**Threshold selection** depends on the trading objective:
- High precision, low recall: fewer trades, higher win rate
- High recall, low precision: capture more opportunities, lower win rate
- The optimal threshold depends on costs and capacity constraints
~~~~~~

<<<ML4T-ZH-BEGIN:c0080-p000>>>
<<<ML4T-ZH-END:c0080-p000>>>

### c0081-p000

~~~~~~markdown
### Fold-Aware Binary Evaluation

Just as with IC, we should compute ROC AUC per fold to assess out-of-sample
classification performance.
~~~~~~

<<<ML4T-ZH-BEGIN:c0081-p000>>>
<<<ML4T-ZH-END:c0081-p000>>>

### c0083-p000

~~~~~~markdown
## Summary

### Key Metrics for Signal Evaluation

| Metric | What It Measures | How to read it |
|--------|------------------|----------------|
| **IC** | Cross-sectional predictability | Against its own standard error; the literature bands are printed under *Interpreting an IC magnitude* |
| **ICIR** | Risk-adjusted IC (mean/std) | Together with IC; a near-zero ICIR says the mean is inside the daily dispersion |
| **Fold ICIR** | IC stability across test folds | Alongside which dates the folds actually cover |
| **Spread** | Top-bottom quantile difference | Sign first, then size against costs |
| **Monotonicity** | Spearman rho of quantile rank against mean return | Magnitude against the bands printed under *Monotonicity Interpretation*; sign first |
| **Turnover** | Signal stability | Against the break-even cost computed above |
| **Half-life** | Signal decay rate | Only where the horizon profile actually decays |

### Fold-Aware Evaluation (Critical)

Always compute metrics **per fold** using walk-forward validation:

1. Create expanding-window or rolling-window splits.
2. Compute IC (or AUC) on each test fold.
3. Report the **distribution** of fold-level metrics, not just pooled values.
4. Before reading a gap between the pooled and fold-level figures, recompute the pooled
   statistic **on the fold dates only**. This notebook's own decomposition showed the
   whole gap was a period effect: the folds covered a favourable stretch near the front
   of the panel, and nothing about aggregation or overfitting was involved. A gap
   between two statistics computed over different dates is not evidence of either.

### API Reference
~~~~~~

<<<ML4T-ZH-BEGIN:c0083-p000>>>
<<<ML4T-ZH-END:c0083-p000>>>

### c0083-p001

~~~~~~markdown

[[ML4T_A3_0001]]

### Next Notebooks

- [[[ML4T_A3_0002]]](06_ic_inference.ipynb) - HAC adjustment and block bootstrap for IC inference
- [[[ML4T_A3_0003]]](07_multiple_testing.ipynb) - FDR control when evaluating many factors
~~~~~~

<<<ML4T-ZH-BEGIN:c0083-p001>>>
<<<ML4T-ZH-END:c0083-p001>>>
