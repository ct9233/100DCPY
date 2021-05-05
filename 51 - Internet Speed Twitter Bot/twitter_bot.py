import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

load_dotenv("C:/data/.env")

twitter_email = os.getenv("TWITT_EMAIL")
twitter_password = os.getenv("TWITT_PASS")


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/data/chromedriver")
        

    def tweet_at_provider(self, complaint_tweet):
        self.driver.get("https://twitter.com/login")
        self.tweet = complaint_tweet

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
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )

        tweet_compose.send_keys(self.tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
        )
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()