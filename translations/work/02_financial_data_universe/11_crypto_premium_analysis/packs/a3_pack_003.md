# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：02_financial_data_universe/11_crypto_premium_analysis.ipynb；A3 Pack 003；單元 5 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Volatility → 波動率
- Standard deviation → 標準差

## 待翻譯英文單元

### c0037-p000

~~~~~~markdown
One more count, and it needs labelling carefully. The share of settlements whose estimated
APY exceeds a chosen level and the share where the clamp binds are different quantities, and
the relation between them runs one way. Exceeding the threshold requires a binding clamp,
because funding without one is pinned at the interest rate and annualizes far below any
threshold worth setting. The clamp binding does not require exceeding the threshold: it binds
whenever the premium sits more than the clamp half-width from the interest rate, which is a
routine condition, and the resulting APY is usually nowhere near the threshold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>

### c0039-p000

~~~~~~markdown
---

## Section 6: Loading this data elsewhere

Everything above went through [[ML4T_A3_0001]], which is the loader the rest of the book
uses. The [[ML4T_A3_0002]] package also exposes [[ML4T_A3_0003]], a class-based API over the
same files, and the case study reaches for it where it needs the download path as well as the
read path.

There is nothing to demonstrate here that the sections above have not already shown, so this
section states which entry point to use rather than importing one to print that it exists.
[[ML4T_A3_0004]] for reading a panel, [[ML4T_A3_0005]] when you also need to fetch.
~~~~~~

<<<ML4T-ZH-BEGIN:c0039-p000>>>
<<<ML4T-ZH-END:c0039-p000>>>

### c0040-p000

~~~~~~markdown
---

## Key Takeaways

1. **The premium index is not the perpetual-spot difference, and the gap matters.** Binance
   computes it from the impact bid and ask against the price index, with a numerator that is
   zero whenever the index sits between them. That dead zone is why a large share of the
   column is exactly zero, why the share rises as liquidity falls, and why those zeros are
   measurements rather than gaps. [[ML4T_A3_0001]] measures all three.

2. **The funding clamp is on the difference, not on the premium.** Binance settles
   [[ML4T_A3_0002]], so whenever the premium sits within the clamp of
   the interest rate the whole expression reduces to the interest rate exactly.
   Funding then has a dead zone of its own, and better than a third of realized settlements
   on the most liquid contract sit precisely on it. Clamping the premium instead removes that
   point mass and reproduces the exchange's own rate several times less accurately - both
   versions are computed above and scored against six years of published rates.

3. **The clamp does not cap the funding rate.** Outside the dead zone it saturates and
   funding tracks the premium with a fixed offset, so the rate is unbounded by that
   mechanism. Realized settlements run to many times the ceiling the clamp appears to imply,
   and the real cap is a separate per-contract limit that differs by an order of magnitude
   across this universe. Reading the clamp as a cap understates a funding strategy's tail
   badly, and most on the contracts where the tail is worst.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0040-p001

~~~~~~markdown

4. **Two different counts, one label.** The share of settlements whose APY exceeds a chosen
   threshold and the share where the clamp binds are different quantities, and the
   implication runs one way: exceeding the threshold requires a binding clamp, while the
   clamp binds routinely at premiums that move the APY hardly at all. Both are printed
   above, and they differ by tens of percentage points.

5. **The estimate is a proxy and says so.** Binance computes funding from a time-weighted
   average of the premium over the interval; this notebook has eight-hour bars and uses the
   close, which is the most accurate of the proxies available here and still not exact. Where
   the realized series exists, use it - the case study does.

6. **Premium volatility spans the universe by more than an order of magnitude**, and the
   dispersion is episodic rather than steady: the widest contracts earn their standard
   deviations in a handful of dislocations. Contract selection for a funding strategy is a
   choice about which tail to hold, and the per-symbol table above is where that choice is
   made.

### Implications for the funding-arbitrage case study
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p001>>>
<<<ML4T-ZH-END:c0040-p001>>>

### c0040-p002

~~~~~~markdown

- **Direction**: the mean premium is negative for every contract in this panel, and the mean
  realized funding rate is *positive* for nearly all of them. The transform is monotone - a
  larger premium never produces a smaller funding rate - but it does not preserve sign: it
  has a plateau at the interest rate covering every premium within the clamp of it, and the
  interest rate is positive. Whether that plateau is enough to carry the mean across zero
  depends on how much of the distribution sits below the plateau and how far, which is a
  question about this sample and not an implication. In this sample it does. Read direction
  off the realized funding column in the per-symbol table above, never off the premium's
  sign, and treat both as properties of this window rather than laws.
- **Regimes**: the rolling premium changes sign for long stretches, so a static threshold
  fires in one regime and never in the other. [[ML4T_A3_0001]] carries
  the regime-aware version.
- **Ties**: the premium's point mass at zero reaches a third of observations on the thinnest
  contracts, so any percentile or z-score feature built on this column is standardising a
  distribution with a large tie group.

**Next**: [[ML4T_A3_0002]] profiles the third 24/7-adjacent dataset —
G10 FX pairs at 4h cadence — completing the global market-data tour.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p002>>>
<<<ML4T-ZH-END:c0040-p002>>>
