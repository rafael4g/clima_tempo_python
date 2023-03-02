from typing import Optional
from sqlmodel import Field, SQLModel


class WeatherCurrent(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    id_data: int
    city_name: str
    description: str
    temp_day: str
    temp_min: str
    temp_max: str
    temp_city_lat: str
    temp_city_lon: str

class Cities(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    id_data: int
    city_name: str
    city_country: str
    city_population: int
    city_timezone: str    

class Interval(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    id_data: int
    interval_dt_unix: int
    current_city_interval_main_temp: str
    current_city_interval_main_fells_like: str
    current_city_interval_main_temp_min: str
    current_city_interval_main_temp_max: str
    current_city_interval_main_humidity: int
    current_city_interval_weather_main: str
    current_city_interval_weather_description: str
    current_city_interval_weather_icon: str
       