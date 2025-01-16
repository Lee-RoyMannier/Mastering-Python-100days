from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

cooki = driver.find_element(By.ID, "cookie")

timeout = time.time() + 60*5
check_bonus_time = time.time() + 5

panels = driver.find_elements(By.CSS_SELECTOR, "#store div")
panel_ids = [div.get_attribute("id") for div in panels]

while time.time() < timeout:
    nb_coockie = driver.find_element(By.ID, "money")
    nb_coockie = int(nb_coockie.text.replace(",", "").strip())

    prices_element = driver.find_elements(By.CSS_SELECTOR, "#store b")
    prices = []

    for price in prices_element:
        price_refactor = price.text
        print(price_refactor)
        print("-----------")
        if price_refactor != "":
            price_r = int(price_refactor.split("-")[-1].strip().replace(",", ""))
            prices.append(price_r)

    panel_elements = {}

    for i in range(len(prices)):
        panel_elements[prices[i]] = panel_ids[i]

    if time.time() > check_bonus_time:
        for price_el, id_element in panel_elements.items():
            if nb_coockie >= price_el:
                press_item = driver.find_element(By.ID, id_element)
                press_item.click()

    cooki.click()





