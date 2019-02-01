# -*- coding: utf-8 -*-
import time

import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from common.my_logger import logger
from framework.base_page import BasePage
from framework.caiyun.extension_page import ExtensionPage
from framework.caiyun.login_page import LoginPage
from framework.caiyun.other_elements import Rule_index_url, Rule_add_url, Ruleherf_loc, Taskherf_loc


# 采集规则列表页实现类
from framework.caiyun.task_page import TaskIndexPage, TaskAddPage


class RuleIndexPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    pagetitle = '采云 - 采集规则'
    add_rule_loc = '//*[@id="contentheight"]/div/div[1]/div[3]/div[2]/span[2]/a'
    next_page_loc = '//*[@id="contentheight"]/div/div[3]/div[1]/a[7]'
    closebtn_loc = '/html/body/div[1]/section/div/div[2]/div/div[1]/a'
    result_loc = '/html/body/div[1]/section/div/div[2]/div/div[1]/p/span'
    errinfo_loc = '/html/body/div[1]/section/div/div[2]/div/div[2]'
    title_text_loc = '/html/body/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div[1]'
    content_text_loc = '/html/body/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div[2]'
    input_loc = '//*[@id="contentheight"]/div/div[3]/div[2]/input'
    confirmbtn_loc = '//*[@id="contentheight"]/div/div[3]/div[2]/button'

    # 调用base_page中的_open打开链接
    def open(self):
        self._open(Rule_index_url)

    def add_rule(self):
        self.find_element(self.add_rule_loc).click()

    def next_page(self, num):
        el = self.find_element(self.input_loc)
        self.send_keys(el, num)
        self.click_element(self.confirmbtn_loc)

    def get_result(self, count_num):
        break_flag = False
        n = count_num//10 +1
        m = count_num%10 +1
        for i in range(1, n):
            for index in range(1, 11):
                if i == n-1 and index == m:
                    break_flag = True
                    break
                rule_name_loc = '//*[@id="contentheight"]/div/table/tbody/tr[{}]/td[2]/span'.format(index)
                testbtn_loc = '//*[@id="contentheight"]/div/table/tbody/tr[{}]/td[10]/a[4]'.format(index)
                type_loc = '//*[@id="contentheight"]/div/table/tbody/tr[{}]/td[3]/span'.format(index)
                rule_name = self.find_element(rule_name_loc).text
                type = self.find_element(type_loc).text
                time.sleep(1)
                self.click_element(testbtn_loc)
                time.sleep(20)
                if type == '列表页':
                    result = self.find_element(self.result_loc).text

                    if result == '共0条数据':
                        errinfo = self.find_element(self.errinfo_loc).text
                        logger.error("规则名称:(第{}页第{}个){},{},#{}".format(i, index, rule_name, result, errinfo))
                    else:
                        logger.info("规则名称:(第{}页第{}个){},{}".format(i, index, rule_name, result))
                    time.sleep(2)
                elif type == '正文页':
                    try:
                        title_text = self.find_element(self.title_text_loc).text
                        content_text = self.find_element(self.content_text_loc).text
                        time.sleep(2)
                        logger.info("规则名称:(第{}页第{}个){},title:{};content:{}".format(i, index, rule_name, title_text,
                                                                                   content_text))
                    except:
                        logger.error("规则名称:(第{}页第{}个)页面数据获取有误".format(i, index, rule_name))
                else:
                    logger.error('所属类型有误')

                self.take_screenshot()
                self.click_element(self.closebtn_loc)
            if break_flag:
                break
            time.sleep(1)
            # self..click_element(next_page_loc)
            self.next_page(i + 1)


# 添加采集规则页实现类
class RuleAddPage(BasePage):
    pagetitle = '采云 - 添加规则'
    rulename_loc = '//*[@id="form"]/div/div/div[1]/div/span[2]/input'  # 配置名称输入框
    rulecategory_loc = '//*[@id="form"]/div/div/div[2]/div[1]/span[2]'  # 规则分类
    select_category1_loc = '//*[@id="tree"]/div/ul/li/div/ul/li[3]/div/div/span'  # 选择规则_常规采集
    select_category2_loc = ''
    rule_type1_loc = '//*[@id="form"]/div/div/div[2]/div[2]/div/div/div[1]'  # 页面类型_列表页
    rule_type2_loc = '//*[@id="form"]/div/div/div[2]/div[2]/div/div/div[2]'  # 页面类型_正文页
    pageurl_loc = '//*[@id="form"]/div/div/div[3]/span[2]/input'  # 页面URL输入框
    url_pattern_loc = '//*[@id="form"]/div/div/div[4]/span[2]/textarea'  # URL模板输入框
    rulemark_loc= '//*[@id="form"]/div/div/div[5]/span[2]/input'  # 模板标识输入框
    extract_method1_loc = '//*[@id="form"]/div/div/div[6]/div[1]/div/div/div[1]'  # 配置类型_可视化点选
    extract_method2_loc = '//*[@id="form"]/div/div/div[6]/div[1]/div/div/div[2]'  # 配置类型_自定义点选
    cconfbtn_loc = '//*[@id="form"]/div/div/div[12]/span[2]/div/a[1]'  # 进入点选配置按钮
    savecnewrulebtn_loc = '//*[@id="form"]/div/div/div[12]/span[2]/div/a[2]'  # 保存并创建新规则按钮
    saverulebtn_loc = '//*[@id="form"]/div/div/div[12]/span[2]/div/a[3]'  # 保存按钮
    returnbtn_loc = '//*[@id="form"]/div/div/div[12]/span[2]/div/a[4]'  # 返回按钮

    # 调用base_page中的_open打开链接
    def open(self):
        self._open(Rule_add_url)

    def input_rulename(self, rulename):
        el = self.find_element(self.rulename_loc)
        self.send_keys(el, rulename)

    def click_rulecategory(self):
        self.find_element(self.rulecategory_loc).click()

    def click_select_category(self, category):  # category1：选择规则_常规采集；category2：
        if category == 'category1':
            self.find_element(self.select_category1_loc).click()
        else:
            logger.error('[{}]未找到指定规则分类:{}'.format(os.path.basename(__file__), category))
            raise NoSuchElementException(msg='[{}]未找到指定规则:{}'.format(os.path.basename(__file__), category))

    def select_rule_type(self, rule_type):  # type1：页面类型_列表页；type2：页面类型_正文页
        if rule_type == 'type1':
            self.find_element(self.rule_type1_loc).click()
        elif rule_type== 'type2':
            self.find_element(self.rule_type2_loc).click()
        else:
            logger.error('[{}]未找到指定页面类型:{}'.format(os.path.basename(__file__), rule_type))
            raise NoSuchElementException(msg='[{}]未找到指定页面类型:{}'.format(os.path.basename(__file__), rule_type))

    def input_pageurl(self, pageurl):
        el = self.find_element(self.pageurl_loc)
        self.send_keys(el, pageurl)

    def input_url_pattern(self, url_pattern):
        el = self.find_element(self.url_pattern_loc)
        self.send_keys(el, url_pattern)

    def input_rulemark(self, rulemark):
        el = self.find_element(self.rulemark_loc)
        self.send_keys(el, rulemark)

    def select_extract_method(self, extract_method):  # method1:配置类型_可视化点选;method2:配置类型_自定义点选
        if extract_method =='method1':
            self.find_element(self.extract_method1_loc).click()
        elif extract_method =='method2':
            self.find_element(self.extract_method2_loc).click()
        else:
            logger.error('[{}]未找到指定配置类型:{}'.format(os.path.basename(__file__), extract_method))
            raise NoSuchElementException(msg='[{}]未找到指定配置类型:{}'.format(os.path.basename(__file__), extract_method))

    def click_cconfbtn(self):
        self.find_element(self.cconfbtn_loc).click()

    # 进入点选配置方法
    def click_enter_piontconf(self, rulename, select_category, rule_type, pageurl, url_pattern,
                              rulemark, extract_method):
        self.input_rulename(rulename)
        self.click_rulecategory()
        self.click_select_category(select_category)
        self.select_rule_type(rule_type)
        self.input_pageurl(pageurl)
        self.input_url_pattern(url_pattern)
        self.input_rulemark(rulemark)
        self.select_extract_method(extract_method)
        time.sleep(1)
        self.click_cconfbtn()
        time.sleep(3)

    def click_saverulebtn(self):
        time.sleep(1)
        self.find_element(self.saverulebtn_loc).click()

    def click_savecnewrulebtn(self):
        time.sleep(1)
        self.find_element(self.savecnewrulebtn_loc).click()


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
#     loginpage.find_element(Ruleherf_loc).click()
#     rulepage = RuleIndexPage(driver)
#     rulepage.add_rule()
#     time.sleep(5)
#     handles = driver.window_handles  # 获取所有打开窗口的句柄
#     driver.switch_to.window(handles[1])
#     addrule = RuleAddPage(driver)
#     rulename1 = '新建规则_列表页'
#     select_category1 = 'category1'
#     rule_type1 = 'type1'
#     pageurl1 = 'http://in.nen.com.cn/ssjj/index.shtml'
#     url_pattern1 = 'http://in.nen.com.cn*'
#     rulemark1 = 'test_list'
#     extract_method1 = 'method1'
#     addrule.click_enter_piontconf(rulename1, select_category1, rule_type1, pageurl1, url_pattern1,
#                                   rulemark1, extract_method1)
#     time.sleep(5)
#     handles = driver.window_handles
#     driver.switch_to.window(handles[2])
#     extensionpage = ExtensionPage(driver)
#     extensionpage.add_dongbeinews_listrule()
#     addrule.click_savecnewrulebtn()
#     time.sleep(5)
#     rulename2 = '新建规则_正文页'
#     select_category2 = 'category1'
#     rule_type2 = 'type2'
#     pageurl2 = 'http://in.nen.com.cn/system/2018/03/23/020430991.shtml'
#     url_pattern2 = 'http://in.nen.com.cn*'
#     rulemark2 = 'test_text'
#     extract_method2 = 'method1'
#     addrule.click_enter_piontconf(rulename2, select_category2, rule_type2, pageurl2, url_pattern2,
#                                   rulemark2, extract_method2)
#     time.sleep(5)
#     handles = driver.window_handles
#     driver.switch_to.window(handles[3])
#
#     extensionpage.add_dongbeinews_textrule()
#     addrule.click_saverulebtn()