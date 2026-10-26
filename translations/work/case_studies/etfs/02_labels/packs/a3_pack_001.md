# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/02_labels.ipynb；A3 Pack 001；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cross-validation → 交叉驗證
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# ETFs: Label Engineering

Every model in this case study is trained to predict the label. An error in it produces no
warning here and changes every result that follows, so this notebook defines the labels,
checks the definition, sets the floor a feature must clear, and writes the label files every
later stage of the case study trains and scores against.

## Learning objectives

- Write a forward-return label as a formula: from which price at which time, to which
  price at which time
- Check that every labelled row has a complete forward window inside one symbol
- Measure how much independent information an overlapping label carries, and keep a
  diagnostic clear of the holdout by the date each label resolves rather than the date it
  is observed
- Measure what one unengineered signal earns against the label, on the same rows the
  feature work will be scored on, so later work is compared against a floor fixed first

## Book reference, prerequisites and artifacts

Chapter 7, Section 7.2. Reads split- and dividend-adjusted daily bars via [[ML4T_A3_0001]]
(verified in [[[ML4T_A3_0002]]](01_feasibility_analysis.ipynb)) and
[[ML4T_A3_0003]], which declares the label set, horizons and holdout boundary. Writes
[[ML4T_A3_0004]] and [[ML4T_A3_0005]]. The first notebook to open
them is [[[ML4T_A3_0006]]](05_evaluation.ipynb), which scores engineered features against
the primary label; the model notebooks from [[ML4T_A3_0007]] onward load whichever label they
train on, and the cross-validation folds are cut from that file's own timeline.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
[[ML4T_A3_0001]] and [[ML4T_A3_0002]] cut the universe and the history for a shorter run; both are
unset here. [[ML4T_A3_0003]] sets the smallest cross-section Section E will take
a standard deviation over.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
## Configuration

Every value that defines a label comes from [[ML4T_A3_0001]]: the label set, the
horizons and the holdout boundary. [[ML4T_A3_0002]] reads [[ML4T_A3_0003]] where a
case study declares it and falls back to the cross-validation buffer, which here is the
same number.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## A. The learning task

The hypothesis is cross-sectional: among a fixed universe of liquid ETFs, those that rose
over the past two quarters continue to outrank those that did not over the following month.
The label itself is each ETF's own forward return over a window a monthly hold spans; what
makes the statement a relative one is how the label is scored, by rank correlation across
the ETFs quoted on a date rather than by the level any one of them reached.
[[ML4T_A3_0001]] sets the decision cadence to a month-end close with execution at the next open,
which fixes the primary horizon at one trading month. The weekly variant asks whether the
same hypothesis pays over a shorter hold, which is a question about turnover and cost.

Labels are sampled every session rather than only at month ends. That gives an order of
magnitude more rows, and consecutive rows then overlap; Section F measures how much
independent information they carry.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0007-p000

~~~~~~markdown
## B. Preparation before the label

A forward window is meaningful only on a price series that is adjusted, ordered and
complete; sorting by [[ML4T_A3_0001]] then [[ML4T_A3_0002]] is what makes a shift mean "the next session
for this ETF".

The labels are built on the full price history, and the eligibility rules in
[[ML4T_A3_0003]] are applied afterwards - to the Section G baseline, and to the trainable
panel in [[ML4T_A3_0004]]. The order is what keeps the horizon in trading sessions:
a shift of [[ML4T_A3_0005]] counts [[ML4T_A3_0006]] rows of whatever frame it runs on, so it has to run on the frame
that still has every session in it.

The panel is unbalanced, which matters from Section E onward: several of these ETFs listed
after the history starts, so the number of symbols quoting on a date is not the size of the
universe. Every cross-sectional quantity below - the spread within a date, the rank
correlation - is computed over whatever is quoting that day, and needs a minimum before it
means anything.

The *digest* printed below is a hash of the price values the labels are built from, taken
over the symbol, timestamp and close columns the cell reads. Section H writes it beside each
label file, so a stored label can be traced back to the download it came from.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
## C. Label construction

One execution convention, written once, applied to both horizons:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is the adjusted close and [[ML4T_A3_0003]] counts [[ML4T_A3_0004]] **trading sessions** for symbol [[ML4T_A3_0005]].
This is Chapter 7.2's close-to-close convention. The two labels, written to columns
[[ML4T_A3_0006]] and [[ML4T_A3_0007]], share the anchor and differ only in [[ML4T_A3_0008]].

Two bookkeeping columns are numbered alongside them, on the complete price series before any
row is dropped: [[ML4T_A3_0009]] counts back from each symbol's last session for Section D, and
[[ML4T_A3_0010]] numbers its bars forward for Section F. Neither is written to the label parquet.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
## D. Window validity

A shift always returns something; the question is whether it is the quantity the label
claims. Four properties have to hold, and each fails without raising an error, so the cell
below checks them with [[ML4T_A3_0001]]:

1. A row whose forward window is incomplete carries a null, never a value.
2. No labelled window spans a gap in the data. The tolerance is derived rather than tuned:
   [[ML4T_A3_0002]] trading sessions cover about [[ML4T_A3_0003]] calendar days on a five-session week, plus a
   week for exchange holidays.
3. No label crosses from one symbol into the next. The labelled row count equals the bar
   count less [[ML4T_A3_0004]] rows per symbol, which holds only if every window closed inside the
   symbol it opened in.
4. No discrete label is derived from a null return. Both labels here are continuous, so
   this is a check on their dtype.

Property 2 measures the window in calendar days, so it catches a hole of a week or more and
not a single missing session. An exact session count needs an exchange calendar.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
The assertions stop the run, but they do not show *where* each label ends. The figure below
does. Position zero is each symbol's last session, and the share of symbols carrying a label
falls to zero over exactly the last [[ML4T_A3_0001]] positions and sits flat at one before them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>
