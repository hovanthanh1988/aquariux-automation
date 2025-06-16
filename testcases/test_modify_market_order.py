import pytest
import config
from pages.trading_home_page import TradingHomePage


@pytest.mark.usefixtures("setup", "login")
class TestModifyMarketOrder:

    def test_edit_sl_tp_open_position(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        sl_price = ask_price - config.SL
        tp_price = ask_price + config.TP
        trading_home_page.send_buy_order(config.SIZE, sl_price, tp_price)
        trading_home_page.click_edit_position_button()
        trading_home_page.click_increase_sl_price()
        trading_home_page.click_increase_tp_price()
        sl_price_updated = trading_home_page.get_stop_loss_price_on_edit_popup()
        tp_price_updated = trading_home_page.get_take_profit_price_on_edit_popup()
        sl_price_formatted = format(sl_price_updated, ",")
        trading_home_page.click_update_order_button()
        trading_home_page.click_edit_confirmation_confirm_button()
        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "edit_open_position", ask_price, config.SIZE,
                                                                    sl_price_updated, tp_price_updated)
        trading_home_page.validate_placed_details_on_open_position_table("BUY", config.SIZE, ask_price, tp_price_updated, sl_price_formatted)

    def test_close_partial_open_position(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        sl_price = ask_price - config.SL
        tp_price = ask_price + config.TP
        trading_home_page.send_buy_order(config.SIZE, sl_price, tp_price)
        sl_price_formatted = format(sl_price, ",")
        trading_home_page.click_close_open_position_button()
        trading_home_page.input_volume_on_close_order_popup("0.05")
        volume_updated = 0.01
        trading_home_page.click_close_order_button()

        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "close_open_position", ask_price, volume_updated,
                                                                    sl_price, tp_price)
        trading_home_page.validate_placed_details_on_open_position_table("BUY", volume_updated, ask_price, tp_price, sl_price_formatted)

    def test_close_full_open_position(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        sl_price = ask_price - config.SL
        tp_price = ask_price + config.TP
        trading_home_page.send_buy_order(config.SIZE, sl_price, tp_price)
        sl_price_formatted = format(sl_price, ",")
        trading_home_page.click_close_open_position_button()
        trading_home_page.click_close_order_button()

        trading_home_page.validate_order_details_with_notification(config.SYMBOL, "BUY", "close_open_position", ask_price, config.SIZE,
                                                                    sl_price, tp_price)
        trading_home_page.validate_order_detail_not_present_on_open_position_table(sl_price_formatted)

    def test_bulk_close_open_position(self):
        trading_home_page = TradingHomePage(self.driver)
        ask_price = trading_home_page.get_ask_price()
        sl_price = ask_price - config.SL
        tp_price = ask_price + config.TP
        trading_home_page.send_buy_order(config.SIZE, sl_price, tp_price)
        trading_home_page.click_bulk_close_dropdown_and_select("all")
        trading_home_page.click_bulk_close_all_confirmation_button()
        trading_home_page.validate_all_open_positions_closed()