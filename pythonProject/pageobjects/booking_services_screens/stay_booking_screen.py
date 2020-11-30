import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LocatorsStayBookingScreen import LocatorsStayBookingScreen
from Logger import log_assert
from pageobjects.selection_screens.date_selection_screen import DateSelectionScreen
from pageobjects.selection_screens.location_selection_screen import DestinationScreen


class StayBookingScreen:
    def __init__(self, driver):
        try:
            self.driver = driver
            self.location = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsStayBookingScreen.location_android)))
            self.dates = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsStayBookingScreen.dates_android)))
            self.group = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsStayBookingScreen.group_android)))
            self.search_button = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsStayBookingScreen.search_button_android)))
            logging.error('ERROOOOOOOOOOR-----------------------')
        except TimeoutException:
            log_assert('location' in dir(self), "Cannot find element LOCATION")
            log_assert('dates' in dir(self), "Cannot find element DATES")
            log_assert('group' in dir(self), "Cannot find element GROUP")
            log_assert('search_button' in dir(self), "Cannot find element SEARCH_BUTTON")

    # STAY OPTIONS
    def tap_location(self):
        self.location.click()
        return DestinationScreen(self.driver)

    def tap_dates(self):
        self.dates.click()
        return DateSelectionScreen(self.driver)

    def tap_group(self):
        self.group.click()

    def tap_search(self):
        self.search_button.click()
