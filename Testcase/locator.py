#Klasa do definiowania lokalizacji na testowanej stronie

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[placeholder='What you search for...']")
    NETWORK_BUTTON = (By.PARTIAL_LINK_TEXT, "network")
    PROFILE_BUTTON = (By.PARTIAL_LINK_TEXT, "profile")
    MOVIES_BUTTON = (By.PARTIAL_LINK_TEXT, "movies")
    PUBLICATIONS_BUTTON = (By.PARTIAL_LINK_TEXT, "publications")
    ACTIVITIES_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[1]")
