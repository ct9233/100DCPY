from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/data/.env")

CHROME_DRIVER_PATH = "/data/chromedriver"
FORM_URL = os.getenv("APT_FORM_URL")

class DataCompiler():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)