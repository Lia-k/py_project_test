import time

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement


def test_task_1():
    driver = Chrome("./drivers/chromedriver.exe")
    input_field_locator = "//*[@id='search']/input"
    search_button_locator = "//*[@id='search']/span"
    iphone_locator = "//a[text() = 'iPhone']"

    driver.get("http://opencart.abstracta.us/")
    input_field_element: WebElement = driver.find_element_by_xpath(input_field_locator)
    input_field_element.send_keys('iphone')
    search_button_element: WebElement = driver.find_element_by_xpath(search_button_locator)
    search_button_element.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    iphone_element: WebElement = driver.find_element_by_xpath(iphone_locator)
    iphone_element.is_displayed()
