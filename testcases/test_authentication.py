import random
import pytest
import config
from pages.trade_page import TradePage
from pages.login_page import LogIn
from pages.trading_home_page import TradingHomePage

@pytest.mark.usefixtures("setup")
class TestAuthentication:

    def test_register_account_success(self):
        trade_page = TradePage(self.driver)
        random_number = random.randint(1, 9999)

        self.driver.get(config.BASE_URL)
        trade_page.click_start_demo_button()
        trade_page.input_email("test" + str(random_number) + "@gmail.com")
        trade_page.click_check_box()
        trade_page.click_get_start_button()
        trade_page.verify_demo_account_successful_creation_message()

    def test_login_success(self):
        trade_page = TradePage(self.driver)
        login_page = LogIn(self.driver)
        trading_home_page = TradingHomePage(self.driver)

        self.driver.get(config.BASE_URL)
        trade_page.click_start_demo_button()
        trade_page.click_login_button()
        login_page.login(config.USER_NAME, config.PASS_WORD)
        trading_home_page.validate_page_is_trading_homepage(config.USER_NAME)
