import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class HeadlessAutomotion():

    def test(self):
        # headless part
        headless_option = webdriver.ChromeOptions()
        headless_option.headless = True
        driver= webdriver.Chrome(executable_path="E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe", options=headless_option)
        base_url= "https://www.dotinternetbd.com/"
        driver.get(base_url)
        web_title=driver.title
        print("Opened Page Title IS : " + web_title)

test_obj=HeadlessAutomotion()
test_obj.test()
