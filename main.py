from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

CHROMIUM_PATH = Service("chromedriver path")
SIMILAR_ACCOUNT = "target account"
USERNAME = "username"
PASSWORD = "password"


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[text()="Accept All"]').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(3)
        self.find_followers()

    def find_followers(self):
        self.driver.get(f" https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(3)
        pop_up_window = WebDriverWait(
            self.driver, 2).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
        for i in range(10):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(1)
        self.follow()

    def follow(self):
        follow_list = self.driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/ul/div'
                                                          '//button[text()="Follow"]')
        for item in follow_list:
            self.driver.execute_script("arguments[0].click();", item)
            time.sleep(1)


follower_bot = InstaFollower(CHROMIUM_PATH)
follower_bot.login()
