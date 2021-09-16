from selenium.webdriver.support.wait import WebDriverWait


class BasePageCookie:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)
