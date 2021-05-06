import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv("C:/data/.env")

CHROME_DRIVER_PATH = "/data/chromedriver"
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()