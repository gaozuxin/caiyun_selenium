# -*- coding: utf-8 -*-
import unittest, time
import sys
import warnings
import os
from common.other import fail_run, one_browser_window
from common.my_redmine import link_redmine
from common.chrome_browser import driver
from common.my_logger import logger
from common.my_mysql import mysql
from framework.caiyun.data_page import DataPage
from framework.caiyun.extension_page import ExtensionPage
from framework.caiyun.index_page import IndexPage
from framework.caiyun.login_page import LoginPage
from framework.caiyun.other_elements import Taskherf_loc
from framework.caiyun.rule_page import RuleIndexPage, RuleAddPage
from framework.caiyun.task_page import TaskIndexPage, TaskAddPage
n = 2


class CaseDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("************************************{}start*************************************".format(__name__))
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
        # mysql.close()
        logger.info("************************************{}end*************************************".format(__name__))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip
    # @fail_run(n)
    def test_demo_001(self):
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
    # @fail_run(n)
    def test_demo_002(self):
        """用户名注册验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_regist()
        usr_data = [
            # {'usr': '', 'show_info': '此处不能为空'},
            # {'usr': '_____', 'show_info': ''},
            {'usr': 'a', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': 'a_', 'show_info': ''},
            {'usr': '123456789012345678901', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': '12345678901234567890', 'show_info': ''},
            {'usr': '</>', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            # {'usr': '1gao高_', 'show_info': ''}
        ]
        for index in range(len(usr_data)):
            self.loginpage.input_regist_username(usr_data[index]['usr'])
            self.loginpage.switch_regist_img()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_registuser()
            logger.info("[{}]用户名：{}；期望：{}；实际：{}".format(os.path.basename(__file__), usr_data[index]['usr'],
                                                        usr_data[index]['show_info'], show_info_l))
            self.assertIn(usr_data[index]['show_info'], show_info_l, msg="注册用户，用户名提示信息有误")
            time.sleep(1)

        self.loginpage.regist('gaozuxin', 'gzx123456', '13683066505', '9274', 'A1b8S')
        # show_info_r = self.loginpage.showinfo_regist()
        # self.assertEqual('用户名已存在，请更换', show_info_r, msg="注册用户，用户名错误提示信息有误")
        time.sleep(2)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    @unittest.skip
    @fail_run(n)
    def test_demo_003(self):
        """用户登录、配置规则、添加任务"""
        logger.info('*===============用例{}\{}开始执行===============*'.format(__name__, sys._getframe().f_code.co_name))
        one_browser_window()
        sql1 = "delete from task_rule where uid = 163 and rule_name like '新建规则_%页';"
        sql2 = "delete from task_info where uid = 163 and task_name like '新建任务_非异步';"
        flag1 = mysql.update(sql1)
        flag2 = mysql.update(sql2)
        self.assertEqual(1, flag1, msg="规则删除失败")
        self.assertEqual(1, flag2, msg="任务删除失败")
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        # self.loginpage.find_element(Ruleherf_loc).click()
        self.rulepage.open()
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
        self.loginpage.find_element('//*[@id="layui-layer4"]/div[3]/a[1]').click()
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
        time.sleep(1)
        self.loginpage.find_element('//*[@id="layui-layer4"]/div[3]/a[1]').click()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        self.extensionpage.add_dongbeinews_textrule()
        self.addrule.click_saverulebtn()
        self.addrule.take_screenshot()
        driver.switch_to.window(handles[0])
        # self.loginpage.find_element(Taskherf_loc).click(
        self.taskpage.open()
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
        sql3 = "select task_id from task_info where uid = 163 and  task_name = '新建任务_非异步';"
        task_id1 = mysql.select_one(sql3)
        time.sleep(100)
        # self.loginpage.find_element(Dataherf_loc).click()
        self.datapage.open()
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
    def test_demo_004(self):
        """任务界面【测试/修改/删除】按钮有效性验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        sql1 = "delete from task_info where uid = 163 and (task_name = '脚本使用任务_常规采集' or task_name = '脚本使用任务_常规采集_copy');"
        sql2 = "INSERT INTO `task_info` (`uid`, `task_name`, `task_config`, `category`, `lang`, `period_cron`, `dt`, `taskstatus`, `notifycls`, `time_break`, `cookie`, `is_agent`, `agent_type`, `agent_value`, `spider_type`, `url`, `spider_status`, `create_uid`, `update_uid`, `trigger_condition`, `warn_grade`, `warn_status`, `mid`, `modelkeywords`, `task_type`) VALUES ('163', '脚本使用任务_常规采集', '{\"max_step\":2,\"spider_type\":1,\"keywords\":[],\"recursion_count\":1,\"recursion_field\":\"\",\"config\":[{\"step_id\":\"data1\",\"step_name\":\"data1\",\"data_name\":\"data1\",\"url\":\"http://in.nen.com.cn/ssjj/index.shtml\",\"rule_id\":\"920\",\"rule_mark\":\"\",\"time_out\":\"5000\",\"rule_type\":1,\"detail_rule_type\":2,\"delete\":false,\"wait\":0,\"filter\":\"url\",\"filter_con\":1,\"filter_type\":false,\"step_col\":\"url\",\"page_num\":0,\"check\":true,\"rend\":true,\"rendrule\":false},{\"step_id\":\"data2\",\"step_name\":\"data2\",\"data_name\":\"data2\",\"url\":\"url\",\"rule_id\":\"919\",\"rule_mark\":\"\",\"time_out\":\"5000\",\"rule_type\":2,\"detail_rule_type\":2,\"delete\":false,\"wait\":0,\"step_col\":\"\",\"page_num\":0,\"filter\":\"\",\"filter_con\":1,\"filter_type\":false,\"check\":true,\"sample_url\":\"http://in.nen.com.cn/system/2018/03/23/020430991.shtml\",\"rend\":true,\"rendrule\":false,\"moving\":false}],\"loginform\":{\"formtype\":\"FORM\",\"submittype\":\"POST\",\"url\":\"http://\",\"body\":true,\"header\":true,\"bodys\":[],\"headers\":[]},\"notify\":{\"notify\":false,\"notify_url\":\"\",\"cls_type\":\"\",\"cls_field\":\"\",\"tag_type\":\"0\",\"tag\":\"\",\"data_map\":[{\"data1._SEED_URL\":\"_SEED_URL\"},{\"data1.title\":\"title\"},{\"data1.url\":\"url\"},{\"data2._SEED_URL\":\"_SEED_URL\"},{\"data2.title\":\"title\"},{\"data2.dt\":\"dt\"},{\"data2.content\":\"content\"}],\"data_map_constant\":[],\"cls_map\":[]}}', '1315', 'zh-CN', '*/1 * * * *', '2019-01-25 16:27:13', 'OFF', '', '30', '', '0', '2', '', '1', 'http://in.nen.com.cn/ssjj/index.shtml', NULL, '163', '163', NULL, NULL, NULL, NULL, NULL, '1');"
        flag1 = mysql.update(sql1)  # 先删除历史任务
        self.assertEqual(1, flag1, msg="删除历史任务失败")
        time.sleep(2)
        flag2 = mysql.update(sql2)  # 插入新任务
        self.assertEqual(1, flag2, msg="插入新任务失败")
        one_browser_window()
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        # self.loginpage.find_element(Taskherf_loc).click()
        self.taskpage.open()
        task_name1 = self.taskpage.get_first_taskname()
        self.assertEqual("脚本使用任务_常规采集", str(task_name1), msg="任务名称获取有误")
        self.taskpage.click_first_testbtn()
        time.sleep(20)
        result_text = self.taskpage.get_firstresult()
        logger.info("测试任务抓取条数:{}".format(result_text))
        self.taskpage.take_screenshot()
        self.assertEqual("共30条数据", str(result_text), msg="测试按钮抓取数据异常")
        self.taskpage.click_first_close()
        time.sleep(1)
        self.taskpage.click_first_modifybtn()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        self.addtask.input_cron('59 23 31 12 *')
        time.sleep(1)
        self.addtask.click_savecnfbtn()
        time.sleep(1)
        self.addtask.click_confirmbtn()
        time.sleep(2)
        self.addtask.click_backlistbtn()
        time.sleep(1)
        schedul = self.taskpage.get_first_schedul()
        logger.info("获取任务的调度文本：{}".format(schedul))
        self.assertEqual("每年12月31日23时59分", str(schedul), msg="修改按钮校验失败")
        self.taskpage.click_first_deletebtn()
        time.sleep(1)
        self.taskpage.click_confirmbtn()
        time.sleep(2)
        sql3 = "select * from task_info where uid = 163 and task_name = '脚本使用任务_常规采集_copy' and taskstatus != 'DELETE' ;"
        task_name = mysql.select_all(sql3)  # 查询任务是否删除
        self.assertEqual('()', str(task_name), msg="删除按钮校验失败")
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')


if __name__ == '__main__':
    unittest.main()
