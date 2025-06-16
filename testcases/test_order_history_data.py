import pytest
import config
from pages.trading_home_page import TradingHomePage


@pytest.mark.usefixtures("setup", "login")
class TestOrderHistoryData:

    def test_deleted_pending_order_on_history_table(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        price_limit = ask_price - 1000
        sl_price = price_limit - config.SL
        tp_price = price_limit + config.TP

        trading_home_page.click_buy_button()
        trading_home_page.click_order_type_dropdown_and_select("Limit")
        trading_home_page.input_size(config.SIZE)
        trading_home_page.input_price_limit(price_limit)
        trading_home_page.input_sl_price(sl_price)
        trading_home_page.input_tp_price(tp_price)
        trading_home_page.click_expiry_type_dropdown_and_select("good-till-cancelled")
        sl_price_formatted = format(sl_price, ",")
        trading_home_page.click_trade_button()
        trading_home_page.click_confirm_button()
        trading_home_page.click_pending_order_tab()
        order_id = trading_home_page.get_pending_order_id(sl_price_formatted)
        trading_home_page.click_delete_pending_order(sl_price_formatted)
        trading_home_page.click_delete_pending_confirmation_button()
        trading_home_page.click_history_tab()
        trading_home_page.validate_order_on_history_table(order_id)