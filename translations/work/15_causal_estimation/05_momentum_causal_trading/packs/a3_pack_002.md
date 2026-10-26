# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：15_causal_estimation/05_momentum_causal_trading.ipynb；A3 Pack 002；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Portfolio → 投資組合
- Sharpe ratio → 夏普比率
- Out-of-sample → 樣本外
- Correlation → 相關性

## 待翻譯英文單元

### c0028-p000

~~~~~~markdown
Raw long-short positions are converted into gross-normalized portfolio
weights so that regime scaling actually changes gross exposure. Without
this normalization, a market-wide scale would cancel out of exposure-
weighted returns and only affect costs through turnover.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
Portfolio return is the sum of weight × outcome across the cross-section;
turnover is the sum of absolute weight changes between consecutive dates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
Combine quintile construction, weight normalization, regime scaling, and
turnover costs into one backtest function used for both train and test
periods.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
## 5. Out-of-Sample Evaluation

Everything above was fitted on the training period alone: the regime thresholds, the CATE
estimates and the scaling factors they produce. All three are now fixed, and the test
period sees them for the first time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
Compute comparable risk/return metrics for each strategy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
### In-Sample Against Out-of-Sample
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
### Sensitivity to the Transaction-Cost Assumption
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
### The Three Strategies Side by Side
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0048-p000

~~~~~~markdown
## 6. What the Holdout Settles
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
### Reading the comparison

The information coefficient printed above is a property of the signal rather than of any
strategy built on it: the average, over dates, of the rank correlation between momentum
and the forward return within that date's cross-section. A sign change between the
training period and the holdout says the association the three rules all lean on was not
stable, which is the first thing to know about any of them. It does not by itself settle
what a strategy earned - the rules trade quintile spreads with regime-dependent exposure,
and an average that flips sign is consistent with several quintile patterns. The three
Sharpe ratios below say what each rule actually did, and neither they nor the IC are
evidence about the causal estimate that produced the scaling.

What the causal analysis establishes is a statement about confounding in the training
period, conditional on the controls being adequate. It is not a forecast, and the holdout
is not a test of it. A regime-conditional effect can be correctly estimated and still fail
to earn anything, because whether it persists is a separate empirical question that the
estimate makes no claim about.

Three practical consequences:
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0050-p001

~~~~~~markdown

- **Compare against a baseline that costs nothing.** [[ML4T_A3_0001]] uses no causal
  machinery. Any gap between it and the causal rule is what the machinery bought; where
  there is no gap, it bought nothing here.
- **Read the sizing rule's floor and cap.** The scaling is clipped to
  [[ML4T_A3_0002]] and shrunk toward neutral by [[ML4T_A3_0003]], so a
  noisy CATE cannot produce a large position. That bounds the damage and it also bounds
  the upside.
- **Vary the cost assumption before believing any of it.** The sensitivity table above
  sweeps the round-trip cost, and a ranking that changes across that sweep is a ranking
  about the cost assumption rather than about the strategies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p001>>>
<<<ML4T-ZH-END:c0050-p001>>>
