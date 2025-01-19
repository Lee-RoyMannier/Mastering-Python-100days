from selenium import webdriver
from dotenv import load_dotenv
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.getenv('url'))
driver.implicitly_wait(10)

# First step, the login
time.sleep(2)
btn_login = driver.find_element(By.LINK_TEXT, "S’identifier")
btn_login.click()
time.sleep(2)

username = driver.find_element(By.NAME, "session_key")
username.send_keys(os.getenv('LOGIN'))
password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.getenv('PASSWORD'))
password.send_keys(Keys.ENTER)

jobs = driver.get(os.getenv('url_jobs'))
list_jobs = driver.find_element(By.CSS_SELECTOR, """.UwxpnwBISmOFPIwyYXZPiisFfsyZrfpAIsaVTI
          
          """)

for i in range(5):
    list_jobs.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

jobs = driver.find_elements(By.CSS_SELECTOR, ".DTSuQQBApapgtrqjEeiNZmrisBXNCXASC li a")
jobs_offers = []

for job in jobs:
    jobs_offers.append(job.get_attribute("href"))

for job in jobs_offers:
    job_url = driver.get(job)
    try:
        btn_follow = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div/div/main/div[2]/div[1]/div/div[1]/div/div/div/div[5]/div/button')
    except NoSuchElementException:
        pass
    else:
        btn_follow.click()
    time.sleep(5)