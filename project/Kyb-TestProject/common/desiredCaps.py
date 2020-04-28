import yaml
import logging.config
import os
import multiprocessing
from appium import webdriver
from time import ctime
from server.appiumDeviceSync import *

# 读取日志配置文件
CONLOG = '../config/log.conf'
logging.config.fileConfig(CONLOG)
logging = logging.getLogger()

# 读取capability.yaml配置文件
with open('../config/capability.yaml', 'r', encoding='utf-8') as file:
    # 原yaml.load(file)方法已被舍弃，新写法如下
    data = yaml.load(file, Loader=yaml.FullLoader)
    # 获取设备列表
    devicesList = data['devicesList']


# 定义desired
def appium_desired():
    host = data['host']
    port = data['port']
    start_appium_action(host, port)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['devicesList'][0]
    desired_caps['udid'] = data['devicesList'][0]
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
    # print('Appium port:%s Start run %s at %s' % (port, index, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)

    driver.implicitly_wait(2)
    return driver


def close_appium():
    host = data['host']
    port = data['port']
    release_port(host,port)
# 构建进程组
# desired_process = []
# # 多进程启动测试
# for i in range(len(devicesList)):
#     port = data['port'] + 2 * i
#     desired = multiprocessing.Process(target=appium_desired, args=(i, port))
#     desired_process.append(desired)


if __name__ == '__main__':
    #
    # for desired in desired_process:
    #     desired.start()
    # for desired in desired_process:
    #     desired.join()
    appium_desired()
