import pytest
from selenium.webdriver import Chrome
from .pages.cookie import Cookie
from .pages.local_storage import LocalStorage


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome(
        '../../drivers/chromedriver.exe')
    driver.get("http://opencart.abstracta.us/")
    yield driver
    driver.quit()


@pytest.fixture
def cookie(driver):
    yield Cookie(driver)


@pytest.fixture
def local_storage(driver):
    yield LocalStorage(driver)
