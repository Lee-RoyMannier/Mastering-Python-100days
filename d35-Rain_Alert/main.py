import requests
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
URL_API = "https://api.openweathermap.org/data/2.5/forecast"
LAT = 43.709423
LONG = -1.055488

param = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}

r = requests.get(URL_API, params=param)
data = r.json()
weather_days = data["list"]

is_rain = False
for day in weather_days:
    if day["weather"][0]["id"] < 700:
        is_rain = True

if is_rain:
    print("Bring a umbrella")