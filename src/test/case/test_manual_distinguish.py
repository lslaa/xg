import sys 
import time
import unittest
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.login.SellerCenter.resource_upload_page import Resourceuploadpage
from src.test.page.login.SellerCenter.resource_management_page import Resourcemanagementpage
from src.test.page.login.SellerCenter.order_add_page import orderaddpage
from src.test.page.login.SellerCenter.buyer_center_page import BuyerCenterpage
from src.test.page.login.SellerCenter.seller_center_page import SellerCenterpage


class Testorder(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_order.xlsx'

    def sub_setUp(self):
        self.page = LoginPage().get(self.URL,open = True)

    def test_manual_add(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])
                time.sleep(2)

                self.page = Resourceuploadpage(self.page)
                self.page.Manualresourceupload(d['varieties'],d['PlaceofOrigin'],d['Brand'],d['specification'],str(d['length']),str(d['quantity']),str(d['Totalweight']),d['Warehouse'],str(d['Price']),d['technicalstandard'])
                time.sleep(1)

                self.page = Resourcemanagementpage(self.page)
                self.page.Resourcemanagement_a(d['specification'],str(d['price_a']))
                time.sleep(1)

                self.page = orderaddpage(self.page)
                self.page.login_a(d['user2'],d['password2'])
                time.sleep(1)
                order_no=self.page.orderadd_a(d['specification'])
                time.sleep(1)

                self.page = BuyerCenterpage(self.page)
                self.page.BuyerCenter(order_no)
                time.sleep(1)

                self.page = orderaddpage(self.page)
                self.page.login_a(d['user'],d['password'])
                time.sleep(1)
                
                self.page = SellerCenterpage(self.page)
                Order_status = self.page.SellerCenter(order_no)
                time.sleep(1)
                if Order_status=='撤销':
                    print('订单流程完成')
                else:
                    print('单据状态错误')
        
    def sub_tearDown(self):
        self.page.quit()

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_manual_add.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(Testorder('test_manual_add'))