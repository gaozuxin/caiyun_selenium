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
n = 2


class CaseMain(unittest.TestCase):

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
        cls.redmine_user = 'gaozuxin'
        cls.redmine_pwd = ''
        warnings.simplefilter("ignore", ResourceWarning)

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
    @fail_run(n)
    def test001_regist(self):
        """新用户注册"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))

        sql = "delete from user_info where phone='18637607203';"
        sql1 = "DELETE FROM category_tree where media_name = 'gaozuxin'";
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
            self.assertEqual('gaozuxin', islogin, msg="注册并登录失败")
        except:
            data = {
                "subject": '[自动创建]新用户注册并登录异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual('gaozuxin', islogin, msg="注册并登录失败")
        self.indexpage.click_exit_userbtn()
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))

    # @unittest.skip
    @fail_run(n)
    def test002_task(self):
        """用户登录、配置规则、添加任务"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        sql1 = "delete from task_rule where uid = 163 and rule_name like '新建规则_%页';"
        sql2 = "delete from task_info where uid = 163 and task_name like '新建任务_非异步';"
        flag1 = mysql.update(sql1)
        flag2 = mysql.update(sql2)
        self.assertEqual(1, flag1, msg="规则删除失败")
        self.assertEqual(1, flag2, msg="任务删除失败")
        driver.set_window_size(900, 600)
        window_size = driver.get_window_size()
        logger.info(window_size)

        time.sleep(2)
        driver.maximize_window()
        window_size = driver.get_window_size()
        logger.info(window_size)

        time.sleep(2)
        driver.set_window_size(3000, 1000)
        window_size = driver.get_window_size()
        logger.info(window_size)

        # driver.set_window_size(1000, 812)
        # window_size = driver.get_window_size()
        # logger.info(window_size)

        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        self.loginpage.find_element(Ruleherf_loc).click()
        self.rulepage.add_rule()
        time.sleep(1)
        handles = driver.window_handles  # 获取所有打开窗口的句柄
        driver.switch_to.window(handles[1])
        rulename1 = '新建规则_列表页'
        select_category1 = 'category1'
        rule_type1 = 'type1'
        pageurl1 = 'http://in.nen.com.cn/ssjj/index.shtml'
        url_pattern1 = 'http://in.nen.com.cn*'
        rulemark1 = 'test_list'
        extract_method1 = 'method1'
        self.addrule.click_enter_piontconf(rulename1, select_category1, rule_type1, pageurl1, url_pattern1,
                                      rulemark1, extract_method1)
        time.sleep(1)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        self.extensionpage.add_dongbeinews_listrule()
        self.addrule.click_savecnewrulebtn()
        self.addrule.take_screenshot()
        time.sleep(5)
        rulename2 = '新建规则_正文页'
        select_category2 = 'category1'
        rule_type2 = 'type2'
        pageurl2 = 'http://in.nen.com.cn/system/2018/03/23/020430991.shtml'
        url_pattern2 = 'http://in.nen.com.cn*'
        rulemark2 = 'test_text'
        extract_method2 = 'method1'
        self.addrule.click_enter_piontconf(rulename2, select_category2, rule_type2, pageurl2, url_pattern2,
                                      rulemark2, extract_method2)
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        self.extensionpage.add_dongbeinews_textrule()
        self.addrule.click_saverulebtn()
        self.addrule.take_screenshot()
        driver.switch_to.window(handles[0])
        self.loginpage.find_element(Taskherf_loc).click()
        self.taskpage.add_task()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        taskname = '新建任务_非异步'
        taskcategory = 'category1'
        tasktype = '调度任务'
        cron = '*/1 * * * *'
        timebreak_loc = '30'
        isagent = '否'
        self.addtask.collect_init(taskname, taskcategory, tasktype, cron, timebreak_loc, isagent)
        urllist_lis = 'http://in.nen.com.cn/ssjj/index.shtml'
        select_extractrule_list = "新建规则_列表页"
        check1_list = 'url'
        check2_list = '当选中字段已经存在时跳过'
        turnpagec_list = '0'
        opentimeout_list = '5秒'
        waittime_list = '不等待'
        sampleurl_text = 'http://in.nen.com.cn/system/2018/03/23/020430991.shtml'
        selcet_extractrule_text = "新建规则_正文页"
        turnpagec_text = '0'
        opentimeout_text = '5秒'
        waittime_text = '不等待'
        self.addtask.new_regular_collection(urllist_lis, select_extractrule_list, check1_list, check2_list,
                                       turnpagec_list, opentimeout_list, waittime_list, sampleurl_text,
                                       selcet_extractrule_text, turnpagec_text, opentimeout_text, waittime_text)
        self.addtask.click_savecnfbtn()
        self.addtask.click_confirmbtn()
        self.addrule.take_screenshot()
        time.sleep(2)
        self.addtask.click_effectivenowbtn()
        self.loginpage.take_screenshot()
        driver.switch_to.window(handles[0])
        sql3 ="select task_id from task_info where uid = 163 and  task_name = '新建任务_非异步';"
        task_id1 = mysql.select_one(sql3)
        time.sleep(220)
        self.loginpage.find_element(Dataherf_loc).click()
        task_id2 = self.datapage.get_first_taskid()
        self.loginpage.take_screenshot()
        try:
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="任务id获取异常")
        except:
            data = {
                "subject": '[自动创建]新建非异步常规任务id获取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="任务id获取异常")
        self.datapage.click_see_details()
        tasks = self.datapage.get_first_tasks()
        logger.info("任务抓取条数{}".format(tasks))
        try:
            self.assertEqual('30', str(tasks), msg="任务数据抓取异常")
        except:
            data = {
                "subject": '[自动创建]非异步常规任务数据抓取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual('30', str(tasks), msg="任务数据抓取异常")
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))

    # @unittest.skip
    @fail_run(n)
    def test003_task(self):
        """用户登录、配置规则、添加任务（异步抓取）"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        sql1 = "delete from task_rule where uid = 163 and rule_name like '新建规则_%页_异步';"
        sql2 = "delete from task_info where uid = 163 and task_name like '新建任务_异步';"
        flag1 = mysql.update(sql1)
        flag2 = mysql.update(sql2)
        self.assertEqual(1, flag1, msg="规则删除失败")
        self.assertEqual(1, flag2, msg="任务删除失败")
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        self.loginpage.find_element(Ruleherf_loc).click()
        self.rulepage.add_rule()
        time.sleep(1)
        handles = driver.window_handles  # 获取所有打开窗口的句柄
        driver.switch_to.window(handles[1])
        rulename1 = '新建规则_列表页_异步'
        select_category1 = 'category1'
        rule_type1 = 'type1'
        pageurl1 = 'http://in.nen.com.cn/ssjj/index.shtml'
        url_pattern1 = 'http://in.nen.com.cn*'
        rulemark1 = 'test_list'
        extract_method1 = 'method1'
        self.addrule.click_enter_piontconf(rulename1, select_category1, rule_type1, pageurl1, url_pattern1,
                                      rulemark1, extract_method1)
        time.sleep(1)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        self.extensionpage.add_dongbeinews_listrule_ajax()
        self.addrule.click_savecnewrulebtn()
        self.addrule.take_screenshot()
        time.sleep(5)
        rulename2 = '新建规则_正文页_异步'
        select_category2 = 'category1'
        rule_type2 = 'type2'
        pageurl2 = 'http://in.nen.com.cn/system/2018/03/23/020430991.shtml'
        url_pattern2 = 'http://in.nen.com.cn*'
        rulemark2 = 'test_text'
        extract_method2 = 'method1'
        self.addrule.click_enter_piontconf(rulename2, select_category2, rule_type2, pageurl2, url_pattern2,
                                      rulemark2, extract_method2)
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        self.extensionpage.add_dongbeinews_textrule()
        self.addrule.click_saverulebtn()
        self.addrule.take_screenshot()
        driver.switch_to.window(handles[0])
        self.loginpage.find_element(Taskherf_loc).click()
        self.taskpage.add_task()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        taskname = '新建任务_异步'
        taskcategory = 'category1'
        tasktype = '调度任务'
        cron = '*/1 * * * *'
        timebreak_loc = '30'
        isagent = '否'
        self.addtask.collect_init(taskname, taskcategory, tasktype, cron, timebreak_loc, isagent)
        urllist_lis = 'http://in.nen.com.cn/ssjj/index.shtml'
        select_extractrule_list = "新建规则_列表页_异步"
        check1_list = 'url'
        check2_list = '当选中字段已经存在时跳过'
        turnpagec_list = '2'
        opentimeout_list = '5秒'
        waittime_list = '不等待'
        sampleurl_text = 'http://in.nen.com.cn/system/2018/03/23/020430991.shtml'
        selcet_extractrule_text = "新建规则_正文页_异步"
        turnpagec_text = '0'
        opentimeout_text = '5秒'
        waittime_text = '不等待'
        self.addtask.new_regular_collection(urllist_lis, select_extractrule_list, check1_list, check2_list,
                                       turnpagec_list, opentimeout_list, waittime_list, sampleurl_text,
                                       selcet_extractrule_text, turnpagec_text, opentimeout_text, waittime_text)
        self.addtask.click_savecnfbtn()
        self.addtask.click_confirmbtn()
        self.addrule.take_screenshot()
        time.sleep(2)
        self.addtask.click_effectivenowbtn()
        self.loginpage.take_screenshot()
        driver.switch_to.window(handles[0])
        sql3 ="select task_id from task_info where uid = 163 and  task_name = '新建任务_异步';"
        task_id1 = mysql.select_one(sql3)
        time.sleep(220)
        self.loginpage.find_element(Dataherf_loc).click()
        task_id2 = self.datapage.get_first_taskid()
        self.loginpage.take_screenshot()
        try:
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="任务id获取异常")
        except:
            data = {
                "subject": '[自动创建]新建异步常规任务id获取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="任务id获取异常")
        self.datapage.click_see_details()
        tasks = self.datapage.get_first_tasks()
        logger.info("任务抓取条数{}".format(tasks))
        try:
            self.assertEqual('60', str(tasks), msg="任务数据抓取异常")
        except:
            data = {
                "subject": '[自动创建]异步常规任务数据抓取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual('60', str(tasks), msg="任务数据抓取异常")
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))

    @unittest.skip
    @fail_run(n)
    def test004_task(self):
        """微信采集_公众号采集"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        sql1 = "delete from task_info where uid = 163 and task_name = '微信采集_公众号_久其智通';"
        flag1 = mysql.update(sql1)
        self.assertEqual(1, flag1, msg="微信采集公众号任务删除失败")
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        self.loginpage.find_element(Taskherf_loc).click()
        self.taskpage.add_task()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        taskname = '微信采集_公众号_久其智通'
        taskcategory = 'category2'
        tasktype = '调度任务'
        cron = '*/1 * * * *'
        timebreak_loc = '30'
        isagent = '否'
        self.addtask.collect_init(taskname, taskcategory, tasktype, cron, timebreak_loc, isagent)
        wxkeyword = '久其智通'
        self.addtask.new_wechat_collection(wxkeyword)
        time.sleep(2)
        self.addtask.click_savecnfbtn1()
        self.addtask.click_confirmbtn()
        self.addrule.take_screenshot()
        time.sleep(5)
        self.addtask.click_effectivenowbtn1()
        self.loginpage.take_screenshot()
        driver.switch_to.window(handles[0])
        sql3 = "select task_id from task_info where uid = 163 and  task_name = '微信采集_公众号_久其智通';"
        task_id1 = mysql.select_one(sql3)
        time.sleep(120)
        self.loginpage.find_element(Dataherf_loc).click()
        task_id2 = self.datapage.get_first_taskid()
        self.loginpage.take_screenshot()
        try:
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="微信采集任务id获取异常")
        except:
            data = {
                "subject": '[自动创建]新建微信公众号采集任务id获取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="微信采集任务id获取异常")
        self.datapage.click_see_details()
        tasks = self.datapage.get_first_tasks()
        logger.info("任务抓取条数{}".format(tasks))
        try:
            self.assertNotEqual('0', str(tasks), msg="微信采集任务数据抓取异常")
        except:
            data = {
                "subject": '[自动创建]微信公众号采集任务数据抓取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertNotEqual('0', str(tasks), msg="微信采集任务数据抓取异常")
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))

    @unittest.skip
    @fail_run(n)
    def test005_task(self):
        """微博采集_微博号采集"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        sql1 = "delete from task_info where uid = 163 and task_name = '微博采集_微博号_大数据';"
        flag1 = mysql.update(sql1)
        self.assertEqual(1, flag1, msg="微博采集微博号任务删除失败")
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        self.loginpage.find_element(Taskherf_loc).click()
        self.taskpage.add_task()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        taskname = '微博采集_微博号_大数据'
        taskcategory = 'category2'
        tasktype = '调度任务'
        cron = '*/1 * * * *'
        timebreak_loc = '30'
        isagent = '否'
        self.addtask.collect_init(taskname, taskcategory, tasktype, cron, timebreak_loc, isagent)
        wbkeyword = '大数据'
        self.addtask.new_weibo_collection(wbkeyword)
        time.sleep(2)
        self.addtask.click_savecnfbtn1()
        self.addtask.click_confirmbtn()
        self.addrule.take_screenshot()
        time.sleep(5)
        self.addtask.click_effectivenowbtn1()
        self.loginpage.take_screenshot()
        driver.switch_to.window(handles[0])
        sql3 = "select task_id from task_info where uid = 163 and  task_name = '微博采集_微博号_大数据';"
        task_id1 = mysql.select_one(sql3)
        time.sleep(120)
        self.loginpage.find_element(Dataherf_loc).click()
        task_id2 = self.datapage.get_first_taskid()
        self.loginpage.take_screenshot()
        try:
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="微博采集任务id获取异常")
        except:
            data = {
                "subject": '[自动创建]新建微博微博号采集任务id获取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertEqual(str(task_id1[0]), str(task_id2), msg="微博采集任务id获取异常")
        self.datapage.click_see_details()
        tasks = self.datapage.get_first_tasks()
        logger.info("任务抓取条数{}".format(tasks))
        try:
            self.assertNotEqual('0', str(tasks), msg="微博采集任务数据抓取异常")
        except:
            data = {
                "subject": '[自动创建]微博微博号采集任务数据抓取异常',
                "description": ''
            }
            link_redmine(self.redmine_user, self.redmine_pwd, data)
            self.assertNotEqual('0', str(tasks), msg="微博采集任务数据抓取异常")
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))

    @unittest.skip
    @fail_run(n)
    def test006_rule(self):
        """规则模板验证"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        self.indexpage.click_exit_userbtn()
        self.loginpage.open_login()
        self.loginpage.login('admin', 'caiyun123', 'A1b8S')
        self.loginpage.find_element(Ruleherf_loc).click()
        self.rulepage.get_result(count_num=72)  # 规则条数
        logger.info('*===============用例{}\{}执行结束===============*'.format(__name__, sys._getframe().f_code.co_name))


if __name__ == '__main__':
    unittest.main()
