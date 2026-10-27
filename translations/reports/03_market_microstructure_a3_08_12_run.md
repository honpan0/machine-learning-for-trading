# 第三章 A3 v3.1：08–12 翻譯紀錄

日期：2026-10-25。完成 78/95 單元、8 個 Pack；17 個單元待續。

| Notebook | 單元 | Pack | Build／獨立 Verify | 中文抽查 | 異常 |
|---|---:|---:|---|---|---|
| 08_databento_lob_reconstruction | 25/25 | 2/2 | PASS／PASS | F/T 語意、TOB、UNDEF_PRICE、深度失衡通過 | 無 |
| 09_databento_mbo_analysis | 0/17 | 未建立 | 未執行 | 未執行 | prepare 因單美元公式歧義停止 |
| 10_iex_lob_reconstruction | 18/18 | 2/2 | PASS／PASS | L2 更新、零數量移除、測試資料限制通過 | 無 |
| 11_algoseek_taq_eda | 19/19 | 2/2 | PASS／PASS | NBBO、延遲回報、交易場所、股票分割通過 | 無 |
| 12_algoseek_taq_lob_reconstruction | 16/16 | 2/2 | PASS／PASS | Lee-Ready、as-of、失衡、同期相關性通過 | 無 |

四份已完成 Notebook 的來源 SHA-256 與 A3 Manifest 一致；已收集 inbox 雜湊、BEGIN/END 配對與順序、佔位符順序及 responses 完整性均通過。獨立 Verify 確認英文逐字保留，程式碼與輸出完全一致；collect 完成保護片段還原驗證。每份均抽查開頭、技術段落與結尾，未發現中文語意異常；此為抽查，非完整人工審稿。

## 待續：09_databento_mbo_analysis

- 命令：`python3 translation_tools/a3_pack.py prepare 03_market_microstructure/09_databento_mbo_analysis.ipynb`
- 結果：exit 1，`未閉合或歧義的單美元公式；停止產生翻譯 Pack`。
- 來源第 31 儲存格（零起算）含表格列：`| Aspect | ITCH (Free) | DataBento (~$10/symbol/mo) |`。第 10 儲存格另有正式 LaTeX 公式與行內公式。只記錄所觀察的來源內容，未修改來源或遮蔽器，也未繞過保護機制。
- A3 Manifest／Pack 未建立；A2 工作區與 Manifest 保留，全部 17 個單元待處理。待遮蔽歧義排除後，再建立 A3 Pack，依既有流程翻譯、collect、Build、獨立 Verify 及中文抽查。
- 待續單元：c0000-p000, c0001-p000, c0006-p000, c0009-p000, c0010-p000, c0013-p000, c0014-p000, c0018-p000, c0019-p000, c0022-p000, c0024-p000, c0025-p000, c0026-p000, c0028-p000, c0029-p000, c0031-p000, c0031-p001。

未重做 01–07，未處理 13 或之後 Notebook。未修改來源 Notebook、Python、A3 工具或驗證器；未執行 Notebook、下載市場資料、安裝套件、呼叫付費 API、重跑全套測試或執行 Git 操作。
