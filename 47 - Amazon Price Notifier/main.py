import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("C:/data/.env")
smtp_address = os.getenv("SMTP_ADDRESS")
send_address = os.getenv("SEND_ADDRESS")
send_password = os.getenv("SEND_PASS")
to_address = os.getenv("RECEIVE_ADDRESS")

url = "https://www.amazon.com/eufy-Security-eufyCam-Wireless-180-Day/dp/B07W1HKYQK"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-US,en;q=0.5"
}

BUY_PRICE = 200

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text()
price_number = float(price.split("$")[1])

coupon = soup.find(id="vpcButton")
coupon_details = ''
try:
    coupon_details = coupon.contents[5].get_text()
except AttributeError:
    pass

message = ''
if price_number < BUY_PRICE:
    message = message + f"{title} is now {price}\n"
if coupon_details != '':
    message = message + f"Coupon available: {coupon_details}"

if message != '':
    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(send_address, send_password)
        connection.sendmail(
            from_addr=send_address,
            to_addrs=to_address,
            msg=f"Subject:Amazon Price Notification\n\n{message}\n{url}"
        )