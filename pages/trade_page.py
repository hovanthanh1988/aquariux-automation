from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class TradePage(BasePage):

    _start_demo_button_locator = "//span[@data-title='Start Demo']"
    _email_input_locator = "//input[@class='InputStyles__StyledInput-sc-1rb0qf-1 eeYAwF']"
    _check_box_locator = "//img[@alt='checkbox']"
    _get_start_button_locator = "//button[@class='Buttonstyled__Button-sc-1s3irv9-0 vteFn']"
    _demo_acc_create_message_locator = "//h2[text()='Your demo account is ready!']"
    _login_button_locator = "//button[normalize-space()='Login']"


    def __init__(self, driver):
        super(TradePage, self).__init__(driver)
    def click_start_demo_button(self):
        self.click_element((By.XPATH, self._start_demo_button_locator))

    def input_email(self, email):
        self.input_text_to_element((By.XPATH, self._email_input_locator), email)

    def click_check_box(self):
        self.click_element((By.XPATH, self._check_box_locator))

    def click_get_start_button(self):
        self.click_element((By.XPATH, self._get_start_button_locator))

    def verify_demo_account_successful_creation_message(self):
        success_message = self.find_element((By.XPATH, self._demo_acc_create_message_locator)).text
        assert success_message == 'Your demo account is ready!'

    def click_login_button(self):
        self.click_element((By.XPATH, self._login_button_locator))
