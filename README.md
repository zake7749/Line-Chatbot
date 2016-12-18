# Line 天氣應答機器人
![Result](http://i.imgur.com/OEYUfCZ.jpg?1)
## 環境配置

本專案採用 python3 開發，

### 套件需求

```
Django==1.10.4
future==0.16.0
gunicorn==19.6.0
line-bot-sdk==1.0.2
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

Line 機器人的 Webhook URL 連結設定為：`https://lineweatherbot.herokuapp.com/line_bot/callback/`

## Heroku 配置

參考聊天機器人佈署：[\[[Bot] Deploy LineBot on Heroku \]](http://lee-w-blog.logdown.com/posts/1148021-deploy-linebot-on-heroku)
* 其中 Heroku 環境變數的設定要[稍做修正](https://devcenter.heroku.com/articles/config-vars)，更改為 `key=value`
* 請注意，在佈署至 Heroku 前務必完成*設定方式*中 4 個環境變數的配置
