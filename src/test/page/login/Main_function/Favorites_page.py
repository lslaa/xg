from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time
import sys 

class Favoritespage(Page):
    #收藏夹查询操作
    Favorites_click = (By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div[3]/span[1]')
    query_input = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[2]/div/input')
    query_click = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[2]/div/span/span/i')
    specifications_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[7]/div/div')

    #收藏夹删除物资
    delete = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[11]/div/div/div/a/span')
    define = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[3]/div/div[2]/div[2]/button[1]/span')
    point_out_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div/div[3]/div/span')

    #清除下架资源
    clean_up = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/button[2]/span')
    define = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[3]/div/div[2]/div[2]/button[1]/span')

    #清空收藏夹资源
    Select_All = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[3]/div[1]/label/span')

    def Favorites_query(self,qi):
        '''收藏夹查询数据'''
        self.find_element(*self.Favorites_click).click()
        time.sleep(1)
        self.find_element(*self.query_input).send_keys(qi)
        time.sleep(1)
        self.find_element(*self.query_click).click()
        time.sleep(1)
        Favorites_specifications = self.find_element(*self.specifications_text).text
        return Favorites_specifications
    
    def Favorites_delete(self):
        '''收藏夹删除数据'''
        self.find_element(*self.delete).click()
        time.sleep(1)
        self.find_element(*self.define).click()
        time.sleep(1)
        point_out = self.find_element(*self.point_out_text).text
        if point_out=='暂无数据':
            print('删除数据成功')
        else:
            print('删除数据失败')
    
    def Clear_Off_shelf_Resources(self,qi):
        '''收藏夹清除下架资源'''
        self.find_element(*self.Favorites_click).click()
        time.sleep(1)
        self.find_element(*self.query_input).send_keys(qi)
        time.sleep(1)
        self.find_element(*self.query_click).click()
        time.sleep(1)
        self.find_element(*self.clean_up).click()
        time.sleep(1)
        self.find_element(*self.define).click()
        time.sleep(1)
        point_out = self.find_element(*self.point_out_text).text
        if point_out=='暂无数据':
            print('清除已下架数据成功')
        else:
            print('清除已下架数据失败')

    def empty_Favorites(self):
        '''清空收藏夹'''
        self.find_element(*self.Favorites_click).click()
        time.sleep(1)
        point_out = self.find_element(*self.point_out_text).text
        if point_out!='暂无数据':
            self.find_element(*self.Select_All).click()
            time.sleep(1)
            self.find_element(*self.delete).click()
            time.sleep(1)
            self.find_element(*self.define).click()
            time.sleep(1)
        else:
            pass
