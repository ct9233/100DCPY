import os
from dotenv import load_dotenv
import requests

load_dotenv("C:/data/.env")

sheety_endpoint = os.getenv("SHEETY_FLIGHT_PRICES_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass