from selenium.webdriver.chrome.webdriver import WebDriver

from .base_page_cookie import BasePageCookie


class Cookie(BasePageCookie):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_cookie(self):
        site_cookie = self._driver.get_cookies()
        return site_cookie
