import time
import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_and_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form > button')
    assert button, 'Button is not found'
    time.sleep(5)