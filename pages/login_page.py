from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    First_Name = (By.ID, "firstname")
    Last_Name = (By.ID, "lastname")
    Email_Adress = (By.ID, "email_address")
    Passpord = (By.ID, "password")
    Password_Con = (By.ID, "password-confirmation")
    LOGIN_BUTTON = (By.XPATH, "//button[@title='Create an Account']")


    def login(self, first_name, last_name,email_address,password,password_con):
        # sign up for new user
        self.enter_text(self.First_Name, first_name)
        self.enter_text(self.Last_Name, last_name)
        self.enter_text(self.Email_Adress, email_address)
        self.enter_text(self.Passpord, password)
        self.enter_text(self.Password_Con, password_con)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
