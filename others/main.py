import requests

# hide warnings
import warnings
warnings.filterwarnings("ignore")

# .env
from decouple import config

# datetimes
from datetime import datetime
year_month_day = datetime.strftime(datetime.now(), "%Y-%m-%d")

# variables
API_KEY_ENV=config("API_KEY")
API_CITY_NAME='TAQUARAL'
#API_CITY_ID=3411454
# MIRASSOL 3457095
# DRACENA 3459452
# GUAPIACU 3461954
# POTIRENDABA 3452547
# BADY BASSITT 3471210
# PRESIDENTE BERNARDES 3452335
# SANTA BARBARA DOESTE 3450404

# link_weather_day
link_weather_day = f'https://api.openweathermap.org/data/2.5/weather?q={API_CITY_NAME}&lang=pt_br&appid={API_KEY_ENV}'
#link_weather_day = f'https://api.openweathermap.org/data/2.5/weather?id={API_CITY_ID}&lang=pt_br&appid={API_KEY_ENV}'
reqs_weather_day = requests.get(link_weather_day)
reqs_weather_day_dic = reqs_weather_day.json()

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

# [new dictionary]
# descrição
current_daily_id = reqs_weather_day_dic['id']
current_daily_name = reqs_weather_day_dic['name']
current_daily_descript = reqs_weather_day_dic['weather'][0]['description']
current_daily_temp_day = reqs_weather_day_dic['main']['temp'] -273.15
current_daily_temp_min = reqs_weather_day_dic['main']['temp_min'] -273.15
current_daily_temp_max = reqs_weather_day_dic['main']['temp_max'] -273.15
current_daily_lat = reqs_weather_day_dic['coord']['lat']
current_daily_lon = reqs_weather_day_dic['coord']['lon']

print(reqs_weather_day_dic)

# link_weather_interval_3hrs_5days
#link_weather_interval = f'https://api.openweathermap.org/data/2.5/forecast?lat={current_city_lat}&lon={current_city_lon}&lang=pt_br&appid={API_KEY_ENV}'
#
#reqs_weather_interval = requests.get(link_weather_interval)
#reqs_weather_interval_dic = reqs_weather_interval.json()
#
#current_city_id = reqs_weather_interval_dic['city']['id']
#current_city_name = reqs_weather_interval_dic['city']['name']
#current_city_country = reqs_weather_interval_dic['city']['country']
#current_city_population = reqs_weather_interval_dic['city']['population']
#current_city_timezone = reqs_weather_interval_dic['city']['timezone']
#
#
#for interval_list in reqs_weather_interval_dic['list']:
#    current_city_interval_id = interval_list['city']['id']
#    current_city_interval_dt_unix = interval_list['dt']
#    current_city_interval_main_temp = interval_list['main']['temp']
#    current_city_interval_main_fells_like = interval_list['main']['feels_like']
#    current_city_interval_main_temp_min = interval_list['main']['temp_min']
#    current_city_interval_main_temp_max = interval_list['main']['temp_max']
#    current_city_interval_main_humidity = interval_list['main']['humidity']
#    current_city_interval_weather_main = interval_list['weather']['main']
#    current_city_interval_weather_description = interval_list['weather']['description']
#    current_city_interval_weather_icon = interval_list['weather']['icon']


#print(reqs_weather_interval_dic)




