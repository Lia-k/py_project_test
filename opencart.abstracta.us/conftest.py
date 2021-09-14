import pytest
from selenium.webdriver import Chrome
from pages.dashboard import Dashboard
from pages.product_list_page import ProductListPage


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("C:/Users/Asus/Desktop/py_project_test/opencart.abstracta.us/drivers/chromedriver.exe")
    driver.get("http://opencart.abstracta.us/")
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)


@pytest.fixture
def product_list(driver):
    yield ProductListPage(driver)
