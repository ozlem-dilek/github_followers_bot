from userinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []


    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.ID,"login_field").send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.NAME, "commit").click()


    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary").text)


    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        self.loadFollowers()

        while True:
            links = self.browser.find_element(By.CSS_SELECTOR, ".pagination").find_elements(By.TAG_NAME, "a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()


                else:
                    break
            
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        
                        self.loadFollowers()


                    else:
                        continue

print(username, password)
github = Github(username, password)
github.signIn()
github.getFollowers()
print(github.followers)
print(len(github.followers))
time.sleep(3)
