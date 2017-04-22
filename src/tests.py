import unittest
import skyinterface

class TestStringMethods(unittest.TestCase):
    def setUp(self):

        self.user = skyinterface.User(latitude=42.7284,longitude=73.6918)

        #print lucien.clear_dark_sky.getCloudCover()

    def test_cloud_cover(self):
        self.user.clear_dark_sky.getCloudCover()
        pass

    def test_location_of_m33(self):
        m33location =  "1 33 50, +30 39 37"
        self.assertEqual(self.user.getRADEC('M33'),m33location)

    def test_location_of_jupiter_today(self):
        jupiterlocationtoday= "13 01 51.4 -4 53 52.9"
        ##april 22nd, 2017
        self.assertEqual(self.user.getRADEC('jupiter',time.time(1492894680.65)),jupiterlocationtoday)

    def test_altaz_of_north_star(self):
        northstarlocationatmidnight = "00 00 00 00 00 00"
        self.assertEqual(self.user.getAltAz('north star',time.time("April 23rd 2017, 00:00:00")))


if __name__ == '__main__':
    unittest.main()
