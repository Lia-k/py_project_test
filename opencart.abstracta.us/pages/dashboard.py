from typing import Tuple

from basepage import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver


from selenium.webdriver.common.by import By


class Dashboard(BasePage):
    # locators
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__input_field_locator = "//*[@id='search']/input"
        self.__search_button_locator = "//*[@id='search']/span"
        self.__iphone_locator = "//a[text() = 'iPhone']"

    # methods for elements manipulation
    def choose_category(self, item: str) -> None:
        self._click((By.XPATH, f"//*[@class='nav navbar-nav']/li[{item}]/a"))

    def choose_sub_category(self, item: str):
        self._click((By.XPATH, f"//*[@class='nav navbar-nav']/li[1]/div/div/ul/li[{item}]/a"))

    def fill_in_the_search_field(self, text):
        self._send_keys_to_input(self.__input_field_locator, text)
        self._click(self.__search_button_locator)

    def check_searched_element_is_displayed(self, name: str):
        self._check_if_element_is_displayed((By.XPATH, f"//a[text() = {name}]"))
