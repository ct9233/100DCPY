from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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

# Sign in process
time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(account_email)
password_field = driver.find_element_by_id("password")
password_field.send_keys(account_password)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

# Collect jobs for applying
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(2)

    # Determine apply button presence and simple application status
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone_num = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone_num.text == "":
            phone_num.send_keys(phone_number)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If submit button is 'next' button bypass
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
        else:
            submit_button.click()

        # Close popup after applying
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("Apply button not present, skipped.")
        continue

time.sleep(5)
driver.quit()