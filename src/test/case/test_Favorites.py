import sys 
import time
import unittest
from selenium import webdriver
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.login.Main_function.Product_search_page import Productsearchpage
from src.test.page.login.SellerCenter.resource_upload_page import Resourceuploadpage
from src.test.page.login.SellerCenter.resource_management_page import Resourcemanagementpage
from src.test.page.login.SellerCenter.order_add_page import orderaddpage
from src.test.page.login.Main_function.Favorites_page import Favoritespage
import random

A=str(random.randint(1,100))
B=str(random.randint(1000,9999))
c=str(random.randint(1000,9999))
Specifications=''+A+'*'+B+'*'+c+''

class Testorder(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_Shopping_Cart.xlsx'

    def sub_setUp(self):
        self.page = LoginPage().get(self.URL,open = True)

    def test_Favorites(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])
                time.sleep(2)

                #资源上传
                self.page = Resourceuploadpage(self.page)
                self.page.Resourceupload(d['material'],Specifications)
                self.page.Manualresourceupload(d['varieties'],d['PlaceofOrigin'],d['Brand'],d['specification'],str(d['length']),str(d['quantity']),str(d['Totalweight']),d['Warehouse'],str(d['Price']),d['technicalstandard'])
                time.sleep(1)

                #资源上架
                self.page = Resourcemanagementpage(self.page)
                self.page.Resourcemanagement_b(Specifications)
                self.page.Resourcemanagement_b(d['specification'])

                #清空收藏夹
                try:
                    self.page = Favoritespage(self.page)
                    self.page.empty_Favorites()
                except:
                    pass
                #加入收藏夹测试
                self.page = Productsearchpage(self.page)
                self.page.Add_Favorites(Specifications)
                self.page.Add_Favorites(d['specification'])

                #收藏夹搜索测试
                self.page = Favoritespage(self.page)
                Specifications_a=self.page.Favorites_query(Specifications)
                if Specifications_a==Specifications:
                    print('收藏夹查询数据正确')
                else:
                    print('收藏夹查询数据失败')
                
                #收藏夹删除物资测试
                self.page.Favorites_delete()

                #收藏夹清除下架资源
                self.page = Resourcemanagementpage(self.page)
                self.page.Resources_off_the_shelf(d['specification'])

                self.page = Favoritespage(self.page)
                self.page.Clear_Off_shelf_Resources(d['specification'])

    def sub_tearDown(self):
        self.page.quit()

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_Favorites.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(Testorder('test_Favorites'))