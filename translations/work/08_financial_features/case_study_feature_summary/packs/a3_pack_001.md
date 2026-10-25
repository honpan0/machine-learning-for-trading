# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：08_financial_features/case_study_feature_summary.ipynb；A3 Pack 001；單元 9 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Volatility → 波動率

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Cross-Case-Study Feature Evaluation Summary

**Chapter 8: Feature Engineering**
**Section Reference**: 8.6 - Combining Features and Controlling Search
**Docker image**: [[ML4T_A3_0001]]

## Purpose

This notebook is the cross-case-study inventory and presentation layer: it
aggregates engineered features and the strongest registry IC per case study across
all 9 asset classes. It surfaces:
- **Feature counts and families**: how large each case study's feature space is
- **Best IC per case study** (from the model registry): how predictive the
  strongest family is, by asset class
- **Cross-asset patterns**: which feature families generalize vs which are asset-specific

The HAC-adjusted significance and BH-FDR survival counts themselves are computed
upstream, in each case study's [[ML4T_A3_0002]]; this notebook reads and
presents their results rather than recomputing them.

## Learning Objectives

1. Compare feature predictability across diverse asset classes
2. Read off each case study's best registry IC and feature-space size
3. Identify feature families that generalize vs those that are asset-specific
4. Understand how universe size (breadth) interacts with IC magnitude

## Prerequisites

- Case study feature notebooks must have produced [[ML4T_A3_0003]]
- A case study whose [[ML4T_A3_0004]] directory holds no panel yet shows as "awaiting".
  A checkout that is not wired to a case study at all cannot tell that apart from
  an empty one, so it refuses rather than reporting a range over what it could see.
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0003-p000

~~~~~~markdown
## Load Feature Data

Scan all case study [[ML4T_A3_0001]] directories for the [[ML4T_A3_0002]]
produced by the feature engineering notebooks. We introspect schemas to count
features and compare across case studies.
~~~~~~

<<<ML4T-ZH-BEGIN:c0003-p000>>>
<<<ML4T-ZH-END:c0003-p000>>>

### c0006-p000

~~~~~~markdown
## Feature Inventory Summary

How many features and feature families does each case study engineer, and what
are its largest families? (The multiple-testing survival counts are produced
upstream in each case study's [[ML4T_A3_0001]]; here we inventory the
feature space.)
~~~~~~

<<<ML4T-ZH-BEGIN:c0006-p000>>>
<<<ML4T-ZH-END:c0006-p000>>>

### c0008-p000

~~~~~~markdown
## Feature Count Comparison

How does feature set size vary across case studies? More features provide
a richer signal space but also increase the multiple testing burden.
~~~~~~

<<<ML4T-ZH-BEGIN:c0008-p000>>>
<<<ML4T-ZH-END:c0008-p000>>>

### c0010-p000

~~~~~~markdown
## Feature Family Distribution

We group features into *families* by their name prefix (the token before the
first underscore: [[ML4T_A3_0001]] and [[ML4T_A3_0002]] both count as [[ML4T_A3_0003]]). This is a coarse,
mechanical lens - across nine very different markets it yields on the order of a
hundred prefixes, but that overstates the number of distinct ideas. Two effects
inflate it: each asset class contributes genuinely specialized measures that
appear nowhere else (option [[ML4T_A3_0004]]/[[ML4T_A3_0005]]/[[ML4T_A3_0006]], microstructure [[ML4T_A3_0007]]/[[ML4T_A3_0008]],
crypto [[ML4T_A3_0009]]/[[ML4T_A3_0010]], futures term-structure), and inconsistent naming
splits a few shared concepts ([[ML4T_A3_0011]] vs [[ML4T_A3_0012]] for the same Bollinger %B;
[[ML4T_A3_0013]]/[[ML4T_A3_0014]]/[[ML4T_A3_0015]] all momentum windows). Read the y-axis as prefixes, not as a
taxonomy.

What the figure *is* good for is the cross-asset pattern. A heatmap is the right
lens for the prefixes that *recur* - momentum, volatility, and returns show up
almost everywhere - so we keep those (used in two or more case studies, broadest
on top) in the heatmap, and collapse the long tail of single-market prefixes
into a companion bar counting how many specialized measures each asset class
adds.
~~~~~~

<<<ML4T-ZH-BEGIN:c0010-p000>>>
<<<ML4T-ZH-END:c0010-p000>>>

### c0012-p000

~~~~~~markdown
## Representative Features Across Case Studies

A sample of each case study's feature space, the first few feature names in schema
order, to illustrate the engineered inputs. This is an inventory view,
not an IC ranking (per-feature IC is computed in each case study's evaluation
notebook).
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
## Breadth vs IC: The Fundamental Law Perspective

The Fundamental Law of Active Management says:

[[ML4T_A3_0001]]

where [[ML4T_A3_0002]] is the number of independent bets, roughly the universe size. The cell below
works the law through two contrasting cases so the arithmetic is visible rather than
asserted: a wide universe with a small IC against a narrow one with an IC three times
larger. Read which of the two reaches the higher information ratio, and by how much.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0018-p000

~~~~~~markdown
Read the two encodings in that figure separately, because they say different things.

Vertical position is the per-bet information coefficient, and it does not rise with
universe size. The highest coefficient in the panel comes from a case study of about a
hundred instruments, and two of the widest universes sit well below it. Nothing here
supports "more instruments, better signal".

Marker area is the estimated information ratio, and the largest circles are at the
right-hand end of the axis. That is the law at the top of this section doing its work:
an information ratio is a coefficient multiplied by the square root of breadth, so a
universe a hundred times wider turns a coefficient ten times smaller into the same
ratio. The wide-universe case studies reach competitive ratios on individually weaker
signals.

Two cautions about reading this as a result. The estimated ratio is the law applied to
the plotted coefficient rather than a measured backtest quantity, so the relationship
between area and position is partly arithmetic rather than empirical. And breadth in the
law means *independent* bets; a universe of three thousand equities that move together
supplies far fewer than three thousand, which is the correction the law is most often
used without.
~~~~~~

<<<ML4T-ZH-BEGIN:c0018-p000>>>
<<<ML4T-ZH-END:c0018-p000>>>

### c0019-p000

~~~~~~markdown
## What the Panels Above Show

The notebook aggregates whatever is present in each case study's
[[ML4T_A3_0001]] and the model registry. The substantive
findings, meaning which feature families have predictive content for which label
and horizon, how many features survive HAC + BH-FDR, and how breadth
and how breadth interacts with IC magnitude, are produced by the per-case-study evaluation
notebooks ([[ML4T_A3_0002]] in each case study). This summary
notebook is a cross-case-study inventory and presentation layer; it does
not itself compute IC or run multiple-testing correction.

**Next**: See [[ML4T_A3_0003]] for the
temporal/model-based feature companion view.
**Book**: Chapter 8.6 discusses combining features and controlling the
search space to avoid data mining.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>
