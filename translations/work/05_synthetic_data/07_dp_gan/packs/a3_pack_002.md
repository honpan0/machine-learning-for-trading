# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/07_dp_gan.ipynb；A3 Pack 002；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Correlation → 相關性

## 待翻譯英文單元

### c0028-p000

~~~~~~markdown
**Interpretation**: With differential privacy, the generator adds calibrated noise
to protect individual training records. This typically results in less tight
overlap between real and synthetic distributions compared to non-private GANs.
The trade-off is intentional: stronger privacy guarantees (lower ε) mean more
noise and less fidelity. The quantitative metrics below measure this trade-off.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0029-p000

~~~~~~markdown
## 8. Evaluate Synthetic Data Quality
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
### Run Quality Evaluation
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## 9. Visualize Training and Results
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
**Interpretation**: The loss curves reveal the tension between adversarial training and
privacy noise. Unlike standard GANs where losses stabilize, DP-GAN losses remain noisier
because Opacus injects calibrated Gaussian noise into every gradient step. The epsilon
trajectory in the right panel shows privacy budget consumption -- it increases monotonically
because each training step spends a fraction of the total budget. Faster epsilon growth
means more information is being extracted from the real data per step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0038-p000

~~~~~~markdown
**Interpretation**: this figure is about the generator trained above, at the budget
this notebook spends. Read the two matrices against the same colour scale. The real one
is mostly pale, because these features are only weakly correlated with each other. The
synthetic one is saturated almost everywhere off the diagonal, every pair sitting at
one end of the scale or the other.

That is not a weak version of the real structure, it is a different kind of object.
Correlations of plus or minus one mean each feature is close to a deterministic
function of the others, which is what a generator produces once it has collapsed onto
a low-dimensional set instead of a distribution. The fidelity figure above shows the
same thing geometrically: the synthetic points lie along thin bands and arcs rather
than filling the space the real points occupy.

So the failure here is not that privacy noise drowned out the subtler correlations
while the strong ones survived. Under this budget and this much training the generator
has stopped producing a spread at all, and every correlation it reports is an artifact
of that collapse. Keep this in view when reading the sweep below: a summary distance
between two correlation matrices can sit in a narrow range while one of the two
matrices is degenerate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000

~~~~~~markdown
## 10. Privacy-Utility Trade-off Analysis

Let's see how different privacy budgets affect synthetic data quality.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0042-p000

~~~~~~markdown
**Interpretation**: differential privacy trades utility for guarantees - a tighter
budget means more noise per gradient step, and the distribution that reaches the other
side of it is coarser. What the sweep shows is one large effect and a great deal of noise around it.

The large effect is at the tightest budget, where the mean absolute difference is
several times its value anywhere else. That much is clear in the left panel and is
the part worth carrying away.

Across the looser budgets the same measure lands in a narrow band with no clean
ordering, and the correlation distance in the right panel is not even monotonic: it
rises, falls to its lowest value, and rises again. Read the printed table for the
figures. Differences that small sit inside the run-to-run variation of a single short
training run per budget, so this sweep cannot resolve a monotonic curve, and drawing a
smooth "quality improves with epsilon" line through it would be reading the noise.
Separating the moderate budgets would take several independent runs at each, averaged.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0042-p001

~~~~~~markdown

One caution carried forward from the correlation matrices: both measures here are
summaries of a difference, and a difference between two correlation matrices cannot
say whether either of them describes a real spread. That is why the sweep also prints
[[ML4T_A3_0001]] and [[ML4T_A3_0002]] per budget, with the real data's
values above them for reference. Both samples are put on the real data's feature
scales first, so the dimension count is a statement about the shape of the sample and
not about which feature happens to be measured in the largest units. Compare each
budget's pair against the real one: an off-diagonal correlation near one, or a
variance the real data spreads over many directions concentrated into a couple, is a
generator that has collapsed rather than one that is merely noisy.
Where that is what the numbers show, a flat correlation-distance curve says the metric
does not separate these settings, not that the settings are equally good.

In regulated settings - sharing client trading data, say - a ceiling on the privacy
budget is often imposed regardless of where the utility optimum falls.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p001>>>
<<<ML4T-ZH-END:c0042-p001>>>

### c0043-p000

~~~~~~markdown
## Key Takeaways

1. **Privacy-utility tradeoff is real but dominated by the strict-privacy regime**:
   A tighter budget injects more noise into the gradients and coarsens the synthetic
   data. In this sweep the cost is large and unambiguous at the tightest budget, and
   the looser ones fall into a narrow band with no clean ordering. One short run per
   budget cannot resolve a monotonic curve, so the defensible reading is that a very
   tight budget is expensive and the moderate ones are not separated here; separating
   them would take several runs at each, averaged.

2. **Per-sample gradients via Opacus are essential**: Standard PyTorch clips the
   *batch* gradient, which does not bound any individual sample's contribution.
   Opacus computes per-sample gradients using [[ML4T_A3_0001]], clips each independently
   to [[ML4T_A3_0002]], then adds calibrated noise. Manual implementations of this
   are notoriously error-prone -- Opacus makes it correct by construction.

3. **Epsilon measures cumulative information leakage**: Each training step consumes
   a fraction of the privacy budget. The privacy accountant (Renyi DP) tracks this
   precisely. Once epsilon is spent, no further training is possible without weakening
   the guarantee. This is why [[ML4T_A3_0003]] calibrates noise to spread
   the budget evenly across epochs.

4. **Architecture constraints matter**: BatchNorm violates DP because it computes
   statistics across the batch, leaking information about other samples. GroupNorm
   and LayerNorm are DP-safe alternatives. Use [[ML4T_A3_0004]] to check compatibility
   before training.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>
