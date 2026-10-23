# ML4T 第三版｜繁體中文翻譯術語表

版本：v1.0

## 一、翻譯基本原則

- 使用台灣繁體中文，採用台灣金融、統計及機器學習領域常見用語。
- 忠實翻譯英文原文，不自行增加解釋、刪減內容或改變作者論述。
- 原始英文將由本機工具保留，AI 只需輸出對應的繁體中文。
- 不翻譯 Python 變數、函式名稱、檔案路徑、套件名稱及網址。
- 數學公式、LaTeX 語法、數值、單位與引用標記必須保持正確。
- Markdown 標題、清單、粗體、連結等格式須保留。
- 首次出現重要專業術語時，可採「中文（English）」形式。
- 術語表是預設譯法；若特定段落的專業語境不同，應以原文真正含義為準，不得強行套用。

## 二、金融與量化交易

| 英文 | 建議繁體中文 |
|---|---|
| Asset returns | 資產報酬率 |
| Factor | 因子 |
| Factor returns | 因子報酬率 |
| Factor premium | 因子溢酬 |
| Risk premium | 風險溢酬 |
| Market regime | 市場狀態 |
| Market microstructure | 市場微觀結構 |
| Momentum | 動能 |
| Value strategy | 價值策略 |
| Carry trade | 利差交易 |
| Defensive strategy | 防禦型策略 |
| Portfolio | 投資組合 |
| Portfolio optimization | 投資組合最佳化 |
| Asset allocation | 資產配置 |
| Backtesting | 回測 |
| Trading signal | 交易訊號 |
| Transaction costs | 交易成本 |
| Slippage | 滑價 |
| Drawdown | 回撤 |
| Maximum drawdown | 最大回撤 |
| Sharpe ratio | 夏普比率 |

## 三、統計與機器學習

| 英文 | 建議繁體中文 |
|---|---|
| Machine learning | 機器學習 |
| Deep learning | 深度學習 |
| Feature | 特徵 |
| Feature engineering | 特徵工程 |
| Label | 標籤 |
| Training set | 訓練集 |
| Validation set | 驗證集 |
| Test set | 測試集 |
| Out-of-sample | 樣本外 |
| Cross-validation | 交叉驗證 |
| Walk-forward validation | 滾動向前驗證 |
| Data leakage | 資料洩漏 |
| Look-ahead bias | 前瞻偏誤 |
| Survivorship bias | 存活者偏誤 |
| Overfitting | 過度擬合 |
| Underfitting | 擬合不足 |
| Hyperparameter | 超參數 |
| Gaussian mixture model (GMM) | 高斯混合模型 |
| Cluster | 群集 |
| Clustering | 分群 |
| Time series | 時間序列 |
| Cross-sectional | 橫斷面 |
| Volatility | 波動率 |
| Standard deviation | 標準差 |
| Correlation | 相關性 |
| Covariance | 共變異數 |

## 四、特殊注意事項

以下術語必須依上下文判斷，不應固定成單一中文：

- **Return**：金融情境通常譯為「報酬率」，程式函式或傳回值情境須另行判斷。
- **Regime**：市場環境分析可譯為「市場狀態」，其他領域可能需要「狀態」或不同譯法。
- **Alpha**：可能代表超額報酬、風險調整後的績效或模型截距，依上下文判斷。
- **Exposure**：可能是曝險、部位曝險或因子曝險。
- **Carry**：依金融工具與策略，可使用利差交易、持有收益或其他更準確的譯法。
- **Bias**：統計上的偏差與研究方法上的偏誤應依語境區分。

## 五、跨 AI 翻譯規範

每次交給 AI 的翻譯任務，應同時提供：

1. 當次的 `batch_XXX.md`。
2. 本術語表 `glossary_zh_TW.md`。

AI 必須遵循翻譯任務檔內的單元編號及輸出標記格式。

不得修改或省略 `ML4T-ZH-BEGIN`、`ML4T-ZH-END` 等標記。

術語表後續修改時，應由專案管理者統一更新並納入 Git 版本管理，以確保不同 AI 使用相同標準。