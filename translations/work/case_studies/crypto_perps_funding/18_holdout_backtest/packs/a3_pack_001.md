# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/crypto_perps_funding/18_holdout_backtest.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Slippage → 滑價
- Label → 標籤
- Out-of-sample → 樣本外
- Covariance → 共變異數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Crypto Perpetuals Funding: Holdout Backtest

**Chapter 20 - Out-of-sample evaluation**

[[[ML4T_A3_0001]]](17_holdout_predictions.ipynb) refitted the selected
configuration on history ending before 2024 and wrote its predictions over 2024-25. This
notebook trades them with the sizing and the overlay that configuration carries, and
registers the result under [[ML4T_A3_0002]].

**Prerequisites:** [[[ML4T_A3_0003]]](17_holdout_predictions.ipynb). This notebook
does not fit; if the prediction set it needs is absent, it raises rather than producing
one.

**Scope:** one backtest. The comparison against validation, and the correction that
comparison needs, are [[[ML4T_A3_0004]]](19_strategy_analysis.ipynb)'s.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## 1. The configuration, and the predictions it produced on the holdout

The selected configuration is resolved the same way [[[ML4T_A3_0001]]](16_costs.ipynb) and
[[[ML4T_A3_0002]]](17_holdout_predictions.ipynb) resolve it, so all three run the
same configuration by construction rather than by a hash copied between them.

Which holdout prediction set belongs to it is derived rather than searched for. Re-deriving the
holdout training specification reproduces the training identity 17 registered - the derivation is
deterministic and the identity covers it - so the prediction set is looked up by that identity
and the selected configuration's checkpoint. A search over holdout prediction sets would have to
guess which one belonged to this configuration.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. What the allocator needs before the window opens

This configuration allocates by [[ML4T_A3_0001]], which is a moment estimator: it reads a
rolling window of underlying prices and produces weights from their covariance. That window
does not restart because the evaluation period does. Loading the holdout slice alone would
leave the first rebalance with no history to estimate from, and the loader would fall back
to a median-imputed warmup - so the first weeks of the holdout would be traded on weights
that describe nothing, and the resulting Sharpe would be a measurement of the fallback.

So the prices are loaded with the same lookback the allocator was given on validation.
[[ML4T_A3_0002]] declares [[ML4T_A3_0003]], which is 240 eight-hourly bars, about
eighty days. The loader leaves the start of the window unconstrained by that much and still
caps the end at the canonical window end; the extra prefix is consumed by the rolling
window and does not enter return aggregation, because the engine only aggregates over the
rebalance timestamps the predictions carry.

The conformal branch below is inert for this configuration and is kept because the selected
configuration is resolved rather than fixed. [[ML4T_A3_0004]] sizes from residuals the model
has already made, and on the holdout there are none to use - every holdout return realises inside
the window being evaluated - so a conformal configuration would calibrate from validation
residuals with an embargo covering the label horizon. This one allocates from price moments and
needs no calibration at all.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 3. The backtest

The strategy specification is the selected configuration's own, re-pointed at the holdout
prediction set and the holdout price window. Nothing else about it changes - the signal, the
allocator and the [[ML4T_A3_0001]] overlay are carried across, and the commission and slippage are
the levels [[ML4T_A3_0002]] declares, the same ones every validation number in this case study was
net of and the same ones sitting inside the swept grid in [[[ML4T_A3_0003]]](16_costs.ipynb).

The run registers under [[ML4T_A3_0004]], which the registry derives from the prediction
set's split rather than from anything asserted here.

The window carries one backtest at a time, for the same reason 17 lets it carry one
prediction generation at a time. 17's guard is on the model - the training identity and the
checkpoint - and it cannot see this one: a changed allocator, overlay or cost level
produces the same holdout predictions and a different result from them.

Two fields are rebuilt rather than carried. [[ML4T_A3_0005]] records the digests of the data a
run actually read - here the price panel and the official funding settlements - and the selected
configuration's copy describes the validation window. Cloning it produces a record that names
inputs the run never touched, which is exactly what a consumer checking a price digest against
the canonical one would refuse. They are derived from the holdout frames instead.

The funding settlements are also passed to the runner, not merely digested. This case study
is about a cashflow that accrues on holding rather than trading, every validation number in
it is net of the funding the position actually paid or received, and a holdout run that
omitted it would compare a strategy without its central economics against one with it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0008-p001

~~~~~~markdown

The test is the backtest hash, not a field-by-field comparison. Every input that changes
the result is in that hash by construction, and a guard naming fields instead has to be
right about all of them. The hash is resolved before anything runs, so nothing is evaluated
on the holdout before the question is answered, and it comes from [[ML4T_A3_0001]] -
the call the runner itself makes - so the guard and the runner cannot disagree about
identity. The run asserts they still agree afterwards, because a guard that had quietly
stopped predicting the hash would let everything through while looking correct.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p001>>>
<<<ML4T-ZH-END:c0008-p001>>>

### c0010-p000

~~~~~~markdown
## 4. What it came out at

The two numbers below are one strategy measured on two disjoint periods, and the gap
between them is not an estimate of decay. The validation figure is the maximum of a ranking
over thousands of backtests, so it carries the selection; the holdout figure is one
measurement, so it carries its own sampling error. Both push the pair apart before any real
change in the strategy's edge.
[[[ML4T_A3_0001]]](19_strategy_analysis.ipynb) is where they are given intervals and
the selection correction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>
