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

driver.get('http://brainiverse.cktech.eu/search')
driver.implicitly_wait(3)
print(driver.title)

search_page = driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
search_page.clear()
search_page.send_keys('covid')
search_button = driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
search_button.click()
time.sleep(2)

element = driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[1]")
element.click()
time.sleep(2)

check = element.get_attribute("class")

print (check == 'ng-star-inserted')

time.sleep(2)

driver.quit()
