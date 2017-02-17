# Auto Car Window Visor

This hack is designed to create window tinting based on the conditions: time of the day, latitude, longitude, and heading of the car. The software uses an algorithm to determine the angle of the car relative to the sun. This dictates which window of the car should be tinted.

The original idea was to get an input from GPS (https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/using-your-gps), and weather data. The GPS is made but not available for testing at this time. The weather data would also be included to improve the tinting algorithm.

We saw the idea in a movie and thought of how to implement it in real life. The prototype would use a raspberry pie 3, relay and smart glass(http://www.smartglassinternational.com/). The raspberry pie would be used to run the algorithm and trigger the relay with 5Volt trigger. Once the relay switch is on it would power the smart glass and change its polarity.

Run the TestGUI.py and enter the following parameter:

Azimuth Angle: The angle of the sun from the North.
Elevation Angle: Angle of the Sun from the horizon.
Heading: The direction car is facing.


![alt tag](http://i.imgur.com/haofkhT.png)
