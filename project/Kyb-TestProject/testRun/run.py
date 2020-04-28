import unittest
import time
import logging
import sys
import os

# 添加根目录相对路径到系统path中，以便批处理运行时调用根目录模块，不然会显示无法import某些文件
sys.path.append(os.path.realpath('..'))
# 导入报告生成模块HTMLTestRunnerCN为中文版HTMLTestRunnerEN为英文版
from config.HTMLTestRunnerCN import HTMLTestReportCN
from common.desiredCaps import close_appium

# 设置测试用例路径与生成报告路径
test_dir = '../testcase'
report_dir = '../reports'

# 装载测试用例，“*”为通配符，例如：test*.py即为执行所有开头为“test”的用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='testLogin.py')

# 获取当前时间
now = time.strftime('%Y' + '年' + '%m' + '月' + '%d' + '日' '%H' + '点' + '%M' + '分' + '%S' + '秒')

# 设置测试报告位置及名称格式
report_name = report_dir + '/' + now + 'TestReport.html'

# Python3给open函数添加了名为encoding的新参数，而这个新参数的默认值却是‘utf-8’。这样在文件句柄上进行read和write操作时，系统就要求开发者必须传入包含Unicode字符的实例，而不接受包含二进制数据的bytes实例。
# 解决方法：
# 使用二进制写入模式（‘wb’）来开启待操作文件，而不能像原来那样，采用字符写入模式（‘w’）。
# 文件读取数据的时候也有类似的问题。解决这种问题的办法也相似：用'rb'模式（二进制模式）打开文件，而不要使用'r'模式。
with open(report_name, 'wb') as file:
    # 设置测试报告标题、描述、测试人员等信息
    runner = HTMLTestReportCN(stream=file, title='测试报告', description='考研帮Android APP测试报告', tester='CaptainJi')
    logging.info('测试开始')

    runner.run(discover)
    close_appium()
    logging.info('测试结束，测试报告请查看%s' % report_name)
