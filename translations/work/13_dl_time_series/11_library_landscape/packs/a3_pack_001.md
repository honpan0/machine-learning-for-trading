# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：13_dl_time_series/11_library_landscape.ipynb；A3 Pack 001；單元 13 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Test set → 測試集
- Cross-sectional → 橫斷面
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# The same forecast, written six ways

**Docker image**: [[ML4T_A3_0001]]

Every notebook in this chapter has been written directly against PyTorch: a model
class, a training loop, an evaluation block. That is the right way to learn an
architecture and a poor way to try five of them. This notebook writes the same
univariate forecast through several libraries and compares the *experience* -
how many lines, what has to be installed, what the interface constrains.

**sktime** is the one to understand, because it is not a model library. It is an
interface - [[ML4T_A3_0002]], [[ML4T_A3_0003]], [[ML4T_A3_0004]] - that delegates to NeuralForecast,
PyTorch Forecasting, HuggingFace and classical methods, so swapping an LSTM for
Chronos or for ARIMA is a constructor change rather than a rewrite. **Darts**
takes the other approach: its own [[ML4T_A3_0005]] container and its own model
implementations.

**What the table measures is effort, not accuracy.** The rows do not share a target
scale or a test set, so the error column cannot be read across them - which is
stated where the table appears and marked in the table's own columns. A last-value
baseline is included precisely so that the one comparison that *is* like-for-like
is on the page.

**Learning objectives**:
- Write the same forecast against a raw framework and against a wrapper, and count
  what the wrapper actually saved.
- Read a comparison table and identify which columns can be compared across rows
  and which cannot.
- Say what a rank correlation means when the target is a price level rather than a
  return.
- Decide when the interface constraint is worth the boilerplate it removes.

**Book Reference**: Chapter 13, Section 13.7 (A practical framework)

**Prerequisites**: ETF price data via the canonical [[ML4T_A3_0006]] loader
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
Three of the libraries below write progress banners to standard error - the accelerator
they picked, a suggestion to install a logging integration, a deprecation inside
[[ML4T_A3_0001]] reached through sktime's Chronos wrapper. None of it reports a problem
and none of it is this notebook's output, so each is quieted by name at its own logger
rather than by a blanket filter. Anything these libraries raise as a warning still
reaches the render.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0006-p000

~~~~~~markdown
## Data: SPY Close Prices

We use a single univariate series (SPY daily closes) so every library sees
identical input. We prepare two representations: NumPy sequences for raw
PyTorch, and a pandas Series with business-day index for sktime/Darts.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
The order of the two steps above matters. The train/test boundary is fixed in
sequence space *first*, and the normalisation statistics are then computed from
prices up to [[ML4T_A3_0001]] only - the last price index any training sequence can
reach, its input window plus the forecast horizon. Normalising with the full
series' mean and standard deviation would fold test-period price levels into the
training inputs, which is a leak that leaves no trace in any split.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0009-p000

~~~~~~markdown
### PyTorch Sequences (Normalized)
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
### sktime / Darts Series (Prices with DatetimeIndex)
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
### Evaluation Helper

**The IC here is not the IC in the rest of the chapter.** Notebooks 04 through 10
compute a *cross-sectional* rank correlation: on each date, do the predicted ranks
of the funds match the realised ranks? There is one series here, so there is no
cross-section, and what this helper computes is the rank correlation between
predicted and actual values across time.

On a price level that number is close to one for anything that tracks the level,
including a forecast that just repeats the last observation - the baseline below
demonstrates it. Read the [[ML4T_A3_0001]] column as a check that a model is not producing
nonsense, and read MSE for anything else.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
### The forecast to beat

Before any library: forecast the next [[ML4T_A3_0001]]-day mean as the last observed
price. It costs one line, it is what every model below has to improve on, and on a
price level it is hard to beat - which is exactly why it belongs in the table.

The IC column needs the same warning. On a trending price level, any forecast that
tracks the level correlates with the outcome almost perfectly, so a rank correlation
near one is a statement about the series, not about the model. The baseline row is
what makes that visible.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## Part 1: Raw PyTorch LSTM

The "full control" baseline: model definition, training loop, and evaluation
require roughly 50 lines of boilerplate.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
The raw PyTorch LSTM requires defining the model class, training loop, and
evaluation - approximately 50 lines. Full control over architecture and training
dynamics, at the cost of that boilerplate.

Compare the two lines printed above before reading anything else in this notebook as
a result. Both are on the same scale and the same test points, which is the only
such comparison here, and the baseline needed no training at all.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0021-p000

~~~~~~markdown
## Part 2: sktime + NeuralForecast LSTM

sktime wraps NeuralForecast's LSTM: three lines replace the 50-line training
loop. The underlying recurrent architecture is equivalent.

**Dependency note**: sktime's neural forecasters require [[ML4T_A3_0001]], which
depends on [[ML4T_A3_0002]], and Python 3.14 wheels for ray are still pending
([ray-project/ray#56434]([[ML4T_A3_0003]])). This
section describes the call rather than running it. Note also that recent sktime
releases renamed the wrapper's [[ML4T_A3_0004]] argument to [[ML4T_A3_0005]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0022-p000

~~~~~~markdown
The shape of the call, when it can be made, is
[[ML4T_A3_0001]]
followed by [[ML4T_A3_0002]] and [[ML4T_A3_0003]] - the whole of Part 1's model class and training
loop replaced by a constructor. That is the argument for the wrapper, and this
environment is also the argument against depending on one: the code above cannot
run here at all.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0023-p000

~~~~~~markdown
## Part 3: sktime + PyTorch Forecasting N-BEATS

N-BEATS (Section 13.2) via sktime's PyTorch Forecasting wrapper. Same
[[ML4T_A3_0001]]/[[ML4T_A3_0002]] API, different architecture underneath.

**Dependency note**: sktime's PyTorch Forecasting wrapper requires
[[ML4T_A3_0003]], and the last attempt also hit a wrapper API mismatch around
[[ML4T_A3_0004]] and [[ML4T_A3_0005]]. This section describes the call
rather than running it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>
