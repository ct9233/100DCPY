from bs4 import BeautifulSoup
import requests

ZILLOW_URL = ''

class ApartmentResearch():
    def __init__(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Accept-Language": "en-US,en;q=0.5"
        }
        response = requests.get(url=ZILLOW_URL, headers=header).text
        self.soup = BeautifulSoup(response,'html.parser')
        
    def get_data(self):
      anchor_tags_div = self.soup.find_all(name="div", class="list-card-top")