# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：06_strategy_definition/02_cv_foundations.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cross-validation → 交叉驗證
- Look-ahead bias → 前瞻偏誤
- Hyperparameter → 超參數

## 待翻譯英文單元

### c0024-p000

~~~~~~markdown
---

## 5. Label Buffer (Purging)

Walk-forward CV respects temporal order, but there's a subtler problem:
**labels take time to materialize**. A 21-day forward return label computed
at time [[ML4T_A3_0001]] uses prices from [[ML4T_A3_0002]] to [[ML4T_A3_0003]]. If validation starts at [[ML4T_A3_0004]],
the training label has "seen" 11 validation-period prices.

This is **label leakage** — the most common form of look-ahead bias.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
### Visualizing the Overlap Problem
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
### The Solution: Label Buffer (Purge Gap)

End training at least [[ML4T_A3_0001]] samples before validation starts, where [[ML4T_A3_0002]] is the
label horizon. López de Prado (2018) calls this **purging**.

[[ML4T_A3_0003]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0029-p000

~~~~~~markdown
### Walk-Forward CV with Label Buffer

[[ML4T_A3_0001]] implements label buffer via the [[ML4T_A3_0002]] parameter.
With [[ML4T_A3_0003]], the gap is counted in **NYSE trading days**.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
The hatched regions are **label buffer gaps**: 21 NYSE trading days where
training labels would overlap with validation. These samples are excluded
from training but not used for validation — they are simply discarded.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
---

## 6. Feature Buffer (Embargo)

The label buffer prevents **forward-looking** leakage: training labels that
peek into the validation period. But there is a second leakage channel:
**backward-looking features** computed from validation data that bleed into
training.

This matters in **CPCV** and **k-fold** schemes where a training block can
appear *after* a validation block in calendar time. A 60-day rolling feature
computed for the first training sample after the validation block uses 60 days
of validation-period prices.

López de Prado (2018) calls this the **embargo**.

| Buffer | Direction | Protects Against | When It Matters |
|---|---|---|---|
| **Label buffer** (purge) | Forward-looking | Training labels peeking into validation | Always |
| **Feature buffer** (embargo) | Backward-looking | Training features using validation data | CPCV, k-fold |

In pure walk-forward CV (training always precedes validation), the feature
buffer is **zero** because no training sample follows a validation block.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
**(a)** In walk-forward, training precedes validation. The label buffer
removes training samples whose labels extend into the validation period.

**(b)** In CPCV, a training block can follow a validation block. The feature
buffer removes training samples whose backward-looking features use
validation data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000

~~~~~~markdown
---

## 7. Calendar-Aware Cross-Validation

A **critical subtlety**: financial markets don't trade every calendar day.
The NYSE has ~252 trading days per year, not 365. When we specify a label
horizon of 21 days for monthly forward returns, we mean **21 trading days**.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0037-p000

~~~~~~markdown
### The Problem: Naive Calendar-Day Purging

January 2024 has 31 calendar days but only 21 NYSE trading days.
A naive 21-calendar-day purge before February 1 (Jan 11-31) only removes 14
trading days — allowing 7 trading days of leakage.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000

~~~~~~markdown
**Rule**: Always count purge gaps in **trading days**, not calendar days.
[[ML4T_A3_0001]] handles this automatically when given a [[ML4T_A3_0002]] parameter.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0040-p000

~~~~~~markdown
### Calendar-Aware Splits in Practice

Passing [[ML4T_A3_0001]] ensures [[ML4T_A3_0002]] counts the label buffer
in NYSE trading days, skipping weekends and holidays.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
Each fold withholds 21 trading sessions - the label horizon - and those 21
sessions span roughly 30 calendar days once weekends and holidays are counted.
A naive implementation that purges 21 *calendar* days instead (Jan 11-31, 2024,
say) removes only 14 trading days and leaves 7 days of label leakage. The
[[ML4T_A3_0001]] parameter is what makes the buffer count sessions.

One arithmetic note, because it is easy to misread the numbers above: the *index*
distance between the last training row and the first validation row is 22, not 21.
Purging 21 sessions leaves 21 rows in between, so the endpoints sit 22 apart. The
buffer is 21; 22 is an off-by-one waiting to be quoted as a fact.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
---

## 8. Nested Walk-Forward

Standard walk-forward CV tunes hyperparameters on one validation period
(e.g., 2019–2023), then tests once on the holdout (2024–2025). By the time
we reach 2025, those hyperparameters may be stale.

**Nested walk-forward** adds an **outer loop** that rolls the test window
forward, retuning hyperparameters at each step.

- **Inner loop**: Walk-forward CV selects hyperparameters [[ML4T_A3_0001]]
- **Outer loop**: Advances the test window and reruns the inner loop

This produces **multiple test points**, each with freshly tuned
hyperparameters — capturing tuning instability over time.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
### Nested Walk-Forward Timeline

Each outer fold runs a full inner walk-forward CV to select
[[ML4T_A3_0001]], then evaluates on its test year.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>
