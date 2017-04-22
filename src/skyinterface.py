import astropy
import astropy.coordinates
from astropy.coordinates import EarthLocation
import os
import requests

class Astronomer:
    #astropy.coordinates.AltAz()
    def __init__(self,location):
        self.location = location

    def getTime(self):
        return time

    def getObject(self,name):
        ##Perhaps get name to astropyname database going in dynamoDB in AWS?
        ##for now, astropy should be good enough for most objects.
        ##Should accept Messier designation, NGC, and proper noun name. #perhaps interface with a
        return string#returns the astropy object.

    def getRADEC(self,obj):
        return RADEC#Ra Dec astropy object.

    def getAltAz(self,obj):
        return ALTAZ#altaz astropy object

    def getClosestParallel(self,obj):
        return astrobject

    def getRandomParallel(self):
        return (astrobject1,astrobject2)##A bright star and a


##cleardarksky class.
##No inheritance, because we need to get things done fast.
##has a reference to a user, because we need latitude and longitude.
##returns all the weather/seeing data from cleardarksky.
class ClearDarkSky:
    #Cache data for the past hour.
    ##api limits to 1000 api calls.
    def __init__(self,location):
        self.location = location
        self.api_key = os.getenv("DARK_SKY_API_KEY",'')
        self.url = "https://api.darksky.net/forecast/"
        self.cachedJSON = ""#not necessary until we need to reduce processing time, or api calls.

    def getJSON(self):
        url = self.url+self.api_key+"/"+self.location.latitude()+","+self.location.longitude()
        r = requests.get(url)
        print r

    def getCloudCover():
        ##caching attempt, but now ignore this.
        json = getJSON()
        data = json["currently"]["data"]
        cloud_cover = data["cloudCover"]
        return cloud_cover

    def getTransparency():
        json = getJSON()
        data = json["currently"]["data"]
        transparency = data["transparency"]
        return transparency

    def getVisibility():
        json = getJSON()
        data = json["currently"]["data"]
        visibility = data["visibility"]
        return visibility

    def getDarkness():
        ##
        pass

    def getWind():
        json = getJSON()
        data = json["currently"]["data"]
        wind_speed = data["windSpeed"]
        return wind_speed

    def getHumidity():
        json = getJSON()
        data = json["currently"]["data"]
        humidity = data["humidity"]
        return humidity

    def getTemperature():
        json = getJSON()
        data = json["currently"]["data"]
        visibility = data["temperature"]
        return temperature



class User:
    def __init__(self,longitude,latitude):
        self.latitude = latitude
        self.longitude = longitude

        earthloc = EarthLocation(longitude,latitude,20)
        print earthloc
        self.location = earthloc.from_geodetic(longitude,latitude,20)
        print "latitude:",self.location.latitude
        print "longitude:",self.location.longitude

        self.clear_dark_sky = ClearDarkSky(self.location)
        self.astronomer = Astronomer(self.location)

    ##wrapper classes called by ALEXA
    #weather classes
    #def getCloudCover():
        #

    #...
    #wrapper classes for astronomer
    ##
