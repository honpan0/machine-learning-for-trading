# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/05_diffusion_ts.ipynb；A3 Pack 003；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Out-of-sample → 樣本外
- Cluster → 群集
- Clustering → 分群
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0059-p000

~~~~~~markdown
**Interpretation**: a low KS statistic means the marginal distribution for an asset
is well matched. Correlation error tests whether cross-asset dependence survived, and
autocorrelation error whether the weak serial dependence of daily returns did.

Read each mean against the range printed beside it, not on its own. Five of the nine
printed numbers are means. Four of those - the KS statistic, the mean error, the
standard-deviation error and the autocorrelation error - average over assets, while
the correlation error averages the absolute difference between corresponding entries
of the real and synthetic correlation matrices, so it averages over asset pairs. The
other four are not means: [[ML4T_A3_0001]] counts the assets, and the two extreme KS values
and the largest autocorrelation error are each one asset's.

All of these errors are absolute, so a small mean cannot come from large errors
cancelling; it comes from many small ones diluting a few large ones. The extreme
per-asset KS values say whether that happened: a maximum near the mean means the fit
is even across assets, and one far above it means the mean describes the assets the
model handles and conceals the one it does not. The maximum per-asset autocorrelation
error reads the same way.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p000>>>
<<<ML4T-ZH-END:c0059-p000>>>

### c0061-p000

~~~~~~markdown
**Interpretation**: Overlapping PCA/t-SNE point clouds confirm that synthetic
sequences occupy the same region of feature space as real data. Gaps or
isolated clusters would indicate missing regimes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0061-p000>>>
<<<ML4T-ZH-END:c0061-p000>>>

### c0062-p000

~~~~~~markdown
### TSTR Evaluation

We evaluate downstream utility via **extreme-move classification**: predict
whether the next-day absolute return exceeds the 90th percentile.

**Important context**: this is a heavily imbalanced task. The threshold is a high
percentile of absolute *training* returns, so only that tail fraction of the training
window is positive by construction. Applied out-of-sample to a calmer holdout period,
fewer test days still clear the bar, which pushes the accuracy of a classifier that
never predicts the positive class very high. Both rates are printed below. Read the
**TSTR ratio** (synthetic over real), not raw accuracy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0062-p000>>>
<<<ML4T-ZH-END:c0062-p000>>>

### c0064-p000

~~~~~~markdown
**Interpretation**: the TSTR ratio is one accuracy divided by another, so it says
how the two models compare and nothing about whether either one works. Two models
that both fall short put it at one just as readily as two that both succeed, and
neither of the accuracies printed above reaches the naive baseline printed beside
them. Precision and recall are
where a model that finds the rare large moves separates from one that predicts the
negative class throughout, and the accuracy column cannot make that distinction
because the positive class is a few percent of the test rows.

**Trading context**: extreme-move prediction leans on volatility clustering, so this
section was meant to ask whether the synthetic paths carry it. A ratio near one
answers that only once both models clear the naive baseline on the metric the ratio
is built from. Where neither does, the ratio establishes nothing either way about
volatility clustering, and the precision and recall columns are the ones to read
instead: they are computed on the positive class, so they separate a model that finds
some extreme moves from one that never predicts them, which accuracy at this
prevalence cannot. The lag-1 autocorrelation reported earlier does not settle the
question either, being computed on returns rather than on squared returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0065-p000

~~~~~~markdown
### Sample Sequences and Decomposition

Visualize example synthetic paths and the model's internal trend+seasonal
decomposition. The decomposition shows what the model attributes to slow
drift versus periodic patterns at a given noise level.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0066-p000

~~~~~~markdown
Daily returns on the left show moment-to-moment behaviour; the cumulative series on
the right makes drift visible, which a returns plot hides.

The windows to plot are drawn at random rather than taken from the front of the array.
The sequences are overlapping rolling windows, so the first ten start on consecutive
days: they are one short stretch of history repeated with a nine-day shift, not ten
samples of it, and a quiet fortnight would make the real panel look calmer than the
data it came from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0068-p000

~~~~~~markdown
**Interpretation**: ten windows drawn at random from each, on a shared scale per
column. Compare how far the two rows spread, in the daily returns and in what those
returns accumulate to, rather than tracking any individual line.

Do not read a population claim off ten paths, in either direction: ten windows are a
thin sample, and the real ones overlap each other, so they carry less independent
information than ten separate lines suggest. The statistical tests above - the KS
statistics and the correlation error - are the population comparison for these
unconditional samples.

Not the regime histograms further down: those plot [[ML4T_A3_0001]], generated
separately under classifier guidance and without the variance rescaling applied here,
so they measure conditional generation and say nothing about [[ML4T_A3_0002]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0070-p000

~~~~~~markdown
**Interpretation**: the trend component carries slow drift, the seasonal component
carries periodic oscillation, and the residual carries what neither explains. The
decomposition is analogous to classical STL, but learned end-to-end inside the
diffusion framework rather than imposed.

Read the vertical scales before reading the shapes. At this noise level the residual
is far larger than the trend and seasonal components put together, so most of what
the model is reconstructing here is not being explained by the interpretable parts.
That is what the chosen noise level buys: the sample is drawn a quarter of the way
through the diffusion schedule, where a lot of noise is still present and there is
correspondingly less structure to attribute. The decomposition gets noisier still at
larger [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>
