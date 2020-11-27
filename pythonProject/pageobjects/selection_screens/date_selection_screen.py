from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.LocatorsDateSelectionScreen import LocatorsDateSelectionScreen


class DateSelectionScreen:
    def __init__(self, driver):
        self.driver = driver
        self.calendar_view = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsDateSelectionScreen.calendar_view)))
        self.confirm_button = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsDateSelectionScreen.confirm_button)))

    def tap_select_dates(self, timelapse):
        initial_date = self.driver.instance.find_element_by_xpath(LocatorsDateSelectionScreen.initial_date_android)
        initial_date.click()
        end_date = self.driver.instance.find_element_by_xpath(LocatorsDateSelectionScreen.end_date_android)
        end_date.click()

    def tap_confirm_dates(self):
        # Si no, import cíclico
        from pageobjects.booking_services_screens.stay_booking_screen import StayBookingScreen
        self.confirm_button.click()
        return StayBookingScreen(self.driver)

    def tap_confirm_dates_car(self):
        # Si no, import cíclico
        from pageobjects.booking_services_screens.car_rental_screen import CarRentalScreen
        self.confirm_button.click()
        return CarRentalScreen(self.driver)
