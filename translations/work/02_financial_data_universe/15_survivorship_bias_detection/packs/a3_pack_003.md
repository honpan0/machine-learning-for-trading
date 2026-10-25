# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/15_survivorship_bias_detection.ipynb；A3 Pack 003；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Survivorship bias → 存活者偏誤

## 待翻譯英文單元

### c0040-p000

~~~~~~markdown
## 8. What happened to the symbols that left?

The scenarios in §4 model what holders received *after* the last quote. This section looks at
the part the panel does observe: how the leavers performed *while* they were still quoted.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0043-p000

~~~~~~markdown
Leavers hold their shorter window and, over it, underperform the survivors. That is the
mechanism behind the positive bias in §6: dropping them from the universe removes the weaker
half of the distribution. The terminal-return scenarios then adjust the estimate at the
margin — they do not create it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
## 9. Detecting bias in your own data

Two cheap tests. The first catches a universe filtered to today's constituents; the second
catches the pattern this panel shows, where exits are recorded but only for part of the history.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0046-p000

~~~~~~markdown
The panel passes the first two tests, on the delisting rate and on the number of distinct
exit dates, and fails the third. A delisting rate on its own is not evidence of a
survivorship-aware panel, because a panel that recorded exits for only the last few years
of its history produces the same rate. **Ask when the delistings happened.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0047-p000

~~~~~~markdown
## 10. Universe completeness

Survivorship asks whether exits are recorded. Completeness asks the mirror question: are
**entries** recorded? A panel can carry every delisting and still miss every IPO.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0049-p000

~~~~~~markdown
For context, the US listed-company count peaked near 8,090 in 1996 (World Bank) and has run
4,000–5,000 since 2010. A panel of ~3,200 symbols is a subset, not the market.
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0051-p000

~~~~~~markdown
### Interpretation

Both flows fail, and they fail at opposite ends of the panel:

1. **Exits are missing before ~2014** — the panel was backfilled from a snapshot of
   then-living symbols (§1).
2. **Entries dry up after ~2014** — contributors stopped adding IPOs, and the feed stopped
   entirely in March 2018.
3. **The panel is a subset** — ~3,200 symbols against a 4,000–5,000 name market, skewed
   toward liquid names.

Bias-free is not the same as complete, and this panel is neither over its full span. It *is*
usable for survivorship work over 2014–2018, which is what §6 measures. For anything longer,
use a panel with an explicit universe definition and delisting returns: CRSP, Compustat, or a
commercial vendor.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0052-p000

~~~~~~markdown
## Key takeaways

**What it does.** Measures how much an equal-weight portfolio of survivors overstates the
same portfolio built on the full starting universe, over the only window in which the US
equities panel records exits.

**What it finds.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0052-p001

~~~~~~markdown

1. **The panel records exits only from its final few years.** Every exit in a panel that
   starts in the 1960s falls after 2014, as the chart in §1 shows. Firms exited before then;
   the collection process did not capture it. Absence of evidence, not evidence of absence,
   and no way to recover what is missing.
2. **The adjusted prices carry unadjusted corporate actions.** Reverse splits and
   post-bankruptcy reorganisations on reused tickers print single-session steps of two
   orders of magnitude that are not returns at all, and the [[ML4T_A3_0001]] column records
   nothing for any of them. They are a small fraction of one percent of the rows; §3 lists
   them and counts them.
3. **Those rows decide the sign of the answer.** Uncorrected, the survivors-only portfolio
   appears to *underperform* the full universe. Repaired, it overstates — the direction the
   literature reports. The survivorship check cannot run ahead of the corporate-action check.
4. **The terminal-return model is the least consequential part of the estimate.** Setting
   every terminal return to zero moves the empirical-scenario bias by well under a point. The
   bias comes from the *observed* returns of the symbols that left, not from what they paid
   out afterwards. Assumption risk (which scenario) exceeds sampling risk (the Monte Carlo
   band) by an order of magnitude.
5. **Bias-free is not complete.** The panel adds almost no new listings after 2014, and §10
   measures how much of the market it holds. A dataset can record every delisting and still
   miss every IPO.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p001>>>
<<<ML4T-ZH-END:c0052-p001>>>

### c0052-p002

~~~~~~markdown

**What it means.** Survivorship bias is not a fact you look up; it is an estimate you build,
and it inherits every defect of the data underneath it. The direction of the bias depends on
the delisting mix, its magnitude on the leavers' observed returns, and its *sign*, here, on
whether anyone checked the corporate actions first. Applying a zero terminal value to
delisted symbols is not bias-free; it is merely unrealistic.

**Next**: [[ML4T_A3_0001]] moves from one panel's internal bias to stitching several
providers together, where universe and coverage definitions diverge. **Book reference**: §2.3.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p002>>>
<<<ML4T-ZH-END:c0052-p002>>>
