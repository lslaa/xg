import sys 
import time
import unittest
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.login.BuyerCenter.Inquiry_Upload_page import InquiryUploadpage
from src.test.page.login.BuyerCenter.Inquiry_management_page import Inquirymanagementpage
from src.test.page.login.Main_function.Inquiry_zone_page import Inquiryzonepage
from src.test.page.login.SellerCenter.order_add_page import orderaddpage
from src.test.page.login.SellerCenter.quotation_management_page import quotationmanagementpage
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

    def test_Inquiry_zone(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])
                time.sleep(2)

                #询单专区前置条件创建实单
                self.page = InquiryUploadpage(self.page)
                self.page.Character_recognition(d['material'],Specifications,d['Place'])

                #发布
                self.page = Inquirymanagementpage(self.page)
                Inquiry_No=self.page.Inquirymanagement_a(d['Place'])

                #询单专区前置条件创建虚单
                self.page = InquiryUploadpage(self.page)
                self.page.Character_recognition_a(d['material'],Specifications,d['Place'])

                #发布
                self.page = Inquirymanagementpage(self.page)
                Inquiry_No_a=self.page.Inquirymanagement_a(d['Place'])

                #询单专区发布公司、询单类型查询
                self.page = Inquiryzonepage(self.page)
                self.page.Inquiry_zone(d['supplier'])

                #询单报价
                self.page = orderaddpage(self.page)
                self.page.login_a(d['user2'],d['password'])

                self.page = quotationmanagementpage(self.page)
                self.page.quotationmanagement(Inquiry_No,d['Warehouse'],d['PlaceofOrigin'],str(d['quantity']),str(d['Totalweight']),str(d['Price']))

                #询单选单
                self.page = orderaddpage(self.page)
                self.page.login_a(d['user'],d['password'])
                
                self.page = Inquirymanagementpage(self.page)
                self.page.Inquirylistselection(Inquiry_No,str(d['quantity_a']))

                #选单中阶段查询
                self.page = Inquiryzonepage(self.page)
                self.page.In_the_menu_query()

                #询单完成
                self.page = Inquirymanagementpage(self.page)
                self.page.Inquiry_completed(Inquiry_No)

                #已完成阶段查询
                self.page = Inquiryzonepage(self.page)
                self.page.Completed_query()

                #虚单报价
                self.page = orderaddpage(self.page)
                self.page.login_a(d['user2'],d['password'])

                self.page = quotationmanagementpage(self.page)
                self.page.quotationmanagement_a(Inquiry_No_a,d['PlaceofOrigin'],str(d['Price']))

                #虚转实
                self.page = Inquirymanagementpage(self.page)
                self.page.Transferred_document(Inquiry_No_a)

                #取消发布
                self.page = Inquirymanagementpage(self.page)
                self.page.Inquiry_Unpublish(Inquiry_No_a)

                #已结束查询
                self.page = Inquiryzonepage(self.page)
                self.page.Closed_query()
                
                #查看详情
                self.page = Inquiryzonepage(self.page)
                self.page.detailed_information()
    def sub_tearDown(self):
        self.page.quit()

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_Inquiry_zone.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(Testorder('test_Inquiry_zone'))