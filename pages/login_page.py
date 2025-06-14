from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LogIn(BasePage):

    _demo_account_tab_locator = "//div[@class='sc-1jd986s-0 iqiCBC']"
    _account_id_input_locator = "//input[@data-testid='login-user-id']"
    _password_input_locator = "//input[@data-testid='login-password']"
    _sign_in_button_locator = "//button[@type='submit' and text()='Sign in']"


    def __init__(self, driver):
        super(LogIn, self).__init__(driver)

    def login(self, username, password):
        self.click_element((By.XPATH, self._demo_account_tab_locator))
        self.input_text_to_element((By.XPATH, self._account_id_input_locator), username)
        self.input_text_to_element((By.XPATH, self._password_input_locator), password)
        self.click_element((By.XPATH, self._sign_in_button_locator))