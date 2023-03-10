from selenium.webdriver.common.by import By
from src.test.common.page import Page
from src.test.page.login.Main_function.Product_search_page import Productsearchpage
import time

class ShoppingCartpage(Page):
    #清空购物车操作
    shopping_cart = (By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/span')
    empty = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[2]/a/span')
    determine = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[3]/div/div[2]/div[2]/button[1]')
    Tips_text = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div/div/div[2]/p')

    #删除选择商品
    Tick = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[2]/div[1]/label/span[1]/span')
    delete = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[3]/div/button[2]')
    define = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[3]/div/div[2]/div[2]/button[1]')

    #一键下单
    One_click_order_button = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[2]/div[3]/div/button[1]')
    specifications_text = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div')
    weight_text = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[9]/div/div/span[2]')
    unit_price_text = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[10]/div/div/div/span')
    amount_of_money_text = (By.XPATH,'/html/body/div/div/div/section/div[2]/div[2]/div[1]/div[3]/div/div[3]/table/tbody/tr/td[11]/div/div/div/span')

    #删除失效商品
    Delete_invalid_push_button = (By.XPATH,'/html/body/div[1]/div/div/section/div[2]/div[2]/div[1]/div[2]/div/a/span')

    def empty_Shopping_Cart(self):
        '''清空购物车'''
        self.find_element(*self.shopping_cart).click()
        time.sleep(1)
        self.find_element(*self.empty).click()
        time.sleep(1)
        self.find_element(*self.determine).click()
        time.sleep(1)
        Tips = self.find_element(*self.Tips_text).text
        if Tips=='还没有添加资源奥,快去选购吧^~^':
            print('购物车清空成功')
        else:
            print('购物车清空失败')

    def Delete_material(self):
        '''删除购物车物资'''
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.delete).click()
        time.sleep(1)
        self.find_element(*self.define).click()
        time.sleep(1)
        Tips = self.find_element(*self.Tips_text).text
        if Tips=='还没有添加资源奥,快去选购吧^~^':
            print('删除所选物资成功')
        else:
            print('删除所选物资失败')

    def One_click_order(self):
        '''一键下单'''
        self.find_element(*self.Tick).click()
        time.sleep(1)
        self.find_element(*self.One_click_order_button).click()
        time.sleep(1)
        specifications = self.find_element(*self.specifications_text).text
        weight = self.find_element(*self.weight_text).text
        unit_price = self.find_element(*self.unit_price_text).text
        amount_of_money = self.find_element(*self.amount_of_money_text).text
        
    def Delete_invalid(self):
        '''删除失效商品'''
        self.find_element(*self.shopping_cart).click()
        time.sleep(1)
        self.find_element(*self.Delete_invalid_push_button).click()
        time.sleep(1)
        Tips = self.find_element(*self.Tips_text).text
        if Tips=='还没有添加资源奥,快去选购吧^~^':
            print('删除失效物资成功')
        else:
            print('删除失效物资失败')
