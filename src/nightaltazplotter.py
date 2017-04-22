##python practice file
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
bear_mountain = EarthLocation(lat=42.6*u.deg, lon=-83.14*u.deg, height=0.0*u.m)
utcoffset = -4*u.hour  # Eastern Daylight Time
time = Time('2017-2-1 23:00:00') - utcoffset

midnight = Time('2017-2-2 00:00:00') - utcoffset
delta_midnight = np.linspace(-2, 10, 100)*u.hour
'''

plt.plot(delta_midnight, m33airmasss_July13night)
plt.xlim(-2, 10)
plt.ylim(1, 4)
plt.xlabel('Hours from EDT Midnight')
plt.ylabel('Airmass [Sec(z)]')
plt.show()
'''
###the sun
from astropy.coordinates import get_sun
delta_midnight = np.linspace(-12, 12, 1000)*u.hour
times_July12_to_13 = midnight + delta_midnight
frame_July12_to_13 = AltAz(obstime=times_July12_to_13, location=bear_mountain)
sunaltazs_July12_to_13 = get_sun(times_July12_to_13).transform_to(frame_July12_to_13)
plt.plot(delta_midnight, sunaltazs_July12_to_13.alt, color='r', label='Sun')



def objectSky(name):
    m33 = SkyCoord.from_name(name)



    m33altaz = m33.transform_to(AltAz(obstime=time,location=bear_mountain))
    print(name+"'s Altitude = {0.alt:.2}".format(m33altaz))


    frame_July13night = AltAz(obstime=midnight+delta_midnight,
                              location=bear_mountain)
    m33altazs_July13night = m33.transform_to(frame_July13night)


    m33airmasss_July13night = m33altazs_July13night.secz

    m33altazs_July12_to_13 = m33.transform_to(frame_July12_to_13)
    ###specific stars
    plt.scatter(delta_midnight, m33altazs_July12_to_13.alt,
                c=m33altazs_July12_to_13.az, label=name, lw=0, s=8,
                cmap='viridis')
    #return (m33altazs_July12_to_13,)


objectSky("SAO 109740")
objectSky("Sirrah")






#after shit.
plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                 sunaltazs_July12_to_13.alt < -0*u.deg, color='0.5', zorder=0)
plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                 sunaltazs_July12_to_13.alt < -18*u.deg, color='k', zorder=0)
plt.colorbar().set_label('Azimuth [deg]')
plt.legend(loc='upper left')
plt.xlim(-12, 12)
plt.xticks(np.arange(13)*2 -12)
plt.ylim(0, 90)
plt.xlabel('Hours from EDT Midnight')
plt.ylabel('Altitude [deg]')
plt.show()
