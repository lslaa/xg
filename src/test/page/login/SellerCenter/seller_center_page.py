from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SellerCenterpage(Page):
    Seller_Center = (By.XPATH,'//*[@id="homeTop"]/div/div[2]/div[2]/span[1]')
    Sales_order = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[1]/div/div[2]/div/ul/li[2]/ul/li[1]')
    order_no_input = (By.XPATH,'//*[@id="inputboxoneRef"]/div/div[1]/form/div[1]/div/div/div/input')
    query = (By.ID,'queryBtn')
    Cancel_confirmation = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div/div[4]/div[2]/table/tbody/tr/td[9]/div/div/div/a/span')
    reason_input = (By.XPATH,'//*[@id="repealRef"]/div/div[2]/div/form/div/div/div/textarea')
    yes = (By.XPATH,'//*[@id="repealRef"]/div/div[2]/div/div/button[1]/span')
    Order_status_text = (By.XPATH,'//*[@id="tableBox"]/div/div[3]/table/tbody/tr/td[6]/div/div/div/span')

    def SellerCenter(self,order_no):
        self.find_element(*self.Seller_Center).click()
        time.sleep(1)
        self.find_element(*self.Sales_order).click()
        time.sleep(1)
        self.find_element(*self.order_no_input).send_keys(order_no)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.Cancel_confirmation).click()
        time.sleep(1)
        self.find_element(*self.reason_input).send_keys('不要就不要')
        time.sleep(1)
        self.find_element(*self.yes).click()
        time.sleep(1)
        order_state = self.find_element(*self.Order_status_text).text
        return order_state