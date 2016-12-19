import parse_weather

def main():

    b = LineBot()
    while True:
        print(b.getResponse(input()))

class LineBot(object):

    """
    實現 Echo 與應答天氣訊息的聊天機器人
    """

    def __init__(self):

        self.weather_parser = parse_weather.WeatherParser()
        self.taiwan_cities = ["臺北市","新北市","桃園市","臺中市","臺南市",
                            "高雄市","基隆市","新竹市","嘉義市","新竹縣","苗栗縣",
                            "彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","宜蘭縣",
                            "花蓮縣","臺東縣","臺東市","澎湖縣","金門縣","連江縣"]

    def getResponse(self, sentence):

        """
        讀入一個句子, 傳回該句子對應的回覆
        """

        if "天氣" in sentence:
            location = self.getLocation(sentence)
            report = self.weather_parser.getReport(location) # 依照地點取得該地今天的天氣
            response = "目前%s的天氣是%s" % (location,report)
        else:
            response = self.echo(sentence)
        return response

    def getLocation(self, sentence):

        """
        比對 sentence 與臺灣的 23 個縣市,
        如果比對成功回傳該縣市名, 否則回傳臺南市
        """
        for city in self.taiwan_cities:
            if city in sentence:
                return city
        return "臺南市"

    def echo(self, sentence):
        return sentence

if __name__ == '__main__':
    main()
