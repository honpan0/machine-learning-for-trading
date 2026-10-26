# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/etfs/11a_pca.ipynb；A3 Pack 003；單元 7 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Factor returns → 因子報酬率
- Feature → 特徵
- Label → 標籤
- Cross-sectional → 橫斷面
- Correlation → 相關性
- Covariance → 共變異數

## 待翻譯英文單元

### c0021-p000

~~~~~~markdown
### The prediction does not move within a fold

Read section 3 step 3 again: a fund's predicted return is its loadings times the training-window
factor premia. Both are fitted once per fold and neither depends on the validation date, so every
fund carries one number for the whole of a fold's validation window and the cross-sectional
ranking is fixed until the next fold refits it.

That is a reading of how the forecast is assembled, and it is worth checking against what was
actually published rather than left as an inference. The cell below counts the distinct predicted
values each fund holds within each fold, and raises if any of them is more than one. If a later
version of the estimator gains a time-varying term, this is what tells you, and everything the
rest of this section says about a static ranking stops holding at the same moment.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
### How much the ranking changes between folds

A static ranking within a fold leaves one thing to look at: how much it moves when the next fold
refits it on a training window extended by one more block of history. If consecutive folds
produce nearly the same ordering, the model is saying the same thing about these funds throughout
the validation period and its IC is close to one long bet on a fixed ordering. If the ordering
turns over, the additional history is changing which directions dominate the return panel.

The measure is the rank correlation between the predicted cross-sections of consecutive folds,
over the funds both folds predicted. It is a property of the fitted model rather than of its
accuracy: a high value is not good news and a low one is not bad news, and neither is evidence
about the forecast being right.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0026-p000

~~~~~~markdown
### The eight folds behind each average

[[ML4T_A3_0001]] above is the equal-weight mean of eight per-fold correlations, and section 5 argues
from how those eight are spread rather than from where they average. A run that reuses a
published fit prints nothing while fitting, so the fold rows are read back from the registry
here - the same rows the mean was taken over - and every per-fold number section 5 quotes comes
from this table.

[[ML4T_A3_0002]] is how many funds the fold **scored**, which is not the number it fitted on: the
training window reaches further back than the validation block and carries funds that have since
left the panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
## 5. What to notice

**The forward-return panel's own covariance structure does not rank these funds.** On the primary
label the mean validation IC is **-0.033**, and on the five-day variant **+0.010**. Neither is
evidence of skill, and the negative one is not an inverted signal either: the eight fold ICs
behind it run -0.076, -0.025, -0.003, +0.116, -0.104, +0.065, -0.182, -0.051, so the sign changes
four times and the spread across folds is several times the size of the average. That is the
shape of a quantity centred on nothing.

**The ordering itself reverses when the model is refitted.** The rank correlation between
consecutive folds' predicted cross-sections is negative on two of the seven pairs (-0.45 and
-0.60) and above +0.5 on two others. A fund near the top of one fold's ranking is as likely to
be near the bottom of the next as to stay where it was. The sign ambiguity of a principal
component does not explain this - the premium is averaged from the same fitted factor returns
the loadings came from, so a flipped component flips both and cancels - which leaves the
ordering genuinely turning over as the training window rolls forward.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0028-p001

~~~~~~markdown

**The daily IC has far fewer independent observations than [[ML4T_A3_0001]] suggests.** The check
above established that each fund holds one predicted value per fold, so across 1,995 validation
dates this model expresses **eight** rankings, not 1,995. Every date inside a fold is scoring the
same ordering against a different day of returns. [[ML4T_A3_0002]] would therefore
understate the uncertainty on [[ML4T_A3_0003]] by a wide margin, and that is why no such interval is
computed here. It is a property of any model whose forecast is constant within a fold, and it is
worth carrying into the notebooks that follow, where the forecast moves and the count means more.

**What this establishes for the rest of the family.** PCA is the member that reads none of the
71 feature columns, and it sets the bar the four conditioned members are measured against. That
bar is at zero. A conditioned member that ranks these funds materially better is being helped by
the conditioning rather than by the factor structure, which is the comparison
[[[ML4T_A3_0004]]](13_model_analysis.ipynb) is arranged to make with every family in front of
it.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p001>>>
<<<ML4T-ZH-END:c0028-p001>>>

### c0028-p002

~~~~~~markdown

**Known limitations.** The matrix decomposed is the label's forward returns, and those overlap:
consecutive rows of the 21-day column share twenty of their twenty-one days. Much of the
covariance structure PCA finds is therefore that overlap rather than same-day co-movement, and
this is not the object a daily-return covariance matrix would be. It is the same target every
conditioned member of the family decomposes, which is what keeps the comparison in
[[[ML4T_A3_0001]]](11c_conditional_autoencoder.ipynb) a comparison about
conditioning rather than about the target. [[ML4T_A3_0002]] is declared rather than chosen, and
nothing here tests whether a different count would order the cross-section better - that would be
a search, and a search over validation IC is what this notebook is arranged to avoid. The
cross-section narrows as the window rolls forward - the [[ML4T_A3_0003]] column above falls from 92
funds on the first fold to 77 on the last - so the eight fold ICs are not eight readings of the
same experiment. And every number here is measured on validation folds that have been read many
times over by the time a case study reaches this notebook.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p002>>>
<<<ML4T-ZH-END:c0028-p002>>>

### c0029-p000

~~~~~~markdown
**Next**: [[[ML4T_A3_0001]]](11b_ipca.ipynb) keeps the factor structure and drops the assumption that a
fund's exposure is a fixed number, letting the characteristics this notebook ignored set it
instead.
~~~~~~

<<<ML4T-ZH-BEGIN:c0029-p000>>>
<<<ML4T-ZH-END:c0029-p000>>>
