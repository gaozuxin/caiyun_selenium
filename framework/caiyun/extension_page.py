# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from framework.base_page import BasePage


# 采云助手页面实现类
class ExtensionPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    stop_pointbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[1]/a[1]'  # 停止点选按钮
    clear_allconfbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[1]/a[2]'  # 清除所有配置按钮
    select_similarelbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[2]/div/a[contains(text(), "选择同类元素")]'  # 选择同类元素按钮
    extract_textbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[2]/div/a[contains(text(), "提取文本")]'  # 提取文本按钮
    fieldname_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/input'  # 字段名称
    field1_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/select'  # 提取属性
    field2_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[3]/select'  # 提取属性
    field3_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[4]/select'  # 提取属性
    confirm1_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[5]/a'  # 确认按钮
    confirm2_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[2]/a'  # 翻页确认按钮
    extract_attributebtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[2]/div/a[contains(text(), "提取属性")]'  # 提取属性按钮
    set_pageturnbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[2]/div/a[contains(text(), "设置翻页")]'  # 设置翻页按钮
    pageturn_type1_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[1]/div/select'  # 翻页类型1
    pageturn_type2_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/select'  # 翻页类型2
    application_csspathbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[3]/a[1]'  # 应用css路径按钮
    el_csspath_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[3]/textarea'  # css路径输入框
    select_superiorelbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[2]/div[3]/a[2]'  # 选择上级元素按钮
    AJAXload_loc = '//*[@id="caiyunextend"]/div[1]/div[3]/div/span'  # AJAX异步加载
    test_rulebtn_loc = '//*[@id="caiyunextend"]/div[1]/div[3]/a[3]'  # 测试规则按钮
    save_rulebtn_loc = '//*[@id="caiyunextend"]/div[1]/div[3]/a[2]'  # 保存规则按钮
    cancelbtn_loc = '//*[@id="caiyunextend"]/div[1]/div[3]/a[1]'  # 撤消保存规则按钮

    def click_stop_pointbtn(self):
        self.find_element(self.stop_pointbtn_loc).click()

    def click_clear_allconfbtn(self):
        self.find_element(self.clear_allconfbtn_loc).click()

    def click_select_similarelbtn(self):
        self.find_element(self.select_similarelbtn_loc).click()

    def click_extract_textbtn(self):
        self.find_element(self.extract_textbtn_loc).click()

    def input_fieldname(self, fieldname):
        el = self.find_element(self.fieldname_loc)
        self.send_keys(el, fieldname)

    def click_extract_attributebtn(self):
        self.find_element(self.extract_attributebtn_loc).click()

    def click_set_pageturnbtn(self):
        self.find_element(self.set_pageturnbtn_loc).click()

    def click_application_csspathbtn(self):
        self.find_element(self.application_csspathbtn_loc).click()

    def input_el_csspath(self, el_csspath):
        el = self.find_element(self.el_csspath_loc)
        self.send_keys(el, el_csspath)

    def click_select_superiorelbtn(self):
        self.find_element(self.select_superiorelbtn_loc).click()

    def click_AJAXload(self):
        self.find_element(self.AJAXload_loc).click()

    def click_test_rulebtn(self):
        self.find_element(self.test_rulebtn_loc).click()

    def click_save_rulebtn(self):
        time.sleep(1)
        self.find_element(self.save_rulebtn_loc).click()
        time.sleep(1)

    def click_cancelbtn(self):
        self.find_element(self.cancelbtn_loc).click()

    def click_confirm1(self):
        self.find_element(self.confirm1_loc).click()

    def click_confirm2(self):
        self.find_element(self.confirm2_loc).click()

    # 提取文本方法
    def extract_text(self, text_xpath, fieldname, field1_text, field2_text, field3_text):
        self.click_extract_textbtn()
        self.leftclick(text_xpath)
        self.input_fieldname(fieldname)
        self.select_element(self.field1_loc, field1_text)
        self.select_element(self.field2_loc, field2_text)
        self.select_element(self.field3_loc, field3_text)
        self.click_confirm1()
        # if field3_text == '正则':
        #     pass
        # else:
        #     pass

    # 提取属性方法
    def extract_attribute(self, attribute_xpath, attributename, field1_attribute, field2_attribute, field3_attribute):
        self.click_extract_attributebtn()
        self.leftclick(attribute_xpath)
        self.input_fieldname(attributename)
        self.select_element(self.field1_loc, field1_attribute)
        self.select_element(self.field2_loc, field2_attribute)
        self.select_element(self.field3_loc, field3_attribute)
        self.click_confirm1()

    def extract_url(self):
        pass

    def add_dongbeinews_listrule(self):
        select_news_area = '/html/body/div[6]/div/div[1]/div[1]/ul'
        select_news_title = '/html/body/div[6]/div/div[1]/div[1]/ul/li[1]/a'
        self.leftclick(select_news_area)
        self.input_el_csspath('UL.list.dotB>LI')
        self.click_application_csspathbtn()
        self.click_select_similarelbtn()
        self.click_extract_textbtn()
        self.leftclick(select_news_title)
        # 东北新闻网页面
        text_xpath = select_news_title
        fieldname = 'title'
        field1_text = '文本'
        field2_text = 'STRING'
        field3_text = '无'
        self.extract_text(text_xpath, fieldname, field1_text, field2_text, field3_text)

        attribute_xpath = select_news_title
        attributename = 'url'
        field1_attribute = 'href'
        field2_attribute = 'URL'
        field3_attribute = '无'
        self.extract_attribute(attribute_xpath, attributename, field1_attribute, field2_attribute,
                                        field3_attribute)
        self.click_save_rulebtn()

    def add_dongbeinews_listrule_ajax(self):
        select_news_area = '/html/body/div[6]/div/div[1]/div[1]/ul'
        select_news_title = '/html/body/div[6]/div/div[1]/div[1]/ul/li[1]/a'
        self.leftclick(select_news_area)
        self.input_el_csspath('UL.list.dotB>LI')
        self.click_application_csspathbtn()
        self.click_select_similarelbtn()
        self.click_extract_textbtn()
        self.leftclick(select_news_title)
        # 东北新闻网页面
        text_xpath = select_news_title
        fieldname = 'title'
        field1_text = '文本'
        field2_text = 'STRING'
        field3_text = '无'
        self.extract_text(text_xpath, fieldname, field1_text, field2_text, field3_text)

        attribute_xpath = select_news_title
        attributename = 'url'
        field1_attribute = 'href'
        field2_attribute = 'URL'
        field3_attribute = '无'
        self.extract_attribute(attribute_xpath, attributename, field1_attribute, field2_attribute,
                                        field3_attribute)

        # nextbtn = '//*[@id="downpage"]'
        self.click_set_pageturnbtn()
        self.leftclick(select_news_title)
        self.select_element(self.pageturn_type1_loc, '点击翻页')
        self.select_element(self.pageturn_type2_loc, '打开新页面')
        self.input_el_csspath('A.next#downpage')
        self.click_application_csspathbtn()
        self.click_confirm2()
        self.click_AJAXload()
        self.click_save_rulebtn()

    def add_dongbeinews_textrule(self):
        select_news_area = '/html/body/div[5]/div'
        select_news_title = '/html/body/div[5]/div/div[2]/h1'
        select_news_dt = '/html/body/div[5]/div/div[2]/div/div[1]'
        select_news_fmedia = '/html/body/div[5]/div/div[2]/div/div[1]'
        select_news_content = '/html/body/div[5]/div/div[3]/div[2]'
        self.leftclick(select_news_area)
        self.input_el_csspath('body > div.content > div')
        self.click_application_csspathbtn()
        self.click_select_similarelbtn()

        self.click_extract_textbtn()
        self.leftclick(select_news_title)
        # 东北新闻网页面
        fieldname_title = 'title'
        field1_title_text = '文本'
        field2_title_text = 'STRING'
        field3_title_text = '无'
        self.extract_text(select_news_title, fieldname_title, field1_title_text, field2_title_text, field3_title_text)

        fieldname_dt = 'dt'
        field1_dt_text = '文本'
        field2_dt_text = 'DATE'
        field3_dt_text = '无'
        self.extract_text(select_news_dt, fieldname_dt, field1_dt_text, field2_dt_text,
                            field3_dt_text)
        # fieldname_fmedia = 'fmedia'
        # field1_fmedia_text = '文本'
        # field2_fmedia_text = 'STRING'
        # field3_fmedia_text = '正则'
        # # 正则需要extract_text函数内特殊处理
        # self.extract_text(select_news_fmedia, fieldname_fmedia, field1_fmedia_text, field2_fmedia_text,
        #                     field3_fmedia_text)

        fieldname_content = 'content'
        field1_content_text = 'INNER_HTML'
        field2_content_text = 'STRING'
        field3_content_text = '无'
        self.extract_text(select_news_content, fieldname_content, field1_content_text, field2_content_text,
                            field3_content_text)
        self.click_save_rulebtn()


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     extensionpage = ExtensionPage(driver)