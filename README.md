# 自動報班好夥伴
- 常常為了忘記報班而苦惱，因此動手寫了一個腳本來跑，沒啥技術含量，只是想讓自己更懶。
### 環境需求
- Python 3
- Selenium套件
- Firefox瀏覽器
- geckodriver(Mozilla推出的驅動程式，[Github載點在這](https://github.com/mozilla/geckodriver/releases))
    - 載下來之後，把裡面的geckodriver.exe拉到當前這個資料夾裡面，auto.py執行的時候才找的到

### 介紹
- 使用常見的Python Selenium
- 請先至config.sample.py依序填入目標網站、帳號、密碼等等需要的內容，再將config.sample.py重新命名為config.py，這樣腳本才讀的到你的帳密喔。
- 執行完成之後會輸出'報班成功!'，並且儲存一個截圖，可以當作確認的依據。
- 後續部署的步驟要請大家自行發揮(例如:Azure, 自己的主機...)，可以用個crontab讓它定期自動執行
### 執行
```
$ python auto.py
```