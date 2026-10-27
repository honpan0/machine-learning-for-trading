# 第三章 A3 v4：13–17 翻譯紀錄

日期：2026-10-25。依指定順序完成 102/102 個單元，12/12 個 Pack，無續翻 Pack。

| Notebook | 完成單元 | Pack 成功／總數 | Build／獨立 Verify | 中文抽查 | 未完成問題 |
|---|---:|---:|---|---|---|
| 13_algoseek_minute_bars_eda | 28/28 | 4/4 | PASS／PASS | 開頭、OFI 公式附近、結尾通過；分鐘 K 棒、成交分桶、壓力、FINRA 語意 | 無 |
| 14_itch_bar_sampling | 20/20 | 2/2 | PASS／PASS | 開頭、固定失衡門檻公式附近、結尾通過；逐筆／成交量／成交金額 K 棒與 Lee-Ready 語意 | 無 |
| 15_itch_lee_ready | 12/12 | 1/1 | PASS／PASS | 開頭、報價／價格跳動檢定技術段、結尾通過；原文無 LaTeX 公式 | 無 |
| 16_itch_information_bars | 10/10 | 2/2 | PASS／PASS | 開頭公式附近、自適應失控段、結尾通過；預期大小、預期失衡及門檻漂移語意 | 無 |
| 17_databento_bar_sampling | 32/32 | 3/3 | PASS／PASS | 開頭、E[T]／α 段、校準建議、結尾通過；多日校準、涵蓋率及美元金額保護 | 無 |

五份均先寫入 UTF-8 inbox，核對 BEGIN/END 配對、單元順序與佔位符順序，再經既有 collect 匯入 responses、Build 及工具內建驗證；另外逐份執行 `nb_zh.py verify`，均為 PASS。原英文逐字保留，130 個程式碼儲存格及其輸出完全一致。中文為開頭、技術／公式附近與結尾抽查，非完整人工審稿。

五份 A3 Manifest 的來源 SHA-256、Pack 任務 SHA-256、已回收 inbox SHA-256 均核對通過；所有單元 mask_version 均為 4。各份保留既有 A2 工作區，僅因缺少 A3 Pack 而 prepare；未修改工具或保護規則。無遮蔽異常、無效佔位符或未完成單元。

保留前 12 份成果；未開始第 18 份。未執行 Notebook、安裝套件、下載資料、使用額外付費 API 或重跑無關測試。未執行 Git add、commit、push。
