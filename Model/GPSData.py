#!/usr/bin/enc python

#import gps

'''
using GPS chip to get and set following data
    - Latitude
    - Longitude
    - Altitude
    - Speed
    - Heading
    - Climb
    - Elevation Angle
    - Azimuth Angle
    - UTC
'''

class GPSData():


   # def __init__(self, latitude, longitude, altitude, speed, heading, climb, elevationAngle, azimuthAngle, UTC):
    #    self.latitude = latitude
    #    self.longitude = longitude
    #    self.altitude = altitude
    #    self.speed = speed
    #    self.heading = heading
    #   self.climb = climb
        #self.elevationAngle = elevationAngle
        #self.azimuthAngle = azimuthAngle
        #self.UTC = UTC

    def __init__(self, heading, elevationAngle, azimuthAngle):
        self.heading = heading
        self.elevationAngle = elevationAngle
        self.azimuthAngle = azimuthAngle

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        self._altitude = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading= int(value)

    @property
    def climb(self):
        return self._climb

    @climb.setter
    def climb(self, value):
        self._climb = value

    @property
    def elevationAngle(self):
        return self._elevationAngle

    @elevationAngle.setter
    def elevationAngle(self, value):
        self._elevationAngle = int(value)

    @property
    def azimuthAngle(self):
        return self._azimuthAngle

    @azimuthAngle.setter
    def azimuthAngle(self, value):
        self._azimuthAngle = int(value)

    @property
    def UTC(self):
        return self._UTC

    @UTC.setter
    def UTC(self, value):
        self._UTC = value