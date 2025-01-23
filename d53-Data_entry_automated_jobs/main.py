import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



google_forms = "https://docs.google.com/forms/d/e/1FAIpQLSel4u2iQaq921iojqgG-L9J-zs_t5ZYQckhb24vFhA-G9_eSw/viewform?usp=sharing"

# Site to scrap
url_renting = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
# First step: loging to the renting url and take all the url of rantals
response = requests.get(url=url_renting, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
find_rentals = soup.select(".StyledPropertyCardDataWrapper a")
links_rentals = [link.get("href") for link in find_rentals]

find_adress = soup.select(".StyledPropertyCardDataWrapper address")
address_rentals = [address.get_text().replace(" | ", " ").strip() for address in find_adress]

find_prices = soup.select(".StyledPropertyCardDataWrapper span")
prices = [price.get_text().replace("/mo", "").split("+")[0] for price in find_prices]

# Now we can create row in the google sheet with google form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

for i in range(len(links_rentals)):
    driver.get(google_forms)
    print(driver.page_source)
    time.sleep(5)
    address_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_property.send_keys(address_rentals[i])
    price_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_property.send_keys(prices[i])
    link_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_property.send_keys(links_rentals[i], Keys.ENTER)
    btn_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    btn_property.click()


