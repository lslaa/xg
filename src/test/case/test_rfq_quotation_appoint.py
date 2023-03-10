import sys 
import time
import unittest
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.login.BuyerCenter.Inquiry_Upload_page import InquiryUploadpage
from src.test.page.login.SellerCenter.order_add_page import orderaddpage
from src.test.page.login.BuyerCenter.Inquiry_management_page import Inquirymanagementpage
from src.test.page.login.SellerCenter.quotation_management_page import quotationmanagementpage
from src.test.page.login.SellerCenter.buyer_center_page import BuyerCenterpage
from src.test.page.login.SellerCenter.seller_center_page import SellerCenterpage
import random

A=str(random.randint(1,100))
B=str(random.randint(1000,9999))
c=str(random.randint(1000,9999))
Specifications=''+A+'*'+B+'*'+c+''

class Testorder(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_Inquiry.xlsx'

    def sub_setUp(self):
        self.page = LoginPage().get(self.URL,open = True)

    def test_rfq_quotation_appoint(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user2'],d['password2'])
                time.sleep(2)

                self.page = InquiryUploadpage(self.page)
                self.page.Character_recognition(d['material'],Specifications,d['Place'],d['supplier'])

                self.page = Inquirymanagementpage(self.page)
                Inquiry_No_a = self.page.Inquirymanagement(d['Place'])

                self.page = orderaddpage(self.page)
                self.page.login_a(d['user'],d['password'])

                self.page = quotationmanagementpage(self.page)
                self.page.quotationmanagement(Inquiry_No_a,d['Warehouse'],d['PlaceofOrigin'],str(d['quantity']),str(d['Totalweight']),str(d['Price']))
                self.page.Modifyquotation(Inquiry_No_a,str(d['Price_a']))

                self.page = orderaddpage(self.page)
                self.page.login_a(d['user2'],d['password2'])
                
                self.page = Inquirymanagementpage(self.page)
                self.page.Inquirylistselection(Inquiry_No_a,str(d['quantity_a']))

                self.page = Inquirymanagementpage(self.page)
                self.page.Inquiry_completed()

                self.page = BuyerCenterpage(self.page)
                order_no = self.page.BuyerCenter_a(Specifications)
                time.sleep(1)

                self.page = orderaddpage(self.page)
                self.page.login_a(d['user'],d['password'])
                time.sleep(1)

                self.page = SellerCenterpage(self.page)
                Order_status = self.page.SellerCenter(order_no)
                time.sleep(1)

                if Order_status=='撤销':
                    print('询单报价流程完成')
                else:
                    print('订单状态错误')

    def sub_tearDown(self):
        self.page.quit()

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_rfq_quotation_appoint.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(Testorder('test_rfq_quotation_appoint'))