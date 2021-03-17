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

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_exercises = input("Which excercises did you complete? ")

exercise_config = {
    "query": user_exercises,
    "gender": os.getenv("GENDER"),
    "weight_kg": os.getenv("WEIGHT_KG"),
    "height_cm": os.getenv("HEIGHT_CM"),
    "age": os.getenv("AGE"),
}

response = requests.post(EXERCISE_ENDPOINT, json=exercise_config, headers=headers)
response.raise_for_status()
exercise_data = response.json()

print(exercise_data)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

print(today_date)
print(now_time)