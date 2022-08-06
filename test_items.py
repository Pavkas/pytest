from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_basket_on_page(browser):
    browser.get(link)
    time.sleep(30)
    found = len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"))
    assert found > 0, 'OBLOM'