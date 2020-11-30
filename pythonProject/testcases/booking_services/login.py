import unittest

import Logger
from pageobjects.selection_screens.login_popup_screen import LoginPopupScreen
from webdriver import Driver

Logger.set_logger()


class TestCases(unittest.TestCase):

    def setUp(self):
        print('Setting up driver')
        self.driver = Driver()

    def test_account_selection(self):
        print('test_account_selection')
        login = LoginPopupScreen(self.driver)
        login.account_selection()

    def tearDown(self):
        print('Quit driver')
        # self.driver.instance.quit()
