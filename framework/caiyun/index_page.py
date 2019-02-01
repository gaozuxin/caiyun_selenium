# -*- coding: utf-8 -*-
from framework.base_page import BasePage
from framework.caiyun.other_elements import Index_url


class IndexPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    pagetitle = '采云 - 概览'
    regular_tasks_loc = '/html/body/div[1]/section/div/div[1]/div[1]/div[1]/h3/a'  # 常规采集任务数
    recursive_tasks_loc = '/html/body/div[1]/section/div/div[1]/div[1]/div[2]/h3/a'  # 递归采集任务数
    execute_tasks_loc = '/html/body/div[1]/section/div/div[1]/div[1]/div[3]/h3/a'  # 正在执行任务数
    wechat_tasks_loc = '/html/body/div[1]/section/div/div[1]/div[1]/div[4]/h3/a'  # 微信公众号采集量
    weibo_task_loc = '/html/body/div[1]/section/div/div[1]/div[1]/div[5]/h3/a'  # 微博公众号采集量
    execution_fail_loc = '/html/body/div[1]/section/div/div[1]/div[1]/div[6]/h3/a'  # 执行失败任务数
    collection_rules_loc = '/html/body/div[1]/section/div/div[1]/div[2]/div[1]/h3/a'  # 采集规则数
    exception_rules_loc = '/html/body/div[1]/section/div/div[1]/div[2]/div[2]/h3/a'  # 异常规则数
    exit_userbtn_loc = '/html/body/nav/div[3]/ul[2]/li[4]/a/span'  # 退出用户按钮
    username_loc = '/html/body/nav/div[3]/ul[2]/li[3]/a/span'  # 登录用户名
    # 调用base_page中的_open打开链接
    def open_login(self):
        self._open(Index_url)

    def click_exit_userbtn(self):
        self.click_element(self.exit_userbtn_loc)

    def get_loginuser(self):
        username = self.find_element(self.username_loc).text
        return username


