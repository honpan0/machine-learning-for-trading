# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：10_text_feature_engineering/02_asset_embeddings.ipynb；A3 Pack 002；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合

## 待翻譯英文單元

### c0023-p000

~~~~~~markdown
The two printed means are the test and the matrix shows its shape. These companies sit
close to one another and further from a random draw of other widely-held stocks, which is
what co-ownership predicts: an institution large enough to file a 13F holds most of them,
so they appear in the same portfolios in the same region of the ordering.

The matrix carries something the means do not. It splits into two blocks - the technology
names close to one another, the bank, oil major, carmaker and conglomerate forming a
looser second group - with lighter cells between them. That is what differentiated
co-holding would look like, and it is not a test of it: these nine are all widely held but
not equally so, and nothing here holds frequency fixed while varying who holds what. The
benchmark below is where the popularity comparison is actually made.

It is worth being clear about what that does not establish. These are the most widely held
stocks in the sample, so they co-occur with almost everything, and a method that placed all
frequent items together for no other reason would produce the same picture. Separating
those two explanations needs a baseline that is itself popularity-driven, which the
benchmark below adds alongside the uniform-random one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0024-p000

~~~~~~markdown
## Managed Portfolio Benchmark: Masked Asset Prediction

This is the key empirical test from Gabaix et al. (2025). The benchmark asks:
**Given the rest of a portfolio, can the embeddings name the holding that was removed?**

Methodology:
1. For each test portfolio, mask one position (e.g., the 5th largest holding)
2. Use the surrounding context to predict which stock was masked
3. Report accuracy@k: Is the true stock in the top k predictions?

This directly tests the Word2Vec hypothesis: stocks appearing in similar
portfolio positions should have similar embeddings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### Predict Masked Asset
Given a portfolio with one position masked, use surrounding context to predict the hidden stock.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
### HitRecord and Benchmark Evaluation
Track per-sample prediction outcomes and aggregate benchmark metrics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
### Run Benchmark Evaluation
Sample masked positions across portfolios and compute accuracy metrics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0034-p000

~~~~~~markdown
### Bootstrap Confidence Intervals
Compute CIs for benchmark metrics using raw per-sample hit records.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
### One number over all of it, pooled rather than averaged

A single rate for the whole benchmark has to be computed over the masked positions, not
over the buckets. The buckets hold very different numbers of positions, so averaging their
three rates would weight a bucket of four thousand the same as one of twelve thousand and
report something no set of trials produced.

Its confidence interval has to be bootstrapped on the pooled outcomes for the same reason.
Averaging the three buckets' interval endpoints yields a pair of numbers with no coverage
property at all - it is not an interval for the pooled rate, or for anything else.

The resampling unit is the portfolio, not the masked position. Each portfolio supplies up
to a hundred positions per bucket, drawn from one holdings list with overlapping context
windows, so those outcomes rise and fall together. Resampling positions would treat them as
independent and return an interval narrower than the sampling variation warrants.

The pooled figure is the one to quote and the least informative one here. It is dominated by
the two large deep-position buckets, where the task is hardest, so it understates what the
method does near the top of a portfolio and overstates what it does at the bottom. The
per-bucket table above is what carries the finding.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000

~~~~~~markdown
### The baseline that actually competes

Beating a uniform draw over eleven thousand stocks is not evidence of much. The claim worth
testing is that the embeddings learned which stocks go together, and the rival explanation
is that they learned which stocks are common - so the baseline has to be a predictor that
only knows popularity.

It is the simplest thing possible: ignore the portfolio entirely and always answer with the
five most widely held stocks in the sample.

It is scored from the hit records themselves rather than by walking the portfolios again.
The benchmark samples a bounded number of positions per bucket per portfolio and skips any
whose context window is empty, so re-deriving the trials would produce a different set with
different bucket weights - and a comparison across two populations says nothing.
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
Both predictors answer the same masked positions, so the two rates are comparable directly.
Read the gap between them rather than either one alone: it is what the rest of the
portfolio is worth, over and above knowing which stocks are widely held.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
## Benchmark Interpretation

- **Hits@k**: fraction of times the true masked stock appears in the top-k
  nearest neighbours of the surrounding context.
- **MRR**: mean reciprocal rank of the true stock; bounded by 1.

Two patterns are worth checking against the table above:

1. The position-bucket effect - top positions (the largest holdings) are more
   consistently held across funds, so their context is predictive; lower
   positions are noisier and Hits@k typically falls.
2. The lift over the analytical random baseline ([[ML4T_A3_0001]]) - even a
   single-quarter Word2Vec model on 500 portfolios should be one-to-two
   orders of magnitude above random, well outside the bootstrap CI.

This is the same masked-asset benchmark Gabaix et al. (2025)
use to compare Word2Vec, BERT, and recommender-system embeddings.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
## Connection to the Paper

Gabaix et al. (2025) compare three embedding methods:

1. **Recommender Systems (RS)**: PCA on investor-asset holdings matrix
2. **Word2Vec**: Skip-gram on portfolio sentences (what we did here)
3. **BERT**: Transformer with attention for contextualized embeddings

This notebook implements the second of those and reproduces the masked-holding benchmark
protocol on a single-quarter 13F snapshot. The paper's own comparisons between the three
methods, and its results on valuation variance, are not reproduced here and are not
measured by anything above; the takeaways below say which numbers came from where.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>
