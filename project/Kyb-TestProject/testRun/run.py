import unittest
import time
import logging
import sys
import os
# 添加根目录相对路径到系统path中，以便bat运行时调用根目录模块，不然会显示无法import某些文件
sys.path.append(os.path.realpath('..'))

from config.BSTestRunner import BSTestRunner


# 设置测试用例路径与生成报告路径
test_dir = '../testcase'
report_dir = '../reports'
# 装载测试用例，“*”为通配符，例如：test*.py即为执行所有开头为“test”的用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='testLogin.py')
# 获取当前时间
now = time.strftime('%Y' + '年' + '%m' + '月' + '%d' + '日' '%H' + '点' + '%M' + '分' + '%S' + '秒')
# 设置测试报告位置及名称格式
report_name = report_dir + '/' + now + 'TestReport.html'

with open(report_name, 'w', encoding='utf-8') as file:
    # 设置测试报告标题
    runner = BSTestRunner(stream=file, title='测试报告', description='考研帮Android APP测试报告')
    logging.info('test')
    runner.run(discover)

