# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/06_llm_tabular_great.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Label → 標籤
- Clustering → 分群
- Time series → 時間序列
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Chapter 5: LLM-Based Tabular Data Generation (GReaT Framework)

**Chapter 5: Synthetic Data Generation**
**Section Reference**: Section 5.7 (LLMs for structured financial data)

**Docker image**: [[ML4T_A3_0001]]

> **GPU recommended**: This notebook trains models with PyTorch/CUDA. It will run on CPU
> but training may be very slow. For GPU acceleration:
> ```bash
> docker compose run --rm ml4t-gpu python 05_synthetic_data/06_llm_tabular_great.py
> ```


## Purpose

This notebook implements **GReaT (Generate Realistic Tabular Data)** using the
actual [[ML4T_A3_0002]] library to generate synthetic financial tabular data with LLMs.

## Learning Objectives

By completing this notebook, you will:
- Understand the serialization insight for applying LLMs to tabular data
- Fine-tune GPT-2 on serialized financial records using the GReaT framework
- Generate synthetic tabular data and evaluate fidelity
- Compare LLM-based generation to traditional methods (GANs, VAEs)

## Cross-References

- **Book**: Section 5.7 discusses GReaT and LLM-based tabular generation
- **Related**: [[[ML4T_A3_0003]]](02_tailgan_tail_risk.ipynb) (GAN for time series comparison)

---

## Key Concepts

1. **Serialization**: Convert table rows to natural language sentences
2. **Fine-tuning**: Train GPT-2 on serialized financial data
3. **Generation**: LLM produces new "sentences" parsed back to table rows
4. **Mixed Types**: Handle categorical, numerical, and text features naturally

## Why LLMs for Tabular Data?

- Captures complex feature dependencies through attention
- No explicit distribution assumptions
- Handles mixed data types naturally
- Pre-trained language understanding helps with feature names

## Prerequisites
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- [[ML4T_A3_0001]] library ([[ML4T_A3_0002]]) for the GReaT framework
- [[ML4T_A3_0003]] library (installed as a [[ML4T_A3_0004]] dependency)
- ETF data via [[ML4T_A3_0005]] from Ch2

## References

- Borisov et al. (2023). "Language Models are Realistic Tabular Data Generators"
- [[ML4T_A3_0006]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0005-p000

~~~~~~markdown
## 1. Load Real ETF Data

We use actual ETF data to create a tabular dataset suitable for GReaT.
The function below engineers a mix of numerical features (returns, volatility)
and categorical features (direction, momentum regime) to showcase GReaT's
ability to handle mixed-type tabular data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0006-p000

~~~~~~markdown
### Build Tabular Feature Set

Each row represents a single observation: lookback features (returns, volatility,
volume ratio) plus a forward-return target. Categorical columns encode direction,
momentum strength, and volatility regime -- feature types that GANs struggle with
but LLMs handle naturally via serialization.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Load and Inspect

Load the ETF feature table and verify the mix of numerical and categorical columns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## 2. GReaT: LLM-Based Generation

Using the actual [[ML4T_A3_0001]] library with distilgpt2 for fast training.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## 3. Generate Synthetic Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0013-p000

~~~~~~markdown
Guided sampling enforces the column schema row by row. It matters most when
fine-tuning has been short, because the unguided sampler tends to drop columns on an
undertrained model - which surfaces later as unparseable rows. On a well-trained
checkpoint [[ML4T_A3_0001]] is faster and produces equivalent quality.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
**Observation**: The generated rows should contain plausible feature values -- returns
near zero with occasional larger moves, volatility in realistic ranges, and valid
categorical labels. Read the per-column parse counts above as the measure of that: a
count below the number of generated rows means the model wrote something that does not
convert to a number in that column. Counting nulls alone understates it, because a cell
holding the words "not the case" is a string the row parser left in place, not a null.
This is a known limitation of autoregressive generation: the model can "hallucinate"
tokens that break column parsing, especially with short fine-tuning. Increasing epochs
and using larger base models (GPT-2 medium/large) reduces parsing errors significantly,
and a count of zero everywhere is what leaves the comparisons below with nothing to
compare.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0016-p000

~~~~~~markdown
## 4. Fidelity: Visual Comparison with PCA and t-SNE

We project both real and synthetic data into 2D using only numerical features
to assess whether the generator covers the same regions of the data manifold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
**Interpretation**: the two clouds do not sit on top of each other. In the PCA panel
the synthetic rows concentrate to one side, including a dense knot, while the real
rows spread further across the plane; in the t-SNE panel each set occupies a different
part of the area, overlapping in places rather than throughout. On this budget - a
short fine-tune of a small backbone - GReaT is not covering the region the real rows
occupy.

Read that as a statement about this run rather than about the method. The two levers
it does not exercise are the ones the approach depends on: backbone size and
fine-tuning length. What the marginal comparisons below add is *where* the coverage
fails, which the projections cannot say, since a projection mixes every feature
together.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## 5. Compare Real vs Synthetic Distributions
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
## 6. Visualize Distributions
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
## 7. TSTR Evaluation: Train Synthetic, Test Real

The key test: Can a model trained on GReaT synthetic data predict real outcomes?

**Task**: extreme-move classification, whether the absolute five-day forward return
clears a high percentile of its own distribution. The task leans on volatility
clustering, which carries real predictive signal, so a classifier can do meaningfully
better than chance on it. Direction prediction cannot, which is why it makes a poor
yardstick: two models both near chance are hard to tell apart.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>
