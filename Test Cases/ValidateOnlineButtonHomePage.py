from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://mola.tv/")
time.sleep(5)
element = browser.find_element_by_id('helpButtonSpan')
time.sleep(5)
element.click()
time.sleep(15)
element = browser.find_element_by_css_selector('body > div.modalContainer.sidebarMaximized.layout-docked.embeddedServiceSidebar > div > div.sidebarBody > div.activeFeature.hideWhileLoading > div > div > div > div.buttonWrapper.embeddedServiceSidebarForm > button > span')
element.is_displayed()
browser.quit()