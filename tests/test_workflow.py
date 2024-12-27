import pytest
import time
import logging
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

# Set up logging
log_file = 'test_workflow.log'  # Define the log file name and location

# Create a logger
logger = logging.getLogger()

# Set the logging level
logger.setLevel(logging.INFO)

# Create a file handler for logging to a file
file_handler = logging.FileHandler(log_file, mode='a')  # 'a' for appending to the file

# Create a log formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add the formatter to both handlers
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)

@pytest.mark.parametrize("first_name, last_name, email_address, password, password_con, item_name", [
    ("John", "Doef", 'johndoe87079@example.com', "Password123", "Password123", "Fusion Backpack")
])
def test_sauce_demo_workflow(driver, first_name, last_name, email_address, password, password_con, item_name):
    logger.info("Starting test: Sauce Demo Workflow")

    # Step 1: Navigate to Login Page
    logger.info("Navigating to login page")
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

    # Initialize LoginPage object
    login_page = LoginPage(driver)
    logger.info("LoginPage object created")

    # Step 2: Perform Login
    logger.info(f"Attempting to log in with email: {email_address}")
    login_page.login(first_name, last_name, email_address, password, password_con)
    logger.info("Login attempted")

    # Step 3: Access InventoryPage and perform actions
    logger.info("Navigating to inventory page")
    inventory_page = InventoryPage(driver)

    # Search item
    logger.info(f"Searching for item: {item_name}")
    inventory_page.search_item(item_name)
    logger.info(f"Search completed for item: {item_name}")

    # Add the first item to the cart
    logger.info("Adding the first item to the cart")
    inventory_page.add_first_item_to_cart()
    time.sleep(2)
    logger.info("Item added to cart")

    # Verifying the actions
    try:
        logger.info("Verifying item in the cart")
        cart_count = inventory_page.count_cart()
        assert int(cart_count) == 1, f"Item was not added to the cart. Cart count: {cart_count}"
        logger.info("Item successfully added to the cart")
        logger.info("Verifying empty cart")
        inventory_page.remove_item()
        time.sleep(2)
        assert inventory_page.count_cart() == '', f"cart not empty"
        logger.info("Remove all item in the cart")
    except Exception as e:
        logger.error(f"Verification failed: {e}")
        raise

    # Optional: Verify that the item was correctly added by checking the cart page
    logger.info("Test completed")

