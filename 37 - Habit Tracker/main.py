import os
from dotenv import load_dotenv
import requests

load_dotenv("C:/data/.env")

pixela_endpoint = "https://pixe.la/v1/users"
token = os.getenv("PIXELA_TOKEN")
username = os.getenv("PIXELA_USERNAME")

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)