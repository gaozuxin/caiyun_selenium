# coding=utf-8
"""
    @desc: 登录界面驱动模块
    @file: run_loginpage.py
    @date: 2018/11/19
"""

import unittest, sys
import HTMLTestRunner
import time
from selenium import webdriver

from common.my_logger import logger
from framework.caiyun.login_page import LoginPage


class SeleniumTest (unittest.TestCase):
    """采云项目自动化测试"""
    @classmethod
    def setUpClass(cls):
        print("************************start************************")
        cls.driver = webdriver.Chrome()
        cls.login_url = r'http://172.16.20.15/default/index/login'
        cls.loginpage= LoginPage(cls.driver)
        cls.loginpage.open_login()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print("*************************end*************************")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip
    def test_001(self):
        """错误登录信息失败验证"""
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行开始****************************')
        show_div = self.loginpage.login('18201112814', 'jiayou101900', 'abcd')
        logger.info("登录信息提示：%s"%show_div)
        self.assertEqual('登录成功', show_div, msg="用户登录失败")
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行结束****************************')

    # @unittest.skip
    def test_002(self):
        """错误登录信息成功验证"""
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行开始****************************')
        logger.info("用户登陆信息：18201112814, 123456, abcd")
        show_div = self.loginpage.login('18201112814', '123456', 'abcd')
        logger.info("登录信息提示：%s" % show_div)
        self.assertEqual('验证码不正确！', show_div, msg="提示信息错误")
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行结束****************************')

    # @unittest.skip
    def test_003(self):
        """采云用户名输入框测试"""
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行开始****************************')
        self.loginpage.input_username('1111')
        time.sleep(1)
        self.loginpage.input_username('2222')
        time.sleep(1)
        self.loginpage.input_username('3333')
        time.sleep(1)
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行结束****************************')

    # @unittest.skip
    def test_004(self):
        """采云用户成功登录验证"""
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行开始****************************')
        data = [('admin', 'caiyun123', 'A1b8S','登录成功！')]
        for index in range(len(data)):
            logger.info("用户登陆信息：%s, %s, %s, 期望提示信息：%s" % (data[index][0],data[index][1],data[index][2],data[index][3]))
            res = self.loginpage.login(data[index][0],data[index][1],data[index][2])
            self.loginpage.take_screenshot()
            logger.info("用户登录实际提示信息：%s" % res)
            # self.assertEqual(data[index][3], res, msg="提示信息错误")
            time.sleep(3)
        logger.info('*****************************用例' + sys._getframe().f_code.co_name + '执行结束****************************')


if __name__ == '__main__':
    # unittest.main()
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    filename = r'..\report\caiyun_TestReport.html'  # 测试报告的存放路径及文件名
    fp = open(filename, 'wb')  # 创测试报告html文件，此时还是个空文件
    suite = unittest.TestSuite()  # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    suite.addTest(SeleniumTest('test_001'))  # 向测试套件中添加用例
    suite.addTest(SeleniumTest('test_002'))  # 向测试套件中添加用例
    suite.addTest(SeleniumTest('test_003'))  # 向测试套件中添加用例
    suite.addTest(SeleniumTest('test_004'))  # 向测试套件中添加用例
    # runner = unittest.TextTestRunner()   # 执行套件中的用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='采云自动化测试报告', description='测试结果如下: ')
    #  stream = fp  引用文件流
    #  title  测试报告标题
    #  description  报告说明与描述
    runner.run(suite)   # 执行测试
    fp.close()   # 关闭文件流，将HTML内容写进测试报告文件