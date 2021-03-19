import os
from dotenv import load_dotenv
import requests

load_dotenv("C:/data/.env")

tequila_main_endpoint = "https://tequila-api.kiwi.com"
tequila_locations_query = "/locations/query"
tequila_api_key = os.getenv("KWTQ_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass