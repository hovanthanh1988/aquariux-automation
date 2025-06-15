import time

from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

from pages.login_page import LogIn
from pages.trade_page import TradePage
from pages.trading_home_page import TradingHomePage
import config

driver = None

@fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@fixture(scope="function")
def login(request):
    driver = request.cls.driver
    trade_page = TradePage(driver)
    login_page = LogIn(driver)
    trading_home_page = TradingHomePage(driver)
    driver.get(config.BASE_URL)
    trade_page.click_start_demo_button()
    trade_page.click_login_button()
    login_page.login(config.USER_NAME, config.PASS_WORD)
    trading_home_page.input_symbol(config.SYMBOL)
    time.sleep(5)
    trading_home_page.click_symbol_search_result(config.SYMBOL)
    time.sleep(5)
