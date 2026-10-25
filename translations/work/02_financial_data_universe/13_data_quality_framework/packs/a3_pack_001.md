# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/13_data_quality_framework.ipynb；A3 Pack 001；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Data Quality Framework: Validation, Anomalies, and Remediation

**Docker image**: [[ML4T_A3_0001]]

## Purpose
Demonstrate the four pillars of a production data-quality pipeline applied to US equities
daily OHLCV: structural validation (OHLC invariants, nulls, duplicates), anomaly detection
(return outliers, volume spikes, price staleness), distribution drift (PSI), and ingestion
hygiene (gaps, duplicates, corporate-action detection). All checks come from the
[[ML4T_A3_0002]] and [[ML4T_A3_0003]] modules.

## Learning Objectives
- Run [[ML4T_A3_0004]] and read its issue report, including on data with injected faults.
- See why MAD, Z-score and IQR flag different numbers of events at the same threshold.
- Compute the Population Stability Index, and see what its binning discards.
- Score a corporate-action detector against the split and dividend columns of the same file.

## Book reference
Chapter 2, §2.3 (data quality framework). Downstream chapters that consume the cleaned panel:
[[ML4T_A3_0005]] (bitemporal hygiene), [[ML4T_A3_0006]],
[[ML4T_A3_0007]].

## Prerequisites
- Quandl/Wiki US equities parquet materialized under [[ML4T_A3_0008]] (the legacy dataset;
  ends 2018-03-27).
- Loader [[ML4T_A3_0009]].
- Library packages [[ML4T_A3_0010]] and [[ML4T_A3_0011]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Quieting the library, not the interpreter

The anomaly and validation libraries log a line per symbol per detector through structlog,
which bypasses stdlib logging, so the cells below would print the library's debug stream
rather than their own results. Filtering structlog at WARNING fixes that and leaves
Python's own warnings alone. A blanket [[ML4T_A3_0001]] would also do
it, and would hide the warnings this notebook needs to see: a plotting call that drops its
alt text warns, and under Papermill that warning is the only sign it happened.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
### Declared parameters

Every threshold each detector uses is declared here rather than written into the call that
uses it. Two of them are worth reading before the sections that consume them.

[[ML4T_A3_0001]] is passed unchanged to three detectors that use it as a multiplier on
three different scale estimates, so the same number produces three different cutoffs in
return space. Section 2 measures those cutoffs rather than leaving the comparison implicit.

[[ML4T_A3_0002]] holds five large-cap tickers as the legacy Wiki/Quandl vintage writes them, which
means FB rather than META.

[[ML4T_A3_0003]] is the overnight return above which a move is treated as a
candidate corporate action. The Wiki/Quandl panel carries the actual split ratios and
ex-dividend amounts in its own columns, so Section 4 scores the threshold against them
instead of eyeballing the flagged dates.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0007-p000

~~~~~~markdown
## Load Sample Data

The pre-2018 Wiki/Quandl US equities panel. The validation and anomaly detectors operate on
any DataFrame carrying [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
---

## Part 1: OHLC Invariant Validation

**OHLC invariants** are relationships that hold by the definition of the four fields:

| Invariant          | Why it holds        |
|--------------------|---------------------|
| High >= Low        | by definition       |
| High >= Open, Close| high is the maximum |
| Low <= Open, Close | low is the minimum  |
| Prices > 0         | no negative prices  |
| Volume >= 0        | no negative volume  |

A violation is a provider error, transmission corruption, or an adjustment applied to some
fields and not others.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### A check that passes has not been tested

Every symbol passes, which is the outcome a clean panel should produce and also the outcome
a broken validator would produce. The two are told apart by giving it data known to be bad:
three faults are injected into the demo symbol below, one of each kind the validator claims
to catch, and the report is checked for all three.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
---

## Part 2: Anomaly Detection

Validation asks whether the data is structurally possible. Anomaly detection asks whether
structurally valid data is unusual:

| Detector               | What it finds                  | Method                |
|------------------------|--------------------------------|-----------------------|
| ReturnOutlierDetector  | flash crashes, splits, pumps   | MAD, Z-score, IQR     |
| VolumeSpikeDetector    | unusual trading activity       | rolling Z-score       |
| PriceStalenessDetector | data gaps, illiquid securities | consecutive-unchanged |
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0014-p000

~~~~~~markdown
### The same threshold is three different cutoffs

All three return-outlier methods take a threshold and compare a scaled deviation against it.
They do not scale by the same thing:

- **MAD** flags a return when [[ML4T_A3_0001]] exceeds $\tau \cdot \mathrm{MAD} /
  c[[ML4T_A3_0002]]c$, declared as
  [[ML4T_A3_0003]], is the MAD of a standard normal, which puts the result on the same
  footing as a standard deviation.
- **Z-score** flags it when [[ML4T_A3_0004]] exceeds [[ML4T_A3_0005]].
- **IQR** flags it when [[ML4T_A3_0006]] falls outside $[Q_1 - \tau \cdot \mathrm{IQR},\ Q_3 + \tau \cdot
  \mathrm{IQR}]$.

Running all three at one threshold therefore compares three different cutoffs, not three
ways of applying one. The next cell prints the cutoffs the shared threshold implies in
return space, so the counts that follow can be read against the boundary that produced them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0017-p000

~~~~~~markdown
The counts follow the cutoffs: the method with the narrowest band flags the most, and the
ordering of the counts is the ordering of the bands.

The reason MAD's band is narrowest is worth stating carefully, because the intuitive version
has it backwards. MAD is a robust scale estimate, meaning the extreme returns barely move it:
it is the median of the absolute deviations, and a handful of enormous days cannot shift a
median. The standard deviation has no such protection and is inflated by those same days. So
on a heavy-tailed return series MAD comes out much smaller than sigma, the cutoff built from
it is tighter, and more returns fall outside. MAD flags more because it *ignores* the tails
when measuring scale, not because it is sensitive to them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
### What the detector cannot tell you

The largest flagged moves in this series are not data faults. They are stock splits and an
earnings crash, in a panel that stores prices unadjusted. A return-outlier detector locates
large moves and has no way to attribute them, so the table below is a work queue rather than
a defect list, and Section 4 shows what it takes to resolve one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0022-p000

~~~~~~markdown
### VolumeSpikeDetector

Flags rolling-window volume Z-scores above a threshold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>
