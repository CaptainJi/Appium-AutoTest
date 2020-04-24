from pageObject.baseView import BaseView
from pageObject.desiredCaps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By


class Common(BaseView):
    okBtn = (By.XPATH, '//*[@text=\'确 定\']')
    cancelBtn = (By.XPATH, '//*[@text=\'取 消\'')
    backBtn = (By.XPATH, '//*[@text=\'返 回\'')
    addBtn = (By.XPATH, '//*[@text=\'添 加\'')
    delBtn = (By.XPATH, '//*[@text=\'删 除\'')
    uploadBtn = (By.XPATH, '//*[@text=\'上 传\'')
    loginBtn = (By.XPATH, '//android.view.View[2]/android.widget.Button.text=(\'登 录\')')

    def check_okBtn(self):
        logging.info('查找确定按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.okBtn)
        except NoSuchElementException:
            logging.info('没有找到确定按钮')
        else:
            logging.info('点击确定')
            element.click()

    def check_cancelBtn(self):
        logging.info('查找取消按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('没有找到取消按钮')
        else:
            logging.info('点击取消')
            element.click()

    def check_backBtn(self):
        logging.info('查找返回按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.backBtn)
        except NoSuchElementException:
            logging.info('没有找到返回按钮')
        else:
            logging.info('点击返回')
            element.click()

    def check_addBtn(self):
        logging.info('查找添加按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.addBtn)
        except NoSuchElementException:
            logging.info('没有找到添加按钮')
        else:
            logging.info('点击添加')
            element.click()

    def check_delBtn(self):
        logging.info('查找删除按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.delBtn)
        except NoSuchElementException:
            logging.info('没有找到删除按钮')
        else:
            logging.info('点击删除')
            element.click()

    def check_uploadBtn(self):
        logging.info('查找上传按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.uploadBtn)
        except NoSuchElementException:
            logging.info('没有找到上传按钮')
        else:
            logging.info('点击上传')
            element.click()

    def check_loginBtn(self):
        logging.info('查找登录按钮')
        driver.implicitly_wait(2)
        try:
            element = self.driver.find_element(*self.loginBtn)
        except NoSuchElementException:
            logging.info('没有找到登录按钮')
        else:
            logging.info('点击登录')
            element.click()


if __name__ == '__main__':
    driver = appium_desired()
    # driver.find_element_by_name('登 录').click()
    com = Common(driver)
    com.check_loginBtn()
    com.check_okBtn()
