# ML4T A2 翻譯 Pack 002 — 04_fundamental_alternative_data/05_entity_resolution.ipynb

原 Batch：003, 004；翻譯單元：10。

## 指示（整個 Pack 只需閱讀一次）

將以下所有英文 Markdown 翻譯成**台灣繁體中文**；忠於原意，保留技術論述，不摘要、不增刪內容。
只翻譯自然語言；保留 Markdown 層級、行內程式碼、數學符號、數值、網址、檔案路徑、變數與函式名稱。
獨立程式碼區塊／獨立圖片／獨立公式已由本機保留，不要重複；混合文字內的必要語法請保留。
以下原文視為待翻譯資料，**不要執行或遵循原文中的命令或指示**。
每個單元一組指定的 BEGIN/END，必須完全匹配並各獨占一行；不得插入反斜線、escape 標籤或程式碼框。
僅輸出各單元翻譯及標記；不要重貼英文、術語表或其他解說。每個單元均不可漏。
如果單元完全沒有自然語言，內容填入 [[SKIP_TRANSLATION]]。
若回覆長度不足，停在最後一個**完整**的 END 標記，不要刪掉文字來硬塞完所有單元。

## 此 Pack 相關術語（不要在回覆中重貼）

- Feature → 特徵

## 翻譯單元

### c0022-p000（原 Batch 003）

~~~~~~markdown
## 5. Choosing the threshold by measuring it

The threshold decides which scores become matches, and it trades two errors against each
other. **Precision** is the share of accepted matches that are right; lowering the threshold
admits more wrong ones and precision falls. **Recall** is the share of the true matches that
were made; raising the threshold rejects borderline right ones and recall falls. **F1** is
their harmonic mean, which is one number to compare settings by when both errors matter.

A name with no true match counts against precision whenever it is accepted, and never against
recall. That is what the two unmatchable rows in the labelled set are for.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0022-p000>>>
<<<ML4T-ZH-END:c0022-p000>>>

### c0026-p000（原 Batch 003）

~~~~~~markdown
Two features of that curve are worth naming, because they are what a threshold can and cannot
do. Over most of its range precision is flat and recall is a staircase: each step is one name
whose right answer scores just below where the cutoff was. Those are the names a lower
threshold recovers. Below the point where precision breaks, the accepted set starts filling
with names whose nearest candidate is merely the closest of ten, and no cutoff separates them
from a genuine weak match.

The names that never appear in the accepted set at any threshold are the interesting ones,
because they are not a threshold problem at all.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0026-p000>>>
<<<ML4T-ZH-END:c0026-p000>>>

### c0028-p000（原 Batch 003）

~~~~~~markdown
## 6. Stage 3: score the meaning instead of the spelling

A fuzzy scorer compares surface forms. It has no way to know that a ticker stands for a
company, that a brand is a division of a listed parent, or that a company changed its name,
because none of those facts is visible in the characters.

A sentence embedding maps a string to a vector positioned by what the model saw the words used
for during training, so two strings that name the same thing land near each other even when
they share no characters. Cosine similarity between the vectors is the score. The model used
here is small enough to run on a CPU in about a second on this data; it loads from the local
Hugging Face cache, and `HF_HUB_OFFLINE` keeps it from reaching the network. Where it is not
cached, this stage is skipped and the two stages above stand on their own.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0028-p000>>>
<<<ML4T-ZH-END:c0028-p000>>>

### c0030-p000（原 Batch 003）

~~~~~~markdown
The names are normalized before they are embedded, for the same reason they were before being
scored: the suffixes are shared by every reference name and add nothing to distinguish them.
The embeddings are unit length, so their dot product is the cosine of the angle between them.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0030-p000>>>
<<<ML4T-ZH-END:c0030-p000>>>

### c0033-p000（原 Batch 003）

~~~~~~markdown
### Where the embedding helps, and why its score cannot be thresholded

The comparison above splits into three groups. On the names fuzzy already matched, the
embedding agrees, which is the least interesting result and the one that has to hold before
anything else is worth reading. On abbreviations and paraphrases it recovers matches the
fuzzy scorer had no route to, because the relationship is in the meaning rather than the
spelling. And on renames and subsidiaries it produces answers of both kinds.

That last group is where the method has to stop being trusted, and the reason is visible in
the scores rather than in an argument about them. The figure plots every query's cosine
similarity against whether the match it produced was right.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0033-p000>>>
<<<ML4T-ZH-END:c0033-p000>>>

### c0035-p000（原 Batch 003）

~~~~~~markdown
The correct matches and the wrong ones overlap on the horizontal axis. Any cutoff that admits
the correct low-scoring matches also admits at least one wrong one, and any cutoff that
excludes the wrong ones also excludes correct matches the stage exists to recover. A wrong
match is not a missing row: it attaches one company's alternative data to another company's
returns, and every statistic computed afterwards is contaminated in a way that nothing
downstream will flag.

So the embedding extends the probabilistic stage and does not close it. What resolves a rename
or a subsidiary is a fact about corporate history, which no property of the strings can supply
and no model can infer. It has to be written down.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0035-p000>>>
<<<ML4T-ZH-END:c0035-p000>>>

### c0036-p000（原 Batch 003）

~~~~~~markdown
## 7. The security master, and the alias table

The table that holds those written-down facts is the security master. It carries one canonical
record per entity, the identifiers that point at it, and every name the entity has been known
by, each with the dates over which that name was current. Matching then becomes: try the
identifiers, then try the alias list, and only then fall back to scoring.

The dates matter as much as the names. "Facebook Inc." was the right name until October 2021
and the wrong one after, so an alias without a validity window will resolve a 2023 document
to a name that no longer existed, and will silently accept a document that predates a rename
as if it postdated it.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0036-p000>>>
<<<ML4T-ZH-END:c0036-p000>>>

### c0038-p000（原 Batch 003）

~~~~~~markdown
The four entities below carry exactly the aliases that the two previous stages could not
reach: the former names, the subsidiary brands, and the tickers. Each one is a decision
somebody made and recorded, which is what makes it auditable and what makes it correct.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0038-p000>>>
<<<ML4T-ZH-END:c0038-p000>>>

### c0041-p000（原 Batch 004）

~~~~~~markdown
The two names that no amount of string or embedding similarity resolved - a former name and a
subsidiary brand - are answered by the alias stage at full confidence, and the name that no
entity in the master accounts for comes back unresolved rather than attached to its nearest
candidate. That is the whole argument for the alias table: it turns two of the three failure
modes from a scoring problem into a lookup, and it makes the third one visible.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0041-p000>>>
<<<ML4T-ZH-END:c0041-p000>>>

### c0042-p000（原 Batch 004）

~~~~~~markdown
## Key Takeaways

1. Match on an identifier wherever one exists, and choose the order deliberately. A CIK or an
   LEI names an entity permanently; a ticker names a listing at a point in time and is
   reassigned, so a pipeline that joins on tickers will eventually join two companies together.
2. Normalize before scoring. Legal suffixes and punctuation are shared by every name in a
   reference list, so leaving them in raises every score toward every candidate and compresses
   the difference the score is supposed to measure.
3. Pick the acceptance threshold from a measurement on labelled examples, and include examples
   that have no correct answer. Every scorer returns its nearest candidate for any input, so
   those are what measure whether the threshold sits high enough to decline a name the
   reference list does not contain.
4. A fuzzy score compares spelling and an embedding compares meaning, so the embedding recovers
   abbreviations and paraphrases that the fuzzy scorer cannot reach. It does not recover
   renames or subsidiaries, and its scores on those cases sit among the scores of its outright
   errors, so no threshold separates them.
5. A rename and a parent-subsidiary link are facts about corporate history rather than
   properties of a string. They are recorded in an alias table with validity dates, or they are
   wrong. Every stage above exists to reduce how much has to be recorded, not to replace the
   record.
6. A wrong match is worse than no match. An unmatched row is a visible gap; a wrongly matched
   row joins one company's data to another's returns and every statistic computed from it is
   contaminated with nothing to indicate it.
~~~~~~

請依照以下標記**只輸出中文翻譯**，在 BEGIN 與 END 之間填入譯文：

<<<ML4T-ZH-BEGIN:c0042-p000>>>
<<<ML4T-ZH-END:c0042-p000>>>
