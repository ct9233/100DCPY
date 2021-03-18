import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv("C:/data/.env")

nutritionix_app_id = os.getenv("NUTRIX_APP_ID")
nutritionix_api = os.getenv("NUTRIX_API_KEY")

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.getenv("SHEETY_WKOUT_ENDPOINT")

user_exercises = input("Which excercises did you complete? ")

exercise_config = {
    "query": user_exercises,
    "gender": os.getenv("GENDER"),
    "weight_kg": os.getenv("WEIGHT_KG"),
    "height_cm": os.getenv("HEIGHT_CM"),
    "age": os.getenv("AGE"),
}

response = requests.post(exercise_endpoint, json=exercise_config, headers=headers)
response.raise_for_status()
exercise_data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise_data["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, auth=(os.getenv("WKOUT_USER"), os.getenv("WKOUT_PASS")))

print(sheety_response.text)