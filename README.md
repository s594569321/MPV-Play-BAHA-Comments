# MPV-Play-BAHA-Comments
配合 External Player 自動產生動畫瘋原生風格的彈幕
# 運行效果
![螢幕擷取畫面 2024-02-19 211436](https://github.com/s594569321/MPV-Play-BAHA-Comments/assets/81683926/e053f6b1-71de-4a30-9b47-029402d74521)
# 安裝
1.安裝 External Player  

專案連結: https://github.com/LuckyPuppy514/external-player  

2.將 BahaAssert 放在 MPV 資料夾底下的 scripts 資料夾內

3.(可選) 目前新版 API 需登入巴哈取得 Cookie 才能獲取完整彈幕，否則會有部分彈幕缺失，這裡提供一個解決方案

3-1. 安裝 Get cookies.txt LOCALLY 瀏覽器差件

插件連結: https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc

3-2. 登入動畫瘋點擊插件並 Export Cookie.txt

![image](https://github.com/user-attachments/assets/59dc2f77-9fb3-4bd0-b366-9e0ece929a9f)

3-3. 將 Cookie.txt 放入 BahaAssert 資料夾中即可

# 快捷功能

按下 j 可以開關彈幕

# 注意事項
1.如果遇到第一次使用時沒有出現彈幕，先讓 MPV 設定成以系統管理員身分執行再重開即可

理論上只有開啟過一次權限後面就算關掉也不會有問題

主要原因是透過 Lua script 觸發 python 寫入 ass 彈幕資料時有機會遇到權限不足

我在開發程式時遇到過一次，開啟權限一次後就再也沒遇過了


2.如果有使用 Cookie.txt 需要時常更新否則過一段時間會自動失效，更換時'務必'將舊的 Cookie.txt 刪除乾淨


# Reference
MPV-Play-BiliBili-Comments: https://github.com/itKelis/MPV-Play-BiliBili-Comments?tab=readme-ov-file  
aniGamerDanmu: https://github.com/a20034294/aniGamerDanmu  
ani-gamer-danmu: https://github.com/Yooootsuba/ani-gamer-danmu  
