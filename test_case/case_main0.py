# -*- coding: utf-8 -*-
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

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        mysql.close()
        logger.info("*****************************************end*****************************************")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip
    @fail_run(n=3)
    def test001_regist(self):
        """新用户注册"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        sql = "delete from user_info where phone='18637607203';"
        flag = mysql.update(sql)
        if flag:
            logger.info("用户删除成功")
        else:
            logger.error("用户删除失败")
        one_browser_window()
        self.loginpage.open_regist()
        self.loginpage.regist('gaozuxin', 'gzx123456', '18637607203', '9274', 'A1b8S')
        self.loginpage.take_screenshot()
        islogin = self.indexpage.get_loginuser()
        if islogin == 'gaozuxin':
            logger.info('注册并登录成功')
        else:
            logger.error('注册并登录失败')
        self.indexpage.click_exit_userbtn()
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    @fail_run(n=3)
    def test002_task(self):
        """用户登录、配置规则、添加任务"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__,sys._getframe().f_code.co_name))
        one_browser_window()
        sql1 = "delete from task_rule where uid = 163 and rule_name like '新建规则_%页';"
        sql2 = "delete from task_info where uid = 163 and task_name like '新建任务_非异步';"
        flag1 = mysql.update(sql1)
        flag2 = mysql.update(sql2)
        if flag1 == 1 and flag2 == 1:
            logger.info('任务和规则删除成功')
        else:
            logger.error('任务和规则删除失败')

        # driver.set_window_size(900, 600)
        # window_size = driver.get_window_size()
        # logger.info(window_size)
        #
        # time.sleep(2)
        # driver.maximize_window()
        # window_size = driver.get_window_size()
        # logger.info(window_size)
        #
        # time.sleep(2)
        # driver.set_window_size(3000, 1000)
        # window_size = driver.get_window_size()
        # logger.info(window_size)

        # driver.set_window_size(1000, 812)
        # window_size = driver.get_window_size()
        # logger.info(window_size)

        self.loginpage.open_login()

        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        try:
            self.loginpage.find_element(Ruleherf_loc).click()
        except:
            self.loginpage.take_screenshot()
            exit()
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
        if str(task_id1[0]) == str(task_id2):
            self.datapage.click_see_details()
            tasks = self.datapage.get_first_tasks()
            logger.info("任务抓取条数{}".format(tasks))
            if str(tasks) == '30' :
                logger.info("任务数据抓取正常")
            else:
                logger.error("任务数据抓取异常")
        else:
            logger.error("任务id获取异常")

        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    @unittest.skip
    @fail_run(n=5)
    def test003_task(self):
        """用户登录、配置规则、添加任务（异步抓取）"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        sql1 = "delete from task_rule where uid = 163 and rule_name like '新建规则_%页_异步';"
        sql2 = "delete from task_info where uid = 163 and task_name like '新建任务_异步';"
        flag1 = mysql.update(sql1)
        flag2 = mysql.update(sql2)
        if flag1 == 1 and flag2 == 1:
            logger.info('任务和规则删除成功')
        else:
            logger.error('任务和规则删除失败')
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
        if str(task_id1[0]) == str(task_id2):
            self.datapage.click_see_details()
            tasks = self.datapage.get_first_tasks()
            logger.info("任务抓取条数{}".format(tasks))
            if str(tasks) == '60':
                logger.info("任务数据抓取正常")
            else:
                logger.error("任务数据抓取异常")
        else:
            logger.error("任务id获取异常")
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    @unittest.skip
    @fail_run(n=3)
    def test004_task(self):
        """微信采集_公众号采集"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        sql1 = "delete from task_info where uid = 163 and task_name = '微信采集_公众号_久其智通';"
        flag1 = mysql.update(sql1)
        if flag1 == 1 :
            logger.info('微信采集公众号任务删除成功')
        else:
            logger.error('微信采集公众号任务删除失败')
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
        if str(task_id1[0]) == str(task_id2):
            self.datapage.click_see_details()
            tasks = self.datapage.get_first_tasks()
            logger.info("任务抓取条数{}".format(tasks))
            if str(tasks) != '0':
                logger.info("任务数据抓取正常")
            else:
                logger.error("任务数据抓取异常")
        else:
            logger.error("任务id获取异常")
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    @unittest.skip
    @fail_run(n=3)
    def test005_task(self):
        """微博采集_微博号采集"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        sql1 = "delete from task_info where uid = 163 and task_name = '微博采集_微博号_大数据';"
        flag1 = mysql.update(sql1)
        if flag1 == 1:
            logger.info('微博采集微博号任务删除成功')
        else:
            logger.error('微博采集微博号任务删除失败')
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
        if str(task_id1[0]) == str(task_id2):
            self.datapage.click_see_details()
            tasks = self.datapage.get_first_tasks()
            logger.info("任务抓取条数{}".format(tasks))
            if str(tasks) != '0':
                logger.info("任务数据抓取正常")
            else:
                logger.error("任务数据抓取异常")
        else:
            logger.error("任务id获取异常")
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    @unittest.skip
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

    @unittest.skip
    @fail_run(n=2)
    def test007_rule(self):
        """"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.find_element(Taskherf_loc).click()

        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')


if __name__ == '__main__':
    unittest.main()
