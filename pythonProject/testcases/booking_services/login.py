import unittest

from pageobjects.selection_screens.login_popup_screen import LoginPopupScreen
from webdriver import Driver
import Logger

Logger.set_logger()


class TestCases(unittest.TestCase):

    def setUp(self):
        print('Setting up driver')
        self.driver = Driver()

    def test_account_selection(self):
        Logger.log_assert(False, "Something failedddddddd")
        print('test_account_selection')
        login = LoginPopupScreen(self.driver)
        login.account_selection()

    def tearDown(self):
        print('Quit driver')
        # self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
