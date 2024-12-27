from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            raise Exception(f"Element not found: {locator} - {str(e)}")


    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def send_element(self, locator,item):
        element = self.wait_for_element(locator)
        element.send_keys(item)
        element.send_keys(Keys.RETURN)

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element(locator).text
