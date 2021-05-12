from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/data/.env")

ZILLOW_URL = os.getenv("ZILLOW_SEARCH_URL")

class ApartmentResearch():
    def __init__(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Accept-Language": "en-US,en;q=0.5"
        }
        response = requests.get(url=ZILLOW_URL, headers=header).text
        self.soup = BeautifulSoup(response,'html.parser')
        
    def get_data(self):
        anchor_tags_div = self.soup.find_all(name="div", class_="list-card-top")
        self.links = []
        for div in anchor_tags_div:
            href = div.find(name="a").get("href")
            if "http" not in href:
                self.links.append(f"https://www.zillow.com/{href}")
            else:
                self.links.append(href)

        prices_div = self.soup.find_all(name="div", class_="list-card-price")
        self.prices = [self.strip_price(div.text) for div in prices_div]

        address_div = self.soup.find_all(name="address")
        self.addresses = [div.text for div in address_div]