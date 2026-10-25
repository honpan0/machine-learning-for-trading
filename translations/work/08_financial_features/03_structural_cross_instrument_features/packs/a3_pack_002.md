# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/03_structural_cross_instrument_features.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Risk premium → 風險溢酬
- Momentum → 動能
- Feature → 特徵
- Cross-sectional → 橫斷面
- Volatility → 波動率
- Standard deviation → 標準差
- Correlation → 相關性

## 待翻譯英文單元

### c0029-p000

~~~~~~markdown
**Interpretation**: High-beta ETFs (XLK, QQQ) often show strong raw momentum
that is largely market-driven. Residual momentum isolates the ETF-specific
component, which is what a rotation strategy wants.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>

### c0030-p000

~~~~~~markdown
## Lead-Lag Correlations
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0031-p000

~~~~~~markdown
Does SPY lead the sector ETFs? The loop below correlates the SPY return at t with each
sector's return at t plus a lag, so a non-zero correlation at a positive lag is SPY
moving first.
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
**Interpretation**: If lag-1 correlation (SPY_t vs Sector_{t+1}) is meaningfully
positive, SPY may lead the sector -- a tradeable signal if the lead is genuine
and not a staleness artifact (e.g., less liquid sector ETFs closing before SPY).
Always verify that the leading instrument actually traded at the "lead" timestamp.
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
## Deviation from Peer Mean (Relative Value Z-Score)

For each ETF, compute how far its return deviates from the cross-sectional mean:

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
**Interpretation**: Relative-value z-scores identify assets that have diverged
from their peer group. A z-score of +2 means the asset's 21-day momentum is
two standard deviations above the cross-sectional mean -- a candidate for
mean-reversion or confirmation of breakout depending on the strategy.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0037-p000

~~~~~~markdown
**Full pipelines**: The [[ML4T_A3_0001]] case study ([[ML4T_A3_0002]])
applies cross-asset features to the full 100-ETF universe. The [[ML4T_A3_0003]] case
study uses analogous relative value features for currency pairs.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0038-p000

~~~~~~markdown
---

# Part 3: Options-Implied Features

Options encode the market's probabilistic assessment of future outcomes.
Four key features capture distinct information:

| Feature | What It Measures | Role |
|---------|-----------------|------|
| ATM IV | Expected future volatility | State |
| Risk reversal (25[[ML4T_A3_0001]] skew) | Directional fear/greed | State |
| IV term structure slope | Near-term vs long-term stress | State |
| VRP (IV minus RV) | Variance risk premium | Signal/state |
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0039-p000

~~~~~~markdown
## Load Options and Equity Data
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0041-p000

~~~~~~markdown
## ATM Implied Volatility

ATM IV is the market's expectation of future volatility over the option's life. The
selection below is on **moneyness**, not on delta: [[ML4T_A3_0001]] keeps calls whose
strike sits inside [[ML4T_A3_0002]] of the underlying and whose maturity sits inside
[[ML4T_A3_0003]], then takes the strike closest to the money on each day. Near the money and
near a one-month maturity the closest-to-the-money call has a delta in the region of a
half, which is where "the fifty-delta" as a name for this contract comes from, but the
delta is never read and a contract is never selected by it. The defaults are in the
function signature below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0043-p000

~~~~~~markdown
## Risk Reversal (25-Delta Skew)

The risk reversal measures directional skew: the price of downside protection
relative to upside:

[[ML4T_A3_0001]]

Positive values indicate puts are more expensive (crash fear).
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
## IV Term Structure Slope

The ratio of short-dated to long-dated IV captures near-term stress:

[[ML4T_A3_0001]]

- [[ML4T_A3_0002]]: Inverted (near-term stress, fear of imminent event)
- [[ML4T_A3_0003]]: Normal contango (calm)
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0047-p000

~~~~~~markdown
## Variance Risk Premium (IV - RV)

The VRP as computed here is the difference between a forward-looking implied volatility
and a trailing realized volatility:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] looks back over the twenty sessions ending at [[ML4T_A3_0003]]. The realized leg is
built from split-adjusted closes; the note in [[ML4T_A3_0004]] says why that matters.

Be precise about what this quantity is before reading anything off it. It subtracts a
**trailing** twenty-day realized volatility from a **forward-looking** thirty-day
implied volatility, so the two terms describe different and barely overlapping windows.
It is a spread between two volatility measurements taken on the same day, and it is not
a return: nothing here buys or sells an option, and no position is held to expiry. The
quantity a volatility seller actually earns compares the implied volatility quoted at t
with the realized volatility over the *following* thirty days, which this feature does
not compute.

With that established, the cell below describes the spread's distribution. Read the
share of days on which it is positive together with the median and the mean. A spread
that is positive on most days while its mean sits below its median is left-skewed: small
positive values most of the time, and occasional negative values large enough to move
the average on their own. The most positive and most negative values printed say how
lopsided, and the bottom panel of the figure further down shows the same thing for one
name: a series near zero whose vertical extent is set by a single deep excursion.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p000>>>
<<<ML4T-ZH-END:c0047-p000>>>

### c0047-p001

~~~~~~markdown

The skew is a property of the spread worth carrying forward, because it is what makes a
summary statistic misleading here: a mean and a median disagree about the sign, and
quoting either alone describes a different series. It also suggests treating a feature
built from this spread as a state variable rather than reading it as a signal at face
value. Whether selling volatility is profitable is a separate question that needs
the horizon-matched calculation above, not this table. Note too that the share of
positive days is not uniform across names: check whether every symbol is above a half
before treating "the spread is positive" as something to lean on.
~~~~~~

<<<ML4T-ZH-BEGIN:c0047-p001>>>
<<<ML4T-ZH-END:c0047-p001>>>
