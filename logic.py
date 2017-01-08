from Model import GPSData
from Model import sunLocation
from Model import  driverInfo

#import the gpio for the rasbery pie

class lordsShiva():

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


        if self.whatSideSunIsOn() == "back":
            self.tintBackSide()
        elif self.whatSideSunIsOn() == "right":
            self.tintRightSide()
        elif self.whatSideSunIsOn() == "left":
            self.tintLeftSide()
        else:
            self.tintFrontSide()

    '''
    Determine the position of the sun around the car, depends on 2 variables:
        - azimuth angle
        - heading (GPS.heading)
    '''
    def whatSideSunIsOn(self):
        return "front"

    '''
    direction  = abs (azimuth angle - driving angle)
    direction:
    0 front  +- 60
    90 right +- 60
    -90 left +- 60
    180 back +- 60
    '''

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
