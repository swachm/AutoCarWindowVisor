import datetime


class Logic:

    localTime = datetime.datetime.now()
    carLeft = carRight = carFront = carBack = False

    def __init__(self, GPSData):
        self.GPS = GPSData

    def shouldWindowsBeTinted(self):

        if 60 < self.GPS.elevationAngle < 120:
            print("GPS Elevation angle shows no tinting required")
            return False
        if 180 < self.GPS.elevationAngle < 360:
            print("Sun is below the horizon")
            return False

        angle = ((360 - (self.GPS.azimuthAngle % 360)) + self.GPS.heading) % 360

        if angle < 90 or angle > 270:
            self.carFront = True
        else:
            self.carFront = False

        if 0 < angle < 180:
            self.carLeft = True
        else:
            self.carLeft = False

        if 90 < angle < 270:
            self.carBack = True
        else:
            self.carBack = False

        if angle > 180:
            self.carRight = True
        else:
            self.carRight = False
