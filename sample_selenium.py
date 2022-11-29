from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Access:
    driver.get("https://docs.python.org/ja/3/")

    def __init__(self):
        self.webdriver.Chrome('chromedriver.exe')

      

    def element_action(self,xpath, action, send_param):
        self.driver.find_element(by=By.XPATH, value=xpath)
      if action == "click":
         driver_element.click()
      else:
         driver_element.send_keys(send_param)
