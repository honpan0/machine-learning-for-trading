# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/02_gbm_comparison.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Hyperparameter → 超參數
- Cross-sectional → 橫斷面
- Correlation → 相關性

## 待翻譯英文單元

### c0036-p000

~~~~~~markdown
## 10. GPU Speedup at Scale

The ETF benchmark above is small enough (227K training rows) that GPU
launch overhead competes with kernel time. We re-run the medium preset
on the US Equities Panel (~5M training rows) to demonstrate how dataset
scale changes the picture. LightGBM's CUDA backend computes in double precision
only: its [[ML4T_A3_0001]] toggle "can be used only in OpenCL implementation
([[ML4T_A3_0002]]), in CUDA implementation only double precision is currently
supported" (LightGBM docs). A consumer GPU runs FP64 at a small fraction of its
FP32 throughput, so LightGBM's CUDA path runs and gains far less from the device
than XGBoost or CatBoost.

> **Run this notebook in the [[ML4T_A3_0003]] Docker image.** Only that image
> (and [[ML4T_A3_0004]]) ships a LightGBM compiled from source with [[ML4T_A3_0005]];
> the local [[ML4T_A3_0006]] venv installs the PyPI wheel, which is CPU/OpenCL-only and
> has NO CUDA build. Under [[ML4T_A3_0007]], [[ML4T_A3_0008]] reports
> [[ML4T_A3_0009]], the [[ML4T_A3_0010]] loop skips LightGBM, and its
> GPU rows silently vanish. If the GPU detection panel above does not list
> all three of xgboost/lightgbm/catboost, you are NOT in the CUDA-LightGBM
> image and the GPU numbers are wrong: do not record them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0039-p000

~~~~~~markdown
**Interpretation**: where this run produced the table above, it is this machine on
this run and nothing more. What
carries beyond it is the reason the three libraries differ, which is
architectural rather than incidental: LightGBM's CUDA backend computes in double
precision only, and a consumer GPU runs FP64 at a small fraction of its FP32
throughput, so LightGBM has the least to gain from the device while often being
the quickest of the three on CPU. Read the ratios as a demonstration of that
shape, not as numbers to quote: they move with load, thread count and hardware.
The smaller ETF panel earlier in the notebook makes the same point from the other
side, where launch overhead competes with kernel time and the ordering is less
stable.

Every CPU row of the scale benchmark runs at [[ML4T_A3_0001]], the same thread count as the
ETF benchmark above, so the comparison is per-thread work at the row count printed
with the dataset rather than thread oversubscription on a high-core-count machine.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0040-p000

~~~~~~markdown
## 11. Monotonic Constraints and SHAP Dependence

Monotonic constraints force the model to respect a directional relationship:
a constrained feature cannot reverse direction. We compare SHAP dependence
plots for the same feature with and without a negative monotonic constraint,
demonstrating that constraints eliminate spurious local reversals while
preserving the overall relationship.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
### SHAP Dependence: Constrained vs Unconstrained
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0045-p000

~~~~~~markdown
**What to read off it.** Both panels are on one vertical scale, and that is the
comparison. The constrained model has not bent this feature's contribution into a
downward curve; it has flattened it, which satisfies a non-increasing constraint the
cheap way. A monotone prior imposed on a feature whose empirical relationship is
noisy does not force the model to find a monotone signal - it lets the model stop
using the feature's variation, and the range printed above is how far that went.

The two test ICs are close, and on one fold with no interval that is not evidence
either way about the constraint. A directional prior is worth imposing when it is
right, and this notebook cannot tell you whether it is; that needs the constrained
and unconstrained models scored across folds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0046-p000

~~~~~~markdown
## 12. Learning-to-Rank Worked Example (LambdaMART)

The chapter text discusses a ranking objective for cross-sectional stock
selection. We implement a compact LambdaMART workflow using date-wise query
groups and relevance labels derived from forward returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0050-p000

~~~~~~markdown
### Mean Group NDCG
Compute mean NDCG@k across query groups for learning-to-rank evaluation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0053-p000

~~~~~~markdown
**Interpretation**: the table above scores each model on both metrics. Note what
the NDCG column can and cannot settle: LambdaMART is trained on a ranking
surrogate and scored with a ranking metric, so an advantage there is the setup
working as arranged rather than a finding. The IC column is the interesting one,
because nothing in the ranking objective asks for a correlation with return
magnitude, and on a single fold the two metrics can agree or disagree by chance.

The choice between them is not decided by either number. Ranking suits top-k
selection within a rebalance, regression suits a signal whose magnitude sizes a
position, and either way the comparison needs multiple folds before it means
anything.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0054-p000

~~~~~~markdown
## 13. Key Takeaways

1. **This single-fold benchmark does not rank the libraries on accuracy.** Every
   library and preset lands at a negative test IC on the ETF fold, and the table
   above gives the range. The benchmark is built for engineering questions - timing,
   memory, device behaviour - and an accuracy ordering needs multi-fold CV with tuned
   hyperparameters, which is [[ML4T_A3_0001]].

2. **What a GPU buys depends on the library, and the reason is architectural.**
   LightGBM's CUDA backend is double-precision only and consumer GPUs run FP64 at a
   fraction of FP32 throughput, so it gains least from the device while often being
   quickest on CPU. The ratios in the tables are this machine on this run; the reason
   they differ is what carries. LightGBM's CUDA path needs the [[ML4T_A3_0002]] image at
   all: the PyPI wheel in the local venv has no CUDA build.

3. **CPU and GPU are related but distinct estimators.** Histogram binning at
   different precision changes split points, and those differences cascade through
   the ensemble into IC differences larger than rounding. Do not treat a GPU rerun as
   a reproduction of a CPU result.

4. **The memory panel is a lower bound, and mostly reads zero.** RSS delta is
   dominated by allocator and garbage-collection timing and cannot see native or
   device allocations, so it neither ranks the libraries nor sizes hardware. Use a
   profiler or peak RSS for that; the panel is here to show what the cheap probe does
   and does not capture.
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>
