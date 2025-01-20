import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

login = login
password = password
url = "https://tinder.com/"


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_option)
driver.get(url)

driver.implicitly_wait(10)

login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()

facebook_login = driver.find_element(By.XPATH, '//*[@id="q229060750"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()
time.sleep(2)
facebook_popup = driver.window_handles[1]
driver.switch_to.window(facebook_popup)
autorize_cookies = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]')
autorize_cookies.click()
time.sleep(2)


email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys(login)
password_input = driver.find_element(By.NAME, 'pass')
password_input.send_keys(password, Keys.ENTER)

con = driver.find_element(By.XPATH, '//*[@id="mount_0_0_QY"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div/div')
con.click()