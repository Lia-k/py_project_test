from selenium.webdriver.chrome.webdriver import WebDriver


class LocalStorage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def get_local_storage(self):
        site_local_storage = self.__driver.execute_script(
            'return window.localStorage;'
        )
        return site_local_storage
