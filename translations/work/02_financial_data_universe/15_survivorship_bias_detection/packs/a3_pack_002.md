# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/15_survivorship_bias_detection.ipynb；A3 Pack 002；單元 11 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0016-p000

~~~~~~markdown
Every one of these is a corporate action the adjustment missed, and the [[ML4T_A3_0001]] column
records no split for any of them:

- **HERO** (Hercules Offshore) emerged from Chapter 11 on 2015-11-06. The old equity was
  cancelled and new shares were issued on the same ticker. The two prices either side of the
  jump are quotes for two different securities, so their ratio is not a return. Note the
  zero volume on the days before: those pre-emergence quotes are stale.
- **PCO** (Pendrell) ran a one-for-a-hundred reverse split on 2017-12-05, and the
  [[ML4T_A3_0002]] column never fired.
- **EXXI** (Energy XXI) relisted post-bankruptcy on the same ticker.

The table above carries the prices; what matters here is that each is a step of two orders
of magnitude printed as an ordinary session.

Two rules follow directly, and both are diagnostic rather than cosmetic — they say
*"we cannot compute a return across this event"*, and drop it, rather than shrinking it
toward something plausible:

1. A daily return above [[ML4T_A3_0003]] is not trusted.
2. A daily return computed off a prior session that printed **zero volume** is not trusted
   — the denominator is a stale quote.

Both fire on observable evidence, and neither touches genuine crashes. GT Advanced
Technologies lost most of its value on 2014-10-06 when it filed for Chapter 11, on millions
of shares of real volume. That is a return: the loss is one-sided in the direction the
first rule does not test, and the volume clears the second.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0018-p000

~~~~~~markdown
### Phantom sessions

One more artifact, on the calendar rather than the prices. A handful of symbols — LFVN and END
above all — print quotes on days the US market was closed. A session that only a sliver of the
universe trades on is not a session, and its cross-sectional mean is not a portfolio return.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0020-p000

~~~~~~markdown
Six of these are US market holidays — Martin Luther King Jr. Day, Presidents' Day, Good Friday,
Memorial Day, Independence Day, Labor Day — and 2017-04-14 is Good Friday again. The panel had
no business quoting any of them.

[[ML4T_A3_0001]] is different, and it is a nice illustration of how one bad row breeds another. That
session was genuinely open. It looks empty because a *return* needs a prior quote, and the only
symbol with a 2014-01-01 quote to difference against is LFVN — which printed on New Year's Day.
The rule catches it anyway, which is what a rule keyed to evidence rather than to a holiday
calendar is for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0020-p000>>>
<<<ML4T-ZH-END:c0020-p000>>>

### c0022-p000

~~~~~~markdown
## 4. Delisting outcome scenarios

The terminal return — what a holder received after the last quote — is unobservable here
(§2), so we model the *mix* of outcomes rather than any individual one.

Each scenario specifies how the leavers split across three exit types, and what a holder
earns in each. The shares come from CRSP tabulations; the returns from the delisting-return
literature.

**Sources**

- Eckbo & Lithell (2025), *Merger-Driven Listing Dynamics*, JFQA — Table A1 Panel B,
  2,805 CRSP delistings, 2010–2020.
- Doidge, Karolyi & Stulz (2017), *Are There Too Few Publicly Listed Firms?*
- Shumway (1997) and Beaver, McNichols & Price (2007) on delisting returns.

**The load-bearing fact**: M&A dominates US delistings, and outright bankruptcy is rare
enough that it does not earn a row of its own here. A cause delisting is usually a
compliance failure - a low price, a late filing - rather than a firm going under. The
shares and returns are in [[ML4T_A3_0001]] below and printed in the table that follows it.

**A caveat we carry forward.** These terminal returns are applied *on the delisting date*.
For acquisitions that is generous: deal premiums accrue as rumours circulate and the price
converges toward the offer, so by the last quote most of the premium is already in the
observed path. Applying it again at exit double-counts. §6 measures what this assumption is
worth.
~~~~~~

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0024-p000

~~~~~~markdown
The two panels below are the whole scenario definition: who leaves how, and what a holder
earns when they do. The expected terminal return in the right-hand panel is the
share-weighted average — and note it is *positive* in two of three scenarios, because
acquisitions dominate and acquisitions pay a premium.
~~~~~~

<<<ML4T-ZH-BEGIN:c0024-p000>>>
<<<ML4T-ZH-END:c0024-p000>>>

### c0026-p000

~~~~~~markdown
## 5. The two portfolios

Both are equal-weighted and rebalanced daily, and both use **the same convention** — a
holding is averaged in on every session it is held, contributing zero on a session it is not
quoted. The only difference is who is in them:

- **Biased**: the survivors only. This is what a backtest built from a "current constituents"
  list gets, and it is the wrong answer.
- **Full universe**: every symbol quoted at the start. Leavers are held until their exit
  session, where they are liquidated at [[ML4T_A3_0001]].

[[ML4T_A3_0002]]. **A positive bias means the survivors-only portfolio
overstates.**
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0029-p000

~~~~~~markdown
### How much does the repair in §3 matter?

Run both portfolios on the raw returns and on the repaired returns, with the terminal return
switched off, so the only moving part is the untrusted rows flagged above.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0031-p000

~~~~~~markdown
The sign flips. On the raw series the survivors-only portfolio appears to *underperform* the
full universe; on the repaired series it overstates, which is the direction the literature
reports. The share of rows deciding that is printed above and is a small fraction of one
percent, because a daily-rebalanced equal-weight portfolio compounds every row it is given
and one reorganisation printed as a two-hundred-fold gain moves a two-thousand-name
portfolio by double digits in a single session.

This is Chapter 2's own lesson turned on Chapter 2's own analysis: the survivorship check
cannot run ahead of the corporate-action check. Everything below uses the repaired series.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## 6. Quantify the bias

For each scenario, draw an outcome for every leaver from its share vector, assign the
matching terminal return, and compound the full-universe portfolio. Repeat [[ML4T_A3_0001]] times to
get a percentile band on the bias.

The draws are independent across several hundred symbols, so the band will be tight. That
tightness measures **sampling** uncertainty and nothing else. It says nothing about whether
the outcome shares are right — and §6.1 shows that is where the real uncertainty lives.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000

~~~~~~markdown
### Where the uncertainty actually lives

Two ways to be wrong about the bias. The Monte Carlo prices one of them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0037-p000

~~~~~~markdown
## 7. Summary figure

Left: the two portfolio paths, with the gap between them shaded. Right: the bias under each
scenario, with the Monte Carlo band declared as [[ML4T_A3_0001]].
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>
