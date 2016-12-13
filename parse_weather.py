import requests

from util import get_env_variable

def main():

    wp = WeatherParser()

class  WeatherParser(object):

    def __init__(self):

        self.doc_name = "F-C0032-001"
        self.user_key = get_env_variable("WEATHER_AUTHORIZATION_KEY")
        self.api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (self.doc_name,self.user_key)


    def downloadWeatherReport(self):
        r = requests.get(self.api_link)
        with open('test.xml','r',encoding='utf-8') as op:
            op.write(r.text)
        return r.text

    def parseReport(self, report, location):
        #TODO
        pass

    def getReport(self, location):
        report = self.downloadWeatherReport()
        report = self.parseReport(report,location)
        return report


if __name__ == '__main__':
    main()
