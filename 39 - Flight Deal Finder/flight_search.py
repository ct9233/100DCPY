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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": tequila_api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "USD"
        }