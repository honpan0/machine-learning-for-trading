# ML4T 第三版：方案 B｜Notebook 中英對照翻譯工作站

本工具使用 Python 標準函式庫，不必重新安裝套件。它**只讀取**原始 `.ipynb`，自動切出 Markdown 翻譯批次；AI 回覆存成本機文字檔後匯入；完成全部批次才生成獨立 `_zh.ipynb`。

## 0. 放置方式

下載並解壓縮套件，將 `translation_tools/nb_zh.py` 放到：

`C:\code\ml4t\translation_tools\nb_zh.py`

在 VS Code 左下角已顯示 `WSL: Ubuntu` 的終端機執行下列所有指令。**只複製指令，不要複製 Markdown 程式碼框標記。**

```bash
cd /mnt/c/code/ml4t
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py --help
```

## 1. 為一份 Notebook 建立翻譯任務（只需執行一次）

```bash
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py prepare 01_process_is_edge/factor_regimes.ipynb --max-chars 1800 --batch-chars 5000
```

工具會建立：

```text
translations/work/01_process_is_edge/factor_regimes/
├── manifest.json           # 來源雜湊、單元 ID、批次、固定進度索引
├── tasks/
│   ├── batch_001.md       # 將這份檔案提供給第一個 AI
│   └── batch_002.md       # 將這份檔案提供給第二個 AI（若有）
├── inbox/                  # 將 AI 的回覆存到這裡，例如 batch_001.txt
└── responses/              # ingest 後自動寫入逐單元中文；不需手動編輯
```

`--max-chars 1800` 控制每個 Markdown 單元的**目標**英文長度；為避免切斷句子、程式碼或公式，遇到沒有適當段落界線時可能超過上限。`--batch-chars 5000` 控制送給 AI 的單批英文長度。建議先用預設值試驗；非常容易耗盡額度時，可在**第一次 prepare 時**改用 `--max-chars 900 --batch-chars 2400`。

注意：工作區建立後，**再次 prepare 會拒絕覆蓋**。如需更改切割策略，不要直接刪除進度，應先備份並另作規劃。

## 2. 給另一個 AI 哪些材料？

只要把 `translations/work/01_process_is_edge/factor_regimes/tasks/batch_001.md` **全部內容**複製到另一個 AI 對話，或上傳此 `.md` 檔。

這個檔案已內建角色、翻譯規則、每個固定 ID、英文原文，以及必須採用的回覆標記。**不用上傳完整 `.ipynb`、`.py`、資料集、API Key 或整個 GitHub 專案**。

AI 應只回傳下面這種格式（單元數量視任務而異；ID 必須以任務原文為準）：

```text
<<<ML4T-ZH-BEGIN:c0000-p000>>>
# 以因子為基礎的市場狀態辨識
<<<ML4T-ZH-END:c0000-p000>>>

<<<ML4T-ZH-BEGIN:c0000-p001>>>
市場在不同年份可能有不同表現……
<<<ML4T-ZH-END:c0000-p001>>>
```

不能在標記外補充說明、不能遺漏標記、不能增加額外的三個反引號程式碼框。如果整段完全是純程式碼、公式或圖片、不含可翻譯的自然語言，可在標記內**只寫** `[[SKIP_TRANSLATION]]`，原文會保留但不插入冗餘的中文說明。

要同時使用兩個 AI：把 `batch_001.md` 交給帳號 A、`batch_002.md` 交給帳號 B；工作單元都有唯一 ID，因此不需要讓兩個帳號看到對方的聊天紀錄。

## 3. 收到 AI 回覆，如何導入本機？

在 VS Code 的檔案總管新增純文字檔：

`translations/work/01_process_is_edge/factor_regimes/inbox/batch_001.txt`

把 AI 的**完整回覆**貼到此檔並存成 UTF-8。注意：不要貼入自己的問題、AI 的其他說明或 Markdown 包覆框。

接著在 WSL 終端機執行：

```bash
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py ingest 01_process_is_edge/factor_regimes.ipynb --batch 1 --file translations/work/01_process_is_edge/factor_regimes/inbox/batch_001.txt
```

匯入前會檢查是否少了 ID、重複 ID、有多餘文字、回覆為空或與已存翻譯衝突；批次不完整時**全部不匯入**，不會留下半個批次。成功時，翻譯會變成 `responses/c0000-p000.md` 等獨立檔案。

查看進度：

```bash
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py status 01_process_is_edge/factor_regimes.ipynb
```

今天結束可直接關閉 VS Code。下次重新開啟後，使用上述 `status` 指令，再把尚未完成的 `tasks/batch_###.md` 給任一 AI。**不需要前次對話上下文。**

若想修正已匯入的一批翻譯，先更新 inbox 回覆檔，檢查後顯式增加 `--replace` 重新匯入；原有檔不會在未經同意下被覆寫。

## 4. 所有單元完成後，組裝獨立雙語 Notebook

確認 `status` 顯示 100% 後執行：

```bash
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py build 01_process_is_edge/factor_regimes.ipynb
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py verify 01_process_is_edge/factor_regimes.ipynb
```

結果產生：

`C:\code\ml4t\01_process_is_edge\factor_regimes_zh.ipynb`

這份雙語 Notebook：

- 原始英文逐字保留，繁體中文按 Markdown 單元附在原文之後；使用隱藏 HTML 註解標記方便驗證及重建。
- **所有非 Markdown 儲存格完全照搬**，包括 Python 程式碼、儲存格 metadata、執行次數、圖表與輸出資料。
- Markdown 附件與 metadata 也原樣保留。
- 清除原英文版的 `jupytext` 配對資訊與 `ml4t_provenance` stamp，避免把雙語衍生檔誤當成英文 `.py` 的同步檔案或聲稱已重新執行。
- 保留原有 Jupyter Kernel 設定。用 VS Code 開啟後仍應選 `/home/kim/.venvs/ml4t/bin/python`。

若已生成 `_zh.ipynb`，再次 build 預設拒絕覆蓋。若要修訂已完成的翻譯，先備份（如曾手工編輯），再執行 `build ... --replace`。

這份 `_zh.ipynb` **不會動態載入**原本 `factor_regimes.py`；它包含自己的程式碼儲存格，並會照常匯入專案其他程式庫。也因此原版程式碼將來有改動時，這份譯本不會自動跟著更新。

## 5. 四個設計要求的對應

| 要求 | 實作方式 |
|---|---|
| 可切割 | 依 Markdown 空白段落／安全界線分成 `c0000-p000` 單元；再按字元預算合併成批次。避免在 fenced code 或 `$$` 區塊中分割。 |
| 可接續 | `manifest.json` 記錄全部工作 ID；每個單元翻譯存成獨立 `.md`；`status` 回報已完成與未完成批次。 |
| 可驗證 | 來源 `.ipynb` SHA-256 鎖定；AI 回覆嚴格檢查 ID；build 與 verify 比較所有程式碼儲存格（含輸出）是否完全一致、所有英文能否按標記還原。 |
| 可重建 | 原版 `.ipynb`＋`manifest.json`＋`responses/*.md` 即可重新 build；不依賴聊天上下文或回覆順序。 |

### 驗證的界線

**工具驗證的是結構完整性，不是翻譯準確性。** 內容是否忠實、專有名詞是否一致，仍建議人工抽查，且建立一份 `translations/glossary_zh_TW.md` 共用術語表。

來源 `.ipynb` **只要被改動**（包括 Git 更新、metadata 修改），工具就會拒絕繼續；這是預期的安全保護，不是故障。翻譯期間不要修改原版、也不要使用 `jupytext --sync` 對整個專案批次同步。若想同步新的上游版本，應另行規劃版本遷移，不要直接覆蓋旧進度。

### 不應做的事

- 不要讓 AI 接觸或修改 `.env`、API Key、程式碼或原始 `.ipynb`。
- 不要把 AI 輸出直接貼回原始 `.py`，這是另一種工作方案。
- 不要直接編輯生成的 `_zh.ipynb` 中的程式碼；下次重新組裝會還原成原版。
- 新 `_zh.ipynb` 是獨立衍生檔，不應假設原專案所有 CI、Jupytext、provenance 工具都會管理它；首次生成後應額外跑一次原專案檢查。
- 翻譯教材可能受版權限制；保留在本機使用與公開發布是不同問題，公開前請確認授權。

## 6. 翻譯其他章節／case_studies

只需要更換第一個參數，例如：

```bash
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py prepare 01_process_is_edge/macro_regimes.ipynb --max-chars 1800 --batch-chars 5000
```

`case_studies` 內的 Notebook 也是同樣用法；工作目錄會依原路徑獨立建立，不會混淆同名 Notebook。避免開多個 AI 同時翻同一批次；若真的重複則只能明確 `--replace`。

## 7. 可選：安裝後先自行檢驗工具（不碰原教材）

```bash
cd /mnt/c/code/ml4t
/home/kim/.venvs/ml4t/bin/python translation_tools/selftest.py
```

自動建立暫時的假 Notebook，測試拆分、多批次錯序匯入、跳過純非文字區段、進度恢復、組裝、程式碼遭竄改偵測、英文來源變更偵測與禁止無提示覆寫。測試只在暫存目錄運行，不會修改你的原始 483 組 Notebook。期望最後出現 `ALL TESTS PASSED`。
