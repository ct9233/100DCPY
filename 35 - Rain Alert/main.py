import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
load_dotenv("C:/data/.env")
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWI_ACC_SID")
auth_token = os.getenv("TWI_AUTH_TOK")
twilio_from = os.getenv("TWI_FROM_NUM")
twilio_to = os.getenv("TWI_TO_NUM")

weather_params = {
    "lat": 43.615021,
    "lon": -116.202316,
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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=f"{twilio_from}",
        to=f"{twilio_to}"
    )
    print(message.status)
    # print("Bring an umbrella!")
# print(weather_data["hourly"][0]["weather"][0]["id"])