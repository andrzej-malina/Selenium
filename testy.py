from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/ajankowski/Downloads/chromedriver')

driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

driver.get('http://brainiverse.cktech.eu/network')
driver.implicitly_wait(3)
print(driver.title)

element = driver.find_element(*(By.PARTIAL_LINK_TEXT, "network"))
element.click()

page = driver.page_source
bool = "UNDER CONSTRUCTION" in page
print (bool)

time.sleep(2)

driver.quit()
