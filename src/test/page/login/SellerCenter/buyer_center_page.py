from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class BuyerCenterpage(Page):
    Buyer_Center = (By.XPATH,'//*[@id="homeTop"]/div/div[2]/div[1]/span[1]')
    order_page = (By.XPATH,'//*[@id="menuFont"]/div/ul/li[1]/div/span')
    order_no_input = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/input')
    query = (By.ID,'getBtn')
    Application_for_cancellation = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div[4]/div[2]/table/tbody/tr/td[8]/div/div/div/a/span')
    reason_input = (By.XPATH,'//*[@id="dialog"]/div/div[2]/div/form/div[2]/div/div/textarea')
    yes = (By.XPATH,'//*[@id="dialog"]/div/div[2]/div/div[2]/button[1]')

    Specification_input = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/form/div[5]/div/div/div/div/div/input')
    order_no_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div[3]/table/tbody/tr/td[1]/div/div/a/span')

    def BuyerCenter(self,order_no):
        '''买家申请撤销'''
        self.find_element(*self.Buyer_Center).click()
        time.sleep(1)
        self.find_element(*self.order_page).click()
        time.sleep(1)
        self.find_element(*self.order_no_input).send_keys(order_no)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.Application_for_cancellation).click()
        time.sleep(1)
        self.find_element(*self.reason_input).send_keys('不想要了')
        time.sleep(1)
        self.find_element(*self.yes).click()
        time.sleep(1)

    def BuyerCenter_a(self,si):
        '''询单报价订单撤销'''
        time.sleep(5)
        self.find_element(*self.Buyer_Center).click()
        time.sleep(1)
        self.find_element(*self.order_page).click()
        time.sleep(1)
        self.find_element(*self.Specification_input).send_keys(si)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        order_no = self.find_element(*self.order_no_text).text
        time.sleep(1)
        self.find_element(*self.Application_for_cancellation).click()
        time.sleep(1)
        self.find_element(*self.reason_input).send_keys('不想要了')
        time.sleep(1)
        self.find_element(*self.yes).click()
        time.sleep(1)
        return order_no