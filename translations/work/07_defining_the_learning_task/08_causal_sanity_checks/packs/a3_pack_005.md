# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：07_defining_the_learning_task/08_causal_sanity_checks.ipynb；A3 Pack 005；單元 4 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Momentum → 動能
- Feature → 特徵
- Feature engineering → 特徵工程
- Label → 標籤
- Cross-sectional → 橫斷面

## 待翻譯英文單元

### c0063-p000

~~~~~~markdown
**Interpretation**: 12-1 momentum earns REVISE or PROCEED - it carries timely
cross-sectional information (timing check) that does not predict unrelated
Treasury returns (shared-driver check). The regime heterogeneity check reveals
that the effect attenuates in high-VIX markets, an actionable finding that
motivates regime-conditional modeling in later chapters.

1-day reversal earns STOP - no signal at the 21-day horizon, no regime
drives a significant IC, and its IC is indistinguishable from the permutation
null. The framework correctly rejects a non-signal.

The contrast illustrates the triage value: without these checks, a researcher
might spend chapters modeling reversal on the wrong horizon. The scan in
Section 4 and the mechanism checks here redirect effort toward features with
genuine cross-sectional predictive power.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0064-p000

~~~~~~markdown
## Event-Time Alignment (Concept Only)

This fourth check from Section 7.5 requires event-specific features (e.g.,
earnings surprises, FOMC announcements). Neither momentum nor reversal is
event-driven, so the check does not apply here. Chapter 8 demonstrates
event-time alignment with fundamental features, and Chapter 9 with regime
transitions.

The concept: for event-motivated features, IC should concentrate in the window
where the mechanism predicts an effect. Red flags:
- IC peaking *before* the event (anticipation or leakage)
- Symmetric pre- and post-event IC (confound, not causal timing)
~~~~~~

<<<ML4T-ZH-BEGIN:c0064-p000>>>
<<<ML4T-ZH-END:c0064-p000>>>

### c0065-p000

~~~~~~markdown
## Key Takeaways

1. **Match feature lookback to label horizon**: The scan in Section 4 shows that
   long-lookback momentum features (126d+) carry significant cross-sectional
   information at monthly horizons, while short-term features (1d, 5d) are mostly
   noise. The shortest horizon is where the corrected scan finds anything at all, and
   one of the three cells it finds there is a reversal hit the mechanism checks reject
   as regime-driven. Horizon selection is a modeling decision that changes which
   features appear informative.

2. **State the mechanism first**: Before testing, draw the assumed DAG and identify
   potential confounders, mediators, and colliders.

3. **Timing placebos** are diagnostics, not gates. We report IC half-life and note
   that rolling-window features create mechanical IC persistence through input
   overlap. Focus on decay at lags beyond the lookback window. 12-1 momentum IC was
   strongest at lag 0 and decayed only gradually out to the longest lag tested;
   reversal had no signal to decay.

4. **Shared-driver checks** test whether a feature predicts an outcome it shouldn't.
   We used Treasury forward returns (economic control) and permutation (statistical
   control). The choice of control outcome is feature-dependent: for momentum,
   Treasury co-movement through risk-on/risk-off dynamics is plausible, making this
   a shared-driver diagnostic rather than a strict falsification.
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p000>>>
<<<ML4T-ZH-END:c0065-p000>>>

### c0065-p001

~~~~~~markdown

5. **Regime heterogeneity** reveals whether IC varies across market states but
   cannot distinguish confounding from genuine effect modification. Momentum's
   IC attenuated in high-VIX markets (5x magnitude variation) - consistent with
   the "momentum crash" phenomenon - while maintaining sign across regimes.
   Reversal showed a significant sign flip: an aggregation artifact where
   opposite-sign regime ICs cancel to near-zero unconditional IC.

6. **No feature is guaranteed to pass all checks**. The triage framework produces
   nuanced decisions: STOP (abandon), REVISE (investigate), or PROCEED (continue).
   12-1 momentum earned REVISE, not PROCEED - a realistic outcome that motivates
   regime-aware modeling in later chapters. Reversal earned STOP, correctly
   redirecting effort away from an uninformative feature.

7. **Bivariate limitation**: These checks test one feature at a time. The most
   dangerous confounders in feature engineering are often *other features* in the
   model. Chapter 15 provides multivariate sensitivity analysis (partial IC,
   double/debiased ML) for the features that survive this initial screen.

**Next**: Chapter 8 applies event-time alignment with fundamental features.
Chapter 15 introduces the formal causal inference toolkit (identification, DML,
sensitivity analysis).
~~~~~~

<<<ML4T-ZH-BEGIN:c0065-p001>>>
<<<ML4T-ZH-END:c0065-p001>>>
