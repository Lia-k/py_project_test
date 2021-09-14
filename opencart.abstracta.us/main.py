import time
from selenium.webdriver import Chrome


def test_task_1(dashboard):
    dashboard.fill_in_the_search_field("iPhone")
    time.sleep(3)
    dashboard.check_searched_element_is_displayed("iPhone")


def test_choose_product_category(dashboard):
    time.sleep(3)
    dashboard.choose_category("1")
    time.sleep(3)

def test_check():
    driver = Chrome("./drivers/chromedriver.exe")
    locator = f"//*[@class='nav navbar-nav']/li[1]/a"
    driver.get("http://opencart.abstracta.us/")
    desktop_element = driver.find_element_by_xpath(
        locator)
    desktop_element.click()
    time.sleep()