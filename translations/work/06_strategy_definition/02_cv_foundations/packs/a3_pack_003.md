# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：06_strategy_definition/02_cv_foundations.ipynb；A3 Pack 003；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Sharpe ratio → 夏普比率
- Feature → 特徵
- Label → 標籤
- Out-of-sample → 樣本外
- Overfitting → 過度擬合
- Hyperparameter → 超參數

## 待翻譯英文單元

### c0047-p000

~~~~~~markdown
Each outer fold produces test predictions with freshly selected [[ML4T_A3_0001]].
If [[ML4T_A3_0002]], the selected hyperparameter is not stable across
the two tuning periods, and a single tuned value should not be carried into
production on the strength of one of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0048-p000

~~~~~~markdown
---

## 9. Combinatorial Purged CV (CPCV)

Walk-forward CV produces **one backtest path** — a single sequence of
out-of-sample predictions. That path might reflect luck.

**CPCV** divides time into [[ML4T_A3_0001]] contiguous blocks, holds out [[ML4T_A3_0002]] blocks for
validation, trains on the remaining [[ML4T_A3_0003]] (with purging at boundaries),
and repeats for all [[ML4T_A3_0004]] combinations. The validation predictions
are then assembled into **multiple complete backtest paths**, each covering
every time block exactly once.

Each path is a complete out-of-sample backtest — one prediction per block,
assembled from different splits so no block's prediction depends on its own
training data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
The figure below shows block occupancy for every split: the y axis is the split and
the x axis is the sample index. Nothing is plotted against a value, because a split
has no value. It is a partition, and the only information in it is which block each
sample falls in.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0052-p000

~~~~~~markdown
Amber is validation and slate is training. Purged and embargoed samples are grey,
but at this scale they are a sliver a few pixels wide at each block boundary - the
buffer is 5 + 2 samples against blocks of 84 - so the counts are printed below
rather than left to the eye. Read across the amber positions: no two splits
validate the same pair of blocks, which is what "combinatorial" means here.

### Assembling the paths

The claim this section rests on is that [[ML4T_A3_0001]] splits yield **5** backtest
paths, and that is worth showing rather than asserting. A *path* is a set of splits
whose validation blocks tile the whole timeline exactly once - so each path needs
[[ML4T_A3_0002]] splits, and [[ML4T_A3_0003]] paths. Each block is validated in [[ML4T_A3_0004]]
different splits, once per path.

Constructing them is the round-robin pairing used to schedule a tournament: fix one
block, rotate the rest, and read off the pairs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0054-p000

~~~~~~markdown
Gray regions are samples removed by the label buffer (purge) and feature
buffer (embargo) at block boundaries. With [[ML4T_A3_0001]], [[ML4T_A3_0002]]: 15 splits produce
5 independent backtest paths.

If all paths show similar Sharpe ratios → robust. If they vary wildly →
path-dependent (possibly overfit). Bailey et al. (2014) formalize this into
the **Probability of Backtest Overfitting (PBO)** — the fraction of paths
whose in-sample rank doesn't hold out-of-sample. We return to PBO in
Chapter 17 when assembling full backtest results.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0055-p000

~~~~~~markdown
---

## 10. Putting It Together

### CV Method Comparison

| Method | Paths | Label Buffer | Feature Buffer | When to Use |
|---|---|---|---|---|
| Walk-Forward | 1 | Yes | No (train < val) | Standard evaluation |
| Nested Walk-Forward | 1 per test year | Yes | No | Multi-year test with retuning |
| CPCV | Multiple | Yes | Yes | Robustness testing (Ch17) |
~~~~~~

<<<ML4T-ZH-BEGIN:c0055-p000>>>
<<<ML4T-ZH-END:c0055-p000>>>

### c0056-p000

~~~~~~markdown
### From Config to Protocol

[[ML4T_A3_0001]] encodes all CV design decisions in a single object.
Each case study's [[ML4T_A3_0002]] stores these commitments; downstream
notebooks load them via [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>

### c0058-p000

~~~~~~markdown
### Loading a Case Study Protocol

Each case study stores its CV protocol in [[ML4T_A3_0001]].
The [[ML4T_A3_0002]] function loads it into a [[ML4T_A3_0003]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0058-p000>>>
<<<ML4T-ZH-END:c0058-p000>>>

### c0060-p000

~~~~~~markdown
This protocol specifies 8 walk-forward splits with 10-year rolling
training windows, 1-year test windows, and a 21-trading-day label buffer
(matching the 1-month forward return labels). The holdout period
(2024–2025) is set aside for final confirmation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0060-p000>>>
<<<ML4T-ZH-END:c0060-p000>>>

### c0061-p000

~~~~~~markdown
---

## Key Takeaways

### Decision-Time Admissibility
- The central constraint: only information available at decision time [[ML4T_A3_0001]]
  can enter training for predictions at [[ML4T_A3_0002]]
- Five leakage channels: label, standardization, threshold, survivorship,
  point-in-time

### Walk-Forward CV
- Training always precedes validation (respects temporal order)
- Expanding (all history) vs rolling (fixed window) — depends on regime beliefs

### Label Buffer (Purging)
- Forward-looking labels can leak validation data into training
- Remove training samples within one label horizon of validation start
- Count in **trading days** using a proper market calendar

### Feature Buffer (Embargo)
- Backward-looking features can leak validation data into training
- Matters in CPCV / k-fold where training follows validation in time
- Zero in pure walk-forward (training always precedes validation)

### Nested Walk-Forward
- Outer loop advances test window; inner loop retunes hyperparameters
- Captures tuning instability — [[ML4T_A3_0003]] should be stable across periods

### Combinatorial Purged CV
- Multiple backtest paths from the same data reveal robustness
- Connects to Probability of Backtest Overfitting (Bailey et al. 2014)
- Full treatment in Chapter 17

**Next**: See [[ML4T_A3_0004]] for applying these concepts
to real trading strategies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>
