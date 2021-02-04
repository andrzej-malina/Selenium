# klasa do definiowania testów
from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "input[placeholder='What you search for...']"

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "App" in self.driver.title

    def is_under_construction_found(self):
        return "UNDER CONSTRUCTION" in self.driver.page_source

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def click_network_button(self):
        element = self.driver.find_element(*MainPageLocators.NETWORK_BUTTON)
        element.click()

    def click_profile_button(self):
        element = self.driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        element.click()

    def click_movies_button(self):
        element = self.driver.find_element(*MainPageLocators.MOVIES_BUTTON)
        element.click()

    def click_publications_button(self):
        element = self.driver.find_element(*MainPageLocators.PUBLICATIONS_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source

    def no_results_found(self):
        return "No results found." in self.driver.page_source
