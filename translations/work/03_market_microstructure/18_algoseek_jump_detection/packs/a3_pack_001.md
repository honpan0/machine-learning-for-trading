# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：03_market_microstructure/18_algoseek_jump_detection.ipynb；A3 Pack 001；單元 10 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Market microstructure → 市場微觀結構
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Cluster → 群集
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Detecting Price Jumps in Intraday Returns

**Chapter 3: Market Microstructure**

**Docker image**: [[ML4T_A3_0001]]

## Purpose

Realized intraday variance mixes two distinct processes: a continuous
diffusive component driven by the steady arrival of small order-flow
innovations, and a discrete jump component driven by news, scheduled
announcements, and large block trades. This notebook separates the two
on AlgoSeek NASDAQ-100 minute bars using bipower variation
(Barndorff-Nielsen and Shephard, 2004) for the continuous part and the
Lee–Mykland (2008) nonparametric test to time individual jumps. The
resulting daily features — jump count, signed jump variance, jump share
of realized variance — feed directly into the label-conditioning logic
of Chapter 7 and the volatility-regime features of Chapter 8.

## Learning Objectives

- Decompose daily realized variance into continuous and jump components
  via bipower variation
- Apply the Lee–Mykland test to flag individual jumps with a
  leakage-free, multiple-testing-aware critical value
- Quantify how concentrated jumps are in time of day and across the
  trading year
- Show why a naive |z|>k threshold over-detects in low-vol regimes and
  under-detects in high-vol regimes
- Materialize a per-symbol, per-day jump-feature panel ready for
  downstream feature engineering

## Book reference

Section §3.5, *Detecting Price Jumps in Intraday Returns*.

## Prerequisites

- AlgoSeek TAQ minute bars under
  [[ML4T_A3_0002]]
  (Hive-partitioned), loaded via [[ML4T_A3_0003]].
- Companion: [[ML4T_A3_0004]] for raw-bar microstructure
  schema.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0002-p000

~~~~~~markdown
### Declared parameters

[[ML4T_A3_0001]] names three NASDAQ-100 members. AlgoSeek stores the ticker each name carried
at the time, so Meta appears as "FB" for 2020 dates - the change to "META" came in
2022, and asking for the later symbol on an earlier date returns nothing.

[[ML4T_A3_0002]] sets the sampling frequency. Jump tests want bars short enough that a
jump is not averaged away with the diffusion around it, and long enough that the
bid-ask bounce does not dominate the return.

[[ML4T_A3_0003]] is the window, in bars, over which local volatility is estimated. The
test asks whether a return is large relative to volatility *nearby*, so the window has
to be long enough to estimate that and short enough to stay local.

[[ML4T_A3_0004]] is the significance level for the whole session, not for one bar. A
session holds dozens of bars, so testing each one at that level independently would
flag several a day by chance alone; the threshold computed below is the one that
holds the error rate at this level across the session as a whole.
~~~~~~

<<<ML4T-ZH-BEGIN:c0002-p000>>>
<<<ML4T-ZH-END:c0002-p000>>>

### c0005-p000

~~~~~~markdown
## 1. Load minute bars and compute log returns

We restrict to regular hours (09:30–16:00 ET) so that the diffusion
assumption underlying both bipower variation and the Lee–Mykland test
is not contaminated by extended-session stale quotes. Log returns are
computed per symbol-day to avoid bridging the overnight gap, which
behaves as a jump but is not the object of intraday inference.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
## 2. Realized variance and bipower variation

For day [[ML4T_A3_0001]] with [[ML4T_A3_0002]] intraday log returns [[ML4T_A3_0003]], the
realized variance is
[[ML4T_A3_0004]]
which is a consistent estimator of total quadratic variation —
continuous *plus* squared jumps. The bipower variation,
[[ML4T_A3_0005]]
is jump-robust: a single large [[ML4T_A3_0006]] is multiplied by its small
neighbor and contributes negligibly. The gap
[[ML4T_A3_0007]] is therefore an estimate of
the jump-attributable variance on day [[ML4T_A3_0008]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
The jump share of realized variance is right-skewed across symbol-days:
most days are almost purely diffusive (RV ≈ BV, so the jump share sits
near zero), while a heavy right tail carries the episodic jump days. The
ECDF makes the concentration explicit — the median day attributes little
variance to jumps, but the upper decile can attribute a large fraction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0011-p000

~~~~~~markdown
Annualized, BV gives the continuous-volatility floor of each name and
the jump-variance share quantifies how much of the total annual
realized variance is attributable to discrete jumps rather than
diffusion.
~~~~~~

<<<ML4T-ZH-BEGIN:c0011-p000>>>
<<<ML4T-ZH-END:c0011-p000>>>

### c0013-p000

~~~~~~markdown
## 3. The Lee–Mykland jump test

Lee and Mykland (2008) construct a test that times jumps to the bar.
For bar [[ML4T_A3_0001]] within a session of [[ML4T_A3_0002]] bars they form a standardized statistic
[[ML4T_A3_0003]]
where [[ML4T_A3_0004]] is a local bipower volatility built from a window
of [[ML4T_A3_0005]] prior returns *within the same session* — it adapts to slow-moving
intraday volatility regimes and is robust to the jumps it is trying to
detect. Building the window per session avoids bridging the overnight
gap, which behaves as a jump and would contaminate the local-volatility
denominator for the first [[ML4T_A3_0006]] bars of each day. The trade-off is that
the first [[ML4T_A3_0007]] bars of every session are not directly testable.

Under the no-jump-at-[[ML4T_A3_0008]] null and a continuous-diffusion alternative,
[[ML4T_A3_0009]] over the daily session converges to a Gumbel distribution.
The rejection rule at level [[ML4T_A3_0010]] is
[[ML4T_A3_0011]]
and [[ML4T_A3_0012]]. The multiple-testing
burden is absorbed by the [[ML4T_A3_0013]]-dependent constants, not by an ad-hoc
Bonferroni adjustment. Lee and Mykland recommend [[ML4T_A3_0014]]
(≈9 for 78 5-minute bars per day); we use [[ML4T_A3_0015]] as a slightly more
conservative window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0013-p000>>>
<<<ML4T-ZH-END:c0013-p000>>>

### c0015-p000

~~~~~~markdown
The threshold depends on how many bars a session holds, because testing more bars gives
more chances for a large return to appear by accident. It is computed once from the
median session length so that every bar in the study is tested against the same
threshold, rather than a symbol with a slightly longer session facing a slightly
harder test.
~~~~~~

<<<ML4T-ZH-BEGIN:c0015-p000>>>
<<<ML4T-ZH-END:c0015-p000>>>

### c0017-p000

~~~~~~markdown
## 4. How often do jumps fire and how big are they?

A symbol-day typically sees a handful of test rejections; days with
scheduled news cluster materially higher. The signed magnitude of
the underlying log return distinguishes upside surprises from
downside.
~~~~~~

<<<ML4T-ZH-BEGIN:c0017-p000>>>
<<<ML4T-ZH-END:c0017-p000>>>

### c0020-p000

~~~~~~markdown
## 5. Jumps cluster in time of day

The opening minutes and the close concentrate price discovery: news
released overnight is impounded at the auction, and end-of-day
rebalancing flows produce sharp moves. The session-boundary fix means
the first [[ML4T_A3_0001]] bars of each day (≈55 min) are not
testable, so any "first 30 min" detection here is limited; we report
the share within the testable window and look for the close-of-day
uptick that the test can see in full.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>
