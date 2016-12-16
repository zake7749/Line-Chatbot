from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET) # 用於處理 Line 傳過來的訊息


# 用於防範 CSRF
@csrf_exempt
def callback(request):
    if request.method == 'POST':

        # 取得憑證，用於解析時確認訊息是真的來自 Line-Server
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        # 解析事件類型
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError: # 訊息並非來自 Line Server
            return HttpResponseForbidden()
        except LineBotApiError: # Line Server 出現狀況
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage): # 確保為文字訊息
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
