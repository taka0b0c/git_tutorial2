from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Access:
    def practice(self):
        self.webdriver.Chrome('chromedriver.exe')
        self.driver.get("https://docs.python.org/ja/3/")
      

  def element_action(self,xpath, action, send_param):
      self = driver.find_element(by=By.XPATH, value=xpath)
      if action == "click":
         driver_element.click()
      else:
         driver_element.send_keys(send_param)

access = Access()
access.practice,element_action
