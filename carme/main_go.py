from carme.core import (
    add_weather_current_to_database,
    get_weather_current_from_database, 
    add_cities_to_database,
    get_cities_from_database,
    add_interval_to_database,
    delete_interval_from_database,
    get_all_interval_from_database,
    get_interval_current_day_from_database,
    )
# hide warnings
import warnings
warnings.filterwarnings("ignore")

import requests
# .env
from decouple import config

# datetimes
from datetime import datetime
year_month_day = datetime.strftime(datetime.now(), "%Y-%m-%d")
reduce_celcius = 273.15
# variables
API_KEY_ENV=config("API_KEY")
#API_CITY_NAME='CAMPINAS'

def handle_update_data_to_database(city_id: int) -> str:
    API_CITY_ID=city_id   
    #"http://openweathermap.org/img/wn/10d@2x.png"
    # link_weather_day
    #link_weather_day = f'https://api.openweathermap.org/data/2.5/weather?q={API_CITY_NAME}&lang=pt_br&appid={API_KEY_ENV}'
    link_weather_day = f'https://api.openweathermap.org/data/2.5/weather?id={API_CITY_ID}&lang=pt_br&appid={API_KEY_ENV}'
    reqs_weather_day = requests.get(link_weather_day)
    reqs_weather_day_dic = reqs_weather_day.json()

    # [new dictionary]
    # descrição
    current_daily_id = reqs_weather_day_dic['id']
    current_daily_name = reqs_weather_day_dic['name']
    current_daily_descript = reqs_weather_day_dic['weather'][0]['description']
    current_daily_temp_day = reqs_weather_day_dic['main']['temp'] - reduce_celcius
    current_daily_temp_min = reqs_weather_day_dic['main']['temp_min'] - reduce_celcius
    current_daily_temp_max = reqs_weather_day_dic['main']['temp_max'] - reduce_celcius
    current_daily_lat = reqs_weather_day_dic['coord']['lat']
    current_daily_lon = reqs_weather_day_dic['coord']['lon']


    return_weather_current = add_weather_current_to_database(
        id_data=current_daily_id, 
        city_name=current_daily_name, 
        description=current_daily_descript, 
        temp_day=current_daily_temp_day, 
        temp_min=current_daily_temp_min, 
        temp_max=current_daily_temp_max, 
        temp_city_lat=current_daily_lat, 
        temp_city_lon=current_daily_lon)

    if return_weather_current:
        print(f'WeatherCurrent: {current_daily_name} adicionado.')
        
        # link_weather_interval_3hrs_5days
        link_weather_interval = f'https://api.openweathermap.org/data/2.5/forecast?lat={current_daily_lat}&lon={current_daily_lon}&lang=pt_br&appid={API_KEY_ENV}'

        reqs_weather_interval = requests.get(link_weather_interval)
        reqs_weather_interval_dic = reqs_weather_interval.json()

        current_city_id = reqs_weather_interval_dic['city']['id']
        current_city_name = reqs_weather_interval_dic['city']['name']
        current_city_country = reqs_weather_interval_dic['city']['country']
        current_city_population = reqs_weather_interval_dic['city']['population']
        current_city_timezone = reqs_weather_interval_dic['city']['timezone']

        return_citie = add_cities_to_database(
            id_data=current_city_id, 
            city_name=current_city_name, 
            city_country=current_city_country, 
            city_population=current_city_population, 
            city_timezone=current_city_timezone) 
        
        # Clear data > unix_timestamp and id_data
        current_time = datetime.now()   
        unix_timestamp = int(datetime.timestamp(current_time))
        print(unix_timestamp)
        deleted_unix_interval = delete_interval_from_database(interval_dt_unix=unix_timestamp, id_data=current_city_id)
                    
        if return_citie and deleted_unix_interval:
            print(f'Cities id: {current_daily_id} adicionado.')       

            ciclos = 0
            # interval 5 day / 3hrs forecast data
            for interval_list in reqs_weather_interval_dic['list']:
                current_city_interval_id = current_city_id
                current_city_interval_dt_unix = interval_list['dt']
                current_city_interval_main_temp = interval_list['main']['temp'] - reduce_celcius
                current_city_interval_main_fells_like = interval_list['main']['feels_like'] - reduce_celcius
                current_city_interval_main_temp_min = interval_list['main']['temp_min'] - reduce_celcius
                current_city_interval_main_temp_max = interval_list['main']['temp_max'] - reduce_celcius
                current_city_interval_main_humidity = interval_list['main']['humidity'] 
                current_city_interval_weather_main = interval_list['weather'][0]['main']
                current_city_interval_weather_description = interval_list['weather'][0]['description']
                current_city_interval_weather_icon = interval_list['weather'][0]['icon']

                type_interval = add_interval_to_database(
                    id_data=current_city_interval_id, 
                    interval_dt_unix=current_city_interval_dt_unix, 
                    current_city_interval_main_temp=current_city_interval_main_temp, 
                    current_city_interval_main_fells_like=current_city_interval_main_fells_like,
                    current_city_interval_main_temp_min=current_city_interval_main_temp_min,
                    current_city_interval_main_temp_max=current_city_interval_main_temp_max,
                    current_city_interval_main_humidity=current_city_interval_main_humidity,
                    current_city_interval_weather_main=current_city_interval_weather_main,
                    current_city_interval_weather_description=current_city_interval_weather_description,
                    current_city_interval_weather_icon=current_city_interval_weather_icon,
                    unix_timestamp=unix_timestamp) 
                ciclos += 1
            print(f'Interval id: {current_daily_id} , ciclos: {ciclos}, adicionados.')

    return f'Concluido { current_daily_name }'

def __init__(self):
    print('start')  

if __name__ == "__main__":
    string = 'Atenção \N{SNAKE}'
    print(string)