# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/01_feasibility_analysis.ipynb；A3 Pack 002；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子

## 待翻譯英文單元

### c0006-p000

~~~~~~markdown
## B. Universe and cost feasibility

### B.1 Load the data and look at the universe

The loader returns one row per product, delivery month and trading session. Delivery months
are numbered by distance from expiry, so [[ML4T_A3_0001]] is the front month and [[ML4T_A3_0002]] is
the one behind it. Section B.4 uses both; everything else uses the front month alone.

Two price columns come back, and they answer different questions. [[ML4T_A3_0003]] is the
settlement price the exchange actually printed, which is what a trade would have been done
at. [[ML4T_A3_0004]] is *back-adjusted*: each time the series rolls from one delivery month to the
next, the older history is shifted so the jump between the two contracts does not appear as a
price move. Differences of the adjusted series are therefore returns rather than roll
artefacts, which is why it is the one used for measuring moves. It has one property worth
knowing about now: after enough accumulated adjustments the adjusted level can fall to zero or
below, at which point a percentage change computed from it is meaningless. Every division by
it below is guarded for that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
Here is what those 30 products are, and what one contract of each of them commits you to. The
exchange publishes a specification per product, and six of its fields are worth having in
front of you before anything is computed from the prices, because every cost figure in this
notebook is built out of them.

**Contract size.** A futures contract is written on a fixed quantity, and the quoted price is
the price of one unit of that quantity. One corn contract covers 5,000 bushels and corn is
quoted per bushel. One Australian dollar contract covers A[[ML4T_A3_0001]] and is quoted per
Australian dollar. One E-mini S&P 500 contract covers 50 times the index and is quoted in
index points. So the column reads as bushels for corn, as currency units for the Australian
dollar and as dollars per index point for the S&P, and its one job is to turn a quote into an
amount of money.

**Minimum price increment**, or *tick size*. The smallest amount by which a quote may change.
Corn moves in quarter-cents per bushel, the E-mini S&P in quarter index points, the 10-year
Treasury note in 64ths of a percent of face value.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0008-p001

~~~~~~markdown

**Tick value.** What one increment is worth on one contract, in dollars, which is the
increment multiplied by the contract size. The exchange publishes it separately, and it is
worth seeing why the two do not always multiply out. Corn's increment is a quarter of a cent
and its contract is 5,000 bushels, so one increment moves the contract by 1,250 - and that is
1,250 cents, not 1,250 dollars, because corn is quoted in cents per bushel. The tick value the
exchange publishes is in dollars, and the table below shows what it comes to. The grains and
the livestock are quoted in cents; the Treasury contracts are quoted as a percentage of face
value rather than as a fraction of it. Either way the quote is in hundredths of the unit the
contract size counts, a factor of 100. Dividing the published tick value into the increment
times the contract size recovers that factor product by product, which is what the cell below
does. Asserting that it comes out at exactly 1 or exactly 100 is what makes the contract
values in the table dollars rather than cents.

**Contract value**, also called the *notional* value. What one contract is worth outright:
the settlement price, converted to dollars per unit, multiplied by the contract size. The
table takes it at one reference date, the last settlement before the holdout period begins,
so that nothing in it depends on data this notebook is not allowed to read. The spread down
that column is the thing to notice: one corn contract is a commitment of about [[ML4T_A3_0001]] and
one NASDAQ-100 contract is a commitment of about [[ML4T_A3_0002]]. A cost quoted in dollars per
contract would therefore mean something different in every row, which is why every cost below
is expressed relative to contract value instead.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p001>>>
<<<ML4T-ZH-END:c0008-p001>>>

### c0008-p002

~~~~~~markdown

**Initial margin**, and the leverage that comes with it. Holding a contract does not require
paying its contract value. It requires posting a deposit with the clearing house, which is
settled up or down every day as the price moves. The deposit is a few percent of the contract
value, and the ratio between the two is the leverage the position carries: the 2-year
Treasury note below controls about [[ML4T_A3_0001]] of notes for a deposit of about [[ML4T_A3_0002]]. That
ratio is not a measure of how aggressive the position is. The exchange sets the deposit
against how much the contract moves, so the contracts that move least carry the highest
leverage, and the 2-year note at 158 times is closer in daily risk to silver at 8 times than
the two ratios suggest. What it does mean for this strategy is that the capital it has to
fund is a multiple of the deposits, not of the contract values it ranks.

The margin rates used here come from CME's published schedule and are documented under
"Margin Model" in this case study's README, including where they are approximated: the four
equity index contracts share one rate and the four energy contracts share another, which is
why those rows show identical leverage. They give the right order of magnitude for what a
position costs to carry. They are not a quote from a broker.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p002>>>
<<<ML4T-ZH-END:c0008-p002>>>

### c0008-p003

~~~~~~markdown

**Delivery months.** How many contracts a product lists each year, which is how often a
position in it has to be rolled. The energies list all twelve months, so a position held for a
year is rolled twelve times. The currencies, the equity indices and the Treasuries list four,
evenly spaced through the year, so it is rolled four times. The metals, the crops and the
livestock mostly fall between the two, on cycles that follow their delivery and marketing
seasons. Every roll pays the spread twice and
collects or gives up carry, so this column is what turns carry from something earned per roll
into something earned per year.

The last column is the first date on which each product settles in this sample. All of them
are present from the beginning except the E-mini Russell 2000, which arrives in 2017, and that
is what makes the size of the universe a question rather than a constant. Section B.2 takes it
up.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p003>>>
<<<ML4T-ZH-END:c0008-p003>>>
