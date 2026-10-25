# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：09_model_based_features/11_hmm_regimes.ipynb；A3 Pack 003；單元 3 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵
- Label → 標籤
- Cluster → 群集

## 待翻譯英文單元

### c0043-p000

~~~~~~markdown
## The features this notebook produces

| Column | What it is | Causal |
|---|---|---|
| [[ML4T_A3_0001]] | probability of the higher-variance state, from the forward recursion | in its inference, not in its parameters |
| [[ML4T_A3_0002]] | which state that probability favours | same |
| [[ML4T_A3_0003]] | how undecided the model is between states | same |
| [[ML4T_A3_0004]] | how long the model expects the current state to last | a property of the fit |
| [[ML4T_A3_0005]] | the same probability from the switching model | same |
| [[ML4T_A3_0006]], [[ML4T_A3_0007]] | the two rules from Part 1 | fully, they estimate nothing |

The middle column of that table needs its qualifier read. Every probability here is
filtered, so its **inference** uses only observations up to its own session. But the
**parameters** were estimated by fitting the model to the whole sample, so a session's
probability was produced by a transition matrix that had seen every later session. A
strictly point-in-time pipeline refits the model on each fold's training block and
extracts the filtered probabilities per fold, which is what
[[ML4T_A3_0008]] does and what a backtest should read.

This notebook keeps a single fit because the point being taught is the difference between
filtered and smoothed inference, and refitting per fold would put a second thing in the
same figure. Nothing here is written to disk, so nothing downstream can read a column
whose parameters saw its own future.
~~~~~~

<<<ML4T-ZH-BEGIN:c0043-p000>>>
<<<ML4T-ZH-END:c0043-p000>>>

### c0044-p000

~~~~~~markdown
## Key takeaways

1. **Two rules that need no fitting set the bar.** An index threshold and a long moving
   average are transparent, immediate, and free of estimation risk. A fitted model earns
   its place by beating them at something.
2. **Filtered, never smoothed.** The forward recursion conditions on the past; the
   smoothed posterior conditions on everything. They disagree exactly at the transitions a
   regime feature exists to catch, and the notebook measures on what share of sessions.
3. **A hard label needs the same care as a probability.** The model's own [[ML4T_A3_0001]] runs
   a decode over the whole sequence, so a state label taken from it reads the future even
   when the probabilities beside it do not.
4. **Three things break a fitted regime model, and each has an answer.** Local optima,
   answered by seeded or repeated starts; the number of states, answered by a criterion
   that charges for them and then by judgement about what the feature is for; and the
   arbitrary ordering of states, answered by sorting them on something the model defines.
5. **Filtered inference is not the same as a point-in-time feature.** The parameters are
   fitted too, and a fit over the whole sample puts every later session into every earlier
   probability. Refitting per fold closes that, at the cost of one fit per fold, and
   [[ML4T_A3_0002]] is where it is done.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p000>>>
<<<ML4T-ZH-END:c0044-p000>>>

### c0044-p001

~~~~~~markdown

**Known limitations.** One symbol, one fit, one sample. The two-state choice is made
against the criterion rather than by it, on stated grounds a reader may reject. The
comparison between the model and the indicators measures overlap between two different
definitions of a regime and establishes nothing about either. And nothing here evaluates
whether a regime feature improves a downstream model, which is the only question that
decides whether any of it is worth carrying; [[ML4T_A3_0001]] is where that is
asked.

**Next**: [[ML4T_A3_0002]] clusters whole distributions instead of fitting a
state model, and [[ML4T_A3_0003]] puts a regime probability into a model and
measures what it does.
~~~~~~

<<<ML4T-ZH-BEGIN:c0044-p001>>>
<<<ML4T-ZH-END:c0044-p001>>>
