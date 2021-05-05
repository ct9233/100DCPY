from selenium import webdriver
import time

class SpeedTest:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/data/chromedriver")
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