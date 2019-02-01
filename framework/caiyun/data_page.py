# -*- coding: utf-8 -*-
import time
from selenium import webdriver

from framework.base_page import BasePage
from framework.caiyun.login_page import LoginPage
from framework.caiyun.other_elements import Dataherf_loc, Data_url


class DataPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    pagetitle = '采云 - 我的数据'
    collection_tasks_loc = '//*[@id="contentheight"]/div[2]/div/div[1]/h4'  # 采集任务数(个)
    totalcollected_tasks_loc = '//*[@id="contentheight"]/div[2]/div/div[2]/h4'  # 共采集数据总量(条)
    total_time_loc = '//*[@id="contentheight"]/div[2]/div/div[3]/h4'  # 采集总耗时
    average_time_loc = '//*[@id="contentheight"]/div[2]/div/div[4]/h4'  # 平均耗时(条/秒)
    first_taskid_loc = '//*[@id="contentheight"]/div[3]/div/table/tbody/tr[1]/td[1]'  # 第一条任务ID
    first_tasks_loc = '//*[@id="contentheight"]/div[3]/div/table/tbody/tr/td[5]'  # 第一条最近抓取条数
    see_details_loc = '//*[@id="contentheight"]/div[3]/div/table/tbody/tr/td[7]/a[1]'  # 查看详情按钮
    tasks_loc = '/html/body/div[1]/section/div/div[2]/div/div[1]/h4'  # 数据总量(条)

    def open(self):
        self._open(Data_url)

    def get_first_taskid(self):
        taskid = self.find_element(self.first_taskid_loc).text
        return taskid

    def click_see_details(self):
        self.click_element(self.see_details_loc)

    def get_first_tasks(self):
        tasks = self.find_element(self.tasks_loc).text
        return tasks

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
#     loginpage.find_element(Dataherf_loc).click()
#     datapage =DataPage(driver)
#     print(datapage.get_first_taskid())
#     print(datapage.get_first_tasks())
