from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://mola.tv/")
element = browser.find_element_by_css_selector('#app > div._3e0P_ > div._3uKug > a:nth-child(7) > div')
element.click()
time.sleep(5)
assert 'Match List Page' == browser.title
browser.quit()