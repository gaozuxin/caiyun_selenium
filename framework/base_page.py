# -*- coding: utf-8 -*-
"""
    @desc: object测试基类
    @file: base_page.py
    @date: 2018/11/19
"""
from common.my_logger import logger
from random import choice
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import os
import time

UI_WAIT_TIME = 20


# BasePage封装所有页面都公用的方法，例如driver, url ，FindElement等
class BasePage(object):
    def __init__(self, driver):
        self._driver = driver

    def _open(self, url, page_title=None):
        """
        打开指定网页
        :param page_title: 网页title, 非必填
        :return: 若传入的page_title与网页title不同则触发断言
        """
        # self._driver.maximize_window()
        # self._driver.set_window_size(1920, 1080)
        self._driver.get(url=url)

        # if page_title is not None:
        #     assert page_title in self._driver.title

    def find_element_xpath(self, *loc):
        try:
            WebDriverWait(self._driver, 3).until(lambda driver: driver.find_element_by_xpath(*loc).is_displayed())
            return self._driver.find_element_by_xpath(*loc)
        except(NoSuchElementException, TimeoutException):
            pass
            # self._driver.quit()
            # logger.error('[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))
            # raise TimeoutException(msg='[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))

    # 重写元素定位方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self._driver, 20).until(lambda driver: driver.find_element_by_xpath(*loc).is_displayed())
            return self._driver.find_element_by_xpath(*loc)
        except(NoSuchElementException, TimeoutException):
            # self._driver.quit()
            logger.error('[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))
            raise TimeoutException(msg='[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))

    # 重写定义send_keys方法
    def send_keys(self, el, vaule, clear_first=True, click_first=True):
        try:
            if click_first:
                el.click()
            if clear_first:
                el.clear()
                el.send_keys(vaule)
        except (NoSuchElementException, TimeoutException) as e:
            # NoSuchElementException:
            logger.error("[{}]页面中未能找到元素{}".format(os.path.basename(__file__), e))
            raise NoSuchElementException(msg='[{}]页面中未能找到元素{}'.format(os.path.basename(__file__), e))

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self._driver.switch_to_frame(loc)

    # # 切到iframe
    # def switch_frame(self):
    #     iframe = self.find_element('classname=>embed-responsive-item')
    #     try:
    #         self.driver.switch_to_frame(iframe)
    #         # logger.info("The element \' %s \' was clicked." % iframe.text)
    #     except NameError as e:
    #         logger.error("Failed to click the element with %s" % e)

    # 处理标准下拉选择框,随机选择
    def select_element(self, element_xpath, select_text):
        select1 = self.find_element(element_xpath)
        try:
            Select(select1).select_by_visible_text(select_text)
            logger.info("[{}]选择的元素是:{}".format(os.path.basename(__file__), select_text))
        except(NoSuchElementException, TimeoutException) as e:
            logger.error("[{}]无法选择该元素{}".format(os.path.basename(__file__), e))
            raise NoSuchElementException(msg='[{}]无法选择该元素{}'.format(os.path.basename(__file__), e))

    def click_element(self, element_xpath):
        self.find_element(element_xpath).click()

    # 执行js
    def execute_js(self, js):
        self._driver.execute_script(js)

    # 模拟回车键
    def enter(self, selector):
        e1 = self.find_element(selector)
        e1.send_keys(Keys.ENTER)

    # 模拟鼠标左击
    def leftclick(self, element_xpath):
        e1 = self.find_element(element_xpath)
        ActionChains(self._driver).click(e1).perform()

    # 截图，保存在根目录下的screenshots
    def take_screenshot(self):
        rq = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        try:
            self._driver.get_screenshot_as_file(os.path.dirname(os.path.dirname(__file__))
                                                + '\screenshots\{}.png'.format(rq))
            logger.info("[{}]已截屏并保存{}.png!".format(os.path.basename(__file__), rq))
        except Exception as e:
            logger.error("[{}]无法截屏!{}".format(os.path.basename(__file__), e))

    def is_element_exist(self, xpath):
        flag = True
        driver = self._driver
        try:
            driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag

    # 使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
    def on_page(self, pagetitle):
        return pagetitle in self._driver.title

    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
