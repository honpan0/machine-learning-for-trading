# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：11_ml_pipeline/08_ml_backtest_intro.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Portfolio → 投資組合
- Backtesting → 回測
- Transaction costs → 交易成本
- Slippage → 滑價
- Drawdown → 回撤
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# From Signals to Returns: The Reality Check

**Docker image**: [[ML4T_A3_0001]]

**Purpose**: pedagogical end-to-end backtest comparing ML-generated signals
against momentum and equal-weight baselines on the ETF panel. Shows what
happens to a ranking signal once turnover and transaction costs are charged
against it.

**Learning objectives**

- Train Ridge and Logistic models on the canonical 8-fold walk-forward CV
- Convert signals to long-only top-10 portfolios with equal weights
- Compute gross / net Sharpe, annualized return, volatility, drawdown, and
  turnover
- Quantify how transaction-cost drag, charged at [[ML4T_A3_0002]] per side, separates
  high-turnover ML strategies from low-turnover baselines

**Book reference**: Section 11.6 - Case study insights
(the chapter synthesis paragraph on IC vs net Sharpe).

**Prerequisites**

- Ch7 21-day forward return labels at [[ML4T_A3_0003]]
- Ch8 ETF features at [[ML4T_A3_0004]]
- ETF prices via [[ML4T_A3_0005]]
- [[ML4T_A3_0006]] evaluation section for canonical walk-forward splits

**Caveat**: this is a deliberately simplified backtest for pedagogy.
Production backtesting with proper execution modeling, slippage, and risk
management is covered in *Chapter 16*. Portfolio construction with turnover
constraints is *Chapter 17*; transaction-cost modeling is *Chapter 18*.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0005-p000

~~~~~~markdown
## Load Data

Features from Ch8, labels from Ch7, ETF prices from the canonical loader, and the canonical
walk-forward CV splits from the [[ML4T_A3_0001]] evaluation section.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0009-p000

~~~~~~markdown
## Walk-Forward Prediction

The splits come from the [[ML4T_A3_0001]] section of the case study's [[ML4T_A3_0002]], which
declares eight folds of ten years' training and one year's validation, stepping
forward annually. [[ML4T_A3_0003]] purges the 21 sessions a 21-day forward label
needs, so no training row's label resolves inside its own validation window. The cell
above prints how many folds this run actually used.

For each fold we train Ridge and Logistic once, then predict across the entire validation window.
Momentum ranks on [[ML4T_A3_0004]] directly, with no training step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
Ridge and Logistic are fitted once per fold on that fold's training window, at the
library's default regularization strengths. Choosing those strengths honestly is
[[ML4T_A3_0001]]; what this notebook varies is what happens to a signal once it is
traded.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Signal-to-Portfolio Conversion

For each month-end rebalance date within the validation window, we rank
symbols by each signal and select the top-N for equal-weight long portfolios.
Momentum ranks on [[ML4T_A3_0001]] directly, with no model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
## Compute Portfolio Returns

Forward-fill weights to daily frequency and compute daily portfolio returns as
[[ML4T_A3_0001]]. Turnover is measured at each rebalance date.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
## Performance Summary

Annualized Sharpe (gross and net of costs), return, volatility, max drawdown and
average annual turnover, over the validation window the folds span.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
## Equity Curves and Turnover

Two panels over the validation window: growth of \$1 on top, where a solid line is
gross and the dashed line of the same colour is that strategy net of cost, and
one-sided turnover at each monthly rebalance below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
## IC Comparison

Cross-sectional IC per rebalance date, smoothed over a rolling twelve rebalances. IC
scores the ranking; the equity curves above score what holding that ranking cost.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0027-p000

~~~~~~markdown
**Interpretation.** The two rankings above are built from different things and do not
have to agree. Mean IC scores how well a signal orders next month's returns. Net
Sharpe scores what was left after holding the portfolio that ordering implies and
paying to change it. A signal can rank well and still finish behind a rule with no
signal at all, because the cost of acting on a ranking is charged against every
rebalance while the ranking itself is free.

Equal weight is the useful contrast: it holds every asset and trades only the drift
back to [[ML4T_A3_0001]] each month, so its gross and net Sharpe are nearly the same number. The
active strategies re-pick a top-N list each month and pay for the whole difference
between consecutive lists. What that takes from the annualized return is the cost rate
times the fraction traded, so return drag is proportional to turnover. The Sharpe drag
is that return drag divided by the strategy's own volatility, which is a different
ordering: of two strategies that trade the same amount, the steadier one gives up the
larger ratio.

A signal whose IC is near zero or negative can still post a respectable net Sharpe,
and the ranking is not the only thing that could produce it. A long-only top-N
portfolio drawn from a shared universe inherits most of that universe's return
whatever the ranking says, and a lower realized volatility raises the ratio without
raising the return at all. Read the IC column and the Sharpe column as answers to two
questions, not as one score twice.
Turnover-penalized objectives and trading constraints are the response, and Chapters
17 and 18 develop them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0028-p000

~~~~~~markdown
## Key Takeaways

1. **A ranking score and a portfolio result are different measurements.** Mean IC
   says how well a signal orders the cross-section; net Sharpe says what holding the
   implied portfolio returned after costs. The table above shows how far apart the
   two orderings can be on the same eight folds.
2. **Trading is what separates them.** Cost is charged on the difference between
   consecutive weight vectors, so at a fixed cost per side the *return* a strategy
   gives up is proportional to how much it trades. The *Sharpe* it gives up is that
   return divided by its own volatility, so the steadier of two strategies that trade
   equally loses the larger ratio. Equal weight trades only its monthly drift back to
   [[ML4T_A3_0001]]; a monthly top-N re-pick trades most of the book.
3. **Put transaction costs in the objective.** Regularization controls coefficient
   magnitude, not position change, so a penalized fit is not a low-turnover fit.
   Turnover-penalized objectives and trading constraints (*Chapters 17 and 18*) are
   what make a ranking signal worth acting on at this cost level.

**Next**: *Chapter 16* develops production backtesting with proper execution
modeling. *Chapter 17* adds portfolio construction with turnover constraints,
and *Chapter 18* layers in transaction-cost modeling.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>
