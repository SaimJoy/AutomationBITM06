import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragDrop():

    def test_dragdrop(self):
        driver = webdriver.Chrome(executable_path="E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe")
        driver.maximize_window()
        base_url = "https://jqueryui.com/droppable/"
        driver.get(base_url)

        driver.switch_to.frame(0)
        from_element = driver.find_element(By.ID, "draggable")
        to_element = driver.find_element(By.ID, "droppable")
        time.sleep(5)

        try:
             action = ActionChains(driver)
             action.drag_and_drop(from_element, to_element).perform()
             time.sleep(2)
        except:
             print("Drag Drop Failed")


test = DragDrop()
test.test_dragdrop()
