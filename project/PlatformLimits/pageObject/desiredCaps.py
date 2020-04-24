import yaml
import logging.config
from appium import webdriver

conLog = '../config/log.conf'
logging.config.fileConfig(conLog)
logging = logging.getLogger()


def appium_desired():
    stream = open('../yaml/capability.yaml', 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['app'] = data['app']
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
