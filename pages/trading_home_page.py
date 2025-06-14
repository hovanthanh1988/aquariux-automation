from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TradingHomePage(BasePage):

    _account_id_locator = "//div[@data-testid='account-id']"
    _buy_button_locator = "//div[@data-testid='trade-button-order-buy']"
    _sell_button_locator = "//div[@data-testid='trade-button-order-sell']"

    def __init__(self, driver):
        super(TradingHomePage, self).__init__(driver)

    def click_trade_button(self):
        self.click_element((By.XPATH, self._trade_button_locator))

    def verify_is_trading_homepage(self, account_id):
        account = self.find_element((By.XPATH, self._account_id_locator)).text
        buy_button = self.is_element_present((By.XPATH, self._buy_button_locator))
        sell_button = self.is_element_present((By.XPATH, self._sell_button_locator))
        assert account == account_id
        assert buy_button is True
        assert sell_button is True