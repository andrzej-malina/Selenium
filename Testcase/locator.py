# Klasa do definiowania lokalizacji na testowanej stronie

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='What you search for...']")
    SEARCH_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form/div[2]/button")
    NETWORK_BUTTON = (By.PARTIAL_LINK_TEXT, "network")
    PROFILE_BUTTON = (By.PARTIAL_LINK_TEXT, "profile")
    MOVIES_BUTTON = (By.PARTIAL_LINK_TEXT, "movies")
    PUBLICATIONS_BUTTON = (By.PARTIAL_LINK_TEXT, "publications")
    ACTIVITIES_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[1]")
    ANATOMY_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[2]")
    CHEMICALS_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[3]")
    CONCEPTS_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[4]")
    DEVICES_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[5]")
    DISORDERS_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[6]")
    GEO_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[7]")
    LIVING_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[8]")
    OBJECTS_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[9]")
    ORGANIZATIONS_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[10]")
    PHENOMENA_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[11]")
    PHYSIOLOGY_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[12]")
    PROCEDURES_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/label[13]")
    SHOWALL_BUTTON = (By.XPATH, "/html/body/app-root/app-index/main/app-index/form[2]/button")
