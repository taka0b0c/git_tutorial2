from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class access:
  def __init__():
      driver.get("https://docs.python.org/ja/3/")
      driver = webdriver.Chrome('chromedriver.exe')

  def element_action(xpath, action, send_param):
        driver_element = driver.find_element(by=By.XPATH, value=xpath)
      if action == "click":
         driver_element.click()
      else:
         driver_element.send_keys(send_param)
