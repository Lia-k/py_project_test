import pytest
from selenium.webdriver import Chrome
from .pages.base_page import BasePage



@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome(
        '../../drivers/chromedriver.exe')
    driver.get("http://opencart.abstracta.us/")
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    yield BasePage(driver)
