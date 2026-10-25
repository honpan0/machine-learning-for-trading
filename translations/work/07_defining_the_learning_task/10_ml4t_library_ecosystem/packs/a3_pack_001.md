# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/10_ml4t_library_ecosystem.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Momentum → 動能
- Feature → 特徵
- Feature engineering → 特徵工程
- Cross-validation → 交叉驗證
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0001-p000

~~~~~~markdown
# The ml4t Library Ecosystem

**Docker image**: [[ML4T_A3_0001]]

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.1 - Data Preprocessing and Encodings

## Purpose

This notebook introduces the **ml4t library ecosystem** used throughout
Chapters 7-12: data loaders ([[ML4T_A3_0002]]), feature computation
([[ML4T_A3_0003]]), and evaluation tools ([[ML4T_A3_0004]]).

## Learning Objectives

1. Load datasets using the unified [[ML4T_A3_0005]] loaders
2. Discover and compute features via the [[ML4T_A3_0006]] registry
3. Configure features with lists, dicts, or YAML for reproducibility
4. Validate library features against manual implementations
5. Preview feature evaluation with [[ML4T_A3_0007]] (full treatment in
   [[ML4T_A3_0008]])
6. Understand when to use the library vs manual code

## Data Policy

All examples use **real ETF data** (no synthetic data).

## Prerequisites

- [[ML4T_A3_0009]] - establishes the ETF dataset shape used here.
- Polars basics ([[ML4T_A3_0010]], [[ML4T_A3_0011]], [[ML4T_A3_0012]]).
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0004-p000

~~~~~~markdown
## ml4t-data: Unified Data Loaders

The [[ML4T_A3_0001]] module provides consistent interfaces for all seven
datasets introduced in Chapter 2. Each loader returns a Polars DataFrame
with standardized column names.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## ml4t-engineer: Feature Registry

The [[ML4T_A3_0001]] library provides 120+ pre-built features with
consistent naming, validation against reference implementations (TA-Lib
where applicable), and self-documenting metadata.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Feature Metadata

Each registry entry carries its default parameters, input requirements, and
a description, plus a closed-form formula where a standard one exists (about
a quarter of the catalog: momentum and price transforms tend to have one,
while estimator-based volatility and microstructure features do not). This
makes features discoverable without reading source code.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## Config-Driven Feature Computation

[[ML4T_A3_0001]] accepts three input formats, from simplest to most
reproducible:

1. **List of names** - default parameters
2. **List of dicts** - custom parameters per feature
3. **YAML config** - stored configuration for pipelines
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0012-p000

~~~~~~markdown
### Simple Feature List
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Parameterized Features

A list of dicts sets explicit parameters per feature. Each feature name
resolves to one output column per call, so a single call holds one parameter
set per feature. To compute several horizons of the *same* indicator (a
common multi-timeframe setup), call [[ML4T_A3_0001]] once per parameter set
and suffix the columns before joining.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0015-p000

~~~~~~markdown
Each entry below names one feature with an explicit parameter set. Bollinger bands take
their two deviations separately, following TA-Lib, so the upper and lower band need not
sit the same distance from the moving average.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0018-p000

~~~~~~markdown
### YAML Configuration (Production)

For reproducibility across notebooks and case studies, store feature
configurations in YAML:

[[ML4T_A3_0001]]

Load with: [[ML4T_A3_0002]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## Validation: Library vs Manual

The library uses Wilder's smoothing (matching TA-Lib) while a naive
implementation might use EWM span. Let's compare to understand the
difference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
### When to use the library vs manual code

| Use ml4t-engineer | Implement manually |
|---|---|
| Standard indicators (RSI, MACD, ATR) | Custom alpha factors |
| Production pipelines | Pedagogical demonstrations |
| Cross-validation with TA-Lib | Non-standard variations |
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
## ml4t-diagnostic: Feature Evaluation (Preview)

The third library, [[ML4T_A3_0001]], closes the loop: once a feature is
computed, [[ML4T_A3_0002]] measures whether it predicts forward returns in
the cross-section, reporting the Information Coefficient (rank correlation of
factor to forward return), its t-statistic, and quantile spreads. Here we run
a single call to show the [[ML4T_A3_0003]] to [[ML4T_A3_0004]] handoff on the
full ETF panel. Notebook [[ML4T_A3_0005]] develops the full workflow
(ICIR, quantile monotonicity, turnover, half-life).
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
The 21-day momentum factor carries near-zero cross-sectional IC on this ETF
universe, and the t-statistics do not clear conventional significance. A
single raw indicator rarely predicts returns on its own; the feature
engineering and model-based combination methods in Chapters 8 through 12 are
what turn raw features into usable signals. The point here is the interface:
[[ML4T_A3_0001]] produces the factor and [[ML4T_A3_0002]] scores it, with no
glue code in between.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
## Key Polars Patterns for Feature Engineering

These three patterns account for most of the feature-engineering code in this book.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>
