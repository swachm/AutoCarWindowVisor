#!/usr/bin/enc python
from Model import GPSData
import urllib.request
import json

'''
using API to get and set following data
    - localTime
    - sunsetTime
    - sunriseTime
    - solarNoon
    - Cloudiness

need data from the GPS Class:
    - Latitude
    - Longitude
'''

GPSInfo = GPSData.GPSData

class sunLocation():
    """docstring for httpRequest"""
    currentDataURL = "http://api.sunrise-sunset.org/json?lat="

    def makeCurrentURLRequest(self):
        url = str(self.currentDataURL) + str(GPSInfo.latitude) + "&lng=" + str(GPSInfo.longitude) + "&date=today"
        return self.parseToJson(self.url)


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
            solarNoon = getData["results"]["solar_noon"]
        else:
            sunset = 0
            sunrise = 0
            solarNoon = 0
