from Model import GPSData
from Model import SunLocation
from Model.SunLocation import SunLocation

from Model.SunTime import SunTime

from Model import CarWindow
import datetime

#import the gpio for the rasbery pie

class Logic():
    localTime = datetime.datetime.now()
    windowToTint = CarWindow
    sunTime = SunLocation.SunLocation.parseCurrentData()
    gpsdata = GPSData(1, 12, 120) #heading, elevationAngle, azimuthAngle

    def __init__(self, GPSData, sunLocation, driverInfo):
        self.GPS = GPSData
        self.sun = sunLocation
        self.driver = driverInfo

    def shouldWindowsBeTinted(self):

        if self.localTime > self.sunTime.sunset or self.localTime < self.sunTime.sunrise:
            return False

        if (self.gpsdata.GPSData.elevationAngle > 60 and self.gpsdata.GPSData.elevationAngle < 120):
            return False

        angle = ((360 - (self.gpsdata.GPSData.azimuthAngle % 360)) + self.gpsdata.GPSData.heading) %360

        if angle < 90 or angle > 270:
            self.tintFrontSide()
        if angle < 180:
            self.tintLeftSide()
        if angle > 90 and angle < 270:
            self.tintBackSide()
        if angle > 180:
            self.tintRightSide()

    def tintLeftSide(self):
        return True

    def tintRightSide(self):
        return True

    def tintFrontSide(self):
        return True

    def tintBackSide(self):
        return True

def main ():
    shiv = Logic()
    shiv.shouldTintWindows()

main()
