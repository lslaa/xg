from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class Inquirymanagementpage(Page):
#询单发布操作
    Place_of_delivery =(By.XPATH,'//*[@id="input_box"]/div/div[1]/form/div[5]/div/div/div/input')
    query = (By.ID,'queryBtn')
    Inquiry_No_text = (By.XPATH,'//*[@id="listtableRef"]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span')
    modify = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[2]/span')
    sj = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[2]/div/div/div[2]/div[2]/form/div[4]/div[1]/div/div/div/label[2]/span[1]/span')
    preservation = (By.ID,'saveBtn')
    Inquiry_No_input = (By.XPATH,'//*[@id="input_box"]/div/div[1]/form/div[1]/div/div/div/input')
    release = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[1]/span')
    Unpublish = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a/span')
    determine_1 = (By.XPATH,'/html/body/div[2]/div/div[3]/button[2]/span')
    determine_2 = (By.XPATH,'/html/body/div[3]/div/div[3]/button[2]')

#询单选单操作
    Buyer_Center = (By.XPATH,'//*[@id="homeTop"]/div/div[2]/div[1]/span[1]')
    Inquiry_management = (By.XPATH,'//*[@id="menuFont"]/div/ul/li[2]/ul/li[3]')
    Inquiry_No_a = (By.XPATH,'//*[@id="input_box"]/div/div[1]/form/div[1]/div/div/div/input')
    query = (By.ID,'queryBtn')
    Inquiry_list_selection = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[1]/span')
    Number_of_selected_documents = (By.XPATH,'//*[@id="MenuTabListRef"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/div/div/div/input')
    Tick = (By.XPATH,'//*[@id="MenuTabListRef"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')
    Confirm_menu = (By.ID,'quedingxuandan')
    Inquiry_completed_click = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[1]/span')

#虚单转实单操作
    Transferred = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[2]/span')
    determine_a = (By.XPATH,'/html/body/div/div/div/section/div[2]/div/div/div[2]/div/div/div[4]/div[3]/div[2]/button[2]/span')
    quantity_click = (By.XPATH,'//*[@id="uploadTableRef"]/div[1]/div[3]/div/div/table/tbody/tr[1]/td[9]/div/span')
    quantity_input = (By.XPATH,'//*[@id="uploadTableRef"]/div[1]/div[3]/div/div/table/tbody/tr[1]/td[9]/div/div/div/div/input')
    weight = (By.XPATH,'//*[@id="uploadTableRef"]/div[1]/div[3]/div/div/table/tbody/tr[1]/td[11]/div/div/div[1]/div/input')
    quantity_click_a = (By.XPATH,'//*[@id="uploadTableRef"]/div[1]/div[3]/div/div/table/tbody/tr[2]/td[9]/div/span')
    quantity_input_a = (By.XPATH,'//*[@id="uploadTableRef"]/div[1]/div[3]/div/div/table/tbody/tr[2]/td[9]/div/div/div/div/input')
    weight_a = (By.XPATH,'//*[@id="uploadTableRef"]/div[1]/div[3]/div/div/table/tbody/tr[2]/td[11]/div/div/div[1]/div/input')


    def Inquirymanagement(self,si):
        '''询单发布'''
        self.find_element(*self.Place_of_delivery).send_keys(si)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        Inquiry_No =self.find_element(*self.Inquiry_No_text).text
        time.sleep(1)
        self.find_element(*self.modify).click()
        time.sleep(2)
        self.find_element(*self.sj).click()
        time.sleep(1)
        self.find_element(*self.preservation).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_No_input).send_keys(Inquiry_No)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.release).click()
        time.sleep(1)
        self.find_element(*self.Unpublish).click()
        time.sleep(1)
        self.find_element(*self.determine_1).click()
        time.sleep(1)
        self.find_element(*self.release).click()
        time.sleep(1)
        return Inquiry_No
        
    def Inquirylistselection(self,Inquiry_No,ni):
        '''询单选单'''
        self.find_element(*self.Buyer_Center).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_management).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_No_a).send_keys(Inquiry_No)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_list_selection).click()
        time.sleep(1)
        self.find_element(*self.Number_of_selected_documents).clear()
        self.find_element(*self.Number_of_selected_documents).send_keys(ni)
        time.sleep(1)
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.Confirm_menu).click()
        time.sleep(1)

    def Inquiry_completed(self,Inquiry_No):
        '''询单完成'''
        try:
            self.find_element(*self.Inquiry_completed_click).click()
            time.sleep(1)
            self.find_element(*self.determine_1).click()
        except:
            self.find_element(*self.Buyer_Center).click()
            time.sleep(1)
            self.find_element(*self.Inquiry_management).click()
            time.sleep(1)
            self.find_element(*self.Inquiry_No_a).send_keys(Inquiry_No)
            time.sleep(1)
            self.find_element(*self.query).click()
            time.sleep(1)
            self.find_element(*self.Inquiry_completed_click).click()
            time.sleep(1)
            try:
                self.find_element(*self.determine_1).click()
            except:
                self.find_element(*self.determine_2).click()

    def Inquirymanagement_a(self,si):
        '''询单发布'''
        self.find_element(*self.Place_of_delivery).send_keys(si)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        Inquiry_No =self.find_element(*self.Inquiry_No_text).text
        time.sleep(1)
        self.find_element(*self.release).click()
        time.sleep(1)
        return Inquiry_No


    def Inquiry_Unpublish(self,Inquiry_No):
        '''取消发布'''
        time.sleep(1)
        self.find_element(*self.Inquiry_No_a).send_keys(Inquiry_No)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.Unpublish).click()
        time.sleep(1)
        self.find_element(*self.determine_1).click()
        time.sleep(1)

    def Transferred_document(self,Inquiry_No):
        '''虚单转实单'''
        self.find_element(*self.Buyer_Center).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_management).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_No_a).send_keys(Inquiry_No)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.Transferred).click()
        time.sleep(2)
        # self.find_element(*self.quantity_click).click()
        # time.sleep(1)
        # self.find_element(*self.quantity_click).clear()
        # time.sleep(1)
        # self.find_element(*self.quantity_input).send_keys(qi)
        # time.sleep(1)
        # self.find_element(*self.weight).clear()
        # time.sleep(1)
        # self.find_element(*self.weight).send_keys(wi)
        # time.sleep(1)
        # self.find_element(*self.quantity_click_a).clear()
        # time.sleep(1)
        # self.find_element(*self.quantity_input_a).send_keys(qi)
        # time.sleep(1)
        # self.find_element(*self.weight_a).clear()
        # time.sleep(1)
        # self.find_element(*self.weight_a).send_keys(wi)
        # time.sleep(1)
        self.find_element(*self.determine_a).click()
        time.sleep(1)