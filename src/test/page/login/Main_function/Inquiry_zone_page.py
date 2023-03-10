from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class Inquiryzonepage(Page):
    home_page = (By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/img')
    Inquiry_zone_page = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[1]/div/div[4]/a')
    Publishing_company_input = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/input')
    Publishing_company_click_1 = (By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/div[1]/li[2]')
    Publishing_company_click_2 = (By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/div[1]/li[2]')
    click_a = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[3]/div/div[2]/table/thead/tr/th[5]/div')
    Publishing_company_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/div/div')
    Real_bill = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/div/div[1]/div[1]')
    False_bill = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]')
    Inquiry_type_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/div')
    In_inquiry = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[4]/div/div[3]/div/div[1]/div[1]')
    Inquiry_stage_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/div/div/div')
    In_the_menu = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[4]/div/div[3]/div/div[1]/div[2]')
    Completed = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[4]/div/div[3]/div/div[1]/div[3]')
    Closed = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[4]/div/div[3]/div/div[1]/div[4]')
    detailed_information_click = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[9]/div/div/div/div/a/span')
    detailed_information_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]/span')

    def Inquiry_zone(self,pi):
        '''询单专区供应商、询单类型测试'''
        self.find_element(*self.home_page).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_zone_page).click()
        time.sleep(1)
        self.find_element(*self.Publishing_company_input).send_keys(pi)
        time.sleep(2)
        try:
            self.find_element(*self.Publishing_company_click_1).click()
        except:
            self.find_element(*self.Publishing_company_click_2).click()
        time.sleep(1)
        self.find_element(*self.click_a).click()
        time.sleep(1)
        Publishing_company = self.find_element(*self.Publishing_company_text).text
        if Publishing_company=='点鑫广告（上海）有限公司':
            print('询单发布公司查询数据正确')
        else:
            print('询单发布公司查询数据错误')

        self.find_element(*self.Real_bill).click()
        time.sleep(1)
        Inquiry_type=self.find_element(*self.Inquiry_type_text).text
        if Inquiry_type=='实单':
            print('实单查询数据正确')
        else:
            print('实单查询数据错误')

        self.find_element(*self.False_bill).click()
        time.sleep(1)
        Inquiry_type_a=self.find_element(*self.Inquiry_type_text).text
        if Inquiry_type_a=='虚单':
            print('虚单查询数据正确')
        else:
            print('虚单查询数据错误')

        self.find_element(*self.In_inquiry).click()
        time.sleep(1)
        Inquiry_stage = self.find_element(*self.Inquiry_stage_text).text
        if Inquiry_stage=='询价中':
            print('询价中阶段查询数据正确')
        else:
            print('询价中阶段查询数据错误')

    def In_the_menu_query(self):
        '''选单中查询'''
        time.sleep(1)
        self.find_element(*self.home_page).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_zone_page).click()
        time.sleep(1)
        self.find_element(*self.In_the_menu).click()
        Inquiry_stage_a = self.find_element(*self.Inquiry_stage_text).text
        if Inquiry_stage_a=='选单中':
            print('选单中阶段查询数据正确')
        else:
            print('选单中阶段查询数据错误')
    
    def Completed_query(self):
        '''已完成查询'''
        time.sleep(1)
        self.find_element(*self.home_page).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_zone_page).click()
        time.sleep(1)
        self.find_element(*self.Completed).click()
        Inquiry_stage_b = self.find_element(*self.Inquiry_stage_text).text
        if Inquiry_stage_b=='已完成':
            print('已完成阶段查询数据正确')
        else:
            print('已完成阶段查询数据错误')

    def Closed_query(self):
        '''已结束查询'''
        time.sleep(1)
        self.find_element(*self.home_page).click()
        time.sleep(1)
        self.find_element(*self.Inquiry_zone_page).click()
        time.sleep(1)
        self.find_element(*self.Closed).click()
        Inquiry_stage_c = self.find_element(*self.Inquiry_stage_text).text
        if Inquiry_stage_c=='已结束':
            print('已结束阶段查询数据正确')
        else:
            print('已结束阶段查询数据错误')

    def detailed_information(self):
        '''查看详情'''
        self.find_element(*self.detailed_information_click).click()
        time.sleep(1)
        detailed_information = self.find_element(*self.detailed_information_text).text
        if detailed_information=='询单详情页':
            print('查看详情页跳转成功')
        else:
            print('查看详情页跳转失败')