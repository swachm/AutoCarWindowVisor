from Model.GPSData import GPSData
from Model.Logic import Logic
from Model.SunLocation import SunLocation
from PIL import Image

elevation = input("Enter Elevation angle: ")
alpha = input("Enter Azimuth angle: ")
heading = input("Enter heading: ")

testGPS = GPSData(heading, elevation, alpha)

testCar = Logic(testGPS)
testCar.shouldWindowsBeTinted()

pic = ""
if testCar.carFront:
    if testCar.carRight:
        pic = "assets/frontRightTint.png"
    else:
        if testCar.carLeft:
            pic = "assets/frontLeftTint.png"
        else:
            pic = "assets/frontTint.png"
elif testCar.carBack:
    if testCar.carRight:
        pic = "assets/backRightTint.png"
    else:
        if testCar.carLeft:
            pic = "assets/backLeftTint.png"
        else:
            pic = "assets/backTint.png"

if not testCar.carFront and not testCar.carBack:
    if testCar.carRight:
        pic = "assets/rightTint.png"
    if testCar.carLeft:
        pic = "assets/leftTint.png"
    if not testCar.carRight and not testCar.carLeft:
        pic = "assets/noTint.png"

Image.open(pic).show()
