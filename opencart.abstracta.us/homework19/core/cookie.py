from selenium.webdriver.chrome.webdriver import WebDriver


class Cookie:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def get_cookie(self):
        site_cookie = self.__driver.get_cookies()
        return site_cookie
