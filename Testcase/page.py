#klasa do definiowania testów
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

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source

    def no_results_found(self):
        return "No results found." in self.driver.page_source