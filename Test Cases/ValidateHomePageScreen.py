from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://mola.tv/")
time.sleep(5)
assert 'Mola TV - Homepage' == browser.title
browser.quit()