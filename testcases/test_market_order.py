import pytest
import config
from pages.trading_home_page import TradingHomePage
import time


@pytest.mark.usefixtures("setup", "login")
class TestMarketOrder:

    def test_place_market_order_with_sl_tp(self):
        trading_home_page = TradingHomePage(self.driver)
        trading_home_page.click_buy_button()
        trading_home_page.click_order_type_dropdown_and_select("market")
        trading_home_page.input_size(config.SIZE)
        trading_home_page.input_sl_points(config.SL)
        trading_home_page.input_tp_points(config.TP)
        time.sleep(30)  # Wait for the inputs to be processed


