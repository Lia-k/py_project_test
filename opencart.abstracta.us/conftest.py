from typing import Tuple

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboard import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("./drivers/chromedriver.exe")
    driver.get("http://opencart.abstracta.us/")
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
