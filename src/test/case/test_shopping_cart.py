import sys 
import time
import unittest
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.login.Main_function.Product_search_page import Productsearchpage
from src.test.page.login.SellerCenter.resource_upload_page import Resourceuploadpage
from src.test.page.login.SellerCenter.resource_management_page import Resourcemanagementpage
from src.test.page.login.Main_function.Shopping_Cart_page import ShoppingCartpage
from src.test.page.login.SellerCenter.order_add_page import orderaddpage
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

    def test_Shopping_Cart(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])
                time.sleep(2)

                #资源上传
                self.page = Resourceuploadpage(self.page)
                self.page.Resourceupload(d['material'],Specifications)

                #资源上架
                self.page = Resourcemanagementpage(self.page)
                self.page.Resourcemanagement_b(Specifications)
                
                self.page = orderaddpage(self.page)
                self.page.login_a(d['user2'],d['password'])

                #清空购物车测试
                self.page = ShoppingCartpage(self.page)
                self.page.empty_Shopping_Cart()

                #搜索栏搜索测试
                self.page = Productsearchpage(self.page)
                Specifications_a=self.page.Product_search(Specifications)
                if Specifications_a==Specifications:
                    print('现货资源查询成功')
                else:
                    print('现货资源查询失败')

                #立即购买以及加入购物车资源数据测试
                self.page = Productsearchpage(self.page)
                self.page.Buy_Now()

                #删除购物车中所选物资测试
                self.page = ShoppingCartpage(self.page)
                self.page.Delete_material()

                #下单数据测试
                self.page = Productsearchpage(self.page)
                Specifications_a=self.page.Product_search(Specifications)
                self.page = Productsearchpage(self.page)
                self.page.Buy_Now()
                self.page.One_click_order()

                #删除失效物资
                self.page = Resourcemanagementpage(self.page)
                self.page.Resources_off_the_shelf(Specifications)
                self.page = ShoppingCartpage(self.page)
                self.page.Delete_invalid()

      

    def sub_tearDown(self):
        self.page.quit()

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_Shopping_Cart.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(Testorder('test_Shopping_Cart'))