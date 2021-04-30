import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv("C:/data/.env")

PROMISED_DOWN = 150
PROMISED_UP = 10
twitter_email = os.getenv("TWITT_EMAIL")
twitter_password = os.getenv("TWITT_PASS")
chrome_driver_path = "/data/chromedriver"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()