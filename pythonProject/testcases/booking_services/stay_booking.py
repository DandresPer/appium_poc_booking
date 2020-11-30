import unittest
from junit_xml import TestSuite, TestCase

from pageobjects.home_screen import HomeScreen
from webdriver import Driver
import Logger


class TestCases(unittest.TestCase):

    def setUp(self):
        print('Setting up driver')
        self.driver = Driver()
        Logger.set_logger()

    def test_stay_search_flow(self):
        print('test_stay_search_flow')
        home = HomeScreen(self.driver)
        booking_screen = home.tap_navbar_stays()
        location = booking_screen.tap_location()
        date_selection = location.select_stay_location('Barcelona')
        date_selection.tap_select_dates(15)
        booking_screen = date_selection.tap_confirm_dates()
        booking_screen.tap_search()

    def tearDown(self):
        print('Quit driver')
        # self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
