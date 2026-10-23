# 給翻譯 AI 的最簡操作方式

**把 `translations/work/.../tasks/batch_001.md` 的完整內容提供給 AI 即可。**

該任務檔已包含：翻譯規範、英文原文、單元 ID 和指定回覆標記。

AI 回覆後，請將完整的純文字回答存成 UTF-8 `.txt` 檔案，在本機使用：

```bash
/home/kim/.venvs/ml4t/bin/python translation_tools/nb_zh.py ingest 原版相對路徑.ipynb --batch 1 --file 回覆.txt
```

嚴禁直接把 AI 生成的 Notebook 取代英文原版，也不要讓 AI 修改程式碼儲存格。
