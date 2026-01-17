from requests import options
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture()
def setup(browser):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.page_load_strategy = "eager"

    driver = None
    if browser == "chrome":
        service = Service(ChromeDriverManager().install(), log_path="chromedriver.log")
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching Chrome Browser...")
    elif browser == "firefox":
        firefox_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)
        print("Launching Firefox Browser...")
    else:
        # fallback to chrome
        service = Service(ChromeDriverManager().install(), log_path="chromedriver.log")
        driver = webdriver.Chrome(service=service, options=options)
        print(f"Launching default Chrome Browser (unknown option '{browser}')...")

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(120)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass

def pytest_addoption(parser):           # this will get the value from CLI/hooks
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests")

@pytest.fixture()           # this will return the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


# Metadata customization for HTML reports
def pytest_configure(config):
    # Ensure compatibility with pytest-html versions where _metadata may not exist
    if not hasattr(config, "_metadata") or config._metadata is None:
        try:
            config._metadata = {}
        except Exception:
            # If we cannot set _metadata, skip adding metadata
            return

    config._metadata['Project Name'] = 'Ecommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = "It's Me"


#it is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)