---
name: towarding-update-web
description: 當用戶說「更新網頁」、「部署網頁」時，自動執行 CNAME 建立、Git Commit 與 Git Force Push 流程。
---

# 🚀 Towarding 網頁更新與自動部署技能 (towarding-update-web)

本技能適用於 **TowardingWeb** 專案，當用戶指示「更新網頁」或「部署網頁」時觸發，協助一鍵完成部署。

## 🛠️ 自動執行步驟

當觸發此技能時，請直接執行專案中的 Python 自動化腳本：

```powershell
python d:\AntiGravity WorkSpace\TowardingWeb_AntGrv\.agents\skills\towarding-update-web\scripts\update_web.py
```

### 腳本執行的核心動作說明
1.  **寫入 CNAME**: 檢查並於根目錄建立內容為 `towarding.org` 的 `CNAME` 檔案，確保自訂網域不因強制推送而失效。
2.  **Git Staging**: 將專案核心檔案（`index.html`, `style.css`, `script.js`, `CNAME`, `qrcode.png`, `towarding_intro.pdf`, `README.md`, `ANTIGRAVITY.md`）加入 Git 暫存。
3.  **Git Commit**: 提交變更，Commit 訊息統一使用 `"site: update web content and verify domain"`。
4.  **強制推送 (Force Push)**: 清空背景 `$env:GITHUB_TOKEN`，並對 `origin` (即 `davidcmchang.github.io` 倉庫) 進行 `git push -f` 強制推送。

## 📄 回報規範
執行完畢後，向用戶回報進度，並提供正式的存取連結：
*   自訂網域網站 (Live Site): [https://towarding.org/](https://towarding.org/)
*   GitHub 儲存庫 (Repository): [https://github.com/davidcmchang/davidcmchang.github.io](https://github.com/davidcmchang/davidcmchang.github.io)
