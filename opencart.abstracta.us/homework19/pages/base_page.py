from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from ..core.cookie import Cookie
from ..core.local_storage import LocalStorage


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.__cookie = Cookie(self._driver)
        self.__local_storage = LocalStorage(self._driver)
        self.__web_driver_wait = WebDriverWait(self._driver, 10)

    @property
    def cookie(self):
        return self.__cookie

    @property
    def local_storage(self):
        return self.__local_storage
