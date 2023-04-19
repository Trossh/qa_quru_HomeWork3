import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'

    # browser.driver.set_window_size(1980, 1080)
    # browser.execute_script("setTimeout(function(){debugger;}, 5000)")
