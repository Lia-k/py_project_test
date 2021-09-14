from .base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProductListPage(BasePage):
    # locators
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__content_locator = (By.XPATH, "//*[@id='content']")

    def check_searched_element_is_displayed(self, name: str) -> None:
        self._check_if_element_is_displayed(
            (By.XPATH, f"//a[text() = '{name}']"))
