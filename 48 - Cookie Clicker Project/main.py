from selenium import webdriver
import time

chrome_driver_path = "/data/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

game_time_limit = time.time() + 60 * 5
upgrade_check_time = time.time() + 5

while True:
    cookie.click()

    if time.time() > game_time_limit:
        break