import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

@pytest.fixture
def driver():
    try:
        # Attempt to initialize the WebDriver
        driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver  # Provide the WebDriver instance to the test
    except WebDriverException as e:
        raise RuntimeError(f"Failed to initialize the WebDriver: {e}")
    finally:
        try:
            # Attempt to quit the WebDriver
            if driver:
                driver.quit()
        except WebDriverException as e:
            raise RuntimeError(f"Failed to quit the WebDriver: {e}")
