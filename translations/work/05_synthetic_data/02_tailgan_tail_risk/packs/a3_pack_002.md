# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：05_synthetic_data/02_tailgan_tail_risk.ipynb；A3 Pack 002；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Correlation → 相關性

## 待翻譯英文單元

### c0031-p000

~~~~~~markdown
## 11. Create DataLoader
~~~~~~

<<<ML4T-ZH-BEGIN:c0031-p000>>>
<<<ML4T-ZH-END:c0031-p000>>>

### c0033-p000

~~~~~~markdown
## 12. Training Loop
~~~~~~

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0038-p000

~~~~~~markdown
## 13. Generate Synthetic Scenarios
~~~~~~

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0040-p000

~~~~~~markdown
## 14. Evaluation

### Fidelity: visual comparison with PCA and t-SNE

We project both real and synthetic scenarios into 2D to assess whether the
generator covers the same regions of the data manifold.
~~~~~~

<<<ML4T-ZH-BEGIN:c0040-p000>>>
<<<ML4T-ZH-END:c0040-p000>>>

### c0042-p000

~~~~~~markdown
**Interpretation**: the synthetic cloud sits *inside* the real one rather than on
top of it. In both projections the generator's scenarios concentrate near the
centre while the real scenarios spread well beyond them, so the generator is
under-dispersed in this averaged view and does not reach the regimes that produce
the extreme real points.

Read this figure with its own caveat, though: [[ML4T_A3_0001]] averages each
scenario across assets before projecting, which discards the cross-asset structure
and shrinks whatever it plots. It is a coarse view of coverage, not the quantity
Tail-GAN optimises. The tail-risk metrics below operate on portfolio PnL and are
the ones that speak to the model's actual objective - which is why a generator that
looks under-dispersed here can still overstate tail severity there.
~~~~~~

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>

### c0043-p000

~~~~~~markdown
### Tail risk metrics

Both real and synthetic scenarios are in scaled space, so relative error
comparison is valid. We also report unscaled VaR/ES for interpretability.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0045-p000

~~~~~~markdown
Compute empirical Value at Risk and Expected Shortfall from portfolio PnL.
~~~~~~

<<<ML4T-ZH-BEGIN:c0045-p000>>>
<<<ML4T-ZH-END:c0045-p000>>>

### c0048-p000

~~~~~~markdown
The two errors above compare *averages* across strategies, so a strategy the
generator overstates can be cancelled by one it understates. The aggregate is the
number the book quotes, but it is not evidence that any individual strategy is
matched. Measure the per-strategy agreement separately before reading the scatter
plots below.
~~~~~~

<<<ML4T-ZH-BEGIN:c0048-p000>>>
<<<ML4T-ZH-END:c0048-p000>>>

### c0050-p000

~~~~~~markdown
**Interpretation**: both synthetic means printed above are more negative than
their real counterparts, so the generator captures the broad shape of the tail
but overstates its severity - reasonable for a compact pedagogical model, not
production-grade. Because the scaling maps the largest absolute return just
inside the clamp, the full empirical tail is reachable, so the residual error is
a genuine distributional mismatch and not the clamp truncating the tail. The two
relative errors are close because Expected Shortfall is the conditional mean
below VaR, so a displaced VaR moves ES with it. The scatter plots below show
whether the gap is systematic across strategies or driven by a few outliers.
~~~~~~

<<<ML4T-ZH-BEGIN:c0050-p000>>>
<<<ML4T-ZH-END:c0050-p000>>>

### c0051-p000

~~~~~~markdown
## 15. Visualization
~~~~~~

<<<ML4T-ZH-BEGIN:c0051-p000>>>
<<<ML4T-ZH-END:c0051-p000>>>

### c0053-p000

~~~~~~markdown
**Interpretation**: both losses plateau well before the last epoch. In an adversarial
game a plateau does not mean either network has stopped changing - the two are scored
against each other, so the weights and the generated distribution can keep moving
while the losses stay flat. Establishing that would take comparing parameters or
checkpoint outputs, which this notebook does not do.

What the plateau cannot tell you, the per-strategy numbers above do, and they are the
ones to read. The median per-strategy relative error is several times the aggregate
error, so individual strategies are matched far worse than the headline suggests. The
share of strategies the model overstates is close to half, which is what makes the two
consistent: the aggregate is small because overstated and understated strategies
cancel in the average, not because the strategies themselves are close.

The correlations printed alongside are near zero. Read them for what they are - Pearson
correlation measures linear association in this sample, so a value near zero says the
synthetic tail risk does not rise and fall linearly with the real one across
strategies. It is not proof that no relationship of any shape exists; establishing that
would need a rank or dependence measure this notebook does not compute. The claim the
evidence supports is about agreement, and the median error is what carries it. The
scatter panels show the same thing: points spread on both sides of the 45-degree line
rather than tracking it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p000>>>
<<<ML4T-ZH-END:c0053-p000>>>

### c0053-p001

~~~~~~markdown

This is the notebook's most transferable lesson, and it is not specific to Tail-GAN.
Accuracy in an aggregate computed across units does not establish accuracy for any
single unit. If the intended use is per-strategy - sizing one book, stressing one desk -
the aggregate is the wrong number to have been reassured by.
~~~~~~

<<<ML4T-ZH-BEGIN:c0053-p001>>>
<<<ML4T-ZH-END:c0053-p001>>>

### c0054-p000

~~~~~~markdown
## 16. Results Summary
~~~~~~

<<<ML4T-ZH-BEGIN:c0054-p000>>>
<<<ML4T-ZH-END:c0054-p000>>>

### c0056-p000

~~~~~~markdown
## Key Takeaways

1. **Differentiable sorting**: Neural sort enables gradient flow through VaR/ES
   computation, making tail risk metrics trainable loss components
2. **Constraint projection**: Hard projection onto [[ML4T_A3_0001]] ensures
   the discriminator's VaR/ES estimates remain economically consistent
3. **Tail risk preservation**: training on a tail-risk objective gets the
   *aggregate* VaR and ES into the right neighbourhood. Tail-GAN optimises those
   metrics directly; a general-purpose distributional objective would reach them
   only as a by-product of matching the joint distribution, and does not
   prioritise their accuracy. This notebook trains no such baseline, so it shows
   what the targeted objective achieves, not that the alternative fails
4. **An aggregate can hide the disagreement it averages**: the mean VaR and ES
   across strategies agree far better than any individual strategy does, because
   strategies the generator overstates cancel strategies it understates. Read the
   per-strategy correlation and median error before quoting the headline number
5. **Scaling matters**: The generator's clamped [-1, 1] output requires
   careful input scaling to preserve tail structure without saturation

**Next**: See [[ML4T_A3_0002]] for a signature-based approach that
eliminates the adversarial discriminator entirely.

**Book**: Section 5.5 compares Tail-GAN's targeted risk approach with
general-purpose distributional matching.
~~~~~~

<<<ML4T-ZH-BEGIN:c0056-p000>>>
<<<ML4T-ZH-END:c0056-p000>>>
