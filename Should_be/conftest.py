import os
import os.path
import sys
import time
import pytest

# Ensure imports like `from pages.* import ...` work when pytest is run from repo root.
_HERE = os.path.dirname(__file__)
_PAGES_DIR = os.path.join(_HERE, "pages")
for _p in (_HERE, _PAGES_DIR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

def add_bug_to_taiga(taiga_client, item, report, screen_name):
    project = taiga_client.projects.get_by_slug("workerbntu-selenium")
    bug = project.add_issue(
        subject=f"Баг в методе {item.name}",
        description=f"Лог бага: {report.longreprtext}",
        # надо сделать запросы к project.метод_получения чтобы узнать, какие у нас вообще есть priority, status и т.д.

        priority=5365485,
        status=12511907,
        issue_type=5377812,
        severity=8931344
    )
    if screen_name:
        bug.attach(screen_name)

    project.add_user_story(
        subject=f"Починить: {bug.subject}",
        description=f"Исправить баг {bug.ref}\n{bug.description}"
    )


@pytest.fixture(scope="session")
def taiga_client(request):
    if request.config.getoption("taiga"):
        token = os.getenv("TAIGA_TOKEN")
        if not token:
            return None
        try:
            from taiga import TaigaAPI  # optional dependency
        except Exception:
            return None
        return TaigaAPI(token=token)
    return None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--language", action="store", default="ru")
    parser.addoption("--taiga", action="store_true")
    parser.addoption("--headless", action="store_true")

@pytest.fixture(scope="session")
def browser(request):
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
    except Exception as e:
        raise RuntimeError(
            "Selenium не установлен. Поставь зависимости, например: pip install selenium"
        ) from e

    if request.config.getoption("browser") == "Firefox":
        browser = webdriver.Firefox()
    elif request.config.getoption("browser") == "Edge":
        browser = webdriver.Edge()
    else:
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_experimental_option("prefs", {"intl.accept_languages": request.config.getoption("language")})
        if request.config.getoption("headless"):
            options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    taiga_client = getattr(item, "funcargs", {}).get("taiga_client")
    browser = getattr(item, "funcargs", {}).get("browser")

    if not taiga_client:
        return
    if not browser:
        add_bug_to_taiga(taiga_client, item, report, None)
        return

    try:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        screen_name = f"screenshots/fail_{item.name}_{timestamp}.png"
        browser.save_screenshot(screen_name)
    except:
        screen_name = None


    add_bug_to_taiga(taiga_client, item, report, screen_name)