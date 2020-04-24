import yaml
import logging.config
from appium import webdriver
import os

CONLOG = '../config/log.conf'
logging.config.fileConfig(CONLOG)
logging = logging.getLogger()


def appium_desired():
    # 读取capability配置文件
    with open('../config/capability.yaml', 'r', encoding='utf-8') as file:
        # 原yaml.load(file)方法已被舍弃，新写法如下
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}

    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    # 相对路径读取文件
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])

    desired_caps['app'] = app_path
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    logging.info('启动APP')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    driver.implicitly_wait(2)
    return driver


if __name__ == '__main__':
    appium_desired()
