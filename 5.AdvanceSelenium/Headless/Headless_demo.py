from selenium import webdriver
from  selenium.webdriver.common.by import By

class Headless():

    def test_headless_chrome(self):
        options= webdriver.ChromeOptions()
        options.headless=True
        driver= webdriver.Chrome(executable_path="E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe",options=options)
        driver.get("https://www.dotinternetbd.com/")
        title= driver.title
        print("Launch In Chrome:" +title)



test=Headless()
test.test_headless_chrome()