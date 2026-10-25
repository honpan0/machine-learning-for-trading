# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/22_pandas_polars_benchmark.ipynb；A3 Pack 003；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Feature → 特徵

## 待翻譯英文單元

### c0064-p000

~~~~~~markdown
## Category E: Joins

Join operations are critical for tick data processing (trade-quote matching)
and panel data operations.
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0066-p000

~~~~~~markdown
### E1: ASOF Join (Trade-Quote Matching)

Match each trade to the most recent quote - fundamental for tick data analysis.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0067-p000

~~~~~~markdown
Both libraries need their inputs sorted, and they do not want the same sort. pandas'
[[ML4T_A3_0001]] requires the frames ordered by the [[ML4T_A3_0002]] column across the whole frame,
with the [[ML4T_A3_0003]] column handled internally; Polars wants them ordered by the [[ML4T_A3_0004]] column
and then the [[ML4T_A3_0005]] column. The sorting is done once, here, outside the timed region,
because it is a precondition of the join rather than part of it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0067-p000>>>
<<<ML4T-ZH-END:c0067-p000>>>

### c0070-p000

~~~~~~markdown
### E2: Anti-Join (Find Unmatched Trades)

Find trades with no quote at the same timestamp, a data-quality check. Polars has a
native anti-join; where pandas has one it is used, and where it does not the only
route is a left merge with an indicator followed by a filter, which materializes
every matched row on the way to discarding it. That difference in available
algorithm is the thing being measured, so the cell asks the installed pandas which
it has rather than deciding from a version number.

Read the row count as a property of the generator, not as a data-quality finding.
[[ML4T_A3_0001]] stamps trades fifty microseconds off the quote grid, so no trade
shares a timestamp with a quote and every trade comes back unmatched. The join still
does the full amount of work; what it does not do is exercise the matched path, and
on real tick data, where most trades do match, the indicator merge has more rows to
build and discard than it has here.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0071-p000

~~~~~~markdown
The cell below asks pandas whether it has a native anti-join rather than inferring it
from the major version. A version check can be wrong about the installed pandas, and
when it is, the indicator merge runs in both arms and the notebook claims to exercise a
feature it never called.
~~~~~~

<<<ML4T-ZH-BEGIN:c0071-p000>>>
<<<ML4T-ZH-END:c0071-p000>>>

### c0074-p000

~~~~~~markdown
### E3: Inner Join

Standard inner join for combining related tables.
~~~~~~

<<<ML4T-ZH-BEGIN:c0074-p000>>>
<<<ML4T-ZH-END:c0074-p000>>>

### c0075-p000

~~~~~~markdown
One lookup table, built once and converted, rather than two built independently. The
two used to draw their sectors from separate [[ML4T_A3_0001]] calls and take their
symbol order from [[ML4T_A3_0002]] on each library, which does not agree on ordering. The
two joins therefore produced different tables, which is not a comparison.
~~~~~~

<<<ML4T-ZH-BEGIN:c0075-p000>>>
<<<ML4T-ZH-END:c0075-p000>>>

### c0078-p000

~~~~~~markdown
## Category F: Lazy Evaluation and Streaming

Test lazy evaluation benefits on parquet files. This is where Polars
typically shows largest advantages through predicate pushdown.
~~~~~~

<<<ML4T-ZH-BEGIN:c0078-p000>>>
<<<ML4T-ZH-END:c0078-p000>>>

### c0080-p000

~~~~~~markdown
### F1: Lazy Filter (Predicate Pushdown)

Filter during scan - Polars can push predicates into the parquet reader.
~~~~~~

<<<ML4T-ZH-BEGIN:c0080-p000>>>
<<<ML4T-ZH-END:c0080-p000>>>

### c0083-p000

~~~~~~markdown
### F2: Column Projection

Read only needed columns - both libraries optimize this.
~~~~~~

<<<ML4T-ZH-BEGIN:c0083-p000>>>
<<<ML4T-ZH-END:c0083-p000>>>

### c0086-p000

~~~~~~markdown
### F3: Combined Filter + Aggregation (Query Optimization)

Complex query that benefits from Polars' query optimizer.
~~~~~~

<<<ML4T-ZH-BEGIN:c0086-p000>>>
<<<ML4T-ZH-END:c0086-p000>>>

### c0089-p000

~~~~~~markdown
## Category G: Memory Efficiency

This section reports what each library says its own frame costs, and nothing else.

It used to bracket a single copy with [[ML4T_A3_0001]] resident-set readings and report the
difference as the copy's memory. A resident-set delta cannot answer that question: an
allocator satisfies a request from pages it already holds and returns nothing to the
kernel on free, so the reading moves with allocator state rather than with the copy,
and the two numbers it printed fed nothing further in the notebook.

What the two accountings do measure is worth knowing, provided the difference is
stated. The numeric columns are eight bytes a value on both sides and contribute
almost nothing to the ratio. The symbol column is the whole of it, and the two
libraries represent it differently: pandas holds an object column as an array of
pointers to Python string objects, and each of those objects carries its own header,
so a seven-character ticker costs tens of bytes. Polars holds the same column as
packed UTF-8 with offsets, where the ticker costs about what its characters cost.

Neither side is doing anything clever with the repetition here. The column is
[[ML4T_A3_0002]] and stays that way: there are only a handful of distinct symbols, and
casting to a categorical would collapse the column further, but that is a different
measurement from this one and the notebook does not make it.

Both figures below are read in bytes and divided by the same factor. Polars'
[[ML4T_A3_0003]] returns binary megabytes and pandas' [[ML4T_A3_0004]] returns
bytes, so dividing one by 1e6 and taking the other as-is inflates the ratio by about
five percent - small enough to look like a real difference between the libraries.
~~~~~~

<<<ML4T-ZH-BEGIN:c0089-p000>>>
<<<ML4T-ZH-END:c0089-p000>>>

### c0091-p000

~~~~~~markdown
### G1: What each library says the panel costs
~~~~~~

<<<ML4T-ZH-BEGIN:c0091-p000>>>
<<<ML4T-ZH-END:c0091-p000>>>

### c0093-p000

~~~~~~markdown
## Category H: String Operations

String operations are often the bottleneck in a symbol-heavy pipeline. A pandas with
PyArrow-backed strings does this work differently from one without; the setup cell
says which of the two ran.
~~~~~~

<<<ML4T-ZH-BEGIN:c0093-p000>>>
<<<ML4T-ZH-END:c0093-p000>>>
