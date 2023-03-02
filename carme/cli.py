from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from carme.core import add_weather_current_to_database, get_weather_current_from_database

main = typer.Typer(help="Weather Management Application")
console = Console()
@main.command("add")
def weather_add(  
    id_data: int,
    city_name: str,
    description: str,
    temp_day: str,
    temp_min: str,
    temp_max: str,
    temp_city_lat: str,
    temp_city_lon: str,
):
    """Adds a new beer to database."""
    if add_weather_current_to_database(id_data, city_name, description, temp_day, temp_min, temp_max, temp_city_lat, temp_city_lon):
        print("weather added to database")


@main.command("list")
def weather_list(style: Optional[str] = None):
    """lists beers in database."""
    weathers = get_weather_current_from_database()
    table = Table(title="Weather :beer_mug:")
    headers = [       
        "id_data",
        "city_name",
        "description",
        "temp_day",
        "temp_min",
        "temp_max",
        "temp_city_lat",
        "temp_city_lon",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for weather in weathers:
        weather.date = weather.date.strftime("%Y-%m-%d")
        values = [
            str(getattr(weather, header)) for header in headers
        ]  # list comprehension
        table.add_row(*values)
    console.print(table)
