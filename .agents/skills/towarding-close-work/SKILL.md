---
name: towarding-close-work
description: 當用戶說「收工」時，自動備份最新網頁檔案至日期目錄下，然後執行檢查敏感資訊、更新日誌與 Git 提交推送。
---

# 🚪 Towarding 收工與自動備份技能 (towarding-close-work)

本技能適用於 **TowardingWeb** 專案，當用戶說「收工」時觸發。

## 🛠️ 自動執行步驟

### 第一步：備份最新網頁檔案
在執行任何其他收工動作前，請直接執行以下 Python 備份腳本，將當天網頁最新版本所有用到的相關檔案複製到工作目錄下的日期子目錄（格式為 `YYYYMMDD`）：

```powershell
python "d:\AntiGravity WorkSpace\TowardingWeb_AntGrv\.agents\skills\towarding-close-work\scripts\backup_web.py"
```

### 第二步：執行原本的收工動作
1.  **檢查敏感資料**：確保沒有將 API Keys、Tokens、密碼或個人隱私資訊寫入程式碼中。
2.  **更新專案日誌**：在 [README.md](file:///d:/AntiGravity%20WorkSpace/TowardingWeb_AntGrv/README.md) 中更新「已完成事項」、「下一步計畫」及「遇到的問題/踩坑紀錄」。
3.  **檢查 Git 狀態**：執行 `git status` 與 `git diff`。
4.  **精確 Commit 與 Push**：只將本次開發相關的檔案加入暫存區（避免直接 `git add .`），確認無誤後 commit 並 push 到 GitHub 遠端倉庫。
