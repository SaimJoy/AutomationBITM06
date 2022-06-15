from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Screenshot():

    def test_screenshot(self,url,file_name):
        driver = webdriver.Chrome(executable_path="/Drivers/Drivers/chromedriver_102.0.exe")
        base_url=url


        #file_name= ""
        file_extension= ".png"
        file_destination_path= "E:\AutomationBITM06\Screenshot\ "

        driver.get(base_url)

        try:
          driver.save_screenshot(file_destination_path+file_name+file_extension)
          print("Screenshot save to Directory "  +file_destination_path)
        except:
            print("ScreentShot Capture failed")

test=Screenshot()
test.test_screenshot('https://jqueryui.com/droppable/#default','newSS')