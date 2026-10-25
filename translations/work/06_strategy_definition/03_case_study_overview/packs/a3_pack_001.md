# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：06_strategy_definition/03_case_study_overview.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Case Study Overview: Cross-Strategy Summary

**ML4T Third Edition - Chapter 6: Strategy Research Framework**

**Docker image**: [[ML4T_A3_0001]]

This notebook provides a unified view of all 9 case studies used throughout this book.
It consolidates key information that readers need to understand:

- **What datasets we cover**: Asset classes, universes, and time periods
- **Trading setup constraints**: Cost models, horizons, and feasibility analysis
- **Evaluation protocols**: Walk-forward configurations and holdout policies
- **Prediction coverage**: Calendar-year spans for training, validation, and holdout

**Book Reference**: Chapter 6, Sections 6.3 and 6.5

**Prerequisites**: Each case study must have a [[ML4T_A3_0002]] defining
the trading setup, universe, evaluation protocol, and cost model.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0004-p000

~~~~~~markdown
## Load Results

Each case study's [[ML4T_A3_0001]] defines the trading setup, universe,
evaluation protocol, and cost model. We load all available configs and build
comparative tables from them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
### Infer Asset Class
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
### Load All Case Study Configs
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
## Helper: Window Conversion
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
---

## 1. Case Study Inventory

The book uses 9 case studies that span different asset classes, frequencies,
and time horizons. This diversity demonstrates how the same ML4T workflow
adapts to different trading contexts.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
**What to notice**:
- Universe sizes range widely: from 19 (Crypto) and 20 (FX) through the low
  hundreds (ETFs 100, NASDAQ-100 114, the S&P 500 option books ~600-630) up to
  the multi-thousand equity panels (US Firm Characteristics ~2,500, US Equities
  Panel 3,199) - a span that reshapes cross-sectional signal construction
- Data frequencies span 15-minute bars (NASDAQ-100) to weekly (CME Futures, S&P 500)
- Cost models are either "Material" (7 case studies) or "Dominant" (2),
  where dominant costs require exceptionally strong signals
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0017-p000

~~~~~~markdown
### Asset Class Distribution
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
**What to notice**:
- Equities dominate (3 pure + 1 hybrid), reflecting their importance in ML4T
- "Equities+Options" is a hybrid: trades equities using options-derived features
- Each non-equity asset class (Crypto, FX, Futures, Options, Multi-Asset) has
  one dedicated case study showing unique mechanics
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0020-p000

~~~~~~markdown
---

## 2. Evaluation Protocol Summary

Each case study defines a walk-forward evaluation protocol. The key parameters are:
- **Training window**: How much history to use for model fitting
- **Test window**: Validation fold duration
- **Holdout period**: Data set aside for final confirmation
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
**What to notice**:
- Training windows range from 6M (microstructure) to 10Y (firm characteristics),
  reflecting both data availability and stationarity assumptions
- Fold counts vary from 2 (shorter histories: crypto, microstructure, options) to 16 (US equities)
- Every case study sets a holdout aside; this discipline is non-negotiable
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
---

## 3. Cost Model and Horizon Feasibility

Trading costs constrain viable horizons. This section summarizes the cost-horizon
analysis from each setup notebook.

### Cost Model Classes

| Class | Description | Implication |
|-------|-------------|-------------|
| **Dominant** | Costs are first-order; small edges live near the spread | Need very strong predictability; costs dominate feasibility |
| **Material** | Costs affect profitability but don't rule out trading | Horizon choice depends on signal decay vs cost hurdle |

The **dominant** cost regime (NASDAQ-100 microstructure, S&P 500 options) requires
unusually strong signals to overcome friction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0025-p000

~~~~~~markdown
The class alone does not say what the friction is. Each [[ML4T_A3_0001]] declares its own
cost components, in whatever unit that market quotes: basis points a leg, ticks,
a percentage of the option premium. Printing the declared block for the two extremes
is the only way to compare them without a number going stale in the prose here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0027-p000

~~~~~~markdown
**What to notice**:
- FX carries the tightest quoted spreads of the nine, in single-digit basis points a
  leg and tighter on the majors than the crosses, which is what lets it decide daily
- An option's spread is quoted against its own premium rather than against notional,
  and at the fraction printed above the cost is the binding constraint on the strategy
- Horizon choice aligns with cost: higher costs push toward longer holding periods
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>
