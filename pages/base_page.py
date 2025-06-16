from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

TIME_OUT = 20
class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def click_element(self, locator, timeout=TIME_OUT):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator)).click()

    def click_element_by_java_script(self, locator, timeout=TIME_OUT):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def find_element(self, locator, timeout=TIME_OUT):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def input_text_to_element(self, locator, text, timeout=TIME_OUT):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def input_text_to_element_by_java_script(self, locator, text, timeout=TIME_OUT):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        element.clear()

        self.driver.execute_script("""
                        arguments[0].value = arguments[1];
                        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                        arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
                    """, element, text)

    def is_element_present(self, locator, timeout=TIME_OUT):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
            return True
        except:
            return False

