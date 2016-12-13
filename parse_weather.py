import requests


try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et
from util import get_env_variable

def main():

    wp = WeatherParser()
    wp.getReportWithAPI("臺北市")

class  WeatherParser(object):

    def __init__(self):

        self.doc_name = "F-C0032-001"
        self.user_key = get_env_variable("WEATHER_AUTHORIZATION_KEY")
        self.api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (self.doc_name,self.user_key)


    def downloadXMLReport(self):
        r = requests.get(self.api_link)
        with open('test.xml','r',encoding='utf-8') as op:
            op.write(r.text)
        return r.text

    def parseXMLReport(self, report, location):

        parseTree = et.ElementTree(report)
        print(et.tag)

    def getReportWithAPI(self, location):
        headers = {'Authorization': self.user_key}
        res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?locationName=%s" % location,
                    headers=headers)
        return res.json()
        #print(res.text)


    def getReport(self, location):

        """
        可以使用 XML 解析原文件,或者調用 Restful API
        """

        # With xml
        # report = self.downloadWeatherReport()
        # report = self.parseReport(report,location)

        # With Restful api
        report = self.getReportWithAPI(location)

        return report


if __name__ == '__main__':
    main()
