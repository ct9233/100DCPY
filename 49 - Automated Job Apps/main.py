from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/data/.env")
account_email = os.getenv("LINKEDIN_ACCT")
account_password = os.getenv("LINKEDIN_PASS")
phone_number = os.getenv("PHONE_NUM")

chrome_driver_path = "/data/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2485157619&f_AL=true&f_CR=103644278&f_E=2%2C1&f_TPR=r604800&f_WRA=true&keywords=developer&sortBy=DD")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(account_email)
password_field = driver.find_element_by_id("password")
password_field.send_keys(account_password)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone_num = driver.find_element_by_class_name("fb-single-line-text__input")
if phone_num.text == "":
    phone_num.send_keys(phone_number)

submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
