from selenium import webdriver
from pages.login_page import Login

driver =webdriver.Chrome()
driver.get("https://skillrack.com/faces/ui/profile.xhtml")

login_page=Login(driver)

if(login_page.is_loginpage_displayed()):
    login_page.login_meth("22cs018","123")
    print(login_page.get_error_msg())
else:
    print("Login page not displayed")