import requests
import datetime
import json

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

from util import get_env_variable

def main():

    wp = WeatherParser()
    print(wp.getReport("臺南市"))

class  WeatherParser(object):

    def __init__(self):

        self.doc_name = "F-C0032-001"
        self.user_key = get_env_variable("WEATHER_AUTHORIZATION_KEY")
        self.api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (self.doc_name,self.user_key)

    def getReportWithAPI(self, location):

        """
        [本次作業不會用到，助教可以忽略此函式]

        使用中央氣象局的 Restful API 提取資料

        Args:
            - location: 欲查詢的縣市名
        Return:
            - res.json(): 字典形式的天氣資料
        """

        headers = {'Authorization': self.user_key}
        res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?locationName=%s" % location,
                    headers=headers)
        return res.json()

    def parseJSONReport(self, report):

        """
        [本次作業不會用到，助教可以忽略此函式]

        從原始資料中去除不必要的 metadata，只抽取出該縣市的所有氣象資訊（不分時間、類型）

        Args:
            - report:
        Return:
            - weather_elements : 該縣市的氣象資訊列表
        """

        # 依照格式取出當地的氣象資訊
        # location 的 index 為零是因為只取 '1' 個城市的資料
        weather_elements = report['records']['location'][0]['weatherElement']

        #print(weather_elements)
        return weather_elements

    def getReport(self, location):

        """
        可以使用 XML 解析原文件,或者調用 Restful API 去取得氣象資訊

        Args:
            - location: 縣市名稱的字串
        Return:
            - report: 目前該縣市的天氣資訊
        """

        # With xml
        report = self.downloadXMLReport()
        description = self.parseXMLReport(report,location)

        # With Restful api
        # report = self.getReportWithAPI(location)
        # report = self.parseJSONReport(report)
        # weaher_element = self._getWeatherElement(report, data_type="Wx") # 取出 Wx (描述天氣狀況)的 element
        # description = self._selectTimeInterval(weaher_element)

        return description

    def downloadXMLReport(self):
        r = requests.get(self.api_link)
        return r.text

    def parseXMLReport(self, report, location):

        """
        解析 XML　格式的氣象資訊，回傳目標　location 的天氣資訊
        """

        xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
        root = et.fromstring(report)
        dataset = root.find(xml_namespace + 'dataset')
        locations_info = dataset.findall(xml_namespace + 'location')

        # 取得 <location> Elements,每個 location 就表示一個縣市資料
        target_idx = -1
        for idx,ele in enumerate(locations_info):
            locationName = ele[0].text # 取得縣市名
            if locationName == location:
                target_idx = idx
                break

        # 挑選出目前想要 location 的氣象資料
        weather_element = locations_info[target_idx][1] # 取出 Wx (氣象描述)
        block_of_current_time = weather_element[1] # 取出目前時間點的資料
        description = block_of_current_time[2][0].text
        return description

    def _selectTimeInterval(self, weather_element):

        """
        從原始資料的所有時間區段中，挑選出目前的時間區段

        Args:
            - weather_element : 某個 type 的天氣元素字典 (e.g: WX)
        Return:
            - description : 目前時間區段中該 type 的氣象描述
        """

        # 第一份資料為目前時間點
        return weather_element["time"][0]["parameter"]["paramterName"]

    def _getWeatherElement(self, weather_elements, data_type):
        """
        依照 type 從 weahter_elements 中挑出所需的元素

        Args:
            - weather_elements: 天氣元素的列表
            - data_type: 天氣元素的類型
                * Wx: 雲量
                * PoP: 降雨率
                * MinT: 最低溫度
                * MaxT: 最高溫度
                * CI: 寒冷指標
        """
        for ele in weather_elements:
            if ele["elementName"] == data_type:
                return ele

        print("_getWeatherElement(): 讀入未知的天氣類型 %s" % data_type)
        return None

if __name__ == '__main__':
    main()
