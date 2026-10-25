# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：04_fundamental_alternative_data/01_academic_characteristics.ipynb；A3 Pack 003；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Portfolio → 投資組合
- Time series → 時間序列
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0032-p000

~~~~~~markdown
---

## Section 5: The return distribution

The characteristics were ranked; [[ML4T_A3_0001]] was not. It stays in its original scale because a
prediction of it has to be readable as a return, which is what makes the loss function of a
model fitted on this panel comparable to an economic quantity.

Monthly equity returns have far heavier tails than a normal distribution, and the tails grow
heavier in the later decades of this sample. The table gives the moments; the figure gives
the shape.
~~~~~~

<<<ML4T-ZH-BEGIN:c0032-p000>>>
<<<ML4T-ZH-END:c0032-p000>>>

### c0034-p000

~~~~~~markdown
The histogram below is drawn as a density rather than a count, because the three splits hold
very different numbers of rows and raw counts would compare their sizes instead of their
shapes. The horizontal axis is clipped at plus and minus sixty percent: the largest returns in
the panel run to many multiples of that, and leaving them in the frame compresses every bar
into a single spike. The [[ML4T_A3_0001]] column in the table above is where the full range is reported.
~~~~~~

<<<ML4T-ZH-BEGIN:c0034-p000>>>
<<<ML4T-ZH-END:c0034-p000>>>

### c0036-p000

~~~~~~markdown
---

## Section 6: What this panel supports

The anonymization decides which questions this data can answer. Inside a split, an identifier
follows one firm from month to month, so anything that needs a firm's own history is
available: a fixed effect, a per-firm time series, or a portfolio held and rebalanced across
months. That last one is what [[ML4T_A3_0001]] does - it
ranks each month's cross-section on the model's prediction, weights the top and bottom names,
and compounds the realized excess returns those weights earned. A return-based backtest needs
weights and realized returns, and both are here.

Across a split boundary the identifiers are not comparable. The archive publishes no mapping
between the three arrays, so a position cannot be carried from the training years into the
test years and no strategy can be simulated end to end over the full fifty years.

What is missing is price. Without one there is no market value to weight a portfolio by in
currency, no spread or depth to charge a trade against, and no way to say what a position
would have cost to enter. The case studies that ship prices are where execution and cost are
measured; what this panel supports is prediction, and the frictionless portfolio return that
a prediction implies.

Used within those limits, the panel is the cleanest available benchmark for comparing model
families on identical data: the same 46 inputs, the same target, and the same date-ordered
split for every model, so a difference in measured accuracy is a difference between the
models rather than between their datasets.
~~~~~~

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0037-p000

~~~~~~markdown
## Key Takeaways

1. Cross-sectional rank normalization puts every characteristic on the same bounded scale each
   month, which removes the units and caps the influence of any single extreme observation.
   It also discards the levels, so nothing computed from this panel can speak to how expensive
   the market was in a given year.
2. Characteristics arrive in correlated blocks, because several of them are built from the
   same accounting inputs. Fitting an unregularized linear model on all 46 splits coefficients
   arbitrarily within a block; regularization and tree ensembles are the standard answers, and
   Chapters 11 and 12 apply both to this panel.
3. Single-characteristic information coefficients are small in absolute terms. That is the
   normal state of a cross-sectional equity signal and it is why the case study fits models on
   all 46 jointly rather than trading any one of them.
4. Averaging monthly ICs and testing the average as if the months were independent overstates
   significance, because a characteristic stays in favour for stretches. Report the
   Newey-West-corrected statistic, and check how far it moved before drawing a conclusion from
   either.
5. Evaluating characteristics on the training split alone is not a formality. Any ranking
   computed over the whole history has already read the test years, and a model built on that
   ranking inherits the leak.

**Known limitations**: the panel carries no prices and no company names; identifiers are not
comparable across the three splits; and the requirement that all 46 characteristics be present
tilts the universe away from small caps, so coverage is not a random sample of CRSP.

**Next**: [[ML4T_A3_0001]] fits linear, tree and neural models to this
panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0037-p000>>>
<<<ML4T-ZH-END:c0037-p000>>>
