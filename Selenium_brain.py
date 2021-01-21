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
search = driver.find_element_by_css_selector("input[placeholder='What you search for...']")
search.clear()
search.send_keys('help for other people')
search.send_keys(Keys.RETURN)

texts = driver.find_elements_by_xpath("//article/p")
span_texts = [item.text for item in driver.find_elements_by_css_selector('span')]
titles = span_texts[20:25]

print('---------TEXTS--------')
for text in texts:
    print(text.text[:30])

print('---------TITLES--------')
for title in titles:
    print(title)

'''
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "main"))
    )
    print(main.text)
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        print(article)
        p = article.find_elements_by_tag_name('p')
        print(p.text)
finally:
    driver.quit()
'''



#driver.save_screenshot('C:/Users/ajankowski/Downloads/test.png')
#time.sleep(3)

#driver.quit()