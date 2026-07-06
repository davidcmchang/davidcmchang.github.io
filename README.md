# TowardingWeb - 脫引事工網站

這是一個專為「台灣脫引關懷協會 (Towarding)」建置的官方網站專案。

## 🌐 專案成果連結
*   **官方網站 (Live Site)**: [https://towarding.org/](https://towarding.org/)
*   **GitHub 儲存庫 (Repository)**: [https://github.com/davidcmchang](https://github.com/davidcmchang)

---

## 📋 專案開發進度

### ✅ 已完成事項
- [x] **Git 倉庫初始化**與 GitHub CLI 連接設定。
- [x] **首頁結構與現代美學設計** (Vanilla HTML5 / CSS3 / ES6)。
- [x] **響應式導覽列**：支援行動端漢堡選單與 scrolled 滾動收縮。
- [x] **「上帝在網路世代的心意」七大現象課程板塊**。
- [x] **一頁簡介 PDF 靜態連結與 QR Code 產生**。
- [x] **全域關聯更名**：將所有「心又新關懷協會」更名為「脫引關懷協會」。
- [x] **資源中心**：
  - 10 篇真實專欄文章配置。
  - 5 部 YouTube 影片嵌入。
  - 摺疊式常見問題 (FAQ)。
- [x] **Logo 透明去背轉換與尺寸微調**：將頂部 Logo 淡色版與底部 Logo 深色版利用 Python 進行 BFS 去背，並放大尺寸（頂部 `84px`、滾動時 `60px`、底部 `84px`）以提升視覺精緻度。
- [x] **文字內容修改與版面更新** (依據 PDF 20260706C)：
  - 支持我們：修改說明文案，替換新的華南商業銀行與郵局劃撥帳號，增加轉帳後的 Email/簡訊行政作業提醒。
  - 活動與課程：暫時移除 timeline 行程，新增「課程規劃中，敬請期待」的精美 Placeholder。
  - 聯絡我們與頁尾：更新信箱、地址，修改頁尾文案與關聯機構（宇宙光、晨曦會、信友堂）。
  - 高亮字詞：在「關於我們」區塊將「成癮、牽引、轉向、Towarding Dawn」高亮紅色並加大兩號字級。
- [x] **GitHub Pages 發佈與託管**。

### 🚀 下一步計畫
- [ ] 若有其他行銷影片或新專欄文章，可持續於資源中心更新。
- [ ] 視需求將聯絡表單的 JavaScript 送出邏輯對接到實際的後端 API (如 Formspree 或 EmailJS)。

### ⚠️ 踩坑與解決方案紀錄
*   **Windows 下 Git Dubious Ownership**：在 Windows 環境的 Git 初始化時容易觸發安全例外，已透過 `git config --global --add safe.directory` 解決。
*   **Logo 去背與變形**：用戶上傳的 Logo 為 JPG 純白背景，已透過自製 Python 腳本轉為透明 PNG，並在 CSS 裡使用 `width: auto; object-fit: contain;` 以防圖片拉伸變形。
*   **Windows Shell 逸出字元**：直接在 CLI 中呼叫 JSON 容易因逸出字元導致 HTTP 422 錯誤，已透過在 scratch 建立 `pages_payload.json` 並作為 file input 來完美避開此問題。
*   **多處非相鄰 HTML 修改之損毀問題**：當使用 line-based replacement 工具對具有重疊或大量類似結構 tags 的 HTML 進行非相鄰多重修改時，容易引起結構錯亂或代碼遗漏。改用專門的 Python 腳本讀寫檔案並執行精準字串替換，能 100% 確保結構正確且高效。
