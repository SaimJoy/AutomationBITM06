from selenium import webdriver
import unittest
import pytest
class LoginTest(unittest.TestCase):

    def test_invalid_login(self):
        base_url= "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome(executable_path= "E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe")
        driver.maximize_window()
        driver.get(base_url)




