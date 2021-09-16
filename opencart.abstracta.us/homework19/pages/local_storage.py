from selenium.webdriver.chrome.webdriver import WebDriver

from .base_page_cookie import BasePageCookie


class LocalStorage(BasePageCookie):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_local_storage(self):
        site_local_storage = self._driver.execute_script(
            'return window.localStorage;'
        )
        # print(site_local_storage)
        return site_local_storage
