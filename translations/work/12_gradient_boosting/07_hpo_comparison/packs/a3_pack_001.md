# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/07_hpo_comparison.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Out-of-sample → 樣本外
- Overfitting → 過度擬合
- Hyperparameter → 超參數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Grid Search vs Optuna: HPO Method Comparison

**Docker image**: [[ML4T_A3_0001]]

**Chapter 12, Section 12.4**: Advanced Hyperparameter Tuning with Optuna

## Purpose
This notebook compares grid search against Optuna's Bayesian optimization on
the same parameter budget, first on a space grid can enumerate and then on a
continuous one it cannot. It also measures validation overfitting: how
test IC diverges from validation IC as trial count increases.

## Key Insight
The comparison is decided by the space, not by the sampler. On a grid small
enough to exhaust, search has nothing to exploit and exhaustion wins by
construction; a continuous space is where sampling reaches configurations a
discrete grid cannot represent at all. The wall times reported along the way
are single uncontrolled runs, not a cost comparison.

## Cross-References
- **Section 12.4**: TPE, pruning, and its box on validation overfitting
- **Related**: [[ML4T_A3_0002]] (full workflow), [[ML4T_A3_0003]] (multi-objective)

## References
- Bergstra & Bengio (2012). "Random Search for Hyper-Parameter Optimization"
- Akiba et al. (2019). "Optuna: A Next-generation HPO Framework"
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0003-p000

~~~~~~markdown
## Settings

[[ML4T_A3_0001]] is the searched space and the only thing that sets what either search costs.
The grid is exhaustive, so its size is [[ML4T_A3_0002]], and section 5 gives
Optuna that same number of trials because equal budget is what the comparison holds fixed.
There is deliberately no separate trial count beside it: one would let a caller set a budget
that is not the grid's and break the comparison without saying so. Shrink the space and both
searches shrink with it.

[[ML4T_A3_0003]] is the ladder for the overfitting sweep in section 8, which searches the
continuous space. The grid does not bound that space, so the ladder is declared rather than
derived from the grid's size.

[[ML4T_A3_0004]] caps the universe each fit trains on, and is what a reduced run sets. Zero is
the full universe.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0006-p000

~~~~~~markdown
## 2. Load Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## 3. Evaluation Functions
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 4. Grid Search

[[ML4T_A3_0001]] in the settings cell is four parameters with a handful of values each, small
enough that enumerating it is tractable. Its size is what both searches spend.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## 5. Optuna (Same Budget, Same Space)

Run Optuna with the same number of trials as grid combinations,
searching the same categorical parameter space.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Same-Budget Comparison
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
**How to read this comparison.** Grid evaluates every combination in [[ML4T_A3_0001]], so
whatever it returns is that space's maximum by construction. Optuna is given the
same number of trials on the same categorical space, and TPE samples with replacement, so
those trials do not cover that many distinct points. It therefore cannot beat the
enumeration here and can only tie it, by happening to sample the maximum - which is not a
fact about the two samplers. On a space small enough to enumerate there is nothing for a
sampler to exploit in exchange for the coverage it gives up; search pays where the space is
too big to enumerate, which is what section 6 tests instead.

The wall-time column is one uncontrolled measurement on a shared machine, and the two
searches fit different sets of configurations, which cost different amounts to train. It is
neither a benchmark nor evidence that either method is cheaper.

The chapter's recommendation stands either way: grid is fine for ≤4 parameters × ≤3 values
each. What the continuous space adds is reach, to configurations a discrete grid cannot
represent at all - a property of the space, not a measurement of the sampler.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
## 6. Optuna with Continuous Space

The real power of Bayesian optimization: searching continuous hyperparameter
spaces that grid search cannot represent.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## 7. Efficiency: how many trials reach most of the search's final value
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
## 8. Validation Overfitting: IC Divergence

Section 12.4's box on validation overfitting warns that a long search fits the
validation window's noise. This section measures it: for increasing trial budgets,
the highest validation IC the search reached, against the holdout IC of the
configuration it selected at that budget.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0024-p000

~~~~~~markdown
**How to read the two columns, and why only one of them can say anything.** The
validation column cannot fall. Each budget builds a fresh study from the same seed, so a
longer budget repeats the shorter one's trials in the same order before adding any of its
own, and the value it records is a running maximum over them. Whatever that column does is
arithmetic. The holdout column has no such constraint - it is the out-of-sample IC of
whichever configuration the search selected at that budget, and nothing pins it in either
direction - so it is the only one of the two that carries information about the budget.

What the mechanism predicts: past some budget the extra trials buy fit to the validation
window's noise and pay for it out of sample. That is the effect Section 12.4's box on
validation overfitting describes, and the reason a trial budget is a parameter to choose
rather than to maximize.

The ladder is a diagnostic and not a selection procedure, and it is bounded on one side
only: it starts at its shortest budget and cannot see below it. It also varies neither the
seed nor the fold, so it gives a direction without a width. Where the two series sit
relative to each other in level is a property of the holdout window, not a sign that tuning
helped. Section 10 asks a different
question - how the two selected configurations compare after refitting on train plus
validation - and a budget sweep inside one space is not the same measurement as a
comparison of two picks from different spaces.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
Holdout IC is already highest at the shortest budget swept, so the turn this section exists
to show sits at or below the ladder rather than inside it. Read the figure as evidence that
the two criteria diverge, not as a way to locate where.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>
