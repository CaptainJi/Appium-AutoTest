import unittest
import logging
from common.desiredCaps import appium_desired
from time import sleep


class StartEnd(unittest.TestCase):
    # 测试开始前执行
    def setUp(self):
        logging.info('======执行用例======')
        self.driver = appium_desired()

    # 测试结束后执行
    def tearDown(self) -> None:
        logging.info('======结束用例======')
        self.driver.close_app()
        sleep(2)
