
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

    def login_page(self):
        _email_field = self.driver.find_element(By.ID, "txtUsername")
        _password_field = self.driver.find_element(By.ID, "txtPassword")
        _login_btn = self.driver.find_element(By.ID, "btnLogin")

        _email_field.clear()
        _email_field.send_keys()
        _password_field.clear()
        _password_field.send_keys()

        _login_btn.click()
