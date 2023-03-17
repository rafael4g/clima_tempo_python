from typing import List, Optional
from datetime import (
    datetime, 
    timedelta
)

# from sympy import im
from sqlmodel import select
from carme.database import get_session
from carme.models import WeatherCurrent, Cities, Interval

# table weatherCurrent
#------------------------------------------------------------------------------------
def add_weather_current_to_database(  
    id_data : int,
    city_name : str,
    description : str,
    temp_day : str,
    temp_min : str,
    temp_max : str,
    temp_city_lat : str,
    temp_city_lon : str,
) -> bool:
    """
    Add information current day
    """
    with get_session() as session:  
        weather_current = WeatherCurrent(**locals())      
        delete_city_id = delete_weather_current_from_database(id_data=id_data)       
        if delete_city_id:                       
            session.add(weather_current)  # INSERT INTO      
            session.commit()

    return True

def delete_weather_current_from_database(id_data:int) -> bool:
    """ remove weather current id_city """
    with get_session() as session:     
        if id_data:  
            session.query(WeatherCurrent).filter(WeatherCurrent.id_data == id_data).delete(synchronize_session=False)       
            session.commit()

    return True

def get_weather_current_from_database(city: Optional[str] = None, id_data: Optional[int] = None) -> List[WeatherCurrent]:
    with get_session() as session:
        sql = select(WeatherCurrent)
        if city:
            sql = sql.where(WeatherCurrent.city_name == city)
        if id_data:
            sql = sql.where(WeatherCurrent.id_data == id_data)            
        return list(
            session.exec(sql)
        )  # utilizar sem a list para performance e paginação

# table cities
#------------------------------------------------------------------------------------
def add_cities_to_database(  
    id_data: int,
    city_name: str,
    city_country: str,
    city_population: int,
    city_timezone: str,
) -> bool:
    with get_session() as session:
        cities = Cities(**locals())
        delete_city_id = delete_cities_from_database(id_data=id_data)       
        if delete_city_id:                       
            session.add(cities)  # INSERT INTO
            session.commit()

    return True

def delete_cities_from_database(id_data:int) -> bool:
    """ remove weather current id_city """
    with get_session() as session:  
        if id_data:      
            session.query(Cities).filter(Cities.id_data == id_data).delete(synchronize_session=False)       
            session.commit()

    return True


def get_cities_from_database(city: Optional[str] = None, id_data: Optional[int] = None) -> List[Cities]:
    with get_session() as session:
        sql = select(Cities)
        if city:
            sql = sql.where(Cities.city_name == city)
        if id_data:
            sql = sql.where(Cities.id_data == id_data)            
        return list(
            session.exec(sql)
        )  # utilizar sem a list para performance e paginação

# table interval
#------------------------------------------------------------------------------------
def add_interval_to_database(  
    id_data: int,
    interval_dt_unix: int,
    current_city_interval_main_temp: str,
    current_city_interval_main_fells_like: str,
    current_city_interval_main_temp_min: str,
    current_city_interval_main_temp_max: str,
    current_city_interval_main_humidity: int,
    current_city_interval_weather_main: str,
    current_city_interval_weather_description: str,
    current_city_interval_weather_icon: str,
    unix_timestamp: Optional[int] = None,
) -> bool:
    with get_session() as session:
        intervals = Interval(**locals())
        #delete_interval_city_id = delete_interval_from_database(interval_dt_unix=unix_timestamp, id_data=id_data)       
        #if delete_interval_city_id: 
        session.add(intervals)  # INSERT INTO
        session.commit()

    return True

def delete_interval_from_database(interval_dt_unix: int, id_data: int) -> bool:
    """ remove weather current id_city """
    with get_session() as session:  
        if interval_dt_unix:
            current_time = datetime.now()   
            unix_timestamp = int(datetime.timestamp(current_time)) 
            session.query(Interval).\
                filter((Interval.id_data == id_data) & (Interval.interval_dt_unix >= unix_timestamp)).\
                delete(synchronize_session=False)       
            session.commit()

    return True


def get_all_interval_from_database(id_data: Optional[int] = None) -> List[Interval]:
    with get_session() as session:
        sql = select(Interval)
        current_date_time = datetime.now()  # 2023-03-02 15:03:19
        current_date = datetime.strptime(datetime.strftime(current_date_time, "%Y-%m-%d"), "%Y-%m-%d") # 2023-03-02
        yesterday_date = int(datetime.timestamp( (datetime.strptime((current_date.today().replace(hour=23, minute=0, second=0)-timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")) ))
        tomorrow_date = int(datetime.timestamp( (datetime.strptime((current_date.today().replace(hour=0, minute=0, second=0)+timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")) ))  
        
        if id_data:
            sql = sql.where(Interval.id_data == id_data, Interval.interval_dt_unix > yesterday_date, Interval.interval_dt_unix < tomorrow_date).\
                order_by(Interval.interval_dt_unix.asc())   
        return list(
            session.exec(sql)
        )  # utilizar sem a list para performance e paginação

def get_interval_current_day_from_database(id_data: int, interval_dt_current_unix: int) -> List[Interval]:
    with get_session() as session:
        sql = select(Interval)
        if id_data:
            sql = sql.where(Interval).filter(
                (Interval.id_data == id_data) & 
                (Interval.interval_dt_unix >= interval_dt_current_unix))      
        return list(
            session.exec(sql)
        )  # utilizar sem a list para performance e paginação
