# -*- coding: utf-8 -*-
import unittest, time
import sys
import warnings
from common.other import fail_run, one_browser_window
from common.my_redmine import link_redmine
from common.chrome_browser import driver
from common.my_logger import logger
from common.my_mysql import mysql
from framework.caiyun.index_page import IndexPage
from framework.caiyun.login_page import LoginPage
n = 2


class CaseDemo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("************************************{}start*************************************".format(__name__))
        cls.loginpage = LoginPage(driver)
        cls.indexpage = IndexPage(driver)
        cls.redmine_user = 'gaozuxin'
        cls.redmine_pwd = 'jiuqi@310235'
        warnings.simplefilter("ignore", ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        logger.info("************************************{}end*************************************".format(__name__))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip
    # @fail_run(n)
    def test_demo_001(self):
        """用户登陆验证"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        self.loginpage.open_regist()
        self.loginpage.regist('gaogao', 'gzx123456', '18201112814', '9274', 'A1b8S')
        show_info_r = self.loginpage.find_element_xpath('//*[@id="search-form"]/div[2]/input').text
        self.assertEqual('用户名已存在，请更换', show_info_r, msg="注册用户，用户名错误提示信息有误")
        time.sleep(3)
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))

    # @unittest.skip
    # @fail_run(n)
    def test_demo_002(self):
        """新用户注册"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))

        sql = "delete from user_info where phone='18637607203';"
        sql1 = "delete from category_tree where media_name = 'gaozuxin'";
        flag = mysql.update(sql)
        flag2 = mysql.update(sql1)
        self.assertEqual(1, flag, msg="用户删除失败")
        self.assertEqual(1, flag2, msg="用户删除失败")
        one_browser_window()
        self.loginpage.open_regist()
        self.loginpage.regist('gaozuxin', 'gzx123456', '18637607203', '9274', 'A1b8S')
        self.loginpage.take_screenshot()
        islogin = self.indexpage.get_loginuser()
        try:
            self.assertEqual('gaozuxin1', islogin, msg="注册并登录失败")
        except:
            data = {
                "subject": '[自动创建]新用户注册并登录异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual('gaozuxin1', islogin, msg="注册并登录失败")
        self.indexpage.click_exit_userbtn()
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))


if __name__ == '__main__':
    unittest.main()
