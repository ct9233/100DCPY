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

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

create_pixel_endpoint = f"{graph_endpoint}/graph1"

create_pixel_config = {
    "date": "20210312",
    "quantity": "3.4",
}

response = requests.post(url=create_pixel_endpoint, json=create_pixel_config, headers=headers)
print(response.text)