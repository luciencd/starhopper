import astropy

class User:
    latitude = ""
    longitude = ""
    clear_sky_chart = ClearSkyChart()



class Astronomer:
    location;#astropy.coordinates.AltAz()


##cleardarksky class.
##No inheritance, because we need to get things done fast.
##has a reference to a user, because we need latitude and longitude.
##returns all the weather/seeing data from cleardarksky.
class ClearDarkSky:
    user = User()

    def getCloudCover():

    def getTransparency():

    def getSeeing():

    def getDarkness():

    def getWind():

    def getHumidity():

    def getTemperature():

    def apiCall():
