# -*- coding: utf-8 -*-
import unittest, time

import sys
import warnings

from common.other import fail_run, one_browser_window
from common.my_redmine import link_redmine
from common.chrome_browser import driver
from common.my_logger import logger
from common.my_mysql import mysql
from framework.caiyun.data_page import DataPage
from framework.caiyun.extension_page import ExtensionPage
from framework.caiyun.index_page import IndexPage
from framework.caiyun.login_page import LoginPage
from framework.caiyun.other_elements import Ruleherf_loc, Taskherf_loc, Dataherf_loc
from framework.caiyun.rule_page import RuleIndexPage, RuleAddPage
from framework.caiyun.task_page import TaskIndexPage, TaskAddPage


class CaseRule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("****************************************start****************************************")
        cls.loginpage = LoginPage(driver)
        cls.indexpage = IndexPage(driver)
        cls.rulepage = RuleIndexPage(driver)
        cls.addrule = RuleAddPage(driver)
        cls.extensionpage = ExtensionPage(driver)
        cls.taskpage = TaskIndexPage(driver)
        cls.addtask = TaskAddPage(driver)
        cls.datapage = DataPage(driver)

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        mysql.close()
        logger.info("*****************************************end*****************************************")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip
    @fail_run(n=2)
    def test006_rule(self):
        """规则模板验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.indexpage.click_exit_userbtn()
        self.loginpage.open_login()
        self.loginpage.login('admin', 'caiyun123', 'A1b8S')
        self.loginpage.find_element(Ruleherf_loc).click()
        self.rulepage.get_result(count_num=72)  # 规则条数
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')


if __name__ == '__main__':
    unittest.main()
