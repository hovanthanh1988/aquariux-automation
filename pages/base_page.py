from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

TIME_OUT = 10
class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def click_element(self, locator):
        return WebDriverWait(self.driver, TIME_OUT).until(ec.presence_of_element_located(locator)).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, TIME_OUT).until(ec.presence_of_element_located(locator))

    def input_text_to_element(self, locator, text):
        element = WebDriverWait(self.driver, TIME_OUT).until(ec.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, TIME_OUT).until(ec.presence_of_element_located(locator))
            return True
        except:
            return False