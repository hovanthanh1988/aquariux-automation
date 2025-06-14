import os
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
    _sl_points_input_locator = "//input[@data-testid='trade-input-stoploss-points']"
    _sl_price_input_locator = "//input[@data-testid='trade-input-stoploss-price']"
    _tp_points_input_locator = "//input[@data-testid='trade-input-takeprofit-points']"
    _tp_price_input_locator = "//input[@data-testid='trade-input-takeprofit-price']"
    _order_type_dropdown_locator = "//div[@data-testid='trade-dropdown-order-type']"
    _order_type_market_locator = "//div[@data-testid='trade-dropdown-order-type-market']"
    _order_type_limit_locator = "//div[@data-testid='trade-dropdown-order-type-limit']"
    _order_type_stop_locator = "//div[@data-testid='trade-dropdown-order-type-stop']"
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

    def input_symbol(self, symbol):
        self.input_text_to_element((By.XPATH, self._symbol_input_locator), symbol)

    def click_symbol_search_result(self, symbol):
        self.click_element((By.XPATH, self._symbol_search_results_locator.format(f"'{symbol}'")), 20)

    def click_buy_button(self):
        self.click_element((By.XPATH, self._buy_button_locator))

    def click_sell_button(self):
        self.click_element((By.XPATH, self._sell_button_locator))

    def click_order_type_dropdown_and_select(self, value):
        self.click_element((By.XPATH, self._order_type_dropdown_locator))
        self.click_element((By.XPATH, f"//div[@data-testid='trade-dropdown-order-type-{value.lower()}']"))

    def get_current_trading_symbol(self):
        symbol = self.find_element((By.XPATH, self._current_trading_symbol_locator)).text
        return symbol if symbol else None

    def input_size(self, size):
        self.input_text_to_element((By.XPATH, self._size_input_locator), size)

    def input_sl_points(self, sl):
        self.input_text_to_element((By.XPATH, self._sl_points_input_locator), sl)

    def input_sl_price(self, sl):
        self.input_text_to_element((By.XPATH, self._sl_price_input_locator), sl)

    def input_tp_price(self, tp):
        self.input_text_to_element((By.XPATH, self._tp_price_input_locator), tp)

    def get_ask_price(self):
        ask_price = self.find_element((By.XPATH, self._ask_price_locator)).text
        return float(ask_price.replace(',', '')) if ask_price else None

    def get_bid_price(self):
        bid_price_text = self.find_element((By.XPATH, self._bid_price_locator)).text
        return float(bid_price_text.replace(',', '')) if bid_price_text else None
    def get_sl_price(self):
        return self.find_element((By.XPATH, self._sl_price_input_locator)).get_attribute('value')

    def get_tp_price(self):
        return self.find_element((By.XPATH, self._tp_price_input_locator)).get_attribute('value')

    def input_tp_points(self, tp):
        self.input_text_to_element((By.XPATH, self._tp_points_input_locator), tp)

    def click_trade_button(self):
        self.click_element((By.XPATH, self._trade_button_locator))

    def click_confirm_button(self):
        self.click_element((By.XPATH, self._confirm_button_locator))

    def get_notification_title(self):
        title = self.find_element((By.XPATH, self._notifications_title_locator)).text
        return title
    def get_notification_description(self):
        description = self.find_element((By.XPATH, self._notifications_description_locator)).text
        return description

    def validate_placed_details_with_notification(self, symbol, order_action, order_type, size, sl, tp):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'expected_notifications.json')

        data = modify_notification_data(file_path, symbol, size, sl, tp)
        expected_title = data['market']['title']
        expected_description = data['market'][order_action.upper()]

        notification_title = self.get_notification_title()
        notification_description = self.get_notification_description()

        assert notification_title == expected_title
        assert notification_description == expected_description
