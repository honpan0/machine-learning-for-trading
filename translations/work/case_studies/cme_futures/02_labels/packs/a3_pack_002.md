# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/02_labels.ipynb；A3 Pack 002；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Label → 標籤

## 待翻譯英文單元

### c0009-p000

~~~~~~markdown
These are the thirty products, grouped the way the exchange and the strategy group them.
The sectors are what the label has to be comparable across: a ranking model sees one
target column and does not know that a treasury note and a barrel of crude move on
different scales. Section E measures how far apart those scales are.

Two things in the table matter for what follows. [[ML4T_A3_0001]] and [[ML4T_A3_0002]] agree
in every sector but equity index, where one product joins the panel six and a half years
after the other three - a shorter history that the label carries into every fold that
product appears in, and the reason equity index also has the widest spread between
[[ML4T_A3_0003]] and [[ML4T_A3_0004]]. Everywhere else that spread is one or two sessions,
but the level differs by more than a hundred sessions across sectors, because grain,
livestock and financial products keep different exchange holidays. There is no one calendar
to count a horizon against, so the horizon below is counted on each product's own
settlements, and Section D measures how far that stands up.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## C. Label construction

A label is a statement about which two prices a position is opened and closed at. Written
once and applied at both horizons, this one is

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is the ratio-adjusted settlement of product [[ML4T_A3_0003]]'s front contract and [[ML4T_A3_0004]]
counts [[ML4T_A3_0005]] **trading sessions for that product**. Chapter 7.2 calls this close-to-close:
both ends are settlement prices, and a position is treated as opened and closed at the same
moment of the session. [[ML4T_A3_0006]] places the strategy's actual execution at the following
Monday's open, so the label measures the move the strategy is trying to capture rather than
the amount it would collect after filling at a different price.

The denominator is guarded rather than clipped. A settlement can be non-positive - one
deferred crude oil contract in this panel settled below zero on 2020-04-20 - and dividing
by a floor clipped to some small positive number would manufacture an enormous return
where the right answer is that the quantity is undefined. The front contract this notebook
labels never goes non-positive, and Section D's reconciliation is what shows that rather
than asserting it.

Two bookkeeping columns are numbered here, on the complete session series, because both
mean something only before a row is dropped: [[ML4T_A3_0007]] counts back from each product's
last session for Section D's boundary profile, and [[ML4T_A3_0008]] numbers its sessions forward
so Section F's overlap statistics keep counting trading sessions once the null tail and
the holdout are filtered out. Neither reaches a label parquet, which selects four columns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## D. Window validity

A shift always returns something; the question is whether what it returns is the quantity
the label claims. Each property below fails silently and leaves plausible numbers behind,
so each is asserted rather than described.

The second assertion is a full reconciliation rather than a bound. Every row carrying no
label is attributed to exactly one cause - the tail of its product's series, a hole inside
the forward window, or a non-positive settlement at the anchor - and the four counts have
to sum to the height of the frame. A label crossing a product boundary, or a short label
masked by a longer one's null set, would break that identity.

The third assertion bounds the calendar span a window may cover, which is what makes the
hole rule falsifiable rather than a definition: [[ML4T_A3_0001]] trading sessions span about [[ML4T_A3_0002]]
calendar days on a five-session week, plus a week for exchange holidays. The rule fires on
one event, a ten-day break in the three livestock products in February 2012, and without
it the monthly label there would span more days than any holiday pattern can account for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
All four assertions read each product's settlements as its trading calendar. The panel
records settlements rather than opening hours, so that reading is an inference, and it is
worth measuring: a date the product traded but the file has no row for makes every window
across it cover one session more than the horizon names.

The panel carries its own evidence. If one product in a sector settled on a date, that
sector's market was open, so a second product in the same sector with no row on that date
is missing a settlement rather than closed for a holiday. Counting those dates, and the
labelled windows that run across one, bounds how far the horizon can be off; a count large
enough to matter would mean the panel has to be rebuilt before the label can be trusted. A
closure a whole sector shares is invisible to this test, and the calendar-span assertion
above is what catches the long ones.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
Position zero below is each product's last session, position one the session before it, and
so on backwards. The share of products carrying a label has to be zero over exactly the
last [[ML4T_A3_0001]] positions and one everywhere beyond them. Two failures that a count of valid
rows reports as healthy are visible here at a glance: a tail filled in with a fabricated
value instead of a null, which would lift the left end off the floor, and a short label
masked by a longer one's null set, which would move its cliff out to the longer horizon.
The figure reads only which labels are null and never a label's value, so it is drawn over
the whole panel rather than the development window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0019-p000

~~~~~~markdown
## E. Distribution and base rate

What scale is the label, and does it mean the same thing across products and across
regimes? Everything from here through Section G is measured on the **development window**:
the sessions before the held-out test period, and only those whose label has already
resolved by the time that period opens. That second condition is the one that is easy to
get wrong. Filtering on the date a row is observed keeps rows observed in the last weeks of
2023 whose five- or twenty-one-session outcome lands in 2024, so the diagnostic reads
prices from inside the held-out period while looking as though it did not. The filter here
is on [[ML4T_A3_0001]], the date the label's own window closes, which is the observation date
shifted forward by that label's horizon within the product.

The label files themselves keep every row, including the held-out ones: what is withheld is
what this notebook is allowed to look at, not what the later stages are given.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
