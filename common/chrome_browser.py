# -*- coding: utf-8 -*-
import os
from selenium import webdriver


class Chrome_Browser(object):
    def __init__(self, flag):
        self.flag = flag
        self.driver = self.get_driver()

    def get_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # 加上下面两行，解决报错
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1290x1080')  # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        if self.flag:
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        else:
            # 设置应用扩展
            extension_path = os.path.dirname(os.path.dirname(__file__)) + r'\tools\chromeextend.crx'
            chrome_options.add_extension(extension_path)

        chromedriver_path = os.path.dirname(os.path.dirname(__file__)) + r'\tools\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)  # executable_path驱动路径
        driver.maximize_window()
        # driver.set_window_size(1920, 1080)
        # driver.set_window_size(800, 600)
        return driver

    def open_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 关闭当前页面
    def close_browser(self):
        self.driver.close()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)


flag = False  # true:jenkins无界面运行  false:有界面运行
driver = Chrome_Browser(flag).driver

# if __name__ == '__main__':
#     driver = Chrome_Browser()
#     driver.open_url('http://172.16.20.15/caiyun/task/index')
