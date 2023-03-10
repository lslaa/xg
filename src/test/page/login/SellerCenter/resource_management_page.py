from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class Resourcemanagementpage(Page):
    #资源修改、上架
    specifications_input_1 = (By.XPATH,'//*[@id="searBox"]/div/div[1]/form/div[3]/div/div/div/div/div[1]/input')
    specifications_input_2 = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/form/div[3]/div/div/div/div/div[1]/input')
    specifications_choice = (By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/div[1]/li')
    query = (By.ID,'queryBtn')
    modify = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[19]/div/div/div/a[1]/span')
    Price = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div[11]/div/div/div/div[1]/div/input')
    preservation = (By.XPATH,'//*[@id="introduceBox"]/div/div[3]/div[3]/button[1]')
    Tick = (By.XPATH,'//*[@id="multipleTable"]/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')
    Put_on_the_shelf = (By.ID,'upBtn')
    Confirm = (By.XPATH,'//*[@id="introduceBox"]/div/div[4]/div/div/div[3]/div/button[1]')

    #资源下架
    Seller_Center = (By.XPATH,'/html/body/div/div/div/div[1]/div/div[2]/div[2]/span[1]')
    Listing_resources = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[1]/div/div[2]/div/ul/li[1]/ul/li')
    Available = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/span[7]')
    tick = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')
    undercarriage = (By.ID,'downBtn')


    def Resourcemanagement(self,gg,pi):
        '''资源修改、上架'''
        time.sleep(2)
        try:
            self.find_element(*self.specifications_input_1).send_keys(gg)
        except:
            self.find_element(*self.specifications_input_2).send_keys(gg)
        time.sleep(2)
        self.find_element(*self.specifications_choice).click()
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.modify).click()
        time.sleep(1)
        self.find_element(*self.Price).click()
        self.find_element(*self.Price).click()
        self.find_element(*self.Price).click()
        time.sleep(1)
        self.find_element(*self.Price).send_keys(pi)
        time.sleep(1)
        self.find_element(*self.preservation).click()
        time.sleep(1)
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.Put_on_the_shelf).click()
        time.sleep(1)
        self.find_element(*self.Confirm).click()
        time.sleep(2)
    
    def Resourcemanagement_a(self,si,pi):
        '''资源修改、上架'''
        time.sleep(1)
        try:
            self.find_element(*self.specifications_input_1).send_keys(si)
        except:
            self.find_element(*self.specifications_input_2).send_keys(si)
        time.sleep(2)
        self.find_element(*self.specifications_choice).click()
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.modify).click()
        time.sleep(1)
        self.find_element(*self.Price).click()
        self.find_element(*self.Price).click()
        self.find_element(*self.Price).click()
        time.sleep(1)
        self.find_element(*self.Price).send_keys(pi)
        time.sleep(1)
        self.find_element(*self.preservation).click()
        time.sleep(1)
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.Put_on_the_shelf).click()
        time.sleep(1)
        self.find_element(*self.Confirm).click()
        time.sleep(2)
    
    def Resourcemanagement_b(self,si):
        '''资源上架'''
        time.sleep(1)
        try:
            self.find_element(*self.specifications_input_1).send_keys(si)
        except:
            self.find_element(*self.specifications_input_2).send_keys(si)
        time.sleep(2)
        self.find_element(*self.specifications_choice).click()
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.Put_on_the_shelf).click()
        time.sleep(1)
        self.find_element(*self.Confirm).click()
        time.sleep(2)
    
    def Resources_off_the_shelf(self,si):
        '''资源下架'''
        self.find_element(*self.Seller_Center).click()
        time.sleep(1)
        self.find_element(*self.Listing_resources).click()
        time.sleep(1)
        self.find_element(*self.Available).click()
        time.sleep(1)
        try:
            self.find_element(*self.specifications_input_1).send_keys(si)
        except:
            self.find_element(*self.specifications_input_2).send_keys(si)
        time.sleep(2)
        self.find_element(*self.specifications_choice).click()
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.tick).click()
        time.sleep(1)
        self.find_element(*self.undercarriage).click()
        

