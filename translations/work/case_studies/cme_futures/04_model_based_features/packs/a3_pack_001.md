# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/04_model_based_features.ipynb；A3 Pack 001；單元 6 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Standard deviation → 標準差

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# CME Futures: Features That Are Themselves Model Output

Every feature so far has been a formula applied to past prices. This notebook builds
features of a second kind: it estimates a statistical model from past prices and then
emits what that model says about each session as the feature. All three models start
from the same quantity, the **carry** of a futures product - the price difference
between the contract expiring soonest and the one expiring after it, which is what a
trader holding a position earns or pays each time the position is rolled from one to
the next.

1. **ARIMA** forecasts next session's carry from the recent path of carry, one forecast
   per product per session.
2. **A rolling Fourier transform** measures which cycle lengths the carry of a product
   has been oscillating at over the past year.
3. **A two-state hidden Markov model** reads one number per session - carry averaged
   across the whole book - and infers which of two market states the book is in.

It reads the raw CME settlement prices and the forward-return labels written by
[[[ML4T_A3_0001]]](02_labels.ipynb), and it writes one artifact,
[[ML4T_A3_0002]].

**What you will be able to do after reading this**
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

- Say why estimating a model on all your data and then using its output as a feature
  gives you a number no one could have computed at the time, and recognise the shape of
  that mistake in your own code.
- Refresh a model's parameters on a declared schedule, so that the value for any
  session is produced by an estimate made from sessions strictly earlier than it -
  and see why a walk-forward period does not do that job on its own.
- Run a hidden Markov model so that its answer for a given day uses that day and every
  earlier day but no later day, and check by experiment that this is what it did.
- Write the resulting features to a file that records which prices they came from, so a
  model trained on them later can state which version of the features it read.

**Book Reference**: Chapter 9, Sections 9.3-9.5

**Prerequisites**: [[[ML4T_A3_0001]]](02_labels.ipynb). It writes the forward-return file
this notebook reads, and the dates in that file are what the training and evaluation
periods below are cut from. [[[ML4T_A3_0002]]](03_financial_features.ipynb) runs
as a parallel branch on the same raw prices; the two feature sets are read together by
the model notebooks in Chapter 11.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0002-p000

~~~~~~markdown
## Configuration

Five settings, and each one decides something a reader would otherwise have to guess at.
[[ML4T_A3_0001]] and [[ML4T_A3_0002]] exist so a smoke test can run a fraction of the work; both
are zero here, which means the full universe and every evaluation period.

What is *not* here is the estimation schedule. How much history each fitted model spends
before its first estimate, and how often it is refreshed, are part of what the feature
means rather than settings to trade runtime against, so they are read from [[ML4T_A3_0003]]
below alongside the feature windows. [[ML4T_A3_0004]] is the reduction lever for
that: zero here, meaning "use what [[ML4T_A3_0005]] declares", and a positive value replaces
both declared cadences for one run. It is named so nothing reading this file can mistake
a reduction for the definition.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0004-p000

~~~~~~markdown
Three more settings come from [[ML4T_A3_0001]], the file that also configures
[[[ML4T_A3_0002]]](03_financial_features.ipynb). The universe is the thirty
products and the sectors they belong to. The two windows are the ones that stage uses
to smooth carry and to express it as a z-score - the number of standard deviations
carry sits from its own recent average - so that the series built in section C is the
same series that stage writes under the name [[ML4T_A3_0003]], in a different shape.
~~~~~~

<<<ML4T-ZH-BEGIN:c0004-p000>>>
<<<ML4T-ZH-END:c0004-p000>>>

### c0006-p000

~~~~~~markdown
## The data these models read

One row per product, expiry and session, carrying that contract's settlement price.
**Product** is a futures contract's underlying - corn, gold, the S&P 500 index - and
each product trades in several contracts at once that differ only in when they expire.
Those are indexed by [[ML4T_A3_0001]]: position 0 is the contract expiring soonest, the
**front month**; position 1 is the one after it; position 2 the one after that.
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
The thirty products are not thirty interchangeable series. They are seven groups of
things that move for their own reasons, and the models below fit one product at a time,
so a product's group is what the reader should carry forward about it.

Each row is one sector: the products in it, the session its earliest product first
quoted, the session by which all of them were quoting, and how many front-month
product-sessions it contributes. Two things to read off it.

The panel starts together. Every sector's two date columns hold the same session, with
one exception, and that exception is why the equity-index row contributes fewer sessions
than any other four-product sector. Comparing the two date columns is how to find it.

The rest of the spread in the session counts is holiday calendars. These sectors do not
close on the same days, so per product the agricultural and livestock contracts quote
about a hundred fewer sessions across the panel than the financial ones. That is a small
effect for a model fitted one product at a time, and a large one for section C.3, which
has to average carry across all of them on every session and therefore has to decide
what to do about the ones that did not settle.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>
