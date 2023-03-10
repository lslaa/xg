import time
import os
from selenium import webdriver
from src.utils.config import DRIVER_PATH, REPORT_PATH, UPLOAD_PICTURE_PATH
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import time
import cv2
import numpy as np
import requests


# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=15, open = False):
        if open == True:
            self.Binary = FirefoxBinary('D:\\Firefox\\firefox.exe')
            self.driver = webdriver.Firefox(firefox_binary=self.Binary)
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def delete_screen_shot(self):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        
        lists = os.listdir(screenshot_path)
        lists.sort(key=lambda fn:os.path.getmtime(screenshot_path +'\\'+fn))
        file_new = os.path.join(screenshot_path,lists[-1])
        os.remove(file_new)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def isElementExistence(self, *args):
        try:
            self.driver.find_element(*args)
            return True
        except:
            return False

    # 该方法会实现自动上传一张默认图片，但是存放exe文件的路径必须是：当前运行脚本的同目录..\external\upload_picture.exe
    # 因为上传图片无法通过selenium+python直接做到，需要用到录制的exe文件
    def upload_picture(self,Xpath = UPLOAD_PICTURE_PATH):
        os.system(Xpath)

    def handle_switch(self,page = -1):
        handle = self.driver.window_handles #获取当前句柄b
        self.driver.switch_to.window(handle[page]) #在句柄2执行
    
    #这个函数是用来显示图片的。
    def show(self,name):
        cv2.imshow('Show',name)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #获取验证码中的图片
    def get_image(self):
        # 获取背景图片
        image1 = self.driver.find_element(By.CLASS_NAME,'yidun_bg-img').get_attribute('src')  # 获取背景元素下载路径
        print(image1)
        # 获取滑动模块图片
        image2 = self.driver.find_element(By.CLASS_NAME,'yidun_jigsaw').get_attribute('src')  # 获取滑块元素下载路径
        print(image2)
        # request请求图片路径保存为二进制格式，并将其存为图片保存到本地
        res_background = requests.get(image1)
        tth_background = res_background.content
        with open('slide_bkg.png', 'wb+')as f:
            f.write(tth_background)
        res_slider = requests.get(image2)
        tth_slider = res_slider.content
        with open('slide_block.png', 'wb+')as f:
            f.write(tth_slider)
        time.sleep(1)
        return 'slide_bkg.png','slide_block.png'


    #计算缺口的位置
    def get_distance(self,bkg,blk):
        block = cv2.imread(blk, 0)
        template = cv2.imread(bkg, 0)
        cv2.imwrite('template.jpg', template)
        cv2.imwrite('block.jpg', block)
        block = cv2.imread('block.jpg')
        block = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)
        block = abs(255 - block)
        cv2.imwrite('block.jpg', block)
        block = cv2.imread('block.jpg')
        template = cv2.imread('template.jpg')
        result = cv2.matchTemplate(block,template,cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(),result.shape)
        print(str(x),str(y))
        #这里就是下图中的绿色框框
        cv2.rectangle(template, (y, x), (y +50, x + 158), (7, 249, 151), 2)
        #便宜距离低于30的，重新计算一次
        if y<30:
            elem= self.driver.find_element(By.CLASS_NAME,'yidun_refresh')
            sleep(0.5)
            elem.click()
            bkg,blk=self.get_image()
            y,template=self.get_distance(bkg,blk)
        return y,template

    #这个是用来模拟人为拖动滑块行为，快到缺口位置时，减缓拖动的速度，服务器就是根据这个来判断是否是人为登录的。
    def get_tracks(self,dis):
        v=0
        t=0.3
        #保存0.3内的位移
        tracks=[]
        current=0
        mid=(dis+20)*4/5
        while current<=dis:
            if current<mid:
                a=12
            else:
                a=-20
            v0=v
            s=v0*t+0.5*a*(t**2)
            current+=s
            tracks.append(round(s))
            v=v0+a*t
        return tracks

    def move(self):
        try_times = 0
        while try_times<10:
            if try_times==6:#累计6次失败会触发检查机制，需要点击某个特殊区域
                self.driver.find_element(By.CLASS_NAME,'yidun_control yidun_control--moving').click()
                print('由于多次失败，因此刷新滑动图片')
                time.sleep(2)
            #获取背景图片和移动模块图片
            bkg,blk=self.get_image()
            #计算背景图片的缺口位置
            distance,template=self.get_distance(bkg,blk)
            #控制速度
            tracks=self.get_tracks(distance)
            #获取滑动模块位置
            element = self.driver.find_element(By.CLASS_NAME,'yidun_slider')
            ActionChains(self.driver).click_and_hold(on_element=element).perform()
            for track in tracks:
                ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()
            sleep(0.5)
            ActionChains(self.driver).release(on_element=element).perform()
            #调试时用，查看到底定位到哪里了
            #show(template)
            try:
                time.sleep(3)
                if try_times==5:
                    self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]').click()
                self.driver.find_element(By.CLASS_NAME,'yidun_refresh').click()
                print('刷新滑动图片成功')
                #累计一次尝试次数+1
                try_times += 1
                if try_times>=10:
                    print('尝试超过10次,退出程序')
                    self.driver.quit()
                else:
                    continue
            except:
                break
        print("登录成功")
        self.driver.refresh()