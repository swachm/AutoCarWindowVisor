#!/usr/bin/enc python
from Model import SunTime
import urllib.request
import json

class SunLocation():
    """docstring for httpRequest"""
    currentDataURL = "http://api.sunrise-sunset.org/json?lat="

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def makeCurrentURLRequest(self):
        url = str(self.currentDataURL) + str(self.latitude) + "&lng=" + str(self.longitude) + "&date=today"
        print(url)
        return self.parseToJson(url)

    def parseToJson(self, link):
        response = urllib.request.urlopen(link).read()
        decodedResponse = response.decode('utf8')
        data = json.loads(decodedResponse)
        return data

    def parseCurrentData(self):
        getData = self.makeCurrentURLRequest()

        status = getData["status"]
        if status == "OK":
            sunset = getData["results"]["sunset"]
            sunrise = getData["results"]["sunrise"]
        else:
            sunset = 0
            sunrise = 0

        sunData = SunTime.SunTime(sunrise, sunset)
        return sunData
