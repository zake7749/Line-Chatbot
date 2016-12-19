# Line 天氣應答機器人

![result](http://i.imgur.com/OEYUfCZ.jpg?1)

## 設計方式

### 聊天機器人

* 如果對話中包含「天氣」，則回覆目前臺南市的天氣
* 如果對話中包含「天氣」且存在臺灣縣市名，則回傳目前該縣市之天氣
  * 縣市名請用繁體表示，如「臺南市」而非「台南市」
* 否則回傳與輸入相同的對話

天氣資料來源為中央氣象局的開放資料平台，支援 RESTful API 與 XML 兩種爬取方式。

### Django 設定

參考[[Bot] Line Echo Bot on Django](http://lee-w-blog.logdown.com/posts/1134898-line-echo-bot-on-django)

## 環境配置

本專案採用 python-3.5.2 開發

### 套件需求

```
Django==1.10.4
future==0.16.0
gunicorn==19.6.0
line-bot-sdk==1.0.2
requests==2.12.3
```

### 環境變數

本專案一共會使用到四個環境變數

* SECRET_KEY
* LINE_CHANNEL_ACCESS_TOKEN
* LINE_CHANNEL_SECRET
* WEATHER_AUTHORIZATION_KEY:用於從[中央氣象局氣象資料開放平台](http://opendata.cwb.gov.tw/usages)取得資料，申辦完會員後即可取得

#### 設定方式
```sh
export SECRET_KEY='Your django secret key'
export LINE_CHANNEL_ACCESS_TOKEN='Your line channel access token'
export LINE_CHANNEL_SECRET='Your line channel secret'
export WEATHER_AUTHORIZATION_KEY='Your authorization key of opendata platform'
```
## Django 配置

```
Django Project: line_bot
└──app : line_weather_bot
```

Line 機器人的 連結 Line 聊天機器人 Webhook URL 連結設定為：`https://l的i## 設計方式

### 聊天機器人

### Django 配置

參考b

## Heroku 配置

參考聊天機器人佈署：[\[[Bot] Deploy LineBot on Heroku \]](http://lee-w-blog.logdown.com/posts/1148021-deploy-linebot-on-heroku)
* 其中 Heroku 環境變數的設定要[稍做修正](https://devcenter.heroku.com/articles/config-vars)，更改為 `key=value`
* 請注意，在佈署至 Heroku 前務必完成*設定方式*中 4 個環境變數的配置
