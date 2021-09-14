from .base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Dashboard(BasePage):
    # locators
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__input_field_locator = (By.XPATH, "//*[@id='search']/input")
        self.__search_button_locator = (By.XPATH, "//*[@id='search']/span")

    # methods for elements manipulation
    def choose_category(self, item: str) -> None:
        self._click((By.XPATH, f"//*[@class='nav navbar-nav']/li[{item}]/a"))

    def choose_sub_category(self, item: str) -> None:
        self._click((By.XPATH,
                     f"//*[@class='nav navbar-nav']/li[1]/div/div/ul/li[{item}]/a"))

    def find_item_with_search_field(self, text) -> None:
        self._type_in_input(self.__input_field_locator, text)
        self._click(self.__search_button_locator)

    def test_check(self) -> None:
        self._click((By.XPATH, "//*[@id='search']/span"))
