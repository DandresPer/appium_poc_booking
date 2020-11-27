from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "appPackage": "com.booking",
            "appWaitActivity": "com.booking.login.LoginActivity",
            "app": "/Users/dandres/Desktop/booking.apk"
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        # self.instance.implicitly_wait(10)
