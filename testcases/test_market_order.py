import pytest
import config
from pages.trading_home_page import TradingHomePage
import time


@pytest.mark.usefixtures("setup", "login")
class TestMarketOrder:

    def test_place_market_buy_order_with_sl_tp(self):
        trading_home_page = TradingHomePage(self.driver)
        trading_home_page.click_buy_button()
        trading_home_page.click_order_type_dropdown_and_select("market")
        trading_home_page.input_size(config.SIZE)
        ask_price = trading_home_page.get_ask_price()
        sl_price = ask_price - config.SL
        tp_price = ask_price + config.TP
        trading_home_page.input_sl_price(sl_price)
        trading_home_page.input_tp_price(tp_price)
        trading_home_page.click_buy_button()
        trading_home_page.click_trade_button()
        trading_home_page.click_confirm_button()
        trading_home_page.validate_placed_details_with_notification(config.SYMBOL, "BUY", "market", config.SIZE, sl_price, tp_price)
        trading_home_page.validate_placed_details_with_table_detail("BUY", config.SIZE, ask_price, tp_price, sl_price)
    def test_place_market_sell_order_with_sl_tp(self):
        trading_home_page = TradingHomePage(self.driver)
        trading_home_page.click_sell_button()
        trading_home_page.click_order_type_dropdown_and_select("market")
        trading_home_page.input_size(config.SIZE)
        bid_price = trading_home_page.get_bid_price()
        sl_price = bid_price + config.SL
        tp_price = bid_price - config.TP
        trading_home_page.input_sl_price(sl_price)
        trading_home_page.input_tp_price(tp_price)
        trading_home_page.click_sell_button()
        trading_home_page.click_trade_button()
        trading_home_page.click_confirm_button()
        trading_home_page.validate_placed_details_with_notification(config.SYMBOL, "SELL", "market", config.SIZE,
                                                                    sl_price, tp_price)
        trading_home_page.validate_placed_details_with_table_detail("SELL", config.SIZE, bid_price, tp_price, sl_price)



