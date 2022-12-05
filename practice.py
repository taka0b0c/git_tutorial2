from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Access:

  driver = ""

  def __init__(self):
    self.driver = webdriver.Chrome('chromedriver.exe')
    self.driver.get("https://terakoya.sejuku.net/home")


  def element_action(self,xpath, action, send_param):
    driver_element = self.driver.find_element(by=By.XPATH, value=xpath)
    if action == "click":
      driver_element.click()
    else:
      driver_element.send_keys(send_param)



if __name__ == '__main__':
  sample_selenium = Access()
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/header/div[2]/div[2]/div","click","")
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[1]/input","","taka0b0c@gmail.com")
  time.sleep(2)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[2]/input","","自分のパスワード")
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/button","click","")
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/nav/ul/li[9]/a/p","click","")
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/main/div/div/div[1]/div/div[2]/p[1]","click","")
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/main/div/div[3]/section[2]/div/div/textarea","","宿題で送信")
  time.sleep(5)
  sample_selenium.element_action("/html/body/div[1]/div[1]/div/div/main/div/div[3]/section[2]/button/img","click","")
  time.sleep(5)