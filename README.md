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
- [x] **「上帝在網路世代的心意」議題版塊極致微調**：
  - 移除了核心標題上方的 Icon。
  - 針對 `topic_04_3d.png`（問網現象）大腦問號圖標，去背羽化並完美擦除了神燈與火羽。
  - 將核心大標題及卡片標題統一調整為紅橙色（`#c10000`）。
  - 將卡片右上角的數字（01～07）顏色統一調整為純橘色（`#ff7f27`），大小微調為 48px，位置設定在 `top: 35px; right: 45px;` 以符合草圖。
  - 調整卡片 Padding 與 Icon 邊距使版面整體上移、緊湊精美。
  - 依照指示微調了前四個卡片的內文敘述，並將「**每個人**」、「**脫癮而出**」、「**連結**」、「**糾結**」、「**價值觀**」與「**生命主權**」高亮加粗。
- [x] **清理專案多餘資源**：彻底刪除了已無用途的 `80px` 與 `150px` 圖片資料夾與檔案。
- [x] **發佈部署至網站根目錄**：將完成的新版設計複製至專案根目錄發佈，並刪除臨時的 `xinyoutang` 子目錄。
- [x] **按鈕下載並開啟 PDF**：已實現點擊「下載一頁介紹」按鈕後，同時觸發瀏覽器下載 PDF 檔案與在新分頁（Tab）中自動打開該 PDF 供閱讀。
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
- [x] **「上帝在網路世代的心意」七大現象課程板塊。**
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
- [x] **「上帝在網路世代的心意」議題版塊極致微調**：
  - 移除了核心標題上方的 Icon。
  - 針對 `topic_04_3d.png`（問網現象）大腦問號圖標，去背羽化並完美擦除了神燈與火羽。
  - 將核心大標題及卡片標題統一調整為紅橙色（`#c10000`）。
  - 將卡片右上角的數字（01～07）顏色統一調整為純橘色（`#ff7f27`），大小微調為 48px，位置設定在 `top: 35px; right: 45px;` 以符合草圖。
  - 調整卡片 Padding 與 Icon 邊距使版面整體上移、緊湊精美。
  - 依照指示微調了前四個卡片的內文敘述，並將「**每個人**」、「**脫癮而出**」、「**連結**」、「**糾結**」、「**價值觀**」與「**生命主權**」高亮加粗。
- [x] **清理專案多餘資源**：彻底刪除了已無用途的 `80px` 與 `150px` 圖片資料夾與檔案。
- [x] **發佈部署至網站根目錄**：將完成的新版設計複製至專案根目錄發佈，並刪除臨時的 `xinyoutang` 子目錄。
- [x] **按鈕下載並開啟 PDF**：已實現點擊「下載一頁介紹」按鈕後，同時觸發瀏覽器下載 PDF 檔案與在新分頁（Tab）中自動打開該 PDF 供閱讀。
- [x] **網站內容修正、自動備份及 Logo 鏤空去背優化**：
  - 依照指示修改事工發起源起段落及 FAQ 第 4 題文字。
  - 修正「校園講座」介紹中的英文 "of" 為中文 "的"。
  - 優化部署程式 `update_web.py`，每次更新時自動備份完整檔案至 `Backup` 資料夾並推送至 GitHub 用於緊急復原。
  - 分別對淡色版 Header Logo 及深色版 Footer Logo 重新高精度鏤空去背（消除字體內部的殘留白點，並將 Footer 文字改為純白）。
- [x] **GitHub Pages 發佈與託管**。
- [x] **Firebase Firestore 表單連線**：已成功串接 Cloud Firestore，表單能自動將使用者填寫的聯絡資訊（姓名、信箱、主題、訊息、時間戳記）寫入 `contact_messages` 資料庫，並設定了安全的寫入規則（僅允許所有人 create 寫入，禁止 read/update/delete 讀取或修改，確保安全防護）。
- [x] **EmailJS 電子郵件通知整合**：在 `script.js` 與 `index.html` 中引入並配置 EmailJS SDK，綁定 Gmail 發信服務，解決了 Service ID/Template ID 不匹配與 v4 公鑰傳參物件格式等問題，已順利完成端到端發信驗證，管理員信箱（davidcmchang@gmail.com）可成功即時接收通知。
- [x] **網頁標題與圖示 (Favicon) 更換**：將網頁名稱修改為精簡的 `脫引 Twording`；將用戶提供之 Logo 圖片經 Python (BFS 演算法) 進行高精度去背、裁切與比例微調，產出透明背景的 `favicon.png` 與擁有多尺寸的 `favicon.ico` 網頁小圖示，成功修復了 `/favicon.ico 404` 錯誤。

### 🚀 下一步計畫
- [ ] 視後續營運需求，更新或新增網頁宣傳內容、常見問題或表單欄位。
- [ ] 協助用戶在 Gmail 網頁版中啟用 `towardingDawn@gmail.com` 至 `davidcmchang@gmail.com` 的自動信件轉寄設定。

### ⚠️ 踩坑與解決方案紀錄
*   **Windows 下 Git Dubious Ownership**：在 Windows 環境的 Git 初始化時容易觸發安全例外，已透過 `git config --global --add safe.directory` 解決。
*   **Logo 去背與變形**：用戶上傳的 Logo 為 JPG 純白背景，已透過自製 Python 腳本轉為透明 PNG，並在 CSS 裡使用 `width: auto; object-fit: contain;` 以防圖片拉伸變形。
*   **Windows Shell 逸出字元**：直接在 CLI 中呼叫 JSON 容易因逸出字元導致 HTTP 422 錯誤，已透過在 scratch 建立 `pages_payload.json` 並作為 file input 來完美避開此問題。
*   **多處非相鄰 HTML 修改之損毀問題**：當使用 line-based replacement 工具對具有重疊或大量類似結構 tags 的 HTML 進行非相鄰多重修改時，容易引起結構錯亂或代碼遗漏。改用專門的 Python 腳本讀寫檔案並執行精準字串替換，能 100% 確保結構正確且高效。
*   **瀏覽器快取 HTML 與 EmailJS 公鑰失效**：由於 GitHub Pages 靜態網站具有 HTML 快取，更新後 `index.html` 的公鑰可能未被即時載入，導致「Public Key is invalid」錯誤。解決方案是將公鑰直接寫在 `script.js` 中，並作為 `emailjs.send` 的第四個參數傳入以強制覆蓋。
*   **EmailJS v4 參數格式變更**：EmailJS Browser SDK 第 4 版中，`emailjs.send` 的第四個參數必須是 `{ publicKey: "..." }` 的 options 物件格式，如果像舊版一樣直接帶入字串，會導致公鑰被解析為 undefined 並報 400 錯誤。
*   **EmailJS 變數大小寫敏感**：EmailJS 的模板變數（例如 `{{subject}}`）嚴格區分大小寫，必須與 JavaScript 送出之物件 key（`subject`）完全一致，否則主題與信件無法渲染。
