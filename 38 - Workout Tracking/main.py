import os
from dotenv import load_dotenv
import requests
import json


load_dotenv("C:/data/.env")

nutritionix_app_id = os.getenv("NUTRIX_APP_ID")
nutritionix_api = os.getenv("NUTRIX_API_KEY")

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api,
}

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": "did 45 pushups",
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 177,
    "age": 45,
}

response = requests.post(EXERCISE_ENDPOINT, json=exercise_config, headers=headers)
response.raise_for_status()
exercise_data = response.json()

print(exercise_data)