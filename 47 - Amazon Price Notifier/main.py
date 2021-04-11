import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/eufy-Security-eufyCam-Wireless-180-Day/dp/B07W1HKYQK"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_number = float(price.split("$")[1])
print(price_number)
