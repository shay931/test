import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def search_item(self, item_name):
        # Find the search bar, enter the item name, and submit the search
        search_bar_locator = (By.ID, "search")  # Replace with the correct ID or locator for the search bar
        self.send_element(search_bar_locator,item_name)

        # Wait for the search results to load
        p_item = (By.CLASS_NAME, "product-item")
        self.wait_for_element(p_item)

    def add_first_item_to_cart(self):
        # first item
        first_item_locator = (By.XPATH, "(//a[contains(@class, 'product-item-link')])[1]")  # Update XPath if necessary
        first_item = self.wait_for_element(first_item_locator)

        # Click on the first product link
        first_item.click()
        # Wait for the "Add to Cart" button to appear and click it
        add_to_cart_button = (By.XPATH, "//button[@title='Add to Cart']")
        self.wait_for_element(add_to_cart_button)
        self.click_element(add_to_cart_button)
    def remove_all_item(self):
        #remove all the items in the cart
        #click on the cart
        CART_LINK  = (By.CSS_SELECTOR, "a.action.showcart")
        self.wait_for_element(CART_LINK )
        self.click_element(CART_LINK )
        #press on remove butrton
        REMOVE_ITEM_BUTTON = (By.XPATH, '//*[@id="mini-cart"]/li/div/div/div[2]/div[2]/a')
        self.wait_for_element(REMOVE_ITEM_BUTTON )
        self.click_element(REMOVE_ITEM_BUTTON )
        #press 'yes' in the message
        EMPTY_CART_MESSAGE   = (By.XPATH, '/html/body/div[3]/aside[2]/div[2]/footer/button[2]')
        self.wait_for_element(EMPTY_CART_MESSAGE  )
        self.click_element(EMPTY_CART_MESSAGE )

    def count_cart(self):
        # check how many items in the cart
        try:
            # Attempt to find the cart count element
            cart_text = self.driver.find_element(By.CSS_SELECTOR, ".counter-number").text.strip()
            return cart_text
        except Exception as e:
            # Raise a custom exception with a descriptive message
            raise RuntimeError("Failed to find the cart count element with CSS selector '.counter-number'.") from e




