class SunTime():

    def __init__(self, sunrise, sunset,  solarNoon, currentCloudiness):
        self.sunrise = sunrise
        self.sunset = sunset
        self.currentCloudiness = currentCloudiness


    @property
    def sunrise(self):
        return self._sunrise

    @sunrise.setter
    def sunrise(self, value):
        self._sunrise = int(value)


    @property
    def sunset(self):
        return self._sunset

    @sunset.setter
    def sunset(self, value):
        self._sunset = int(value)


    @property
    def currentCloudiness(self):
        return self._currentCloudiness

    @currentCloudiness.setter
    def currentCloudiness(self, value):
        self._sunset = int(value)