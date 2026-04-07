import time

from selenium.webdriver.chrome.options import Options
from pygments.lexer import default
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--language", action="store", default="ru")

@pytest.fixture
def browser(request):
    if request.config.getoption("browser") == "Firefox":
        browser= webdriver.Firefox()
    elif request.config.getoption("browser") == "Safari":
        browser = webdriver.Safari()
    else:
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": request.config.getoption("browser")})
        browser = webdriver.Chrome(options = options)

    browser.implicitly_wait(3)
    yield browser
    browser.quit()