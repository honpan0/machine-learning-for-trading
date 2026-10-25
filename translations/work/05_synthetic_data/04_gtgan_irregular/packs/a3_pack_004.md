# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/04_gtgan_irregular.ipynb；A3 Pack 004；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Backtesting → 回測
- Correlation → 相關性

## 待翻譯英文單元

### c0065-p000

~~~~~~markdown
**Interpretation**: read the four rows together rather than choosing among them. The
discriminative accuracy and AUC sit at their maximum, so the classifier separates
synthetic from real without error: whatever the sequences preserve is not enough to
fool a model that is looking for the difference. The TSTR ratio misses the band the
protocol allows, so a predictor fitted on the synthetic sequences carries more error on
real ones than a predictor fitted on real data does, by the margin the ratio above
gives. Those two rows are not the same finding: a classifier separating two sets
perfectly says nothing about how much of the predictive structure the second set
carries. The
bounded fraction clears its threshold, but it checks something narrower than its name
suggests. It encodes a real window, decodes at the midpoint between each pair of
observation times, and asks whether that value lands between the two neighbouring real
values with a fixed tolerance added on either side. That tolerance is wider than the
mean gap between adjacent observations printed in the interpolation section above, so
most of the band being cleared is tolerance rather than data. And the latent it decodes
comes from encoding a real window, which makes it the one row here that never runs the
generator. The passing row and the failing rows are therefore not in tension: they ask
different questions, and discarding the failing ones to keep the passing one would be
choosing a metric by its answer.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0065-p001

~~~~~~markdown

[[ML4T_A3_0001]] is set to two thousand, which is a short adversarial run, and the
training-progress figure shows the three adversarial losses settling onto a common
flat level well before the end. Lengthening that run is the change to make before any
of these numbers is quoted as a property of GT-GAN rather than of this pass.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p001>>>
<<<ML4T-ZH-END:c0065-p001>>>

### c0066-p000

~~~~~~markdown
## Save Outputs
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0071-p000

~~~~~~markdown
## Key Takeaways

**What GT-GAN Offers for Irregular Data**:

1. **Natural Irregularity**: Uses Chapter 3's information-theoretic bars with genuine
   variable timestamps (not artificial masking)
2. **Continuous Dynamics**: Neural ODEs model evolution between observations
3. **Flexible Generation**: Generate at any timestamps, not just training grid
4. **Time-Aware Discrimination**: Discriminator accounts for irregular spacing

**Comparison with Other Generators**:

| Generator | Time Grid | Best For |
|-----------|-----------|----------|
| TimeGAN | Fixed | Regular daily/hourly data |
| Tail-GAN | Fixed | Tail risk scenarios |
| Sig-CWGAN | Fixed | Multi-asset correlations |
| Diffusion-TS | Fixed | High-dimensional data |
| **GT-GAN** | **Variable** | **Naturally irregular** (tick/volume bars) |

**Use Cases**:

- High-frequency data with variable sampling (tick bars, volume bars)
- Multi-asset data with different trading hours
- Generating scenarios for backtesting irregularly-sampled strategies
~~~~~~

<<<ML4T-ZH-BEGIN:c0071-p000>>>
<<<ML4T-ZH-END:c0071-p000>>>
