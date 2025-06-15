from datetime import datetime
import os
import time

import config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.utils import load_test_data
from utils.utils import modify_notification_data


class TradingHomePage(BasePage):

    _account_id_locator = "//div[@data-testid='account-id']"
    _buy_button_locator = "//div[@data-testid='trade-button-order-buy']"
    _sell_button_locator = "//div[@data-testid='trade-button-order-sell']"
    _size_input_locator = "//input[@data-testid='trade-input-volume']"
    _price_input_locator = "//input[@data-testid='trade-input-price']"
    _sl_points_input_locator = "//input[@data-testid='trade-input-stoploss-points']"
    _sl_price_input_locator = "//input[@data-testid='trade-input-stoploss-price']"
    _tp_points_input_locator = "//input[@data-testid='trade-input-takeprofit-points']"
    _tp_price_input_locator = "//input[@data-testid='trade-input-takeprofit-price']"
    _order_type_dropdown_locator = "//div[@data-testid='trade-dropdown-order-type']"
    _order_type_market_locator = "//div[@data-testid='trade-dropdown-order-type-market']"
    _order_type_limit_locator = "//div[@data-testid='trade-dropdown-order-type-limit']"
    _order_type_stop_locator = "//div[@data-testid='trade-dropdown-order-type-stop']"

    _expiry_type_dropdown_locator = "//div[@data-testid='trade-dropdown-expiry']"
    _expiry_gtc_dropdown_locator = "//div[@data-testid='trade-dropdown-expiry-good-till-cancelled']"
    _expiry_gtd_dropdown_locator = "//div[@data-testid='trade-dropdown-expiry-good-till-day']"

    _symbol_input_locator = "//input[@data-testid='symbol-input-search']"
    _symbol_search_results_locator = "//div[@class='sc-1jx9xug-5 gVqGuT' and text()={}]"
    _trade_button_locator = "//button[@data-testid='trade-button-order']"
    _confirm_button_locator = "//button[@data-testid='trade-confirmation-button-confirm']"
    _notifications_locator = "//div[@data-testid='notification-description']"
    _notifications_title_locator = "//div[@data-testid='notification-title']"
    _notifications_description_locator = "//div[@data-testid='notification-description']"
    _ask_price_locator = "//div[@data-testid='trade-live-buy-price']"
    _bid_price_locator = "//div[@data-testid='trade-live-sell-price']"
    _current_trading_symbol_locator = "//div[@data-testid='symbol-overview-id']"

    _open_date_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]/preceding-sibling::th[@data-testid='asset-open-column-open-date']"
    _open_type_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]/preceding-sibling::td[@data-testid='asset-open-column-order-type']"
    _open_size_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]/preceding-sibling::td[@data-testid='asset-open-column-volume']"
    _open_unit_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]/preceding-sibling::td[@data-testid='asset-open-column-units']"
    _entry_price_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]/preceding-sibling::td[@data-testid='asset-open-column-entry-price']"
    _take_profit_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]/preceding-sibling::td[@data-testid='asset-open-column-take-profit']"
    _stop_loss_locator = "//td[@data-testid='asset-open-column-stop-loss' and text()={}]"

    _edit_position_button_locator = "//div[@data-testid='asset-open-button-edit']"
    _edit_input_stoploss_price_locator = "//input[@data-testid='edit-input-stoploss-price']"
    _edit_stoploss_price_decrease_locator = "//div[@data-testid='edit-input-stoploss-price-decrease']"
    _edit_stoploss_price_increase_locator = "//div[@data-testid='edit-input-stoploss-price-increase']"
    _edit_input_takeprofit_price_locator = "//input[@data-testid='edit-input-takeprofit-price']"
    _edit_takeprofit_price_decrease_locator = "//div[@data-testid='edit-input-takeprofit-price-decrease']"
    _edit_takeprofit_price_increase_locator = "//div[@data-testid='edit-input-takeprofit-price-increase']"
    _edit_order_button_locator = "//button[@data-testid='edit-button-order']"
    _edit_confirmation_confirm_button_locator = "//button[@data-testid='edit-confirmation-button-confirm']"

    _close_open_position_button_locator = "//div[@data-testid='asset-open-button-close']"
    _edit_volume_decrease_locator = "//div[@data-testid='close-order-input-volume-decrease']"
    _close_order_input_volume_locator = "//input[@data-testid='close-order-input-volume']"
    _close_order_button_locator = "//button[@data-testid='close-order-button-submit']"
    _close_notification_locator = "//svg[@data-testid='notification-close-button']"

    def __init__(self, driver):
        super(TradingHomePage, self).__init__(driver)

    def validate_page_is_trading_homepage(self, account_id):
        account = self.find_element((By.XPATH, self._account_id_locator)).text
        buy_button = self.is_element_present((By.XPATH, self._buy_button_locator))
        sell_button = self.is_element_present((By.XPATH, self._sell_button_locator))
        url = self.driver.current_url
        assert url == config.TRADING_HOME_URL
        assert account == account_id
        assert buy_button is True
        assert sell_button is True

    def get_current_trading_symbol(self):
        symbol = self.find_element((By.XPATH, self._current_trading_symbol_locator)).text
        return symbol if symbol else None

    def get_ask_price(self):
        ask_price = self.find_element((By.XPATH, self._ask_price_locator)).text
        return float(ask_price.replace(',', '')) if ask_price else None

    def get_bid_price(self):
        bid_price = self.find_element((By.XPATH, self._bid_price_locator)).text
        return float(bid_price.replace(',', '')) if bid_price else None

    def get_sl_price(self):
        return self.find_element((By.XPATH, self._sl_price_input_locator)).get_attribute('value')

    def get_tp_price(self):
        return self.find_element((By.XPATH, self._tp_price_input_locator)).get_attribute('value')

    def get_notification_title(self):
        title = self.find_element((By.XPATH, self._notifications_title_locator)).text
        return title

    def get_notification_description(self):
        description = self.find_element((By.XPATH, self._notifications_description_locator)).text
        return description

    def get_open_date(self, sl):
        open_date = self.find_element((By.XPATH, self._open_date_locator.format(f"'{sl}'"))).text
        return open_date

    def get_open_type(self, sl):
        open_type = self.find_element((By.XPATH, self._open_type_locator.format(f"'{sl}'"))).text
        return open_type

    def get_open_size(self, sl):
        open_size = self.find_element((By.XPATH, self._open_size_locator.format(f"'{sl}'"))).text
        return float(open_size.replace(',', '')) if open_size else None

    def get_open_unit(self, sl):
        open_unit = self.find_element((By.XPATH, self._open_unit_locator.format(f"'{sl}'"))).text
        return float(open_unit.replace(',', '')) if open_unit else None

    def get_entry_price(self, sl):
        entry_price = self.find_element((By.XPATH, self._entry_price_locator.format(f"'{sl}'"))).text
        return float(entry_price.replace(',', '')) if entry_price else None

    def get_take_profit(self, sl):
        take_profit = self.find_element((By.XPATH, self._take_profit_locator.format(f"'{sl}'"))).text
        return float(take_profit.replace(',', '')) if take_profit else None

    def get_stop_loss(self, sl):
        stop_loss = self.find_element((By.XPATH, self._stop_loss_locator.format(f"'{sl}'"))).text
        return float(stop_loss.replace(',', '')) if stop_loss else None

    def get_stop_loss_price_on_edit_popup(self):
        sl_price = self.find_element((By.XPATH, self._edit_input_stoploss_price_locator)).get_attribute('value')
        return float(sl_price.replace(',', '')) if sl_price else None

    def get_take_profit_price_on_edit_popup(self):
        tp_price = self.find_element((By.XPATH, self._edit_input_takeprofit_price_locator)).get_attribute('value')
        return float(tp_price.replace(',', '')) if tp_price else None

    def get_input_volume_on_close_order_popup(self):
        close_order_input_volume = self.find_element((By.XPATH, self._close_order_input_volume_locator)).get_attribute('value')
        return float(close_order_input_volume)

    def input_symbol(self, symbol):
        self.input_text_to_element((By.XPATH, self._symbol_input_locator), symbol)

    def input_size(self, size):
        self.input_text_to_element((By.XPATH, self._size_input_locator), size)

    def input_price_limit(self, price):
        self.input_text_to_element((By.XPATH, self._price_input_locator), price)

    def input_sl_points(self, sl):
        self.input_text_to_element((By.XPATH, self._sl_points_input_locator), sl)

    def input_sl_price(self, sl):
        self.input_text_to_element((By.XPATH, self._sl_price_input_locator), sl)

    def input_tp_price(self, tp):
        self.input_text_to_element((By.XPATH, self._tp_price_input_locator), tp)

    def input_tp_points(self, tp):
        self.input_text_to_element((By.XPATH, self._tp_points_input_locator), tp)

    def input_volume_on_close_order_popup(self, volume):
        self.input_text_to_element((By.XPATH, self._close_order_input_volume_locator), volume)

    def click_symbol_search_result(self, symbol):
        self.click_element((By.XPATH, self._symbol_search_results_locator.format(f"'{symbol}'")), 20)

    def click_buy_button(self):
        self.click_element((By.XPATH, self._buy_button_locator))

    def click_sell_button(self):
        self.click_element((By.XPATH, self._sell_button_locator))

    def click_order_type_dropdown_and_select(self, value):
        self.click_element((By.XPATH, self._order_type_dropdown_locator))
        self.click_element((By.XPATH, f"//div[@data-testid='trade-dropdown-order-type-{value.lower()}']"))

    def click_expiry_type_dropdown_and_select(self, value):
        self.click_element((By.XPATH, self._expiry_type_dropdown_locator))
        self.click_element((By.XPATH, f"//div[@data-testid='trade-dropdown-expiry-{value.lower()}']"))

    def click_trade_button(self):
        self.click_element((By.XPATH, self._trade_button_locator))

    def click_confirm_button(self):
        self.click_element((By.XPATH, self._confirm_button_locator))

    def click_edit_position_button(self):
        self.click_element((By.XPATH, self._edit_position_button_locator))

    def click_increase_sl_price(self):
        self.click_element((By.XPATH, self._edit_stoploss_price_increase_locator))

    def click_decrease_sl_price(self):
        self.click_element((By.XPATH, self._edit_stoploss_price_decrease_locator))

    def click_increase_tp_price(self):
        self.click_element((By.XPATH, self._edit_takeprofit_price_increase_locator))

    def click_decrease_tp_price(self):
        self.click_element((By.XPATH, self._edit_takeprofit_price_decrease_locator))

    def click_decrease_volume(self):
        self.click_element((By.XPATH, self._edit_volume_decrease_locator))

    def click_update_order_button(self):
        self.click_element((By.XPATH, self._edit_order_button_locator))

    def click_edit_confirmation_confirm_button(self):
        self.click_element((By.XPATH, self._edit_confirmation_confirm_button_locator))

    def click_close_open_position_button(self):
        self.click_element((By.XPATH, self._close_open_position_button_locator))

    def click_close_order_button(self):
        self.click_element((By.XPATH, self._close_order_button_locator))

    def click_close_notification(self):
        if self.is_notification_present():
            self.click_element((By.XPATH, self._close_notification_locator))

    def is_notification_present(self):
        return self.is_element_present((By.XPATH, self._notifications_locator))

    def is_open_position_date_present(self, sl):
        try:
            self.find_element((By.XPATH, self._open_date_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def is_open_position_type_present(self, sl):
        try:
            self.find_element((By.XPATH, self._open_type_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def is_open_position_size_present(self, sl):
        try:
            self.find_element((By.XPATH, self._open_size_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def is_open_position_unit_present(self, sl):
        try:
            self.find_element((By.XPATH, self._open_unit_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def is_open_position_entry_price_present(self, sl):
        try:
            self.find_element((By.XPATH, self._entry_price_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def is_open_position_take_profit_present(self, sl):
        try:
            self.find_element((By.XPATH, self._take_profit_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def is_open_position_stop_loss_present(self, sl):
        try:
            self.find_element((By.XPATH, self._stop_loss_locator.format(f"'{sl}'")))
            return True
        except Exception:
            return False

    def send_buy_order(self, size, sl, tp):
        self.click_buy_button()
        self.click_order_type_dropdown_and_select("market")
        self.input_size(size)
        self.input_sl_price(sl)
        self.input_tp_price(tp)
        self.click_trade_button()
        self.click_confirm_button()
        time.sleep(10)

    def validate_order_details_with_notification(self, symbol, order_action, order_type, entry_price, size, sl, tp):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'expected_notifications.json')

        data = modify_notification_data(file_path, symbol, order_type, entry_price, size, sl, tp)
        expected_title = data[order_type]['title']
        expected_description = data[order_type][order_action.upper()]

        notification_title = self.get_notification_title()
        notification_description = self.get_notification_description()

        assert notification_title == expected_title
        assert notification_description == expected_description

    def validate_placed_details_on_open_position_table(self, order_action, size, entry_price, tp, sl):
        time.sleep(10)
        expected_open_date = datetime.now().date().strftime("%Y-%m-%d")
        actual_open_date = self.get_open_date(sl)
        actual_open_type = self.get_open_type(sl)
        actual_open_size = self.get_open_size(sl)
        actual_open_unit = self.get_open_unit(sl)
        actual_entry_price = self.get_entry_price(sl)
        actual_take_profit = self.get_take_profit(sl)
        actual_stop_loss = self.get_stop_loss(sl)

        assert expected_open_date in actual_open_date
        assert actual_open_type == order_action
        assert actual_open_size == size
        assert actual_open_unit == size
        assert actual_entry_price == entry_price
        assert actual_take_profit == tp
        assert actual_stop_loss == float(sl.replace(',', ''))

    def validate_order_detail_not_present_on_open_position_table(self, sl):
        time.sleep(10)
        open_date = self.is_open_position_date_present(sl)
        open_type = self.is_open_position_type_present(sl)
        open_size = self.is_open_position_size_present(sl)
        open_unit = self.is_open_position_unit_present(sl)
        entry_price = self.is_open_position_entry_price_present(sl)
        take_profit = self.is_open_position_take_profit_present(sl)
        stop_loss = self.is_open_position_stop_loss_present(sl)

        assert not open_date
        assert not open_type
        assert not open_size
        assert not open_unit
        assert not entry_price
        assert not take_profit
        assert not stop_loss

    def validate_placed_details_on_pending_order_table(self, order_action, size, entry_price, tp, sl):
        time.sleep(10)
        expected_open_date = datetime.now().date().strftime("%Y-%m-%d")
        actual_open_date = self.get_open_date(sl)
        actual_open_type = self.get_open_type(sl)
        actual_open_size = self.get_open_size(sl)
        actual_open_unit = self.get_open_unit(sl)
        actual_entry_price = self.get_entry_price(sl)
        actual_take_profit = self.get_take_profit(sl)
        actual_stop_loss = self.get_stop_loss(sl)

        assert expected_open_date in actual_open_date
        assert actual_open_type == order_action
        assert actual_open_size == size
        assert actual_open_unit == size
        assert actual_entry_price == entry_price
        assert actual_take_profit == tp
        assert actual_stop_loss == float(sl.replace(',', ''))


