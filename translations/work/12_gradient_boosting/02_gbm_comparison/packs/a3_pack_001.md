# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：12_gradient_boosting/02_gbm_comparison.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Backtesting → 回測
- Feature → 特徵
- Training set → 訓練集
- Test set → 測試集
- Hyperparameter → 超參數

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# GBM Library Benchmark: sklearn vs XGBoost vs LightGBM vs CatBoost

**Docker image**: [[ML4T_A3_0001]]

**Chapter 12, Section 12.2**: The Workhorse - Gradient Boosting Machines

## Purpose
This notebook benchmarks four gradient boosting implementations across CPU and
GPU, measuring accuracy (IC), training time, and memory consumption. The goal
is to provide practitioners with concrete data for library selection rather
than relying on conventional wisdom.

## Learning Objectives
- Compare sklearn HistGradientBoosting, XGBoost, LightGBM, and CatBoost
- Measure GPU speedup on a real financial dataset
- Understand how model complexity (light/medium/heavy presets) affects the
  accuracy–speed–memory tradeoff
- Demonstrate monotonic constraints and SHAP dependence analysis

## Cross-References
- **Section 12.2**: Library comparison and GPU training discussion
- **Related**: [[ML4T_A3_0002]] for hyperparameter optimization
- **Related**: [[ML4T_A3_0003]] for SHAP fundamentals
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### GPU Detection
Probe NVIDIA GPU availability and test each GBM library's GPU backend.
This determines which benchmark configurations to include.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0007-p000

~~~~~~markdown
## 1. GPU Detection

We probe the system for GPU availability. XGBoost and LightGBM use CUDA
directly; CatBoost has its own GPU backend. sklearn does not support GPU.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0010-p000

~~~~~~markdown
## 2. Load Benchmark Data

We use the ETF dataset (99 symbols, ~251K rows, 71 features) as the benchmark
target. A single walk-forward fold avoids CV overhead while producing a
realistic train/test split.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## 3. Benchmark Infrastructure

We define the benchmark grid: 4 libraries × 3 presets × {CPU, GPU}.
Memory is tracked via RSS delta (process resident memory before/after training).
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0015-p000

~~~~~~markdown
## 4. Run Benchmark

Each configuration trains on the full training set and predicts on the test
set. We record IC, wall-clock training time, and RSS memory delta.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
## 5. Accuracy Results (IC)

Test-set IC by library, preset and device. On one fold, a difference of this size
is not a difference: nothing here carries an interval, so read the table for the
sign and the spread rather than for an ordering.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0021-p000

~~~~~~markdown
**Interpretation**: on a single walk-forward fold of the ETF universe, every
library and preset lands at a negative test IC; the table above gives the range.
That is not a judgement on the GBM family. It is what an untuned 21-day return
regression on noisy ETF features does out of sample, which is the assumption
under test here.
The benchmark is informative for *engineering* (timing, memory, GPU behavior
below); accuracy claims should be made on multi-fold CV with tuned hyper-
parameters (notebook [[ML4T_A3_0001]]). CPU and GPU versions of the same
library can produce different predictions due to floating-point precision
(GPU histogram binning typically uses FP32), so the IC differences between
CPU and CUDA columns above illustrate this and are not implementation bugs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
## 6. Training Time Results

Wall-clock training time reveals hardware and algorithmic efficiency.
LightGBM's histogram method is typically fastest on CPU at moderate
thread counts; GPU provides the largest speedup for CatBoost and
XGBoost on larger tree counts.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
**CPU-thread setup.** Every model is constructed with [[ML4T_A3_0001]]
([[ML4T_A3_0002]] for XGBoost/LightGBM, [[ML4T_A3_0003]] for CatBoost) and the
script is invoked with [[ML4T_A3_0004]] so the scikit-learn
HistGradientBoosting path is bounded too. Eight threads is a
representative reader machine; per-tree split decisions are independent
of thread count, only wall times move.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 7. Prediction Speed

Inference latency matters in two production settings: walk-forward backtesting
(millions of predict calls across folds) and live trading (per-bar latency at
rebalance). We report wall-clock [[ML4T_A3_0001]] time on the held-out test set and
the equivalent rows-per-second throughput, separately for CPU and GPU.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0030-p000

~~~~~~markdown
**Interpretation**: Prediction speed depends on the number of trees, tree
depth, and the library's inference implementation. CatBoost uses *symmetric
(oblivious) trees* which collapse each prediction to a bitwise path lookup,
making inference deterministic and often the fastest at moderate tree counts.
XGBoost and LightGBM walk asymmetric trees and have similar CPU inference
costs. GPU [[ML4T_A3_0001]] is rarely worth the launch overhead for batch
inference at the row counts of a typical case study, and the speedups above
are smaller than the training speedups in §6 and can be below 1× for small
batches.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0031-p000

~~~~~~markdown
## 8. Memory Results

RSS delta (resident memory before vs after [[ML4T_A3_0001]]) is a crude lower bound on
training memory: native C/CUDA allocations and memory the allocator has already
reserved or that [[ML4T_A3_0002]] reclaims mid-measurement do not show up. At these dataset
sizes the delta is dominated by allocator/gc timing rather than steady-state
model size: most cells read zero and the few non-zero values do not rank presets
or libraries in any stable way. Read this panel as "training here fits
comfortably in a few hundred MB", not as a memory ranking; use a dedicated
profiler (or peak RSS) if you need to size hardware.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## 9. Visualization

Three-panel benchmark summary: accuracy, speed, and memory across all
configurations.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>
