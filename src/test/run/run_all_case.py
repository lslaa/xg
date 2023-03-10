import unittest
import os
import sys 
from HTMLTestRunner import HTMLTestRunner
import time
sys.path.append("./")
from src.utils.config import Config, CASE_PATH,REPORT_PATH
from src.utils.mail import Email

def new_report(REPORT_PATH):#获取‘最新’测试报告
    lists = os.listdir(REPORT_PATH)
    lists.sort(key=lambda fn:os.path.getmtime(REPORT_PATH +'\\'+fn))#把所有测试报告按时间排序
    file_new = os.path.join(REPORT_PATH,lists[-1])#取最后一份
    print(file_new)
    return file_new

def all_case():#定义所有测试用例
    discover = unittest.defaultTestLoader.discover(CASE_PATH,#测试路径
                                                    pattern="test_*.py",#执行‘m_’开头的用例
                                                    top_level_dir=None)

    print(discover)
    return discover

if __name__ == "__main__":
    new_report(REPORT_PATH)
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report = REPORT_PATH+'\\'+now+'report.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='自动化测试报告', description='用例执行情况:')
        runner.run(all_case())
        f.close()
    # e = Email(title='三一自动化测试报告',
    #         message='这是今天的测试报告，请查收！',
    #         receiver='823263175@qq.com',
    #         server='smtp.qq.com',
    #         sender='823263175@qq.com',
    #         password='talbfdnnfllbbgac',
    #         path=new_report(REPORT_PATH)
    #         )
    # e.send()