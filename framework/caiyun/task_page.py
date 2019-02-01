# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver
from common.my_logger import logger
from framework.base_page import BasePage
from framework.caiyun.login_page import LoginPage
from framework.caiyun.other_elements import Taskherf_loc, Task_url


class TaskIndexPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    pagetitle = '采云 - 我的采集'
    add_task_loc = '//*[@id="contentheight"]/div/div/div[3]/div[3]/span[2]/a'  # 创建采集
    first_effectivebtn_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[9]/a[1]'  # 生效按钮
    first_iseff_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr/td[4]/span'  # 是否生效
    first_testbtn_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[9]/a[2]'  # 测试按钮
    first_exec_historybtn_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[9]/a[3]'  # 执行历史按钮
    first_modifybtn_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[9]/a[4]'  # 修改按钮
    first_copybtn_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[9]/a[5]'  # 复制按钮
    first_deletebtn_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[9]/a[6]'  # 删除按钮
    confirmbtn_loc = '//*[@id="layui-layer100001"]/div[3]/a[1]'  # 确认按钮
    first_collname_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[2]'  # 采集名称
    first_result_loc = '/html/body/div[1]/section/div/div[3]/div/div[1]/p/span[1]' # 弹窗测试结果
    first_close_loc = '/html/body/div[1]/section/div/div[3]/div/div[1]/a'  # 弹窗关闭按钮
    first_schedul_loc = '//*[@id="contentheight"]/div/div/table/tbody/tr[1]/td[6]'  # 调度
    confirmbtn1_loc = '//*[@id="layui-layer3"]/div[3]/a[1]'  # 确认删除任务

    # 调用base_page中的_open打开链接
    def open(self):
        self._open(Task_url)

    def add_task(self):
        self.find_element(self.add_task_loc).click()

    def click_first_effectivebtn(self):
        self.click_element(self.first_effectivebtn_loc)

    def click_first_testbtn(self):
        self.click_element(self.first_testbtn_loc)

    def click_first_exec_historybtn(self):
        self.click_element(self.first_exec_historybtn_loc)

    def click_first_modifybtn(self):
        self.click_element(self.first_modifybtn_loc)

    def click_first_copybtn(self):
        self.click_element(self.first_copybtn_loc)

    def click_first_deletebtn(self):
        self.click_element(self.first_deletebtn_loc)

    def click_confirmbtn(self):
        self.click_element(self.confirmbtn_loc)

    def click_confirmbtn1(self):
        self.click_element(self.confirmbtn1_loc)

    def get_first_taskname(self):
        task_name = self.find_element(self.first_collname_loc).text
        return task_name

    def get_firstresult(self):
        tasks = self.find_element(self.first_result_loc).text
        return tasks

    def get_first_schedul(self):
        tasks = self.find_element(self.first_schedul_loc).text
        return tasks

    def click_first_close(self):
        self.click_element(self.first_close_loc)

# 添加任务页实现类
class TaskAddPage(BasePage):
    pagetitle = '采云 - 编辑采集'
    taskname_loc = '/html/body/div[1]/section/div/div[2]/div[1]/div[1]/span[2]/input'  # 采集名称输入框
    taskcategory_loc = '/html/body/div[1]/section/div/div[2]/div[1]/div[2]/span[2]/div[1]/p'  # 数据分类
    select_category1_loc = '//*[@id="tree"]/div/ul/li/div/ul/li[3]/div/div/span'  # 数据分类_常规采集
    select_category2_loc = '//*[@id="tree"]/div/ul/li/div/ul/li[1]/div/div/span'  # 数据分类_微信采集
    select_category3_loc = '//*[@id="tree"]/div/ul/li/div/ul/li[2]/div/div/span'  # 数据分类_微博采集
    select_category4_loc = '//*[@id="tree"]/div/ul/li/div/ul/li[4]/div/div/span'  # 数据分类_递归采集
    tasktype_loc = '/html/body/div[1]/section/div/div[2]/div[2]/div[1]/span[2]/select'  # 任务类型下拉选择(调度任务，触发任务)
    cron_loc = '/html/body/div[1]/section/div/div[2]/div[2]/div[2]/span[2]/div/div[1]/input'  # 采集周期输入框
    timebreak_loc = '/html/body/div[1]/section/div/div[2]/div[2]/div[3]/span[2]/input'  # 每次请求间隔输入框
    isagent_loc = '/html/body/div[1]/section/div/div[2]/div[2]/div[4]/span[2]/select'  # 是否使用代理下拉选择(是，否)
    moreconfigbtn_loc = '/html/body/div[1]/section/div/div[2]/div[2]/div[5]/a'  # 更多配置按钮
    piderstype1_loc = '/html/body/div[1]/section/div/div[3]/div[1]/div[1]/h5'  # 常规采集
    piderstype4_loc = '/html/body/div[1]/section/div/div[3]/div[1]/div[2]/h5'  # 递归采集
    piderstype2_loc = '/html/body/div[1]/section/div/div[3]/div[1]/div[3]/h5'  # 微信采集
    piderstype3_loc = '/html/body/div[1]/section/div/div[3]/div[1]/div[4]/h5'  # 微博采集
    public_collection_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]'  # 公众号采集
    wxsearch_collection_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]'  # 微信搜索采集
    addbatchwxnumberbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/a[3]'  # 批量添加公众号
    addsearchwxnumberbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/a[1]'  # 搜索添加公众号
    wxkeyword_loc = '//*[@id="addwx"]/div/div[2]/div[1]/span[1]/input[1]'  # 请输入公众号或微信号
    searchbtn_loc = '//*[@id="addwx"]/div/div[2]/div[1]/span[2]/a'  # 搜索按钮
    addbtn = '//*[@id="addwx"]/div/div[2]/div[2]/table/tbody/tr[2]/td[4]/a'  # 添加按钮
    closebtn = '//*[@id="addwx"]/div/div[1]/a'  # 关闭按钮
    wbnumber_collection_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[1]'  # 微博号采集
    wbsearch_collection_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[2]'  # 微博搜索采集
    addbatchwbnumberbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/a[4]'  # 批次添加微博账号
    addsearchwbnumberbtn_loc = '//html/body/div[1]/section/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/a[2]'  # 搜索添加微博账号
    wbkeyword_loc = '//*[@id="addwx"]/div/div[2]/div[1]/span[1]/input[2]'  # 请输入微博号或微博名称

    listcollec_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[1]'  # 列表页采集
    textcollec_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]'  # 正文页采集
    endnotice_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[3]'  # 结束与通知
    add_listcollec_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[4]/div[1]'  # 添加列表采集
    add_textcollec_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[4]/div[2]'  # 添加正文采集
    # 列表页采集:data1
    urllist_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/span[2]/textarea'  # 列表URL
    extractrule_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/select'  # 提取规则
    testrulebtn_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a[1]'  # 测试规则
    editrulebtn_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a[2]'  # 编辑规则
    addnewrulebtn_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a[3]'  # 添加新规则
    refreshbtn_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a[4]'  # 刷新
    double_check1_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[4]/span[2]/select[1]'  # 去重检查1
    double_check2_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[4]/span[2]/select[2]'  # 去重检查2
    turn_pagec_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[5]/span[2]/input'  # 翻页循环
    opentimeout_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[6]/span[2]/select'  # 打开超时
    waittime_list_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[7]/span[2]/select'  # 等待时间
    # 正文页采集:data2
    sampleurl_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/span[2]/textarea' # 样例URL
    extracttype1_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/div[1]'  # 正文提取_智能提取
    extracttype2_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/div[2]'  # 正文提取_固定规则
    extractrule_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/select'  # 提取规则
    turn_pagec_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[4]/span[2]/input'  # 翻页循环
    opentimeout_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[5]/span[2]/select'  # 打开超时
    waittime_text_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[6]/span[2]/select'  # 等待时间
    # 常规采集按钮
    savecnfbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[4]/a[1]/span'  # 保存配置
    testcollecbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[4]/a[2]'  # 测试采集
    effectivenowbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[4]/a[3]'  # 立即生效
    backlistbtn_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[4]/a[5]'  # 返回列表
    confirmbtn_loc = '//*[@id="layui-layer100001"]/div[3]/a[1]'  # 确认按钮
    # 微信微博按钮
    savecnfbtn1_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[3]/a[1]/span'  # 保存配置
    testcollecbtn1_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[3]/a[2]'  # 测试采集
    effectivenowbtn1_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[3]/a[3]'  # 立即生效
    backlistbtn1_loc = '/html/body/div[1]/section/div/div[3]/div[2]/div[3]/a[4]'  # 返回列表

    def input_taskname(self, taskname):
        el = self.find_element(self.taskname_loc)
        self.send_keys(el, taskname)

    def click_select_category(self, category):  # category1：常规；category2：微信；category3：微博；category4：递归
        if category == 'category1':
            self.find_element(self.select_category1_loc).click()
        elif category == 'category2':
            self.find_element(self.select_category2_loc).click()
        elif category == 'category3':
            self.find_element(self.select_category3_loc).click()
        elif category == 'category4':
            self.find_element(self.select_category4_loc).click()
        else:
            logger.error("未找到指定规则分类")

    def input_cron(self, cron):
        el = self.find_element(self.cron_loc)
        self.send_keys(el, cron)

    def input_timebreak(self, timebreak_loc):
        el = self.find_element(self.timebreak_loc)
        self.send_keys(el, timebreak_loc)

    def input_listurl_list(self, urllist_list):
        el = self.find_element(self.urllist_list_loc)
        self.send_keys(el, urllist_list)

    def input_turn_pagec_list(self, turn_pagec_list):
        el = self.find_element(self.turn_pagec_list_loc)
        self.send_keys(el, turn_pagec_list)

    def input_turn_pagec_text(self, turn_pagec_text):
        el = self.find_element(self.turn_pagec_text_loc)
        self.send_keys(el, turn_pagec_text)

    def input_sampleurl_text(self, sampleurl_text):
        el = self.find_element(self.sampleurl_text_loc)
        self.send_keys(el, sampleurl_text)

    def input_wxkeyword(self, wxkeyword):
        el = self.find_element(self.wxkeyword_loc)
        self.send_keys(el, wxkeyword)

    def input_wbkeyword(self, wbkeyword):
        el = self.find_element(self.wbkeyword_loc)
        self.send_keys(el, wbkeyword)

    def collect_init(self, taskname, taskcategory, tasktype, cron, timebreak_loc, isagent):
        self.input_taskname(taskname)
        self.click_element(self.taskcategory_loc)
        self.click_select_category(taskcategory)
        self.select_element(self.tasktype_loc, tasktype)
        self.input_cron(cron)
        self.input_timebreak(timebreak_loc)
        self.select_element(self.isagent_loc, isagent)

    # 新建常规采集任务
    def new_regular_collection(self, urllist_lis, select_extractrule_list, check1_list, check2_list,
                               turnpagec_list, opentimeout_list, waittime_list, sampleurl_text,
                               selcet_extractrule_text, turnpagec_text, opentimeout_text, waittime_text):
        self.click_element(self.piderstype1_loc)
        self.click_element(self.listcollec_loc)
        self.input_listurl_list(urllist_lis)
        time.sleep(1)  # 加载提取规则
        try:
            self.leftclick(self.extractrule_list_loc)
            time.sleep(6)
            self.select_element(self.extractrule_list_loc, select_extractrule_list)
        except:
            logger.error("[{}]提取规则加载失败".format(os.path.basename(__file__)))
            time.sleep(1)
            self.leftclick(self.extractrule_list_loc)
            time.sleep(6)
            self.select_element(self.extractrule_list_loc, select_extractrule_list)
        time.sleep(1)
        self.select_element(self.double_check1_list_loc, check1_list)
        self.select_element(self.double_check2_list_loc, check2_list)
        self.input_turn_pagec_list(turnpagec_list)
        self.select_element(self.opentimeout_list_loc, opentimeout_list)
        self.select_element(self.waittime_list_loc, waittime_list)

        self.click_element(self.textcollec_loc)
        self.input_sampleurl_text(sampleurl_text)
        self.click_element(self.extracttype2_text_loc)
        time.sleep(1)  # 加载提取规则
        try:
            self.leftclick(self.extractrule_text_loc)
            time.sleep(6)
            self.select_element(self.extractrule_text_loc, selcet_extractrule_text)
        except:
            logger.error("[{}]提取规则加载失败".format(os.path.basename(__file__)))
            time.sleep(1)
            self.leftclick(self.extractrule_text_loc)
            time.sleep(6)
            self.select_element(self.extractrule_text_loc, select_extractrule_list)
        time.sleep(1)
        self.input_turn_pagec_text(turnpagec_text)
        self.select_element(self.opentimeout_text_loc, opentimeout_text)
        self.select_element(self.waittime_text_loc, waittime_text)

    # 新建微信采集
    def new_wechat_collection(self, wxkeyword ):
        self.click_element(self.piderstype2_loc)
        self.click_element(self.public_collection_loc)
        self.click_element(self.addsearchwxnumberbtn_loc)
        self.input_wxkeyword(wxkeyword)
        self.click_element(self.searchbtn_loc)
        time.sleep(8)
        self.click_element(self.addbtn)
        self.click_element(self.closebtn)

    # 新建微博采集
    def new_weibo_collection(self, wbkeyword ):
        self.click_element(self.piderstype3_loc)
        self.click_element(self.wbnumber_collection_loc)
        self.click_element(self.addsearchwbnumberbtn_loc)
        self.input_wbkeyword(wbkeyword)
        self.click_element(self.searchbtn_loc)
        time.sleep(8)
        self.click_element(self.addbtn)
        self.click_element(self.closebtn)

    def click_savecnfbtn(self):
        time.sleep(1)
        self.click_element(self.savecnfbtn_loc)
        time.sleep(1)

    def click_testcollecbtn(self):
        self.click_element(self.testcollecbtn_loc)

    def click_effectivenowbtn(self):
        self.click_element(self.effectivenowbtn_loc)

    def click_backlistbtn(self):
        self.click_element(self.backlistbtn_loc)

    def click_confirmbtn(self):
        self.click_element(self.confirmbtn_loc)

    def click_savecnfbtn1(self):
        self.click_element(self.savecnfbtn1_loc)

    def click_testcollecbtn1(self):
        self.click_element(self.testcollecbtn1_loc)

    def click_effectivenowbtn1(self):
        self.click_element(self.effectivenowbtn1_loc)

    def click_backlistbtn1(self):
        self.click_element(self.backlistbtn1_loc)


# if __name__ == '__main__':
#     chrome_options = webdriver.ChromeOptions()
#     # 设置好应用扩展
#     extension_path = r'E:\jiuqi_python\python_selenium\tools\chromeextend.crx'
#     chrome_options.add_extension(extension_path)
#     # 加上下面两行，解决报错
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
#     chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
#     driver = webdriver.Chrome(options=chrome_options)  # executable_path驱动路径
#     loginpage = LoginPage(driver)
#     loginpage.open_login()
#     loginpage.login('18201112814', 'gzx123456', 'A1b8S')
#     # driver.close()
#     # time.sleep(5)
#     handles = driver.window_handles
#     driver.switch_to.window(handles[0])
#     loginpage.find_element(Taskherf_loc).click()
#     taskpage = TaskIndexPage(driver)
#     taskpage.add_task()
#     time.sleep(2)
#     handles = driver.window_handles
#     driver.switch_to.window(handles[1])
#     addtask = TaskAddPage(driver)
#
#     taskname = '新建任务_{}'.format(time.time())
#     taskcategory = 'category1'
#     tasktype = '调度任务'
#     cron = '*/1 * * * *'
#     timebreak_loc = '30'
#     isagent = '否'
#     addtask.collect_init(taskname, taskcategory, tasktype, cron, timebreak_loc, isagent)
#     urllist_lis = 'http://in.nen.com.cn/ssjj/index.shtml'
#     select_extractrule_list = "新建规则_列表页"
#     check1_list = '不检查'
#     check2_list = ''
#     turnpagec_list = '0'
#     opentimeout_list = '5秒'
#     waittime_list = '不等待'
#     sampleurl_text = 'http://in.nen.com.cn/system/2018/03/23/020430991.shtml'
#     selcet_extractrule_text = "新建规则_正文页"
#     turnpagec_text = '0'
#     opentimeout_text = '5秒'
#     waittime_text = '不等待'
#     addtask.new_regular_collection(urllist_lis, select_extractrule_list, check1_list, check2_list,
#                                    turnpagec_list, opentimeout_list, waittime_list, sampleurl_text,
#                                selcet_extractrule_text, turnpagec_text, opentimeout_text, waittime_text)
#
#     addtask.click_savecnfbtn()
#     addtask.click_confirmbtn()
#     addtask.click_effectivenowbtn()
