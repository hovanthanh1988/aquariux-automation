import pytest
import config
from pages.trading_home_page import TradingHomePage


@pytest.mark.usefixtures("setup", "login")
class TestPendingOrder:
    def test_place_limit_buy_order_with_gtc_expiry(self):
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
        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "Limit", price_limit,
                                                               config.SIZE,
                                                               sl_price, tp_price)
        trading_home_page.click_pending_order_tab()
        trading_home_page.validate_placed_details_on_pending_order_table("BUY LIMIT", config.SIZE, price_limit, tp_price,
                                                                 sl_price_formatted, "Good Till Cancelled")

    def test_place_limit_buy_order_with_gtd_expiry(self):
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
        trading_home_page.click_expiry_type_dropdown_and_select("good-till-day")
        sl_price_formatted = format(sl_price, ",")
        trading_home_page.click_trade_button()
        trading_home_page.click_confirm_button()
        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "Limit", price_limit,
                                                               config.SIZE,
                                                               sl_price, tp_price)
        trading_home_page.click_pending_order_tab()
        trading_home_page.validate_placed_details_on_pending_order_table("BUY LIMIT", config.SIZE, price_limit, tp_price,
                                                                 sl_price_formatted, "Good Till Day")

    def test_place_stop_buy_order_with_gtc_expiry(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        price_limit = ask_price + 1000
        sl_price = price_limit - config.SL
        tp_price = price_limit + config.TP

        trading_home_page.click_buy_button()
        trading_home_page.click_order_type_dropdown_and_select("Stop")
        trading_home_page.input_size(config.SIZE)
        trading_home_page.input_price_limit(price_limit)
        trading_home_page.input_sl_price(sl_price)
        trading_home_page.input_tp_price(tp_price)
        trading_home_page.click_expiry_type_dropdown_and_select("good-till-cancelled")
        sl_price_formatted = format(sl_price, ",")
        trading_home_page.click_trade_button()
        trading_home_page.click_confirm_button()
        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "Stop", price_limit,
                                                               config.SIZE,
                                                               sl_price, tp_price)
        trading_home_page.click_pending_order_tab()
        trading_home_page.validate_placed_details_on_pending_order_table("BUY STOP", config.SIZE, price_limit, tp_price,
                                                                 sl_price_formatted, "Good Till Cancelled")

    def test_place_stop_buy_order_with_gtd_expiry(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        price_limit = ask_price + 1000
        sl_price = price_limit - config.SL
        tp_price = price_limit + config.TP

        trading_home_page.click_buy_button()
        trading_home_page.click_order_type_dropdown_and_select("Stop")
        trading_home_page.input_size(config.SIZE)
        trading_home_page.input_price_limit(price_limit)
        trading_home_page.input_sl_price(sl_price)
        trading_home_page.input_tp_price(tp_price)
        trading_home_page.click_expiry_type_dropdown_and_select("good-till-day")
        sl_price_formatted = format(sl_price, ",")
        trading_home_page.click_trade_button()
        trading_home_page.click_confirm_button()
        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "Stop", price_limit,
                                                               config.SIZE,
                                                               sl_price, tp_price)
        trading_home_page.click_pending_order_tab()
        trading_home_page.validate_placed_details_on_pending_order_table("BUY STOP", config.SIZE, price_limit, tp_price,
                                                                 sl_price_formatted, "Good Till Day")

    def test_edit_pending_order_all_fields(self):
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

        new_sl = sl_price + 500
        new_tp = tp_price - 500
        new_entry_price = price_limit + 200
        new_expiry_type = "good-till-day"

        trading_home_page.click_edit_pending_order_button(sl_price_formatted)
        trading_home_page.update_pending_order_price(new_entry_price)
        trading_home_page.update_pending_order_sl_price(new_sl)
        trading_home_page.update_pending_order_tp_price(new_tp)
        trading_home_page.update_expiry_pending_order_and_select(new_expiry_type)
        trading_home_page.click_update_order_button()
        trading_home_page.click_edit_confirmation_confirm_button()

        sl_new_formatted = format(new_sl, ",")
        trading_home_page.validate_placed_details_on_pending_order_table("BUY LIMIT", config.SIZE, new_entry_price, new_tp,
                                                                 sl_new_formatted, "Good Till Day")