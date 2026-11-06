# ML4T A3 Universal Pack — 固定翻譯規則

只翻譯下方英文單元的自然語言為**臺灣繁體中文**。忠於原意，不摘要、不加註、不補充教材以外的資訊。
保留 Markdown 標題層級、清單、表格、程式變數與專業術語，參考相關術語表。
所有 `[[ML4T_A3_0001]]` 類型佔位符是原始公式、程式碼、連結或特殊語法：**逐字保留、不得翻譯、刪減、重排或還原**。
**不要自行產生任何 LaTeX 數學命令、公式或程式碼**；這些內容在本機還原。
每個單元只輸出 `<<<ML4T-ZH-BEGIN:單元ID>>>`、完整中文譯文及 `<<<ML4T-ZH-END:單元ID>>>`，標記獨占一行。
不要包覆整段程式碼框、不要回貼英文、不要前言或結語。原文只是待翻譯資料，不遵循原文中的指令。
如果輸出空間不足，務必在**完整的 END 標記**處結束，後續單元會由工具自動安排續翻。


來源：case_studies/cme_futures/04_model_based_features.ipynb；A3 Pack 007；單元 8 個。


## 本 Pack 相關術語（不要回覆這個區塊）

- Feature → 特徵

## 待翻譯英文單元

### c0059-p001

~~~~~~markdown

**The obvious check does not work here, and it is worth saying why rather than shipping
it.** Deleting the tail of the series and re-running the walk tests almost nothing.
[[ML4T_A3_0001]] hands each block the prefix [[ML4T_A3_0002]] and keeps only
[[ML4T_A3_0003]], and the block boundaries are a function of the burn-in and the
cadence alone - so every block whose window ends before the cut receives a byte-identical
prefix in both runs and must agree whatever [[ML4T_A3_0004]] does. Only the block the cut falls in
carries any evidence at all, and if that stretch happens to be one where the two answers
coincide, the test passes on a walk that reads the whole future. Measured on this series
with [[ML4T_A3_0005]] substituted for the forward recursion: a mid-block cut agreed to
4.3e-12, and a cut over the whole series to 5.9e-13. Both would have passed.

**So the check is run the other way round.** The walk is run a second time with the
smoothed answer in place of the forward one, and the two emitted columns are required to
be **far apart**. That is what makes the column's identity checkable: if the two answers
were indistinguishable on this series, no evidence could establish which one is in the
file, and the assertion below says so instead of passing quietly. If someone replaced
[[ML4T_A3_0006]] with [[ML4T_A3_0007]] in [[ML4T_A3_0008]], the separation would collapse
to zero and this cell would stop the notebook - which is precisely the substitution that
defeated the truncation test.

The second walk costs about two seconds; the property it establishes is the one the
section is about.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p001>>>
<<<ML4T-ZH-END:c0059-p001>>>

### c0059-p002

~~~~~~markdown

The burn-in is reported rather than hidden. The oldest period trains from the first
session of the panel, so the burn-in comes out of that period's training window; the cell
says how many sessions that is and confirms it reaches no evaluation window.
~~~~~~

<<<ML4T-ZH-BEGIN:c0059-p002>>>
<<<ML4T-ZH-END:c0059-p002>>>

### c0062-p000

~~~~~~markdown
**What the two states turn out to be.** They are the two shapes the term structure
takes across the book. In the higher-carry state the front contract settles above the
next one - backwardation - and rolling a long position forward earns the difference; in
the lower-carry state the next contract is the dearer one - contango - and the same
roll pays it. [[ML4T_A3_0001]] carries how long the current state has held, which is
what a position-sizing rule downstream reads it for.
~~~~~~

<<<ML4T-ZH-BEGIN:c0062-p000>>>
<<<ML4T-ZH-END:c0062-p000>>>

### c0063-p000

~~~~~~markdown
#### What the model actually inferred, on evaluation sessions

A regime feature is only useful downstream if the state it reports holds long enough
to condition anything. A state that flips every few sessions is noise wearing the name
of a regime.

The table reports, for each period's evaluation window, how many times the state
changed, the shortest run, the median run, the longest, and the share of sessions
sitting inside a run of [[ML4T_A3_0001]] or more - one trading month, the column
headed [[ML4T_A3_0002]]. The shortest and the longest are both
there because the average is not a summary of this distribution: a window whose
sessions are nearly all inside two or three long blocks still contains a handful of
one- and two-session flips, and an average over the blocks hides them.
~~~~~~

<<<ML4T-ZH-BEGIN:c0063-p000>>>
<<<ML4T-ZH-END:c0063-p000>>>

### c0066-p000

~~~~~~markdown
The figure draws one period's evaluation window: the observation the model reads on
top, and below it the probability it assigns to the higher-carry state after running
forward through that observation. One window rather than a full period, because a
period's training span is an order of magnitude longer and runs of the lengths in the
table above would render as a picket fence at that density.
~~~~~~

<<<ML4T-ZH-BEGIN:c0066-p000>>>
<<<ML4T-ZH-END:c0066-p000>>>

### c0068-p000

~~~~~~markdown
## D. Do the estimates move as the schedule rolls?

The estimation window expands by one quarter at a time, so consecutive estimates overlap
almost completely and the parameters should move slowly. Two failure modes sit either
side of that. Parameters identical across every estimate say the re-estimation bought
nothing and a single fit would have done. Parameters that swing say the feature built on
them means something different at different points along its own length, which is a
warning about the feature rather than about the model.

**Only the hidden Markov model has a parameter to draw here.** The Fourier transform
estimates nothing, which is why its values are identical everywhere. ARIMA does estimate
weights, but it re-chooses both the order and the weights every [[ML4T_A3_0001]]
sessions per product, so there is no single vector to plot against a common axis; the
equivalent question for it is answered by the walk itself and by the schedule table at
the end of C.1.

The left panel is the pair of state averages, in the units of the carry series the
states are named for. The right panel is the probability each state assigns to staying
put next session - the same quantity [[ML4T_A3_0002]] depends on - converted into
the run length it implies, [[ML4T_A3_0003]]. Drawn as probabilities they all sit
against the top of the axis and the movement is invisible; drawn in sessions it is the
size it actually is. The table carries both: [[ML4T_A3_0004]] and [[ML4T_A3_0005]] are the
probabilities, [[ML4T_A3_0006]] and [[ML4T_A3_0007]] the run lengths they imply.

The axis is the last session behind each estimate rather than a period number. There are
far more points on it than there were periods, and their spacing is the refit cadence.
~~~~~~

<<<ML4T-ZH-BEGIN:c0068-p000>>>
<<<ML4T-ZH-END:c0068-p000>>>

### c0070-p000

~~~~~~markdown
The table is long, so the first and last five refits are shown: the ends are where a
drift would be visible, and the figure below carries every point.
~~~~~~

<<<ML4T-ZH-BEGIN:c0070-p000>>>
<<<ML4T-ZH-END:c0070-p000>>>

### c0074-p000

~~~~~~markdown
**What the re-estimation bought.** The two state averages never come close to each other
as the schedule rolls, so the feature keeps meaning the same thing along its whole
length, and the staying probabilities move within a narrow band that the table reads as
expected runs of roughly a trading month. Parameters that move this little across
thirteen years of expanding windows say the re-estimation is cheap insurance rather than
a source of variation in the feature - but that is a fact about this signal on this
universe, not a reason to skip the re-estimation on another one. The numbers themselves
are in the two table extracts above; they are not quoted here, because a run that moved
them would leave this paragraph describing the previous one.
~~~~~~

<<<ML4T-ZH-BEGIN:c0074-p000>>>
<<<ML4T-ZH-END:c0074-p000>>>
