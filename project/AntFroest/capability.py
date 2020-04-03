# capability配置信息
# coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from log import log
# capability信息配置
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '27dc7322'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['app'] = r'C:\Users\CaptainJi\Desktop\apk\alipay.apk'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
desired_caps['noReset'] = True
# 重置键盘
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)



