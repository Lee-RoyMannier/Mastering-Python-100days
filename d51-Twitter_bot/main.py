import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "email"
TWITTER_PASSWORD = "password"
url = "https://x.com/i/flow/login"

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(100)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        speedtest = "https://www.speedtest.net/"
        self.driver.get(speedtest)
        accept_cookie = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookie.click()
        time.sleep(80)
        try:
            start = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        except TimeoutException:
            print("Time out")
        else:
            start.click()
        try:
            time.sleep(150)
            result_download = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))
            )
            result_upload = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
            )
        except TimeoutException:
            print("Time out")
        else:
            results = {"Download": result_download.text,
                       "Upload": result_upload.text}

            return results
        return None


    def tweet_at_provider(self, result):
        self.driver.get(url)
        email_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_box.send_keys(TWITTER_EMAIL, Keys.ENTER)
        password_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_box.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        # Send tweet
        tweet_box = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'))
        )
        tweet_box.click()
        message = f"i have Download :{ result['Download']} and Upload: {result['Upload']}"
        tweet_box.send_keys(message)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet.click()


core = InternetSpeedTwitterBot()
#results = core.get_internet_speed()
data_test = {
    "Download": 12,
    "Upload": 14,
}
core.tweet_at_provider(data_test)