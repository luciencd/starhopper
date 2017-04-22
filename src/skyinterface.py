import astropy
import astropy.coordinates
from astropy.coordinates import EarthLocation
import os
import requests
import json
import time

class Astronomer:
    #astropy.coordinates.AltAz()
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def getTime(self):
        return time

    def getObject(self,name):
        ##Perhaps get name to astropyname database going in dynamoDB in AWS?
        ##for now, astropy should be good enough for most objects.
        ##Should accept Messier designation, NGC, and proper noun name. #perhaps interface with a
        return astroobject#returns the astropy object.

    def getRADEC(self,obj,time=time.time()):

        return RADEC#Ra Dec astropy object.

    def getAltAz(self,obj,time=time.time()):
        return ALTAZ#altaz astropy object

    def getClosestParallel(self,obj,time=time.time()):
        return astrobject

    def getRandomParallel(self,time=time.time()):
        return (astrobject1,astrobject2)##A bright star and a


##cleardarksky class.
##No inheritance, because we need to get things done fast.
##has a reference to a user, because we need latitude and longitude.
##returns all the weather/seeing data from cleardarksky.
class ClearDarkSky:
    #Cache data for the past hour.
    ##api limits to 1000 api calls.
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = os.getenv("DARK_SKY_API_KEY",'')
        self.url = "https://api.darksky.net/forecast/"
        self.cachedJSON = ""#not necessary until we need to reduce processing time, or api calls.

    def getJSON(self):
        print "getURL"
        url = self.url+self.api_key+"/"+str(self.latitude)+","+str(self.longitude)
        #print url
        r = requests.get(url)
        #print r.text
        return json.loads(r.text)

    def getCloudCover(self):
        ##caching attempt, but now ignore this.
        json = self.getJSON()
        data = json["currently"]
        cloud_cover = data["cloudCover"]
        return cloud_cover

    def getTransparency(self):
        json = self.getJSON()
        data = json["currently"]
        transparency = data["transparency"]
        return transparency

    '''def getVisibility(self):
        json = self.getJSON()
        data = json["currently"]
        visibility = data["visibility"]
        return visibility'''

    def getDarkness(self):
        ##
        pass

    def getWind(self):
        json = self.getJSON()
        data = json["currently"]
        wind_speed = data["windSpeed"]
        return wind_speed

    def getHumidity(self):
        json = self.getJSON()
        data = json["currently"]
        humidity = data["humidity"]
        return humidity

    def getTemperature(self):
        json = self.getJSON()
        data = json["currently"]
        visibility = data["temperature"]
        return temperature



class User:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude


        self.clear_dark_sky = ClearDarkSky(self.latitude,self.longitude)
        self.astronomer = Astronomer(self.latitude,self.longitude)

    ##wrapper classes called by ALEXA
    #weather classes
    #def getCloudCover():
        #
    def getCloudCover():
        return self.clear_dark_sky.getCloudCover()

    def getRADEC(name):
        return "nostar1"

    def getAltAz(name):
        return "nostar2"



    #...
    #wrapper classes for astronomer
    ##
