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
- [x] **專屬 Logo 的檔案轉換、去背 (Chroma Key) 與雙倍尺寸放大** (頂部與 Footer Logo 均為 `72px`)。
- [x] **全域關聯更名**：將所有「心又新關懷協會」更名為「脫引關懷協會」。
- [x] **資源中心**：
  - 10 篇真實專欄文章配置。
  - 5 部 YouTube 影片嵌入。
  - 摺疊式常見問題 (FAQ)。
- [x] **GitHub Pages 發佈與託管**。

### 🚀 下一步計畫
- [ ] 若有其他行銷影片或新專欄文章，可持續於資源中心更新。
- [ ] 視需求將聯絡表單的 JavaScript 送出邏輯對接到實際的後端 API (如 Formspree 或 EmailJS)。

### ⚠️ 踩坑與解決方案紀錄
*   **Windows 下 Git Dubious Ownership**：在 Windows 環境的 Git 初始化時容易觸發安全例外，已透過 `git config --global --add safe.directory` 解決。
*   **Logo 去背與變形**：用戶上傳的 Logo 為 JPG 純白背景，已透過自製 Python 腳本轉為透明 PNG，並在 CSS 裡使用 `width: auto; object-fit: contain;` 以防圖片拉伸變形。
*   **Windows Shell 逸出字元**：直接在 CLI 中呼叫 JSON 容易因逸出字元導致 HTTP 422 錯誤，已透過在 scratch 建立 `pages_payload.json` 並作為 file input 來完美避開此問題。
