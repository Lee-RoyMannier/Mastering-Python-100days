import requests
from selenium import webdriver
from selenium.common import ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

url_login = 'https://www.instagram.com/'
instagram_account_followers_url = 'user_to_follow'
profil_name = "profile_name"
password = "password"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options)
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.get(url_login)
        accept_cookies = self.driver.find_element(By.CLASS_NAME, '_a9_0')
        accept_cookies.click()
        time.sleep(3)

        name_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        name_field.send_keys(profil_name)
        password_field.send_keys(password, Keys.ENTER)
        time.sleep(5)
    def find_followers(self):

        self.driver.get(url_login+instagram_account_followers_url+"/followers/")
        time.sleep(3)
        followers_button = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following/')]"))
        )
        time.sleep(5)
        followers_button.click()
        print("Bouton des followers cliqué !")
        time.sleep(5)
        div = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(2):
            time.sleep(5)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div)
            time.sleep(2)

    def follow(self):
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"))
        )
        print("Modal pour suivre les utilisateurs localisé.")

        all_btns = modal.find_elements(By.XPATH, "//button")
        for btn in all_btns:
            if btn.text == "Suivre":
                btn.click()
            else:
                continue
            time.sleep(10)

instagram_bot = InstaFollower()
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()