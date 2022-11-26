from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')

class access:
  def __init__(self):
      self = driver.get("https://docs.python.org/ja/3/")

  def element_action(xpath, action, send_param):
        driver_element = driver.find_element(by=By.XPATH, value=xpath)
      if action == "click":
      driver_element.click()
      else:
      driver_element.send_keys(send_param)

      element_action("/html/body/div[3]/div[1]/div/div/table[1]/tbody/tr/td[1]/p[1]/a", "click", "")
      element_action("/html/body/div[2]/ul/li[12]/div/form/input[1]", "send_key", "send_keysを使用して送付しています")
      
