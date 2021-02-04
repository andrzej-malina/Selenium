# https://www.youtube.com/watch?v=O_sIPPA4euw

import unittest
from selenium import webdriver
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
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    # funkcja sprawdzająca czy są wyniki wyszukiwania dla zapytania 'help for other people'
    def test2_search(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = 'help for other people'
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # funkcja sprawdzająca czy są wyniki wyszukiwania dla bezsensownego zapytania '$%^&*(()_&*('
    def test3_search_stupid(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = '$%^&*(()_&*('
        mainPage.click_search_button()
        time.sleep(2)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.no_results_found()

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

    # funkcja do
    def test8_activities_button(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = 'covid'
        mainPage.click_search_button()
        time.sleep(2)
        page.SearchResultPage(self.driver)

    # funkcja na zakończenie, żeby "posprzątać"
    def clean_End(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
