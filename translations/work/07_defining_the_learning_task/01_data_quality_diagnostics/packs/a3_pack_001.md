# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/01_data_quality_diagnostics.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Feature engineering → 特徵工程

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Data Quality Diagnostics

**Docker image**: [[ML4T_A3_0001]]

**Chapter 7: Defining the Learning Task**
**Section Reference**: 7.1 - Data Preprocessing and Encodings

## Purpose

This notebook provides a **standardized diagnostic survey** across all ML4T datasets.
No cleaning is performed - just assessment. The output is a "health report" identifying
which datasets need active preprocessing versus which are already in good shape.

## Learning Objectives

1. Build reusable diagnostic functions for financial panel data
2. Understand common data quality issues: missingness, duplicates, outliers, gaps
3. Identify dataset-specific quirks that affect ML pipeline design
4. Create a systematic framework for data validation

## Book Reference

Section 7.1 emphasizes that **data quality determines model quality**. This notebook
operationalizes that principle with concrete diagnostics before any feature engineering.

## Prerequisites

- Familiarity with the seven ML4T datasets and their loaders ([[ML4T_A3_0002]] module).
- Polars basics ([[ML4T_A3_0003]], [[ML4T_A3_0004]], [[ML4T_A3_0005]]).
- No prior notebook output is required; this is the entry point of the pipeline.

## Data Contract

- **Input**: Raw datasets from data loaders (ETFs, US Equities, Crypto, etc.)
- **Output**: Diagnostic reports and quality assessments (no mutations)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Diagnostic Function Library

These functions are designed to be **reusable** across datasets and chapters.
They follow a consistent interface: input DataFrame, return diagnostic results.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0004-p000

~~~~~~markdown
### Index Integrity Check

Validates that the time index has correct dtype, monotonicity, and uniqueness.
For panel data, also checks that (date, symbol) pairs are unique.

The monotonicity check reads each symbol's rows in the order they arrive. Sorting the
frame by symbol and time before asking whether time is sorted would return True for
every input, including a frame whose rows are in the wrong order - a check that cannot
fail is the defect this notebook exists to find, and it is an easy one to commit here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
### Duplicate Detection

Finds exact duplicates (identical rows) and near-duplicates (same index, different values).
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
### Coverage Report

Analyzes missingness patterns by field, by asset, and by time period.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### Coverage Heatmap

Visualizes data availability across time × asset for panel data.

The pivot underneath emits one row per month that *has* data, so a month in which the
whole panel is missing - a vendor outage, an ingestion gap - would be absent from the
matrix rather than present as an all-zero row. Any count of "months missing for every
asset" taken off that matrix is therefore zero by construction. Reindexing onto a
continuous month range first is what makes the count capable of firing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
### Distribution Summary

Computes summary statistics and flags extreme values.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Outlier Flags

Detects domain violations and spike anomalies (single-bar reversals).
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
## Dataset Registry

Central registry mapping dataset names to loader functions and metadata.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
## Per-Dataset Diagnostics

Run all diagnostics for each available dataset. Results are stored for the
summary dashboard.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0022-p000

~~~~~~markdown
### ETF Universe

Yahoo Finance data covering 100 ETFs across 9 asset classes. Key concerns:
adjustment artifacts from corporate actions and ticker changes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0027-p000

~~~~~~markdown
ETFs pass index integrity and duplicate checks. Coverage is near-complete for
OHLCV fields. Any outlier flags likely reflect Yahoo Finance adjustment
artifacts (split ratios applied to historical bars) rather than genuine
price anomalies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0027-p000>>>
<<<ML4T-ZH-END:c0027-p000>>>

### c0028-p000

~~~~~~markdown
### US Equities

The longest panel in the survey, and the only survivorship-free one. Key concerns:
penny stocks, stock splits, and delisting events. The loaded span starts at
[[ML4T_A3_0001]] rather than at the vendor's first year.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0031-p000

~~~~~~markdown
### A one-sided filter, and the column that shows it

It is tempting to read "extreme returns" as "corporate actions" and move on. This
dataset ships a [[ML4T_A3_0001]] column, so we do not have to guess - and checking
turns the reading around.

A raw return is bounded below by [[ML4T_A3_0002]], because a price cannot fall below zero. So a
symmetric-looking filter on [[ML4T_A3_0003]] **can only ever fire on the upside**. A reverse
split, which multiplies the price, clears the threshold easily. A forward split, which
divides it, cannot reach [[ML4T_A3_0004]] however large the split, so it is invisible to the filter
by construction rather than by accident.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>
