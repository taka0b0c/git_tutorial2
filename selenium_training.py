from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\user\\Documents\\samurai\\chromedriver')
time.sleep(10)

def access (URL,sleeptime):
    driver.get(URL)
    time.sleep(sleeptime)

access("https://docs.python.org/ja/3/",5)

print("遷移完了しました")
