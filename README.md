# MPV-Play-BAHA-Comments
配合 Play-with-MPV 自動產生動畫瘋原生風格的彈幕
# 運行效果
![螢幕擷取畫面 2024-02-19 211436](https://github.com/s594569321/MPV-Play-BAHA-Comments/assets/81683926/e053f6b1-71de-4a30-9b47-029402d74521)
# 安裝
1.安裝 Play-With-MPV Tampermonkey腳本  

腳本載點: https://greasyfork.org/zh-CN/scripts/444056-play-with-mpv  

2.將 BahaAssert 放在 MPV 資料夾底下的 scripts 資料夾內
# 快捷功能

按下 j 可以開關彈幕

# 注意事項

如果遇到第一次使用時沒有出現彈幕，先讓 MPV 設定成以系統管理員身分執行再重開即可

理論上只有開啟過一次權限後面就算關掉也不會有問題

主要原因是透過 Lua script 觸發 python 寫入 ass 彈幕資料時有機會遇到權限不足

我在開發程式時遇到過一次，開啟權限一次後就再也沒遇過了

# Reference
MPV-Play-BiliBili-Comments: https://github.com/itKelis/MPV-Play-BiliBili-Comments?tab=readme-ov-file  
aniGamerDanmu: https://github.com/a20034294/aniGamerDanmu  
ani-gamer-danmu: https://github.com/Yooootsuba/ani-gamer-danmu  
