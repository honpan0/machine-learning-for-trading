# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/12_wasserstein_regimes.ipynb；A3 Pack 002；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cluster → 群集
- Clustering → 分群
- Volatility → 波動率

## 待翻譯英文單元

### c0015-p000

~~~~~~markdown
## A second opinion that does not depend on the distance used to cluster

Inertia cannot compare the two methods, because each reports it in its own geometry. The
**maximum mean discrepancy** gives a number that neither method optimizes: it embeds two
samples through a kernel and measures the distance between their mean embeddings, so a
small value says the two samples look like draws from one distribution.

It is computed here three times per method, between the members of each cluster and between
the two clusters, over bootstrap resamples because the estimator is biased upward at small
sample sizes and the median across resamples is more stable than one value.

The kernel needs a width, and the answer is not a fixed number: a width far from the scale
of the data drives every kernel value to one or to zero and the discrepancy to nothing. The
median heuristic sets it from the data, at the median distance between pairs of windows,
and the value it picks is printed so it is not a hidden choice.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## A series whose regimes are known

The benchmark needs a ground truth, so the first data is simulated. Two sets of parameters
alternate at fixed points: one with a small positive drift and low volatility, one with a
small negative drift and volatility more than twice as high. Each block is a geometric
Brownian motion, which means the returns inside a block are independent draws from one
normal distribution and the only thing that changes at a switch is which normal.

That makes the experiment favourable to any method that reads the variance, and the point
of running it is not to show that the distributional method works. It is to see how much of
the truth a two-moment summary recovers when the truth is entirely contained in two
moments.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
A window that straddles a switch contains returns from both regimes, so its ground truth is
whichever regime supplied more of its sessions. That convention gives every window a
definite label and a perfect score remains reachable, but the mixed windows are the hard
ones: their returns come from two distributions and the correct answer is decided by a
majority that a near-even split makes arbitrary.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
The **adjusted Rand index** scores an assignment against the truth without caring which
cluster got which number: it counts pairs of windows the two agree to put together or
apart, and subtracts what agreement a random assignment of the same cluster sizes would
reach. One is a perfect match and zero is chance.

The table reports it alongside the discrepancy within each cluster and between the two.
A silhouette score is not reported: it would be computed in a chosen space, and each of
these methods clusters in a different one, so whichever space is picked flatters the method
that optimizes in it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
Read the three rows against each other rather than the first against the truth. The
simulation differs only in a drift and a volatility, so the moment features carry every
quantity that matters; the two fits on those features nonetheless land far apart, and the
mixture lands close to the Wasserstein result. What separates the two moment fits is not
the information available to them but the shape of cluster each can draw, so most of the
gap between the first row and the second is the equal-size spherical geometry that k-means
imposes on standardized moments and not a limitation of moments as such.

The discrepancies say something the Rand index does not. Every method produces clusters
whose members resemble each other far more than they resemble the other cluster's, so all
three found a real division. Only the comparison against the truth says which division.
That is the general shape of the problem: an unsupervised method can always report a clean
separation, and on real data there is no column to check it against.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0025-p000

~~~~~~markdown
## Which session carries a window's label

A window covering sessions [[ML4T_A3_0001]] to [[ML4T_A3_0002]] is only complete at the close of session
[[ML4T_A3_0003]], so that is the first session whose feature can carry the window's label. The
obvious alternative, writing the label back across every session the window covers, would
put a label on session [[ML4T_A3_0004]] that was computed from returns up to [[ML4T_A3_0005]], and any model
reading it would be reading its own future.

The function below therefore stamps each label on the last session of its window and holds
it until the next window closes. Two consequences follow and both are real. The sessions
before the first window closes have no label at all. And a regime change is visible only
once enough of the new regime has entered a window to move it across the boundary, which is
a delay of up to a window plus a step.
~~~~~~

<<<ML4T-ZH-BEGIN:c0025-p000>>>
<<<ML4T-ZH-END:c0025-p000>>>

### c0028-p000

~~~~~~markdown
The top right panel is the reason the method is worth its cost, read in reverse. The split
runs along the spread and the means overlap, which says the clustering has divided the
windows on their volatility and taken no view on their drift. On this simulation that is the
correct division and a two-moment summary could have found it. The bottom right panel shows
the same division as the object the algorithm actually manipulates: two quantile functions,
separated across the whole range rather than at one summary number.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0029-p000

~~~~~~markdown
## The same construction on the index, fitted forward

Everything above is fitted on the whole sample, which is what a benchmark against a known
truth needs and what a feature must not be. The real-data section splits the windows in
time: the centroids are fitted on the first [[ML4T_A3_0001]] of them and every window is
then assigned to the nearest of those fixed centroids. A window after the split is scored
against centroids that no session inside it contributed to.

The split is a single one rather than a rolling refit, and that is a simplification worth
naming. A rolling refit would face the problem [[ML4T_A3_0002]] describes, that cluster
numbers move between fits and have to be tied down by a characteristic of the members; the
ordering rule above is what would do it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0032-p000

~~~~~~markdown
The share of windows in the more volatile cluster differs between the two blocks, and that
is information rather than a defect: the centroids are held fixed, so the share after the
split says how often the later sample looked like the earlier sample's stressed windows.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>
