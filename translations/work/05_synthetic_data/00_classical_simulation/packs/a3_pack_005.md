# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/00_classical_simulation.ipynb；A3 Pack 005；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Clustering → 分群
- Volatility → 波動率

## 待翻譯英文單元

### c0086-p000

~~~~~~markdown
### Bootstrap Key Takeaways

1. **IID bootstrap** reproduces the marginal distribution — the same histogram,
   the same fat tails — and retains essentially none of the volatility
   clustering, which is what resampling one observation at a time implies.
2. **Block and stationary bootstrap** both retain roughly two thirds of SPY's
   squared-return dependence at a 22-day block length. Neither recovers all of
   it: dependence that spans a block boundary is destroyed whatever the block
   length, and lengthening blocks to keep more of it leaves fewer distinct
   blocks to resample.
3. **Random block lengths help, modestly.** The stationary bootstrap retains
   more than the moving block bootstrap in the majority of paired draws, but
   the two distributions overlap heavily, so the advantage shows up across
   replicates and is not something a single resample would establish.

For financial returns with volatility clustering, either block method is a
reasonable default and the choice between them matters less than the block
length.
~~~~~~

<<<ML4T-ZH-BEGIN:c0086-p000>>>
<<<ML4T-ZH-END:c0086-p000>>>

### c0087-p000

~~~~~~markdown
---
# Part 4: Model Comparison Summary

## What Each Method Captures

Fat tails and volatility clustering are separate properties and are measured
separately above: excess kurtosis across [[ML4T_A3_0001]] paths for the parametric
models, retained squared-return autocorrelation across
[[ML4T_A3_0002]] replicates for the resamplers. "Beyond history" asks
whether the method can emit a value larger than any it was given.

| Method | Excess kurtosis above Gaussian | Volatility clustering | Beyond history |
|--------|-------------------------------|-----------------------|----------------|
| GBM | No, by construction | None; this row is the null both columns are read against | Yes |
| Jump-Diffusion | Yes, the heaviest measured here | None; jumps arrive independently | Yes |
| Mean-Reversion | No | None; its dependence is negative autocorrelation in returns, not in squared returns | Yes |
| Heston | Yes, below GARCH | Yes, on most paths, from mean-reverting variance | Yes |
| GARCH | Yes, above Heston | Yes, on every path and the strongest measured | Yes |
| IID Bootstrap | Inherits the sample's | None retained | No |
| Block Bootstrap | Inherits the sample's | About two thirds retained | No |
| Stationary Bootstrap | Inherits the sample's | About two thirds retained, slightly more than fixed blocks | No |

## Key Takeaways
~~~~~~

<<<ML4T-ZH-BEGIN:c0087-p000>>>
<<<ML4T-ZH-END:c0087-p000>>>

### c0087-p001

~~~~~~markdown

1. **Parametric models** can emit values beyond anything in the historical
   sample, which is what makes them usable for stress scenarios, but every
   property they exhibit is one that was chosen or fitted.
2. **Bootstrap methods** reproduce the empirical marginal distribution, fat
   tails included, without any distributional assumption, and cannot produce a
   return larger than the largest one observed.
3. **Heston and GARCH capture both stylized facts; the jump model captures
   only one.** Measured against GBM as the null, jump-diffusion has the
   heaviest tails and no volatility clustering whatever, while Heston and
   GARCH clear the null on both properties, GARCH more strongly on each. On
   clustering, compared against SPY over equal-length windows, GARCH is not
   short of the empirical level at all — its median sits above SPY's. Matching
   one statistic is not matching the series, which is the argument for the
   validation protocol the rest of the chapter builds.
4. **Drift compensation** (jump-diffusion) and **full truncation** (Heston) are
   implementation details that change what is simulated, not stylistic choices;
   without the compensator the requested drift is not the realized drift, and
   without truncation the variance recursion can go negative.
5. **Fitting GARCH by maximum likelihood** replaces two chosen numbers with two
   estimated ones, which is a different claim from producing more realistic
   paths: persistence comes from the data, the level still has to be carried
   across explicitly, as the library comparison above shows.

**Next**: See [[[ML4T_A3_0001]]](01_timegan.ipynb) for the first learned generative model, which uses
adversarial training to capture temporal dynamics that classical models miss.
~~~~~~

<<<ML4T-ZH-BEGIN:c0087-p001>>>
<<<ML4T-ZH-END:c0087-p001>>>

### c0087-p002

~~~~~~markdown

**Book**: Chapter 5, Section 5.4 covers the generative model taxonomy and explains
why learned models complement (rather than replace) classical simulation.
~~~~~~

<<<ML4T-ZH-BEGIN:c0087-p002>>>
<<<ML4T-ZH-END:c0087-p002>>>
