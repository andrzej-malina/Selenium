# https://www.youtube.com/watch?v=O_sIPPA4euw

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import page
import time


class PythonOrgSearch(unittest.TestCase):

    # funkcja do rozpoczęcia, wybór sterownika i strony url do testowania
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ajankowski/Downloads/chromedriver')
        self.driver.get('http://brainiverse.cktech.eu/search')

    # funckcja o nazwie zaczynającej się na test, będzie wykonywana automatycznie,
    # bo dziedziczymy od unittest.TestCase

    # funkcja sprawdzająca czy tytuł strony jest ok
    def test1_title(self):
        assert "App" in self.driver.title

    # funkcja sprawdzająca czy są wyniki wyszukiwania dla zapytania 'covid'
    def test2_search(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(3)
        assert "No results found." not in self.driver.page_source

    # funkcja sprawdzająca czy są wyniki wyszukiwania dla bezsensownego zapytania '$%^&*(()_&*('
    def test3_search_stupid(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('$%^&*(()_&*(')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(3)
        assert "No results found." in self.driver.page_source

    # funkcja sprawdzająca kilknięcie w ikonę NETWORK
    def test4_click_network(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_network_button()
        time.sleep(2)
        assert mainPage.is_under_construction_found()

    # funkcja sprawdzająca kilknięcie w ikonę PROFILE
    def test5_click_profile(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_profile_button()
        time.sleep(2)
        assert mainPage.is_under_construction_found()

    # funkcja sprawdzająca kilknięcie w ikonę MOVIES
    def test6_click_movies(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_movies_button()
        time.sleep(2)
        assert mainPage.is_under_construction_found()

    # funkcja sprawdzająca kilknięcie w ikonę PUBLICATIONS
    def test7_click_publications(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_publications_button()
        time.sleep(2)
        assert mainPage.is_under_construction_found()

    # funkcja do sprawdzenia przycisku activities
    def test8_activities_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        activities_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[1]")
        activities_button.click()
        time.sleep(2)

        assert activities_button.get_attribute("class") == 'ng-star-inserted'

    def test9_anatomy_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        anatomy_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[2]")
        anatomy_button.click()
        time.sleep(2)

        assert anatomy_button.get_attribute("class") == 'ng-star-inserted'

    def test10_chemicals_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        chemicals_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[3]")
        chemicals_button.click()
        time.sleep(2)

        assert chemicals_button.get_attribute("class") == 'ng-star-inserted'

    def test11_concepts_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        concepts_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[4]")
        concepts_button.click()
        time.sleep(2)

        assert concepts_button.get_attribute("class") == 'ng-star-inserted'

    def test12_devices_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        devices_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[5]")
        devices_button.click()
        time.sleep(2)

        assert devices_button.get_attribute("class") == 'ng-star-inserted'

    def test13_disorders_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        disorders_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[6]")
        disorders_button.click()
        time.sleep(2)

        assert disorders_button.get_attribute("class") == 'ng-star-inserted'

    def test14_geo_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        geo_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[7]")
        geo_button.click()
        time.sleep(2)

        assert geo_button.get_attribute("class") == 'ng-star-inserted'


    def test15_living_button(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='What you search for...']")
        search_field.clear()
        search_field.send_keys('covid')
        search_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
        search_button.click()
        time.sleep(2)

        living_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[8]")
        living_button.click()
        time.sleep(2)

        assert living_button.get_attribute("class") == 'ng-star-inserted'

    # funkcja na zakończenie, żeby "posprzątać"
    def clean_End(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
