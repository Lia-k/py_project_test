from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)

    def _wait_until_element_appears(self,
                                    locator: Tuple[By, str]) -> WebElement:
        return self.__web_driver_wait.until(
            ec.presence_of_element_located(locator)
        )

    def _click(self, locator: Tuple[By, str]) -> None:
        self._wait_until_element_appears(locator).click()

    def _type_in_input(self, locator: Tuple[By, str], text) -> None:
        element = self._wait_until_element_appears(locator)
        element.send_keys(text)

    def _check_if_element_is_displayed(self, locator: Tuple[By, str]) -> bool:
        return self._wait_until_element_appears(locator).is_displayed()
