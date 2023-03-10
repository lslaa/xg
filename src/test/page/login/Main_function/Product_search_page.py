from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class Productsearchpage(Page):
    #搜索操作
    Search_bar_input = (By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/input')
    query = (By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/span')
    Specifications_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div')
    buy_now = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/div/div[3]/table/tbody/tr[1]/td[13]/div/div/div/button[1]')
    Support_weight_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/div/div[3]/table/tbody/tr[1]/td[9]/div/div/div/div/div[2]/div[2]')
    Unit_Price_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/div/div[3]/table/tbody/tr[1]/td[10]/div/div/div/div/div/span[2]')
    Specifications_text_a = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/div')
    Support_weight_text_a = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[11]/div/div/div/div/span')
    Unit_Price_text_a = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[12]/div/div/div/span')
    Total_amount_text = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[13]/div/div/div/span')

    #一键下单
    Tick = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[3]/div[1]/label/span[1]/span')
    One_click_order_button = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[3]/div/button[1]')
    specifications_text_b = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div')
    weight_text_b = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[9]/div/div/span[2]')
    unit_price_text_b = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[10]/div/div/div/span')
    amount_of_money_text = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[11]/div/div/div/span')
    
    #加入收藏夹
    breed = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[4]/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div[1]')
    collect = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div/div[3]/div[2]/div[9]/div[2]')
    point_out = (By.XPATH,'/html/body/div[3]/div')

    def Product_search(self,si):
        '''搜索栏搜索'''
        self.find_element(*self.Search_bar_input).send_keys(si)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        global Specifications
        Specifications = self.find_element(*self.Specifications_text).text
        return Specifications
    
    def Buy_Now(self):
        '''立即购买'''
        Support_weight = self.find_element(*self.Support_weight_text).text
        Unit_Price = self.find_element(*self.Unit_Price_text).text
        self.find_element(*self.buy_now).click()
        time.sleep(1)
        global Specifications_a
        Specifications_a = self.find_element(*self.Specifications_text_a).text
        global Support_weight_a
        Support_weight_a = self.find_element(*self.Support_weight_text_a).text
        global Unit_Price_a
        Unit_Price_a = self.find_element(*self.Unit_Price_text_a).text
        global Total_amount
        Total_amount = self.find_element(*self.Total_amount_text).text
        if Specifications==Specifications_a:
            if Support_weight == Support_weight_a[:-1]:
                if Unit_Price==Unit_Price_a:
                    if Total_amount[1:]==round(Unit_Price_a*Specifications_a,2):
                        print('加入购物车资源信息正确')
        else:
            print('加入购物车资源信息错误')

    def One_click_order(self):
        '''一键下单'''
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.One_click_order_button).click()
        time.sleep(1)
        specifications_b = self.find_element(*self.specifications_text_b).text
        weight = self.find_element(*self.weight_text_b).text
        unit_price_b = self.find_element(*self.unit_price_text_b).text
        amount_of_money = self.find_element(*self.amount_of_money_text).text
        if specifications_b == Specifications_a:
            if weight==Support_weight_a:
                if unit_price_b==Unit_Price_a:
                    if amount_of_money==Total_amount:
                        print('下单信息正确')
        else:
            print('下单信息错误')

    def Add_Favorites(self,si):
        '''添加收藏夹'''
        self.find_element(*self.Search_bar_input).clear()
        time.sleep(1)
        self.find_element(*self.Search_bar_input).send_keys(si)
        time.sleep(1)
        self.find_element(*self.query).click()
        time.sleep(1)
        self.find_element(*self.breed).click()
        time.sleep(1)
        self.find_element(*self.collect).click()
        point_out=self.find_element(*self.point_out).text
        if point_out=='收藏成功':
            print('收藏物资成功')
        else:
            print('收藏物资失败')
        time.sleep(1)