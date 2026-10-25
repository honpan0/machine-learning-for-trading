# ML4T A3 Universal Pack v1（繁體中文）

## 核心設計

將現有 A2 `manifest.json`、`pack_manifest.json`、`responses/` 當作可信來源；原始英文 Notebook、對應 `.py`、舊 Batch、A2 Pack、已完成的中文 Notebook 均不會被覆寫。

在**交給 GPT 之前**，A3 自動遮蔽完整的 LaTeX 數學式（`$...$`、`$$...$$`、`\(...\)`、`\[...\]`、指定的數學環境）、程式碼區塊、行內程式碼、網址、圖片及 HTML 標籤等需保留的內容。每個單元的保護區間由原始來源重新計算並以 SHA256 驗證。GPT 只見到 `[[ML4T_A3_0001]]` 一類佔位符；回收時逐字還原。

**無 API 費用**，但依舊需要人工將 Pack 交給 GPT、將回答存成 UTF-8 `.txt`。無法繞過聊天室的模型輸出長度限制；因此會預先依「遮蔽後原文字元數」及「單元數」限制 Pack，避免一包過大。如果仍截斷，僅匯入已完整結束的單元，立即自動生成下一個 A3 Pack，不需切換到舊的 `safe retry` 工具或另一套提示詞。

## 安裝一次即可

將 `ml4t_a3_universal_pack_v1.zip` 放在 Windows 的 `C:\code\ml4t`，WSL 執行：

```bash
cd /mnt/c/code/ml4t
python3 -m zipfile -e ml4t_a3_universal_pack_v1.zip .
python3 translation_tools/test_a3_pack.py
```

安裝包只有新檔案 `translation_tools/a3_pack.py`、`translation_tools/test_a3_pack.py`、`A3_README_zh_TW.md`，不覆寫 A2。

## 日常只要兩個 Python 指令

**1. 準備整章（第一次或想更新佇列時）**

```bash
python3 translation_tools/a3_pack.py prepare 02_financial_data_universe
```

如果某章尚未建立 A2 基礎工作區，A3 會呼叫既有 `prepare_chapter.py --prepare`（原有工作區原樣保留）。已經翻完的 A2 單元會自動略過。

預設每 A3 Pack **遮蔽後最多 6500 字元、最多 14 單元**；這是主動控制輸出長度，不是遇到問題才手動拆補翻。也可先試更大容量（提高吞吐量，但提高截斷風險）：

```bash
python3 translation_tools/a3_pack.py prepare 02_financial_data_universe --max-chars 8500 --max-units 18
```

產生的兩帳號排程表：

- `translations/reports/02_financial_data_universe_a3_queue.md`
- `translations/reports/02_financial_data_universe_a3_queue.csv`

每個 Notebook 的 A3 任務：

- `translations/work/<章>/<notebook>/packs/a3_pack_001.md`

每個 GPT 回覆的正確檔名：

- `translations/work/<章>/<notebook>/inbox/a3_pack_001.txt`

檔名與 Pack 編號以 A3 佇列為準，請勿拿 A2 `pack_001.md` 或 `pack_001.txt` 混用。

**固定提示詞（所有 Notebook/Pack 相同）：**

> 請嚴格執行附件《ML4T A3 Universal Pack》的翻譯規則：只翻譯英文自然語言為臺灣繁體中文，完整保留 `[[ML4T_A3_0001]]` 類型佔位符的拼寫、出現次數及順序，不輸出任何原始 LaTeX 公式或程式碼。依附件單元順序，僅回覆每個單元完整配對的 `ML4T-ZH-BEGIN` 與 `ML4T-ZH-END` 及其間譯文；不得省略、摘要或加入其他文字。如果長度不足，請停在最後一個完整的 END 標記。

**2. 集中回收整章**

```bash
python3 translation_tools/a3_pack.py collect 02_financial_data_universe
```

完成單元進入既有 `responses/`；只要 Notebook 所有翻譯完成，就自動 Build + Verify `_zh.ipynb`，且更新進度報表（若已安裝 progress_dashboard）。若有截斷或佔位符錯誤，會只保存有效單元，並**自動建立新的 A3 Pack**；A3 佇列隨即更新。補翻仍使用同一提示詞和同一回收指令。

如只想操作單一 Notebook，目標亦可使用 `02_financial_data_universe/09_options_continuous.ipynb`：

```bash
python3 translation_tools/a3_pack.py prepare 02_financial_data_universe/09_options_continuous.ipynb
python3 translation_tools/a3_pack.py collect 02_financial_data_universe/09_options_continuous.ipynb
python3 translation_tools/a3_pack.py status 02_financial_data_universe/09_options_continuous.ipynb
```

## 邊界與品質

- 不會自動上傳檔案到 GPT，也不使用隱藏 API 或瀏覽器自動化。人工提交 / 複製回覆仍不可省。
- 某些不成對、非標準、無法安全辨識的 LaTeX 會在 `prepare` 階段**拒絕**，以避免破壞原文；對此需確認原始來源（不能保證 483 份零例外）。
- 輸出長度限制屬於 GPT 聊天環境，不保證每包都不中斷；A3 自動續翻的目的是降低人工處理成本。
- 結構/公式逐字還原驗證 **不代表** 中文的財經/機器學習術語已經人工校對；建議抽查譯文語意。
- 收件目錄仍使用原本已加入 Git ignore 的 `inbox/`；提交 Git 時建議明確加入 `a3_manifest.json`、`packs/a3_pack_*.md`、`responses/`、中文版 Notebook 和報表，**不要 `git add .`**。

## 測試

```bash
python3 translation_tools/test_a3_pack.py
python3 translation_tools/test_repair_ai_response.py
python3 translation_tools/test_a2_packs.py
python3 translation_tools/test_prepare_chapter.py
```

A3 整合測試使用臨時 Git/Notebook 環境，檢查公式與程式碼保護、截斷回覆、佔位符失效、重試自動排程、複用 A2 原工作區，以及 Notebook Build/Verify。沒有對你本機的 483 份原始 Notebook 逐一執行真實翻譯；建議先用第二章做一次實測。
