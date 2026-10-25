# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/03_structural_cross_instrument_features.ipynb；A3 Pack 003；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵

## 待翻譯英文單元

### c0049-p000

~~~~~~markdown
## Visualize Options Features
~~~~~~

<<<ML4T-ZH-BEGIN:c0049-p000>>>
<<<ML4T-ZH-END:c0049-p000>>>

### c0052-p000

~~~~~~markdown
**Interpretation**:
- ATM IV spikes during market stress (the COVID crash, for one), which makes it a state variable
- Positive risk reversal indicates elevated put demand (crash fear)
- Term slope > 1 = inverted term structure (near-term event risk)
- VRP > 0 is normal; extreme VRP signals attractive vol-selling opportunities

**OI-based features** (dealer gamma, positioning) are conceptually valuable
but require granular open interest data not available in this dataset. The
aggregate Greeks approach in [[ML4T_A3_0001]]
provides a workable proxy.

**Surface stability**: If the quote selection policy (delta convention,
interpolation method, maturity mapping) changes mid-backtest, all
options-derived features become contaminated. Version your construction
choices alongside the features.
~~~~~~

<<<ML4T-ZH-BEGIN:c0052-p000>>>
<<<ML4T-ZH-END:c0052-p000>>>

### c0053-p000

~~~~~~markdown
---

# Summary

## Feature Families

| Family | Key Features | Data Required | Primary Role |
|--------|-------------|---------------|-------------|
| **Carry** | Roll yield, funding rate | Multi-tenor futures, perps | Signal |
| **Term Structure** | Slope, curvature | 3+ tenors | Signal/state |
| **Cross-Asset** | Beta, lead-lag, relative value | Multi-asset prices | Signal |
| **Options-Implied** | ATM IV, skew, VRP, term slope | Options chain | State |

## Implementation Rules

1. **Carry requires paired tenors**: Missing deferred contracts produce NaN carry
2. **Beta window matters**: 21d for fast regime, 63d for stable estimate
3. **Lead-lag can be spurious**: Validate that leads aren't staleness artifacts
4. **Options features need surface policy**: Version construction choices
5. **VRP is usually positive**: Negative VRP is extreme and informative

## Practical Takeaways

1. **Carry varies by asset class**: in the snapshot above, CL trades closer to
   backwardation than GC does, which the printed shares either bear out on this sample
   or do not; read them rather than this sentence, and read them as one sample's
   behaviour rather than as the asset-class rule the received explanations describe
2. **Residual momentum isolates idiosyncratic return**: subtracting
   [[ML4T_A3_0001]] removes the market component from each ETF's return.
   Whether residual momentum has higher IC than raw momentum is evaluated in
   the [[ML4T_A3_0002]] case study; this notebook demonstrates only the construction
3. **Options-implied features are state, not signal**: use them to condition
   faster signals
4. **Surface stability is non-negotiable**: changing quote conventions
   mid-backtest invalidates all options features

## Next Notebooks
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0053-p001

~~~~~~markdown

- [[ML4T_A3_0001]]: fundamentals, macro, calendar encodings
- [[ML4T_A3_0002]]: full 30-product futures pipeline
- [[ML4T_A3_0003]]: full equity and options pipeline
- [[ML4T_A3_0004]]: options straddle strategy pipeline
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p001>>>
<<<ML4T-ZH-END:c0053-p001>>>
