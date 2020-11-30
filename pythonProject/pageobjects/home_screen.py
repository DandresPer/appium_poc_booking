from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LocatorsHomeScreen import LocatorsHomeScreen
from pageobjects.booking_services_screens.car_rental_screen import CarRentalScreen
from pageobjects.booking_services_screens.stay_booking_screen import StayBookingScreen


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver
        # ----NAVBAR
        self.navbar_stays = WebDriverWait(self.driver.instance, 8).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsHomeScreen.stay_booking_android)))
        self.navbar_car_rental = WebDriverWait(self.driver.instance, 8).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsHomeScreen.car_rental_android)))
        self.navbar_flights = WebDriverWait(self.driver.instance, 8).until(EC.visibility_of_element_located((
            MobileBy.ID, LocatorsHomeScreen.flight_booking_android)))

    # NAVBAR
    def tap_navbar_stays(self):
        self.navbar_stays.click()
        return StayBookingScreen(self.driver)

    def tap_navbar_car_rental(self):
        self.navbar_car_rental.click()
        return CarRentalScreen(self.driver)

    def tap_navbar_flights(self):
        self.navbar_flights.click()
#        return FlightScreen(self.driver)
