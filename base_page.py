from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    def wait_for_element_present(self,by,value):
        try:
            return self.wait.until(EC.presence_of_element_located((by,value)))
        except Exception as e:
            print(f'Element not present {value} Error:{e}')
            return None
    
    def wait_for_element_clickable(self,by,value):
        try:
            return self.wait.until(EC.element_to_be_clickable((by,value)))
        except Exception as e:
            print(f'Element not clickable {value} Error:{e}')
            return None
        
    def wait_for_element_visible(self,by,value):
        try:
            return self.wait.until(EC.visibility_of_element_located((by,value)))
        except Exception as e:
            print(f'Element not visible {value} Error:{e}')
            return None
    
    def click_text(self,by,value):
        try:
            ele=self.wait_for_element_clickable(by,value)
            if ele:
                ele.click()
                print(f'Clicked on element located by {value}')
        except Exception as e:
            print(f'Error clicking element {value}:{e}')
    
    def enter_text(self,by,value,text):
        try:
            ele=self.wait_for_element_visible(by,value)
            if ele:
                ele.clear()
                ele.send_keys(text)
                print(f'Entered {text} in {value}')
        except Exception as e:
            print(f'Error entering {text} in {value}:{e}')
    
    def get_text(self,by,value):
        try:
            ele=self.wait_for_element_visible(by,value)
            if ele:
                return ele.text
            else:
                return ""
        except Exception as e:
            print(f'Error getting text from {value} :{e}')
            return ""
    
    def is_displayed(self,by,value):
        try:
           ele= self.driver.find_element(by,value)
           return ele.is_displayed()
        except :
            return False
    

