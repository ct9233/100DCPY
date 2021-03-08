import requests
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat":  32.715736,
    "lon":  -117.161087,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())