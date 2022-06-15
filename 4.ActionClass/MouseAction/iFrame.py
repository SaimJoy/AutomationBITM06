import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class iFrame():

    def test_iframe(self):
        base_url='https://the-internet.herokuapp.com/iframe'
        driver=webdriver.Chrome(executable_path="E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe")
        driver.get(base_url)
        time.sleep(5)

  #switch to frame
        driver.switch_to.frame('mce_0_ifr')
        time.sleep(3)

        input_field= driver.find_element(By.ID, "tinymce")
        input_field.click()
        input_field.clear()
        input_field.send_keys("Hello World")
        time.sleep(5)


test_obj=iFrame()
test_obj.test_iframe()