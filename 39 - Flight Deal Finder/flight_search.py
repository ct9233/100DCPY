import os
from dotenv import load_dotenv
import requests

load_dotenv("C:/data/.env")

tequila_main_endpoint = "https://tequila-api.kiwi.com"
tequila_api_key = os.getenv("KWTQ_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{tequila_main_endpoint}/locations/query"
        headers = {"apikey": tequila_api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code