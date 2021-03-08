import requests
import os
from dotenv import load_dotenv

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
load_dotenv("C:/data/.env")
api_key = os.getenv("OWM_API_KEY")

weather_params = {
    "lat":  32.715736,
    "lon":  -117.161087,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella!")
# print(weather_data["hourly"][0]["weather"][0]["id"])