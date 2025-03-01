import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
import argparse

def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='Choose browser Chrome/Firefox'
    )

@pytest.fixture()
def browser(request):
    if request.config.getoption('--browser') == 'firefox':
        browser = Firefox()
    elif request.config.getoption('--browser') == 'chrome':
        browser = Chrome()
    yield browser
    browser.quit()



