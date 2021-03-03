import requests
from datetime import datetime
import smtplib
import time

current_lat = 32.7157
current_long = 117.1611

EMAIL = "user@mail.com"
PASSWORD = "1234PASS"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if current_lat - 5 <= iss_latitude <= current_lat + 5 and current_long - 5 <= iss_longitude <= current_long + 5:
        return True

def is_night():
    parameters = {
        "lat": current_lat,
        "lng": current_long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_time = datetime.now()
    current_hour = current_time.hour

    if current_hour < sunrise or current_hour > sunset:
        return True
    
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.server.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )