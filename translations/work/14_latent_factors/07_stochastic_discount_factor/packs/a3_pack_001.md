# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：14_latent_factors/07_stochastic_discount_factor.ipynb；A3 Pack 001；單元 14 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Factor → 因子
- Portfolio → 投資組合
- Deep learning → 深度學習
- Label → 標籤
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0000-p000

~~~~~~markdown
# Adversarial Stochastic Discount Factors

**Docker image**: [[ML4T_A3_0001]]

**Chapter 14: Latent Factor Models**

Chen, Pelger, and Zhu learn a stochastic discount factor (SDF) by making a
portfolio-weight network compete with an adversarial moment network. This
notebook implements a daily educational adaptation of that design:
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p000>>>
<<<ML4T-ZH-END:c0000-p000>>>

### c0000-p001

~~~~~~markdown

[[ML4T_A3_0001]]

Information through close [[ML4T_A3_0002]] determines weights and instruments; the next
trading day's excess return realizes the factor. A separate beta network
estimates [[ML4T_A3_0003]], the paper's asset-level predictive head.
This SDF is the chapter's exception: it does not expose a swappable Stage 2
factor-premium forecaster.

**Learning objectives**

- align characteristics and macro state at [[ML4T_A3_0004]] with excess returns at [[ML4T_A3_0005]];
- implement the unconditional, adversarial, and conditional training phases;
- separate validation-selected SDF training from a once-only test evaluation;
- distinguish factor Sharpe and pricing errors from asset-level rank IC; and
- interpret beta-network predictions without confusing them with SDF weights.

**Evaluation contract**: the universe, return clipping, macro normalization,
and model checkpoints use training or validation data only. One return date is
embargoed at each boundary for the one-trading-day label. Test metrics are
computed only after the SDF and beta checkpoints are frozen.

**Data limitation**: this is not a reproduction of the paper's monthly CRSP
panel. It uses a training-defined 200-stock daily universe and a small set of
market-observed FRED series. FRED values come from the current snapshot, not a
vintage database; every series is delayed by one calendar day, and revised
lower-frequency releases are excluded.

**Attribution**: Chen, Pelger, and Zhu (2024), "Deep Learning in Asset
Pricing," *Management Science* 70(2), 714-750. See the
[paper]([[ML4T_A3_0006]]) and the
[authors' empirical page]([[ML4T_A3_0007]]).

**Prerequisite**: [[[ML4T_A3_0008]]](06_conditional_autoencoder.ipynb)

**Book reference**: Section 14.7 (The stochastic discount factor and the
supervised autoencoder models)
~~~~~~

<<<ML4T-ZH-BEGIN:c0000-p001>>>
<<<ML4T-ZH-END:c0000-p001>>>

### c0001-p000

~~~~~~markdown
## 1. Setup
~~~~~~

<<<ML4T-ZH-BEGIN:c0001-p000>>>
<<<ML4T-ZH-END:c0001-p000>>>

### c0005-p000

~~~~~~markdown
## 2. Point-in-time panel

Split dates are fixed from the equity calendar before any universe or model
decision. The boundary return date is omitted at each split, providing a
one-period embargo for the next-day label.
~~~~~~

<<<ML4T-ZH-BEGIN:c0005-p000>>>
<<<ML4T-ZH-END:c0005-p000>>>

### c0007-p000

~~~~~~markdown
The universe uses average dollar volume observed strictly before the first
boundary. This avoids using future trading activity to decide which stocks
appear in the historical training panel.
~~~~~~

<<<ML4T-ZH-BEGIN:c0007-p000>>>
<<<ML4T-ZH-END:c0007-p000>>>

### c0009-p000

~~~~~~markdown
Eight trailing characteristics use information available at the decision
close. Each is ranked within that date and mapped to [[ML4T_A3_0001]], matching
the paper's robust cross-sectional normalization idea without fitting a
full-sample scaler.
~~~~~~

<<<ML4T-ZH-BEGIN:c0009-p000>>>
<<<ML4T-ZH-END:c0009-p000>>>

### c0012-p000

~~~~~~markdown
A global trading-date map pairs decision date [[ML4T_A3_0001]] with return date [[ML4T_A3_0002]].
Joining again on [[ML4T_A3_0003]] drops a stock-specific gap instead of carrying a
stale characteristic into a later return.
~~~~~~

<<<ML4T-ZH-BEGIN:c0012-p000>>>
<<<ML4T-ZH-END:c0012-p000>>>

### c0014-p000

~~~~~~markdown
The macro state uses only daily market series. Forward fill operates in
source-time order, then every observation receives a one-calendar-day
availability delay. No backward fill is used. The lagged federal funds rate
supplies a simple daily risk-free proxy for excess returns.
~~~~~~

<<<ML4T-ZH-BEGIN:c0014-p000>>>
<<<ML4T-ZH-END:c0014-p000>>>

### c0016-p000

~~~~~~markdown
Macro means and scales, and the return clipping thresholds, are learned from
training rows only. Date-local coverage filtering removes thin early
cross-sections without consulting later outcomes.
~~~~~~

<<<ML4T-ZH-BEGIN:c0016-p000>>>
<<<ML4T-ZH-END:c0016-p000>>>

### c0019-p000

~~~~~~markdown
Dense tensors retain a Boolean observation mask. Missing asset-days are zero
only after the mask is constructed, so zeros cannot be mistaken for observed
returns in losses or metrics.
~~~~~~

<<<ML4T-ZH-BEGIN:c0019-p000>>>
<<<ML4T-ZH-END:c0019-p000>>>

### c0021-p000

~~~~~~markdown
The pivot helper preserves the training-defined symbol order for every split.
~~~~~~

<<<ML4T-ZH-BEGIN:c0021-p000>>>
<<<ML4T-ZH-END:c0021-p000>>>

### c0023-p000

~~~~~~markdown
Boundary dates are excluded. Validation and test therefore begin after a
one-return-date embargo, equal to the one-period label horizon.
~~~~~~

<<<ML4T-ZH-BEGIN:c0023-p000>>>
<<<ML4T-ZH-END:c0023-p000>>>

### c0026-p000

~~~~~~markdown
## 3. Adversarial networks

The SDF network combines an LSTM macro state with each asset's ranked
characteristics. A bounded output and per-date gross normalization prevent a
few observations from creating an unstable factor while retaining both long
and short weights.
~~~~~~

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000

~~~~~~markdown
The adversary has its own macro state and emits bounded test instruments. It
searches for conditional portfolios with large pricing errors.
~~~~~~

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>
