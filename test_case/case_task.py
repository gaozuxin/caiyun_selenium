import unittest, sys, time
from common.chrome_browser import driver
from common.my_logger import logger
from common.my_mysql import mysql
from common.other import one_browser_window, fail_run
from framework.caiyun.data_page import DataPage
from framework.caiyun.index_page import IndexPage
from framework.caiyun.login_page import LoginPage
from framework.caiyun.other_elements import Taskherf_loc
from framework.caiyun.task_page import TaskIndexPage, TaskAddPage


class CaseTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("****************************************start****************************************")
        cls.loginpage = LoginPage(driver)
        cls.indexpage = IndexPage(driver)
        cls.taskpage = TaskIndexPage(driver)
        cls.addtask = TaskAddPage(driver)
        cls.datapage = DataPage(driver)

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        mysql.close()
        logger.info("****************************************end****************************************")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip
    def test_task_001(self):
        """任务界面【生效/执行历史/失效/删除】按钮有效性验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        sql1 = "delete from task_info where uid = 163 and (task_name = '脚本使用任务_常规采集' or task_name = '脚本使用任务_常规采集_copy') ;"
        sql2 = "INSERT INTO `task_info` (`uid`, `task_name`, `task_config`, `category`, `lang`, `period_cron`, `dt`, `taskstatus`, `notifycls`, `time_break`, `cookie`, `is_agent`, `agent_type`, `agent_value`, `spider_type`, `url`, `spider_status`, `create_uid`, `update_uid`, `trigger_condition`, `warn_grade`, `warn_status`, `mid`, `modelkeywords`, `task_type`) VALUES ('163', '脚本使用任务_常规采集', '{\"max_step\":2,\"spider_type\":1,\"keywords\":[],\"recursion_count\":1,\"recursion_field\":\"\",\"config\":[{\"step_id\":\"data1\",\"step_name\":\"data1\",\"data_name\":\"data1\",\"url\":\"http://in.nen.com.cn/ssjj/index.shtml\",\"rule_id\":\"920\",\"rule_mark\":\"\",\"time_out\":\"5000\",\"rule_type\":1,\"detail_rule_type\":2,\"delete\":false,\"wait\":0,\"filter\":\"url\",\"filter_con\":1,\"filter_type\":false,\"step_col\":\"url\",\"page_num\":0,\"check\":true,\"rend\":true,\"rendrule\":false},{\"step_id\":\"data2\",\"step_name\":\"data2\",\"data_name\":\"data2\",\"url\":\"url\",\"rule_id\":\"919\",\"rule_mark\":\"\",\"time_out\":\"5000\",\"rule_type\":2,\"detail_rule_type\":2,\"delete\":false,\"wait\":0,\"step_col\":\"\",\"page_num\":0,\"filter\":\"\",\"filter_con\":1,\"filter_type\":false,\"check\":true,\"sample_url\":\"http://in.nen.com.cn/system/2018/03/23/020430991.shtml\",\"rend\":true,\"rendrule\":false,\"moving\":false}],\"loginform\":{\"formtype\":\"FORM\",\"submittype\":\"POST\",\"url\":\"http://\",\"body\":true,\"header\":true,\"bodys\":[],\"headers\":[]},\"notify\":{\"notify\":false,\"notify_url\":\"\",\"cls_type\":\"\",\"cls_field\":\"\",\"tag_type\":\"0\",\"tag\":\"\",\"data_map\":[{\"data1._SEED_URL\":\"_SEED_URL\"},{\"data1.title\":\"title\"},{\"data1.url\":\"url\"},{\"data2._SEED_URL\":\"_SEED_URL\"},{\"data2.title\":\"title\"},{\"data2.dt\":\"dt\"},{\"data2.content\":\"content\"}],\"data_map_constant\":[],\"cls_map\":[]}}', '1315', 'zh-CN', '*/1 * * * *', '2018-12-20 16:27:13', 'OFF', '', '30', '', '0', '2', '', '1', 'http://in.nen.com.cn/ssjj/index.shtml', NULL, '163', '163', NULL, NULL, NULL, NULL, NULL, '1');"
        flag1 = mysql.update(sql1)  # 先删除历史任务
        self.assertEqual(1, flag1, msg="删除历史任务失败")
        time.sleep(2)
        flag2 = mysql.update(sql2)  # 插入新任务
        self.assertEqual(1, flag2, msg="插入新任务失败")
        one_browser_window()
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        self.loginpage.find_element(Taskherf_loc).click()
        task_name = self.taskpage.get_first_taskname()
        self.assertEqual("脚本使用任务_常规采集", str(task_name), msg="任务名称获取有误")
        self.taskpage.click_first_effectivebtn()
        time.sleep(1)
        self.taskpage.click_confirmbtn()
        time.sleep(1)
        iseff = self.taskpage.find_element(self.taskpage.first_iseff_loc).text
        self.assertEqual("已生效", str(iseff), msg="生效按钮校验失败")
        time.sleep(220)
        self.taskpage.click_first_exec_historybtn()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        tasks = self.datapage.get_first_tasks()
        logger.info("执行历史任务抓取条数：{}".format(tasks))
        self.assertEqual("30", str(tasks), msg="执行历史按钮抓取数据异常")
        self.loginpage.find_element(Taskherf_loc).click()
        self.taskpage.click_first_effectivebtn()
        time.sleep(1)
        self.taskpage.click_confirmbtn()
        time.sleep(1)
        iseff = self.taskpage.find_element(self.taskpage.first_iseff_loc).text
        self.assertEqual("未生效", str(iseff), msg="失效按钮校验失败")
        self.taskpage.click_first_deletebtn()
        time.sleep(1)
        self.taskpage.click_confirmbtn1()
        time.sleep(2)
        sql3 = "select * from task_info where uid = 163 and task_name = '脚本使用任务_常规采集' and taskstatus != 'DELETE';"
        task_name = mysql.select_all(sql3)  # 查询任务是否删除
        self.assertEqual('()', str(task_name), msg="删除按钮校验失败")
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_task_002(self):
        """任务界面【复制/测试/修改/删除】按钮有效性验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        sql1 = "delete from task_info where uid = 163 and (task_name = '脚本使用任务_常规采集' or task_name = '脚本使用任务_常规采集_copy');"
        sql2 = "INSERT INTO `task_info` (`uid`, `task_name`, `task_config`, `category`, `lang`, `period_cron`, `dt`, `taskstatus`, `notifycls`, `time_break`, `cookie`, `is_agent`, `agent_type`, `agent_value`, `spider_type`, `url`, `spider_status`, `create_uid`, `update_uid`, `trigger_condition`, `warn_grade`, `warn_status`, `mid`, `modelkeywords`, `task_type`) VALUES ('163', '脚本使用任务_常规采集', '{\"max_step\":2,\"spider_type\":1,\"keywords\":[],\"recursion_count\":1,\"recursion_field\":\"\",\"config\":[{\"step_id\":\"data1\",\"step_name\":\"data1\",\"data_name\":\"data1\",\"url\":\"http://in.nen.com.cn/ssjj/index.shtml\",\"rule_id\":\"920\",\"rule_mark\":\"\",\"time_out\":\"5000\",\"rule_type\":1,\"detail_rule_type\":2,\"delete\":false,\"wait\":0,\"filter\":\"url\",\"filter_con\":1,\"filter_type\":false,\"step_col\":\"url\",\"page_num\":0,\"check\":true,\"rend\":true,\"rendrule\":false},{\"step_id\":\"data2\",\"step_name\":\"data2\",\"data_name\":\"data2\",\"url\":\"url\",\"rule_id\":\"919\",\"rule_mark\":\"\",\"time_out\":\"5000\",\"rule_type\":2,\"detail_rule_type\":2,\"delete\":false,\"wait\":0,\"step_col\":\"\",\"page_num\":0,\"filter\":\"\",\"filter_con\":1,\"filter_type\":false,\"check\":true,\"sample_url\":\"http://in.nen.com.cn/system/2018/03/23/020430991.shtml\",\"rend\":true,\"rendrule\":false,\"moving\":false}],\"loginform\":{\"formtype\":\"FORM\",\"submittype\":\"POST\",\"url\":\"http://\",\"body\":true,\"header\":true,\"bodys\":[],\"headers\":[]},\"notify\":{\"notify\":false,\"notify_url\":\"\",\"cls_type\":\"\",\"cls_field\":\"\",\"tag_type\":\"0\",\"tag\":\"\",\"data_map\":[{\"data1._SEED_URL\":\"_SEED_URL\"},{\"data1.title\":\"title\"},{\"data1.url\":\"url\"},{\"data2._SEED_URL\":\"_SEED_URL\"},{\"data2.title\":\"title\"},{\"data2.dt\":\"dt\"},{\"data2.content\":\"content\"}],\"data_map_constant\":[],\"cls_map\":[]}}', '1315', 'zh-CN', '*/1 * * * *', '2018-12-20 16:27:13', 'OFF', '', '30', '', '0', '2', '', '1', 'http://in.nen.com.cn/ssjj/index.shtml', NULL, '163', '163', NULL, NULL, NULL, NULL, NULL, '1');"
        flag1 = mysql.update(sql1)  # 先删除历史任务
        self.assertEqual(1, flag1, msg="删除历史任务失败")
        time.sleep(2)
        flag2 = mysql.update(sql2)  # 插入新任务
        self.assertEqual(1, flag2, msg="插入新任务失败")
        one_browser_window()
        self.loginpage.open_login()
        self.loginpage.login('18201112814', 'gzx123456', 'A1b8S')
        self.loginpage.take_screenshot()
        self.loginpage.find_element(Taskherf_loc).click()
        task_name1 = self.taskpage.get_first_taskname()
        self.assertEqual("脚本使用任务_常规采集", str(task_name1), msg="任务名称获取有误")
        self.taskpage.click_first_copybtn()
        time.sleep(5)
        self.addtask.input_taskname("脚本使用任务_常规采集_copy")
        self.addtask.click_savecnfbtn()
        time.sleep(1)
        self.addtask.click_confirmbtn()
        time.sleep(2)
        self.addtask.click_backlistbtn()
        time.sleep(3)
        self.taskpage.get_first_taskname()
        task_name2 = self.taskpage.get_first_taskname()
        self.assertEqual("脚本使用任务_常规采集_copy", str(task_name2), msg="复制按钮校验失败")
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
