from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Login(BasePage):
    USERNAME = (By.NAME, "j_username")
    PASSWORD = (By.NAME, "j_password")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
    ERROR_MSG= (By.CLASS_NAME, "ui segment raised red big") 

    def enter_username(self,username):
        self.enter_text(*self.USERNAME,text=username)

    def enter_password(self,password):
        self.enter_text(*self.PASSWORD,text=password)

    def click_login(self):
        self.click_text(*self.LOGIN_BUTTON)
    
    def login_meth(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_msg(self):
        return self.get_text(*self.ERROR_MSG)
    
    def is_loginpage_displayed(self):
        return self.is_displayed(*self.LOGIN_BUTTON)
