from userinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password


    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.ID,"login_field").send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.NAME, "commit").click()


print(username, password)
github = Github(username, password)
github.signIn()
time.sleep(3)
