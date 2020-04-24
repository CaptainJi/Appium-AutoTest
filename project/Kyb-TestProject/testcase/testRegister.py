from common.myunit import StartEnd
from businessView.registerView import RegisterView
from common.commonFun import Common
import logging
import random
import unittest


class RegisterTest(StartEnd):

    def test_user_register(self):
        logging.info('测试用户注册')
        csv_file = '../data/account.csv'
        r = RegisterView(self.driver)
        data = r.get_csv_data(csv_file, 3)
        username = 'Klieg' + str(random.randint(1000, 9000))
        password = 'SIegII' + str(random.randint(1000, 9000))
        email = 'kliegSIeg' + str(random.randint(1000, 9000)) + '@163.com'

        # self.assertTrue(r.register_action(data[0], data[1], data[2]))
        self.assertTrue(r.register_action(username,password, email))


if __name__ == '__main__':
    unittest.main()
