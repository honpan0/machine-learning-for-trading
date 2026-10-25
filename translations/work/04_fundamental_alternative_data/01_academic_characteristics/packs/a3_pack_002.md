# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/01_academic_characteristics.ipynb；A3 Pack 002；單元 12 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Label → 標籤
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Correlation → 相關性

## 待翻譯英文單元

### c0008-p000

~~~~~~markdown
### What the identifier is, and how far it reaches

The authors publish each split as its own array whose second axis runs over firms. A firm
keeps its position on that axis for the whole split, and that position is what
[[ML4T_A3_0001]] writes as [[ML4T_A3_0002]]. No mapping between the three arrays is published, so a
position in the training array and the same position in the test array are not known to be
the same company; the loader offsets the three numberings by a million each so that they
cannot be joined by accident.

The useful half of that is measurable. If [[ML4T_A3_0003]] were a row number rather than a firm, each
value would appear once. Counting the months each identifier appears in over the training
split shows what it actually is.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
### How wide is the cross-section?

The number of stocks available in a given month decides how much a cross-sectional statistic
computed on that month can be trusted, and it moves a great deal over fifty years. The
vertical rules mark the two split boundaries read above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
---

## Section 2: The characteristic taxonomy

The 46 columns are not 46 independent ideas. They fall into eight groups, each measuring one
economic quantity in several ways: how cheap a firm is relative to its accounting value, how
profitable it is, how fast it is growing its asset base, how its price has moved recently,
how volatile it is, how easily it trades, how much debt it carries, and how efficiently it
turns assets into sales. Grouping them is what makes the correlation structure in Section 3
and the information coefficients in Section 4 readable.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
### Checking that the ranks were applied

The normalization described in the preamble makes a claim the data can be held to: every
characteristic, in every month, occupies the same bounded range. The check is the smallest
and largest value any of the 46 columns reaches anywhere in the panel. Reading it also
confirms that nothing is missing, which matters because the authors admitted only stocks
with a complete set of characteristics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
Staying inside the interval is not the same as filling it evenly. Wherever many stocks tie on
a characteristic, the ranking piles them at one value and leaves gaps elsewhere, and it is
then carrying less information than its range suggests. Ties depend on the raw variable, so
this has to be measured on each characteristic rather than argued from the procedure. Cutting
the interval into ten equal bins and comparing the fullest with the emptiest gives one number
per characteristic: at one they are equally full, and the further above one, the more the
values bunch.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
The measurement covers all 46; the histogram shows one of them, so that the flatness the
number reports has a shape a reader can recognize when they meet it on their own data.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
---

## Section 3: Correlation structure

Characteristics built from overlapping accounting inputs move together. Two measures of
volatility computed over different windows, or two valuation ratios sharing a denominator,
carry much of the same information, and a linear model fitted on both splits the coefficient
between them arbitrarily. Measuring the redundancy first is what tells you whether the model
you reach for later needs to handle it.

Because each month is normalized on its own, pooling every stock-month into one correlation
measures how the characteristics co-vary within a cross-section, which is the relevant
question here, rather than how their levels drift over the decades.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
The blocks in the heatmap are easier to act on as a list. The pairs below are the ones whose
correlation reaches the redundancy threshold declared in the parameters cell, ordered from
most positive to most negative.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
---

## Section 4: How each characteristic relates to next-month returns

The information coefficient answers one question per month: if you had ordered every stock in
the cross-section by this characteristic, how well would that ordering have matched the order
of the returns that followed? Rank correlation is the right measure because only the ordering
is meaningful once the characteristic has been ranked, and because a single extreme return
then moves the statistic by one rank rather than by its full magnitude. Averaging the monthly
values gives the characteristic's average ordering power, which is the Fama-MacBeth template.

**Everything in this section is computed on the training split alone.** Ranking
characteristics by how well they predicted returns is a selection decision, and a selection
decision taken over the validation and test years leaks those years into every model built on
the ranking, including the ones fitted in Chapters 11 and 12. The panel ships with the split
labels so that the line can be drawn here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
### The two significance tests, and why they differ

A t-statistic on the average of the monthly ICs divides that average by the standard error of
the mean, and computing the standard error that way assumes each month is an independent draw.
The months are not independent: slow-moving common factors keep a characteristic in or out of
favour for stretches at a time, so a run of positive ICs is followed by more positive ICs more
often than chance allows. Newey and West's estimator widens the standard error by the amount
of that serial correlation, using a lag window chosen from the length of the series.

[[ML4T_A3_0001]] reports both: the corrected t-statistic and the uncorrected one, so the
gap between them is visible rather than asserted.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
Plotted in the order above, the ICs show two things at once: how small the largest of them is,
and that the characteristics at the two ends of the range are the ones a reader of the factor
literature would expect there.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
The correction for serial correlation is worth seeing directly. Each point below is one
characteristic, placed by its uncorrected t-statistic and its corrected one. Points on the
diagonal are unaffected by the correction; points pulled toward the horizontal centre line
have had their significance reduced by it. The dotted rules sit at the conventional
two-standard-error threshold, so a point between them fails that test on the corrected
statistic.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>
