import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_css_selector(".upload-speed").text
        self.down = self.driver.find_element_by_css_selector(".download-speed").text

        result = {"upload_speed": self.up, "download_speed": self.down}

        return result

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
        )

        email.send_keys(twitter_email)
        password.send_keys(twitter_password)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my connection speed only {self.down} Down/{self.up} Up when I am paying for {PROMISED_DOWN} Down/{PROMISED_UP} Up?!"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot(chrome_driver_path)

actual_speeds = bot.get_internet_speed()
actual_down = float(actual_speeds["download_speed"])
actual_up = float(actual_speeds["upload_speed"])

if PROMISED_DOWN > actual_down or PROMISED_UP > actual_up:
    bot.tweet_at_provider()