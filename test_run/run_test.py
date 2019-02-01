# -*- coding: utf-8 -*-
import os
from HTMLTestRunner import HTMLTestRunner
import unittest, time
from common.sendemail import Email


def _main():
    email = Email()
    testdir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(testdir, 'test_case')  # 测试用例文件夹
    test_report = os.path.join(testdir, 'report')
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = test_report + '/result_' + now + '.html'
    fp = open(filename, 'wb')
    # stream放生成报告的路径
    runner = HTMLTestRunner(stream=fp, title="测试报告", description='用例执行情况：')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='case_demo*.py')
    runner.run(discover)
    fp.close()
    new_report = email.new_report(test_report)
    email.send_mail(new_report)


if __name__ == "__main__":
    _main()
