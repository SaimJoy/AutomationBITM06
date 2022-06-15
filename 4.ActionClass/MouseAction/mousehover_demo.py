import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MouseHovering():

    def test_mouseHover(self):
        driver = webdriver.Chrome(executable_path="E:\AutomationBITM06\Drivers\Drivers\chromedriver_102.0.exe")
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        login_btn = driver.find_element(By.ID, "btnLogin")

        username.clear()
        username.send_keys("Admin")
        password.clear()
        password.send_keys("admin123")
        login_btn.click()

        try:
            recruitment=driver.find_element(By.XPATH, '//*[@id="menu_recruitment_viewRecruitmentModule"]/b')
            actions=ActionChains(driver)
            actions.move_to_element(recruitment).perform()
            time.sleep(3)

            candidates=driver.find_element(By.ID,"menu_recruitment_viewCandidates")
            candidates.click()
        except:
            print("Hover failed")

test= MouseHovering()
test.test_mouseHover()