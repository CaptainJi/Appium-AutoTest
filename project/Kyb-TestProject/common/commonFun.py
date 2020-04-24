import csv
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.desiredCaps import appium_desired
from base.baseView import BaseView

# 封装公共类


class Common(BaseView):
    # 定义公共元素
    cancelBtn = (By.ID, 'android:id/button2')  # 取消按钮
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')  # 跳过按钮
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')  # 跳过广告

    def check_cancel_btn(self):
        logging.info('检查取消按钮')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('没有找到取消按钮')
        else:
            logging.info('取消升级')
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('检查跳过按钮')
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('没有找到跳过按钮')
        else:
            logging.info('跳过')
            skipBtn.click()

    # 获取屏幕尺寸

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动屏幕

    def swipeLeft(self):
        logging.info('向左滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.9)
        y1 = int(swipe[1] * 0.5)
        x2 = int(swipe[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 500)

    # 向右滑动屏幕

    def swipeRight(self):
        logging.info('向右滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.1)
        y1 = int(swipe[1] * 0.5)
        x2 = int(swipe[0] * 0.9)
        self.swipe(x1, y1, x2, y1, 500)

    # 向上滑动屏幕

    def swipeUp(self):
        logging.info('向上滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.5)
        y1 = int(swipe[1] * 0.9)
        y2 = int(swipe[0] * 0.1)
        self.swipe(x1, y1, x1, y2, 500)

    # 向下滑动屏幕

    def swipeDown(self):
        logging.info('向下滑动')
        swipe = self.get_size()
        x1 = int(swipe[0] * 0.5)
        y1 = int(swipe[1] * 0.1)
        y2 = int(swipe[0] * 0.9)
        self.swipe(x1, y1, x1, y2, 500)

    # 获取当前时间
    def getTime(self):
        # windows文件名禁止使用“:”所以时间格式要避免类似“14:30:25”
        self.now_time = time.strftime('%Y' + '年' + '%m' + '月' + '%d' + '日' '%H' + '点' + '%M' + '分' + '%S' + '秒')
        return self.now_time

    # 获取截图
    def getScreenShot(self, module):
        now_time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s %s.png' % (module, now_time)
        logging.info('获取“%s”屏幕截图' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info('检查广告弹窗')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('关闭广告弹窗')
            element.click()

    # 读取csv数据模块

    def get_csv_data(self,csv_file, line):
        logging.info('获取csv数据')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':

    driver = appium_desired()
    com = Common(driver)
    com.check_cancel_btn()
    com.check_skipBtn()
    print(com.getTime())
    com.swipeLeft()
    com.getScreenShot('测试截图')

    # csv_file = '../data/account.csv'
    # data = get_csv_data(csv_file, 2)
    # print(data)
