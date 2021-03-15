import os
from dotenv import load_dotenv
import requests
from datetime import datetime

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

# date = datetime(year=2021, month=3, day=13)
today = datetime.now()

create_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.2",
}

# response = requests.post(url=create_pixel_endpoint, json=create_pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today.strftime('%Y%m%d')}"

update_pixel_data = {
    "quantity": "2.2",
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
print(response.text)


# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)

