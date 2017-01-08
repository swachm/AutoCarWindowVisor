from Model import GPSData
from Model import sunLocation
from Model import  driverInfo
from Model import Directions
from Model import carWindow
#import the gpio for the rasbery pie

class lordsShiva():

    sunDirection = Directions
    windowToTint = carWindow
    def __init__(self, GPSData, sunLocation, driverInfo):
        self.GPS = GPSData
        self.sun = sunLocation
        self.driver = driverInfo

    '''
    Parameters which determine should the windows be tinted
        - time of the day
        - What side sun is on
        - elevation angle
        - driver horizontal
        - driver verticle
        - car window angle
    '''
    '''
    4 case when driving:
     - sun on the left side     // have to calculate
     - sun on the right side    // have to calculate
     - sun on the back side     // auto tinting on rearview camera, could use same circuit to tint back window
     - sun at front             // calculate
    '''
    def shouldTintWindows(self):

        if (self.shouldWindowsBeTinted() == True):
            if self.WhatSideShouldBeTinted() == "back":
                 self.tintBackSide()
             elif self.WhatSideShouldBeTinted() == "right":
                self.tintRightSide()
            elif self.WhatSideShouldBeTinted() == "left":
                self.tintLeftSide()
            else:
                self.tintFrontSide()
        else:
            return False

    def shouldWindowsBeTinted(self):
        return True

    '''
        direction  = abs (azimuth angle - driving angle)
        in total 4 sides sun can be on and 4 sides car could be facing
        if rounded up to 4. could be

        For Accuracy we could use
        - 0-45
        - 46-90
        - 91-135
        - 136-180
        - 181-225
        - 225-270
        - 271-315
        - 316-360

        8 cases of car  * 8 cases for sun = 64 cases
    '''

    def WhatSideShouldBeTinted(self):
        return False

    '''
        Get this from the GPS.
    '''
    def directionOfCar(self):
        return Directions.NORTH

    '''
        Determine the position of the sun around the car, depends on 2 variables:
            - azimuth angle
            - heading (GPS.heading)
    '''

    def directionOfSun(self):
        return "front"

    def tintLeftSide(self):
        return True

    def tintRightSide(self):
        return False

    def tintFrontSide(self):
        return True

    def tintBackSide(self):
        return True

def main ():
    shiv = lordsShiva()
