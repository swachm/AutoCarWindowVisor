class SunTime:

    def __init__(self, sunrise, sunset):
        self.sunrise = sunrise
        self.sunset = sunset

    @property
    def sunrise(self):
        return self._sunrise

    @sunrise.setter
    def sunrise(self, value):
        self._sunrise = value

    @property
    def sunset(self):
        return self._sunset

    @sunset.setter
    def sunset(self, value):
        self._sunset = value
