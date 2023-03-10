from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class orderaddpage(Page):
    company = (By.XPATH,'/html/body/div/div/div/div[1]/div/div[1]/div/div[1]')
    Log_out = (By.XPATH,'/html/body/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]')
    Sign_in = (By.XPATH,'//*[@id="homeTop"]/div/div[1]/span[1]')
    yh=(By.ID,'tab-accountLogin')
    user_input = (By.XPATH, '//*[@id="pane-accountLogin"]/form/div[1]/div/div/input')
    password_input = (By.XPATH,'//*[@id="pane-accountLogin"]/form/div[2]/div/div/input')
    login_button = (By.XPATH, '//*[@id="pane-accountLogin"]/form/div[3]/div/button')

    search = (By.ID,'btnSear')
    Specification_input = (By.ID,'searchInput')
    Buy_Now = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/div/div[3]/table/tbody/tr/td[13]/div/div/div/button[1]/span')
    Tick = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div/div/div/div/img')
    One_click_order = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/button/span')
    Generate_order = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[3]/button/span')
    order_no_text = (By.XPATH,'//*[@id="__layout"]/div/section/div[2]/div[2]/div/div[1]/div[1]/div[1]/span[2]')

    def login_a(self, ui ,pi):
        """登录"""
        self.find_element(*self.company).click()
        time.sleep(2)
        self.find_element(*self.Log_out).click()
        time.sleep(2)
        self.find_element(*self.Sign_in).click()
        time.sleep(3)
        self.find_element(*self.yh).click()
        self.find_element(*self.user_input).send_keys(ui)
        self.find_element(*self.password_input).send_keys(pi)
        self.find_element(*self.login_button).click()
        time.sleep(2)
        self.move()
        
    def orderadd(self,si):
        '''生成订单'''
        time.sleep(3)
        self.find_element(*self.Specification_input).send_keys(si)
        time.sleep(1)
        self.find_element(*self.search).click()
        time.sleep(1)
        self.find_element(*self.Buy_Now).click()
        time.sleep(1)
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.One_click_order).click()
        time.sleep(1)
        self.find_element(*self.Generate_order).click()
        time.sleep(1)
        order_no=self.find_element(*self.order_no_text).text
        time.sleep(2)
        return order_no

    def orderadd_a(self,si):
        '''生成订单'''
        time.sleep(3)
        self.find_element(*self.Specification_input).send_keys(si)
        time.sleep(1)
        self.find_element(*self.search).click()
        time.sleep(1)
        self.find_element(*self.Buy_Now).click()
        time.sleep(1)
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.One_click_order).click()
        time.sleep(1)
        self.find_element(*self.Generate_order).click()
        time.sleep(1)
        order_no = self.find_element(*self.order_no_text).text
        time.sleep(2)
        return order_no