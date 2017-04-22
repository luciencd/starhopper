import astropy

class Astronomer:
    location;#astropy.coordinates.AltAz()
    def __init__(self,location):
        self.location = location

    def getTime(self):
        return time

    def getObject(self,name):
        ##Should accept Messier designation, NGC, and proper noun name.
        return string#returns the astropy object.

    def getRADEC(self,obj):
        return RADEC#Ra Dec astropy object.

    def getAltAz(self,obj):
        return ALTAZ#altaz astropy object

    def getClosestParallel(self,obj):
        return astrobject

    def getRandomParallel(self):
        return (astrobject1,astrobject2)##A bright star and a


import os
##cleardarksky class.
##No inheritance, because we need to get things done fast.
##has a reference to a user, because we need latitude and longitude.
##returns all the weather/seeing data from cleardarksky.
class ClearDarkSky:

    def __init__(self,location):
        self.location = location
        self.api_key = os.getenv("DARK_SKY_API_KEY",'')
        self.url = "https://api.darksky.net/forecast/"
    /37.8267,-122.4233
    def getJSON():
        url = self.url+self.api_key+"/"+self.location.latitude()+","+self.location.longitude()

        

    def getCloudCover():

    def getTransparency():

    def getSeeing():

    def getDarkness():

    def getWind():

    def getHumidity():

    def getTemperature():

    def apiCall():



class User:
    latitude = ""
    longitude = ""
    clear_sky_chart = ClearSkyChart()
    astronomer = Astronomer()
