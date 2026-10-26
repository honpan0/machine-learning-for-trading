# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/19_holdout_backtest.ipynb；A3 Pack 001；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Slippage → 滑價
- Label → 標籤
- Out-of-sample → 樣本外
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: Holdout Backtest

**Chapter 20 - Out-of-sample evaluation**

[[[ML4T_A3_0001]]](18_holdout_predictions.ipynb) refitted the selected
configuration on the history before the holdout window and wrote its predictions over it.
This notebook trades them, with the concentration, the allocator, the risk overlay and the
cost assumption the rest of the case study used, and registers the result.

Nothing is chosen here. The predictions, the allocator, the concentration, the rebalance
cadence, the overlay and the charge all arrive fixed from earlier notebooks, and the only
thing this notebook decides is that they are applied unchanged. That is the whole design: a
holdout result is worth something exactly to the extent that no decision was made after
seeing it, and every knob left open here would be a decision.

The comparison to validation is printed but not interpreted. The validation figure is the
maximum of a ranking over more than a thousand backtests and the holdout figure is one
measurement over a much shorter window; what can be said about the gap between them is
[[[ML4T_A3_0002]]](20_strategy_analysis.ipynb)'s subject, with the intervals to say
it.

**Prerequisites:** [[[ML4T_A3_0003]]](18_holdout_predictions.ipynb).

**Scope:** one backtest. No selection, no comparison beyond a printed pair.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## 1. The configuration, and the predictions it produced on the holdout

The selected configuration is resolved the same way [[[ML4T_A3_0001]]](17_costs.ipynb) and
[[[ML4T_A3_0002]]](18_holdout_predictions.ipynb) resolve it, so all three run the
same configuration by construction rather than by a hash copied between them.

Which holdout prediction set belongs to it is derived rather than searched for. Re-deriving the
holdout training specification reproduces the training identity 18 registered - the derivation is
deterministic and the identity covers it - so the prediction set is looked up by that identity
and the selected configuration's checkpoint. A search over holdout prediction sets would have to
guess which one belonged to this configuration.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Calibration, where the allocator needs it

An allocator that sizes by a conformal width is calibrated from errors the model has already
made, and on the holdout there are none to use: an error is usable only once the return it
measures has been realised, and every holdout return realises inside the window being evaluated.
Such a selected configuration takes its widths from the validation residuals of the validation
prediction set, which is what the allocator would have had standing at the start of the window.

The embargo matters for this case study's label and would not for every one. A residual
observed at [[ML4T_A3_0001]] measures a return realising over [[ML4T_A3_0002]] sessions, so the last residuals
of the validation span reach into the holdout window, and calibrating on them would size
holdout positions with holdout price information. The step count comes from the reviewed
table in [[ML4T_A3_0003]], which records the label horizon.

The branch is here rather than assumed away because the selected configuration can change. It
does not fire for the one this case study currently reports, which sizes by inverse volatility
over a declared window and needs no calibration - so the line below prints that rather than
staying silent, which is what tells a reader the branch was evaluated.

The widths themselves are NOT written here. Writing them replaces the artifact an already
registered run was sized by, and the replacement guard in section 3 can still refuse this run
afterwards - which would leave the registered holdout pointing at a calibration that no
longer existed. The write is below the guard.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 3. The backtest

The strategy specification is the selected configuration's own, re-pointed at the holdout
prediction set and the holdout price window. Nothing else about it changes - the concentration,
the allocator, the risk overlay and the commission and slippage levels are the ones [[ML4T_A3_0001]]
declares and every validation number in this case study was net of.

The run registers under [[ML4T_A3_0002]], which the registry derives from the prediction set's
split rather than from anything asserted here - and that derivation takes precedence over the
risk block the selected configuration carries, which would otherwise file this as another risk
overlay.

**The window carries one backtest**, for the same reason 18 lets it carry one prediction
generation. 18's guard is on the model - the training identity and the checkpoint - and it
cannot see this one: a changed allocator, overlay, cost level or calibration produces the
same holdout predictions and a different result from them. Like 18's, this guard refuses
rather than offering a replacement, because deleting a result that has been seen does not
unsee it.

The test is the backtest hash, not a field-by-field comparison. Every input that changes the
result is in that hash by construction, and a guard naming fields instead has to be right
about all of them. The hash is resolved before anything runs, so nothing is evaluated on the
holdout before the question is answered, and it comes from [[ML4T_A3_0003]] - the call
the runner itself makes - because asking it is the only way to be sure the guard and the
runner agree about identity. The run asserts they still agree afterwards, because a guard
that had quietly stopped predicting the hash would let everything through while looking
correct.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 4. What it came out at

The two numbers below are one strategy measured on two disjoint periods, and the gap between
them is not an estimate of decay. The validation figure is the maximum of a ranking over more
than a thousand backtests, so it carries the selection; the holdout figure is one measurement
over a much shorter window, so it carries that window's sampling error. Both push the pair
apart on their own, before any real change in the strategy's edge.
[[[ML4T_A3_0001]]](20_strategy_analysis.ipynb) is where they are given intervals and a
paired comparison.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>
