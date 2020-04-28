import logging
from common.commonFun import Common, NoSuchElementException
from common.desiredCaps import appium_desired
from selenium.webdriver.common.by import By

# 封装登录业务逻辑类


class LoginView(Common):
    # 获取用户名、密码输入框元素
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    # 获取登录按钮元素
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    # 获取“我的”按钮元素
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    right_button = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # 获取退出元素
    logout = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    def login_action(self, username, password):
        # 取消升级
        self.check_cancel_btn()
        # 跳过
        self.check_skipBtn()
        logging.info('开始登录')
        logging.info('用户名：%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('密码：%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)
        logging.info('点击登录按钮')
        self.driver.find_element(*self.loginBtn).click()

    def check_account_alert(self):
        logging.info('检查登录警告信息')
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('跳过登录警告信息')
            element.click()

    def check_login_status(self):
        logging.info('检查登录状态')
        self.check_market_ad()
        self.check_account_alert()

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logging.error('登陆失败')
            self.getScreenShot('登陆失败')
            return False
        else:
            logging.info('登陆成功')
            self.getScreenShot('登陆成功')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('退出登录')
        self.driver.find_element(*self.right_button).click()
        self.driver.find_element(*self.logout).click()
        self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.check_cancel_btn()
    l.check_skipBtn()
    l.login_action('', '')
    l.check_login_status()
