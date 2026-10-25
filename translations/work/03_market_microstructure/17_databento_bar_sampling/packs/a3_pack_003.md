# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/17_databento_bar_sampling.ipynb；A3 Pack 003；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Machine learning → 機器學習
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Standard deviation → 標準差

## 待翻譯英文單元

### c0069-p000

~~~~~~markdown
## 12. Calibration Recommendations

Based on this multi-day analysis, here are production-ready recommendations:

### Recommended Thresholds for NVDA (~500 bars/day)

The calibration tables above give each sampler's mean daily bar count and the standard
deviation of that count across days. Read those two against each other: a sampler
whose day-to-day standard deviation approaches its mean is not delivering a
predictable number of bars, and downstream code that assumes one will break on the
quiet days. The comparison table that follows reports distributional diagnostics
instead, which is a separate question from stability.

### How to calibrate a threshold

**Calibrate off the median day, not the mean.** A single heavy day pulls the mean up
and leaves a threshold that produces too few bars on every ordinary day.

**Expect the bar count to move, and decide how much movement is acceptable before
looking.** Fixed-threshold bars track activity by construction, so their count varies
with the market; imbalance bars vary more, because their threshold adapts as well.

**Dollar bars are the reasonable default.** They weight by value rather than share
count, which is the unit portfolio arithmetic is done in, and they absorb a price move
that would change what a volume threshold means. A volume threshold calibrated on a
[[ML4T_A3_0001]] stock samples very differently after it doubles.

**Imbalance bars buy information-driven sampling at the cost of predictability.** Use a
slow decay so the threshold does not run away, and a larger target so that each bar
represents a meaningful accumulation of one-sided flow rather than noise.

### Key Findings
~~~~~~

<<<ML4T-ZH-BEGIN:c0069-p000>>>
<<<ML4T-ZH-END:c0069-p000>>>

### c0069-p001

~~~~~~markdown

1. **Event-driven bars produce lower Jarque-Bera and lower lag-1
   autocorrelation than time bars** on the configurations tested above
   (see the comparison table for the per-bar-type numbers). This notebook
   does not evaluate downstream ML performance on the resulting series.

2. **A threshold calibrated on one day is calibrated on that day.** Daily volume
   varies enough across this sample that a threshold fitted to a single session
   produces a materially different bar count on another - the dispersion measured
   above is what to size that risk against.

3. **Variance Ratio VR(5) ≈ 1** for all bar types:
   - Returns are not distinguishable from a random walk by VR(5)
   - No predictability detected at the 5-bar horizon in this test

---
~~~~~~

<<<ML4T-ZH-BEGIN:c0069-p001>>>
<<<ML4T-ZH-END:c0069-p001>>>

### c0070-p000

~~~~~~markdown
## Bar Type Summary Comparison (Single Day)

For direct comparison in Chapter 3 (Table 3.7), we build bars for one
representative day using recommended thresholds and report statistical
properties. This uses DataBento's direct aggressor labels (no estimation).
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0072-p000

~~~~~~markdown
## Key Takeaways

### Multi-Day Calibration is Essential

ITCH provides single-day data, limiting calibration to one day's activity.
DataBento's multi-day MBO data enables robust threshold selection that
accounts for day-to-day variability.

### Bar Type Selection Guide

| Goal | Recommended Bar | Reason |
|------|-----------------|--------|
| General ML features | Dollar bars | Value-weighted, stable |
| Information arrival | Imbalance bars | Adaptive to order flow |
| High-frequency signals | Tick bars | Normalize by activity |
| Familiar analysis | Time bars | Easy alignment |

### DataBento vs. ITCH for Bar Sampling

| Feature | DataBento | ITCH |
|---------|-----------|------|
| Multi-day data | Many sessions | One session |
| Calibration | Can be fitted across days | Fitted on a single day |
| Aggressor side | Labelled by the venue on most trades | Inferred by the Lee-Ready rule |
| Imbalance bars | Built on labelled sides | Built on inferred sides |

### Next Steps

1. **OFI Analysis**: See [[ML4T_A3_0001]] for order flow imbalance
2. **Lee-Ready Validation**: See [[ML4T_A3_0002]] for classification
3. **ITCH Comparison**: See [[ML4T_A3_0003]] for single-day analysis
4. **Feature Engineering**: See Chapter 8 for bar-based ML features

---

**References**:
- López de Prado (2018): "Advances in Financial Machine Learning" - Ch. 2
- DataBento Documentation: MBO Schema
~~~~~~

<<<ML4T-ZH-BEGIN:c0072-p000>>>
<<<ML4T-ZH-END:c0072-p000>>>
