'''
using inCar/ user Input to get and set following data
    - local irradiation (Sunny, Cloudt, etc....)
    - angle of the front glass
    - distance between roof and head
    - distance of head from the front window
    - sunriseTime
    - Cloudiness
'''

class DriverInfo():

    def __init__(self, verticle, horizontal, glassAngle, shadeLength):
        self.verticle = verticle
        self.horizontal = horizontal
        self.glassAngle = glassAngle
        self.shadeLength = shadeLength

    @property
    def verticle(self):
        return self._verticle

    @verticle.setter
    def verticle(self, value):
        self._verticle = value

    @property
    def horizontal(self):
        return self._horizontal

    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = value

    @property
    def glassAngle(self):
        return self._verticle

    @glassAngle.setter
    def glassAngle(self, value):
        self._glassAngle = value

    @property
    def shadeLength(self):
        return self._shadeLength

    @shadeLength.setter
    def shadeLength(self, value):
        self._shadeLength = value