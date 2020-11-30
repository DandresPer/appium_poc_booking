from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LocatorsLocationSelectionScreen import LocatorsLocationSelectionScreen
from pageobjects.selection_screens.date_selection_screen import DateSelectionScreen


class DestinationScreen:
    def __init__(self, driver):
        self.driver = driver
        try:
            self.search_bar = WebDriverWait(self.driver.instance, 3).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsLocationSelectionScreen.search_bar_stay_android)))
        except TimeoutException:
            self.search_bar = WebDriverWait(self.driver.instance, 3).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsLocationSelectionScreen.search_bar_car_android)))

    def select_stay_location(self, input_text):
        self.search_bar.send_keys(input_text)
        first_location_result = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.XPATH, LocatorsLocationSelectionScreen.first_location_result_stay_android)))
        first_location_result.click()
        return DateSelectionScreen(self.driver)

    def select_car_rental_location(self, input_text):
        from pageobjects.booking_services_screens.car_rental_screen import CarRentalScreen
        self.search_bar.send_keys(input_text)
        first_location_result = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.XPATH, LocatorsLocationSelectionScreen.first_location_result_car_android)))
        first_location_result.click()
        return CarRentalScreen(self.driver)
