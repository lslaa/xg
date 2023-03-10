from src.test.common.browser import Browser
from selenium.common.exceptions import NoSuchElementException
import time


class Page(Browser):
    # 更多的封装请自己动手...
    def __init__(self, page=None, browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def find_element(self, *args):
        try:
            self.driver.find_element(*args)
        except NoSuchElementException as e:
            self.save_screen_shot("find_element")
            print("元素不存在%s" %(args,))
        else:
            return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)