from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time


class LoginPage(Page):
    yh=(By.ID,'tab-accountLogin')
    user_input = (By.XPATH, '//*[@id="pane-accountLogin"]/form/div[1]/div/div/input')
    password_input = (By.XPATH,'//*[@id="pane-accountLogin"]/form/div[2]/div/div/input')
    login_button = (By.XPATH, '//*[@id="pane-accountLogin"]/form/div[3]/div/button')

    def login(self, ui ,pi):
        """登录"""
        time.sleep(3)
        self.find_element(*self.yh).click()
        self.find_element(*self.user_input).send_keys(ui)      
        self.find_element(*self.password_input).send_keys(pi)
        self.find_element(*self.login_button).click()
        time.sleep(2)
        self.move()
