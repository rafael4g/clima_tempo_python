from typing import Union
from datetime import datetime

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from carme.core import (
    get_weather_current_from_database,
    get_all_interval_from_database
)
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(request: Request, item_id: int, q: Union[str, None] = None):
    return templates.TemplateResponse("item2.html", {"request": request, "id": item_id, "q": q})

@app.get("/temp/{id_data}", response_class=HTMLResponse)
def get_weather_current_city(request: Request, id_data: int):
    items = get_weather_current_from_database(id_data=id_data)
    return templates.TemplateResponse("item3.html", {"request": request, "items": items})

@app.get("/interval/{id_interval}")
def get_weather_interval_city(request: Request, id_interval: int):
    intervals = get_all_interval_from_database(id_data=id_interval)
    new_intervals = []
    for interval in intervals:
        new_intervals.append({interval.interval_dt_unix, datetime.fromtimestamp(interval.interval_dt_unix)})
    return new_intervals