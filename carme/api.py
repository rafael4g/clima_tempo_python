from carme.core import (
    get_weather_current_from_database, 
    add_weather_current_to_database,
    add_cities_to_database,
    get_cities_from_database,
    add_interval_to_database,
    get_interval_from_database,
    )
#from .core import add_weather_current_to_database, get_weather_current_from_database
#from .database import get_session
#from .models import Cities, Interval, WeatherCurrent
#from .serializers import WeatherCurrentIn, WeatherCurrentOut

"""
{
    'coord': {'lon': -47.0608, 'lat': -22.9056}, 
    'weather': [{'id': 802, 'main': 'Clouds', 'description': 'nuvens dispersas', 'icon': '03d'}], 
    'base': 'stations', 
    'main': {'temp': 302.04, 'feels_like': 304.15, 'temp_min': 302.04, 'temp_max': 302.04, 'pressure': 1020, 'humidity': 61}, 
    'visibility': 10000, 
    'wind': {'speed': 2.57, 'deg': 150}, 
    'clouds': {'all': 40}, 
    'dt': 1677507930, 
    'sys': {'type': 1, 'id': 8393, 'country': 'BR', 'sunrise': 1677488593, 'sunset': 1677533950}, 
    'timezone': -10800, 
    'id': 3467865, 
    'name': 'Campinas', 
    'cod': 200
}
"""

id_data=3458575
city_name='Limeira'
city_country='BR'
city_population=22605
city_timezone='-10800'
description='nuvens dispersas'
temp_day='302.04'
temp_min='302.04'
temp_max='302.04'
temp_city_lat='-22.9056'
temp_city_lon='-47.0608'

type_return = add_weather_current_to_database(
    id_data=id_data, city_name=city_name, description=description, temp_day=temp_day, temp_min=temp_min, temp_max=temp_max, 
    temp_city_lat=temp_city_lat, temp_city_lon=temp_city_lon)

if type_return:
    city = 'Limeira'
    weathers = get_weather_current_from_database(city=city)
    print(weathers)
 
#type_cities = add_cities_to_database(
#    id_data=id_data, city_name=city_name, city_country=city_country, 
#    city_population=city_population, city_timezone=city_timezone) 
#
#if type_cities:
#    city = 'Campinas'
#    cities = get_cities_from_database(city=city)
#    print(cities)


#id_data=3458575
#interval_dt_unix=1677520700
#current_city_interval_main_temp='302.04'
#current_city_interval_main_fells_like='302.04'
#current_city_interval_main_temp_min='302.04'
#current_city_interval_main_temp_max='302.04'
#current_city_interval_main_humidity=81
#current_city_interval_weather_main='Cloud'
#current_city_interval_weather_description='Nublado'
#current_city_interval_weather_icon='04d'
#
#
#type_interval = add_interval_to_database(
#    id_data=id_data, 
#    interval_dt_unix=interval_dt_unix, 
#    current_city_interval_main_temp=current_city_interval_main_temp, 
#    current_city_interval_main_fells_like=current_city_interval_main_fells_like,
#    current_city_interval_main_temp_min=current_city_interval_main_temp_min,
#    current_city_interval_main_temp_max=current_city_interval_main_temp_max,
#    current_city_interval_main_humidity=current_city_interval_main_humidity,
#    current_city_interval_weather_main=current_city_interval_weather_main,
#    current_city_interval_weather_description=current_city_interval_weather_description,
#    current_city_interval_weather_icon=current_city_interval_weather_icon) 
#
#if type_interval:
#    id_data = '802'
#    interval_list = get_interval_from_database(id_data=id_data)
#    print(interval_list)    