import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--language", action="store", default="ru")


@pytest.fixture(scope="session")
def browser(request):
    if request.config.getoption("browser") == "Firefox":
        browser = webdriver.Firefox()
    elif request.config.getoption("browser") == "Edge":
        browser = webdriver.Edge()
    else:
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": request.config.getoption("language")})
        browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
