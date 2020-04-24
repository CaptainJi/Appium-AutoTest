import logging
from pageObject.comminFun import Common
from pageObject.comminFun import appium_desired
from selenium.webdriver.common.by import By


class LoginView(Common):
    username_type = (By.XPATH, '//android.widget.EditText[1]')
    password_type = (By.XPATH, '//android.widget.EditText[2]')
    loginBtn = (By.XPATH, '//android.view.View[2]/android.widget.Button')

    def login_action(self, username, password):
        logging.info('开始登录')
        logging.info('用户名：%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('密码')
        self.driver.find_element(*self.password_type).send_keys(password)
        logging.info('点击登录')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('登录完成')


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('1', '1')
