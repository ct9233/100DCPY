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

    if time.time() >= upgrade_check_time:
        player_money = int(driver.find_element_by_id("money").text.replace(",", ""))
        upgrade_items = driver.find_elements_by_css_selector("#store b")
        upgrade_dict = {}
        costs = []

        for item in upgrade_items:
            if item.text != "":
                name = item.text.split("-")[0].strip()
                cost = int(item.text.split("-")[1].strip().replace(",", ""))
                costs.append(cost)
            upgrade_dict[cost] = name
            
        costs.sort(reverse=True)

        for cost in costs:
            if cost < player_money:
                driver.find_element_by_id(f"buy{upgrade_dict[cost]}").click()
                break

        upgrade_check_time = time.time() + 5

    if time.time() > game_time_limit:
        cookies_per_sec = driver.find_element_by_id("cps").text
        print(cookies_per_sec)
        break