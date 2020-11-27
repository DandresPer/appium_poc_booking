from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.selection_screens.location_selection_screen import DestinationScreen
from pageobjects.selection_screens.date_selection_screen import DateSelectionScreen
from Locators.LocatorsCarRentalScreen import LocatorsCarRentalScreen


class CarRentalScreen:
    def __init__(self, driver):
        self.driver = driver
        self.location = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsCarRentalScreen.location_android)))
        self.dates = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsCarRentalScreen.dates_android)))
        self.search_button = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsCarRentalScreen.search_button)))

    # STAY OPTIONS
    def tap_location(self):
        self.location.click()
        return DestinationScreen(self.driver)

    def tap_dates(self):
        self.dates.click()
        return DateSelectionScreen(self.driver)

    def tap_search(self):
        self.search_button.click()

