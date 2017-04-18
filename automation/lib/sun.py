import pytz
import datetime
from django.utils.timezone import get_current_timezone
from astral import Astral

class Sun(object):
    """description of class"""
    #tz = pytz.timezone('Europe/Bucharest')
    tz = get_current_timezone()
    @staticmethod
    def Get(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        a = Astral()
        a.solar_depression = 'civil'
        city = a[city_name]
        sun = city.sun(date=date, local=True)
        #sun['dawn'], sun['sunrise'], sun['noon'], sun['sunset'], sun['dusk']
        return sun

    @staticmethod
    def IsDay(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        sun = Sun.Get(city_name, date)
        return sun['sunrise'] < date and date < sun['sunset']

    @staticmethod
    def Sunset(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        sun = Sun.Get(city_name, date)
        return sun['sunset'].time()

    @staticmethod
    def Sunrise(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        sun = Sun.Get(city_name, date)
        return sun['sunrise'].time()

    @staticmethod
    def Dusk(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        sun = Sun.Get(city_name, date)
        return sun['dusk'].time()

    @staticmethod
    def Dawn(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        sun = Sun.Get(city_name, date)
        return sun['dawn'].time()

    @staticmethod
    def Noon(city_name:str = 'Bucharest', date = datetime.datetime.now(tz)):
        sun = Sun.Get(city_name, date)
        return sun['noon'].time()

    @staticmethod
    def Now():
        return datetime.datetime.now(Sun.tz).time()
