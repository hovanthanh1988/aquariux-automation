from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TradingHomePage(BasePage):

    _account_id_locator = "//div[@data-testid='account-id']"
    _buy_button_locator = "//div[@data-testid='trade-button-order-buy']"
    _sell_button_locator = "//div[@data-testid='trade-button-order-sell']"
    _size_input_locator = "//input[@data-testid='trade-input-volume']"
    _sl_points_input_locator = "//input[@data-testid='trade-input-stoploss-points']"
    _tp_points_input_locator = "//input[@data-testid='trade-input-takeprofit-points']"
    _order_type_dropdown_locator = "//div[@data-testid='trade-dropdown-order-type']"
    _order_type_market_locator = "//div[@data-testid='trade-dropdown-order-type-market']"
    _order_type_limit_locator = "//div[@data-testid='trade-dropdown-order-type-limit']"
    _order_type_stop_locator = "//div[@data-testid='trade-dropdown-order-type-stop']"
    _symbol_input_locator = "//div[@data-testid='symbol-input-search']"

    def __init__(self, driver):
        super(TradingHomePage, self).__init__(driver)

    def verify_is_trading_homepage(self, account_id):
        account = self.find_element((By.XPATH, self._account_id_locator)).text
        buy_button = self.is_element_present((By.XPATH, self._buy_button_locator))
        sell_button = self.is_element_present((By.XPATH, self._sell_button_locator))
        assert account == account_id
        assert buy_button is True
        assert sell_button is True

    def input_symbol(self, symbol):
        self.input_text_to_element((By.XPATH, self._symbol_input_locator), symbol)

    def click_buy_button(self):
        self.click_element((By.XPATH, self._buy_button_locator))

    def click_sell_button(self):
        self.click_element((By.XPATH, self._sell_button_locator))

    def click_order_type_dropdown_and_select(self, value):
        self.click_element((By.XPATH, self._order_type_dropdown_locator))
        self.click_element((By.XPATH, f"//div[@data-testid='trade-dropdown-order-type-{value.lower()}']"))

    def input_size(self, size):
        self.input_text_to_element((By.XPATH, self._size_input_locator), size)

    def input_sl_points(self, sl):
        self.input_text_to_element((By.XPATH, self._sl_points_input_locator), sl)

    def input_tp_points(self, tp):
        self.input_text_to_element((By.XPATH, self._tp_points_input_locator), tp)
