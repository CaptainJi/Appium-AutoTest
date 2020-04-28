import logging
import unittest
from common.myunit import StartEnd
from businessView.loginView import LoginView


# 编写测试用例类

class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    # @unittest.skip('跳过')
    def test_login_1(self):
        logging.info('测试登录第一个账户')
        # 调用登录业务模块
        login = LoginView(self.driver)
        # 读取csv数据
        data = login.get_csv_data(self.csv_file, 1)
        # 执行登录业务动作
        login.login_action(data[0], data[1])
        # 断言执行是否成功
        self.assertTrue(login.check_login_status())

    # @unittest.skip('跳过')
    def test_login_2(self):
        logging.info('测试登录第二个账户')
        login = LoginView(self.driver)
        data = login.get_csv_data(self.csv_file, 2)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_status())

    # @unittest.skip('跳过')
    def test_login_3(self):
        logging.info('测试登录第三个账户')
        login = LoginView(self.driver)
        data = login.get_csv_data(self.csv_file, 3)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_status())


if __name__ == '__main__':
    unittest.main()
