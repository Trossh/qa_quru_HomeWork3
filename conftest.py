import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.open_url('https://demoqa.com/automation-practice-form')
    browser.driver.set_window_size(1980, 1080)
    #browser.execute_script("setTimeout(function(){debugger;}, 5000)")


