# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/01_price_volume_features.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Volatility → 波動率

## 待翻譯英文單元

### c0026-p000

~~~~~~markdown
### Rolling Regression Slope

OLS slope over a rolling window measures trend strength more robustly than
endpoint-to-endpoint returns: it uses all intermediate prices and is less
sensitive to start/end outliers.

For evenly spaced data with [[ML4T_A3_0001]]:

[[ML4T_A3_0002]]

We normalize by mean price to get a percentage slope comparable across assets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
### Short-Term Reversal

Over a horizon of a few days, the assets that fell most recently tend to rise, and the
reverse. This is the complement to momentum.

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000

~~~~~~markdown
### Directional Persistence: Distance to MA in ATR Units

This extends the vol-scaled MA distance from **MA Distance (Volatility-Scaled)** above,
with different parameters and a different reading. There a fast moving average over a
matching ATR window measures *current* deviation; here a slower anchor over a shorter
ATR window captures *directional persistence* - how far price has trended away from
that anchor.

[[ML4T_A3_0001]]

ATR is used here for normalization, in price units, rather than as a volatility
estimator. **Volatility Features** below draws that distinction.
~~~~~~

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0032-p000

~~~~~~markdown
Values beyond [[ML4T_A3_0001]] indicate extreme directional extension. This feature
works well as both a signal (contrarian at extremes) and a state variable
(conditioning faster signals on trend context).
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0033-p000

~~~~~~markdown
## Volatility Features

Volatility is essential for:
- **Risk scaling**: Adjust signals by volatility
- **Position sizing**: Kelly criterion, risk parity
- **Regime detection**: High vs low vol environments

### Estimator Efficiency Comparison

| Estimator | Efficiency | Best For |
|-----------|------------|----------|
| Close-to-Close | 1× | Baseline |
| Parkinson (H-L) | ~5× | High-low only |
| Garman-Klass | ~7× | Full OHLC |
| Yang-Zhang | ~8–14× | Best overall |
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0034-p000

~~~~~~markdown
### Realized Volatility (Close-to-Close)

[[ML4T_A3_0001]]
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
### Range-Based Estimators

Range-based estimators use OHLC data for much higher efficiency than
close-to-close. Key formulas:

**Parkinson (1980)** uses the high-low range only:

[[ML4T_A3_0001]]

**Garman-Klass (1980)** adds open-close information:

[[ML4T_A3_0002]]

**Note**: ATR (Average True Range) measures price *range* in dollar terms,
not *volatility* in return terms. ATR is useful for stop placement and
normalization but is not a volatility estimator.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0037-p000

~~~~~~markdown
The four estimators and what each buys. The efficiency column holds the published
asymptotic variance ratio against the close-to-close estimator, derived in each paper
under driftless geometric Brownian motion with no overnight gap. Nothing in this
notebook measures these; they are the reason to reach for a range estimator, and the
figures below are where you see what the assumption costs on real data. The legend of
the overlaid figure reads these same values, so the table and the chart cannot disagree.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0042-p000

~~~~~~markdown
The four panels below share one vertical range. Plotly's [[ML4T_A3_0001]] ties panels
within a row and not across rows, so without an explicit range the top and bottom rows
rescale independently and the estimator with the smallest spread is drawn as tall as the
one with the largest - which is the comparison this figure exists to make.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0044-p000

~~~~~~markdown
**Interpretation**: on one scale the ordering is legible, and it is not a single
ordering. Close-to-close reaches the highest peak and is the most jagged of the four,
but it is not the highest line most of the time: the counts printed below say which
estimator sits on top day by day, and Yang-Zhang holds that position on the majority of
days in this window. Parkinson and Garman-Klass are never the highest and are usually
the lowest.

The smoothness has one cause and the level has another, and it is worth keeping them
apart. Range estimators are smoother because a day's high and low carry more
information about that day's variation than its two endpoints do, which is what the
efficiency column claims. They read lower for a different reason, developed against
the next figure.

This panel covers only the last two years. The overlaid figure below runs the full
history, where a much larger volatility event separates the estimators far more than
this window can.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0046-p000

~~~~~~markdown
### Four OHLC Estimators Overlaid

Overlaying all four estimators on a single panel makes their level and timing
differences directly comparable. Line styles vary alongside color so the series
stay distinct in grayscale.
~~~~~~

<<<ML4T-ZH-BEGIN:c0046-p000>>>
<<<ML4T-ZH-END:c0046-p000>>>

### c0048-p000

~~~~~~markdown
Why the range estimators read low. Parkinson and Garman-Klass read the high, the low,
the open and the close of one session, so every price they touch is inside trading
hours: the jump from the previous close to this open is not in their inputs. They are
therefore estimating the volatility of the within-session return, while close-to-close
estimates the volatility of the whole daily return. The reference row below is that
within-session return volatility, computed directly and divided by the same denominator
as the estimators, so the comparison is against a measured quantity rather than an
assumption.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
Parkinson and Garman-Klass land on the within-session reference, not below
close-to-close by some amount of noise. That is the whole of the level difference: they
answer a different question, and they answer it accurately. Yang-Zhang sits at
close-to-close instead, because it carries an explicit overnight term alongside its range
terms, which is why it stays with close-to-close through the peak while the other two
fall away.

The separation is therefore not a question of efficiency, and the distinction is worth
holding on to: efficiency says how much data an estimator needs to reach a given
precision, and it says nothing about what the estimator is precise about. A more
efficient estimator of the wrong quantity is still an estimator of the wrong quantity.

Which one is right follows from the return being modelled. Reach for Parkinson or
Garman-Klass when the question is about the session itself, such as intraday range or
execution risk inside the day. When the position is held overnight and the daily
close-to-close return is what is being scaled or sized against, their level is the wrong
denominator by the margin in the table above, and the choice is close-to-close for
simplicity or Yang-Zhang for the same quantity with less noise.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
### Volatility-of-Volatility (Vol-of-Vol)

Second moment of volatility, which detects unstable regimes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>
