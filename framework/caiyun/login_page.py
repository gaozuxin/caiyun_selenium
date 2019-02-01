# -*- coding: utf-8 -*-
import time

import os
from selenium import webdriver
from common.my_logger import logger
from common.my_mysql import Mysql
from framework.base_page import BasePage

# 登录页面实现类
from framework.caiyun.other_elements import Login_url, Regist_url


class LoginPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    pagetitle = '采云 - 登录'
    username_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[1]/input'  # 用户名输入框
    showinfo_username_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[1]/span/span/span[3]'  # 登录用户提示信息
    password_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[2]/input'  # 密码输入框
    showinfo_password_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[2]/span/span/span[3]'  # 登录密码提示信息
    verifycode_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[3]/input'  # 验证码输入框
    showinfo_verifycode_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[3]/span/span/span[3]'  # 登录验证码提示信息
    verifyimg_loc = r'//*[@id="form1"]/div/div[3]/div[1]/div[3]/img'  # 验证码图片
    loginbtn_loc = r'//*[@id="form1"]/div/div[3]/div[2]/a'  # 登录按钮
    showinfo_login_loc = r'//*[@id="logincont"]/div[10]'  # 用户登录提示信息
    user_name = r'/html/body/nav/div[3]/ul[2]/li[3]/a/span'  # 登录成功index页面用户名
    regist_username_loc = r'//*[@id="form2"]/div/div/div[1]/div[1]/input'  # 注册用户输入框
    showinfo_registuser_loc = r'//*[@id="form2"]/div/div/div[1]/div[1]/span/span/span[3]'  # 注册用户名提示信息
    regist_password_loc = r'//*[@id="form2"]/div/div/div[1]/div[2]/input'  # 注册密码输入框
    showinfo_registpwd_loc = '//*[@id="form2"]/div/div/div[1]/div[2]/span/span/span[3]'  # 注册密码提示信息
    regist_mobile_loc = r'//*[@id="form2"]/div/div/div[1]/div[3]/input'  # 注册手机号输入框
    showinfo_registmobile_loc = r'//*[@id="form2"]/div/div/div[1]/div[3]/span/span/span[3]'  # 注册手机号提示信息
    regist_code_loc = r'//*[@id="form2"]/div/div/div[1]/div[4]/input'  # 短信注册码输入框
    showinfo_registcode_loc = r'//*[@id="form2"]/div/div/div[1]/div[4]/span/span/span[3]'  # 短信注册码提示信息
    regist_verify_code_loc = r'//*[@id="form2"]/div/div/div[1]/div[5]/input'  # 注册验证码输入框
    showinfo_registvrfcode_loc = '//*[@id="form2"]/div/div/div[1]/div[5]/span/span/span[3]'  # 注册验证码提示信息
    registbtn_loc = r'//*[@id="form2"]/div/div/div[2]/a'  # 注册按钮
    regist_img_loc = r'//*[@id="form2"]/div/div/div[1]/div[5]/img'  # 注册码验证图片
    showinfo_regist_loc = '//*[@id="logincont"]/div[13]/div'  # 用户注册提示信息
    get_verifycode_loc = '//*[@id="form2"]/div/div/div[1]/div[4]/a'  # 获取验证码

    # 调用base_page中的_open打开链接
    def open_login(self):
        self._open(Login_url)

    def open_regist(self):
        self._open(Regist_url)

    # 调用send_keys对象，输入用户名
    def input_username(self, username):
        el = self.find_element(self.username_loc)
        self.send_keys(el, username)

    # 调用send_keys对象，输入密码
    def input_password(self, password):
        el = self.find_element(self.password_loc)
        self.send_keys(el, password)

    def input_verifycode(self, verifycode):
        el = self.find_element(self.verifycode_loc)
        self.send_keys(el, verifycode)

    # 点击登录
    def click_loginbtn(self):
        self.click_element(self.loginbtn_loc)

    def showinfo_username(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_username_loc).text
        except:
            return ''

    def showinfo_password(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_password_loc).text
        except:
            return ''

    def showinfo_verifycode(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_verifycode_loc).text
        except:
            return ''

    # 用户名或密码不合理是Tip框内容展示
    def showinfo_login(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_login_loc).text
        except:
            return ''

    def showinfo_regist(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_regist_loc).text
        except:
            return ''

    def login(self, username, password, verifycode=''):
        logger.info("[{}]login用户登陆信息：{}, {}, {}" .format(os.path.basename(__file__), username,
                                                         password, verifycode))
        self.input_username(username)
        self.input_password(password)
        self.input_verifycode(verifycode)
        self.click_loginbtn()

        # showinfo_login = self.showinfo_login()
        # logger.info("登录提示信息：%s" % showinfo_login)
        # return show_div

    # 更换验证码
    def switch_verifyimg(self):
        self.find_element(self.verifyimg_loc).click()

    # 更换注册验证码
    def switch_regist_img(self):
        self.find_element(self.regist_img_loc).click()

    # 登录成功页面中的用户名称查找
    def show_username(self):
        return self.find_element(self.user_name).text

    def input_regist_username(self, regist_username):
        el = self.find_element(self.regist_username_loc)
        self.send_keys(el, regist_username)

    def showinfo_registuser(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_registuser_loc).text
        except:
            return ''

    def showinfo_registpwd(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_registpwd_loc).text
        except:
            return ''

    def showinfo_registmobile(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_registmobile_loc).text
        except:
            return ''

    def showinfo_registvrfcode(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_registvrfcode_loc).text
        except:
            return ''

    def showinfo_registcode(self):
        try:
            time.sleep(1)
            return self.find_element_xpath(self.showinfo_registcode_loc).text
        except:
            return ''

    def input_regist_password(self, regist_password):
        el = self.find_element(self.regist_password_loc)
        self.send_keys(el, regist_password)

    def input_regist_mobile(self, regist_mobile):
        el = self.find_element(self.regist_mobile_loc)
        self.send_keys(el, regist_mobile)

    def input_regist_code(self, regist_code):
        el = self.find_element(self.regist_code_loc)
        self.send_keys(el, regist_code)

    def input_regist_verifycode(self, regist_verifycode):
        el = self.find_element(self.regist_verify_code_loc)
        self.send_keys(el, regist_verifycode)

    # 点击注册按钮
    def click_registbtn(self):
        self.find_element(self.registbtn_loc).click()

    # 点击注册按钮
    def click_get_verifycode(self):
        self.find_element(self.get_verifycode_loc).click()

    def regist(self, regist_username, regist_password, regist_mobile, regist_code, regist_verifycode):
        logger.info("[{}]regist用户注册信息：{}, {}, {}, {}, {}".format(os.path.basename(__file__),regist_username,
                                                                 regist_password, regist_mobile, regist_code,
                                                                 regist_verifycode))
        self.input_regist_username(regist_username)
        self.input_regist_password(regist_password)
        self.input_regist_mobile(regist_mobile)
        self.input_regist_code(regist_code)
        self.input_regist_verifycode(regist_verifycode)
        self.click_registbtn()
        # 缺少注册提示验证


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
#     loginpage.open_regist()
#     loginpage.regist('gaozuxin', 'gzx123456', '18637607203', '9274', 'A1b8S')
#     islogin = loginpage.find_element('/html/body/nav/div[3]/ul[2]/li[3]/a/span').text
#     if islogin == 'gaozuxin':
#         print('注册并登录成功')
#     else:
#         print('注册并登录失败')
#
#     mysql = Mysql()
#     sql = "delete from user_info where phone='18637607203';"
#     flag = mysql.update(sql)
#     if flag:
#         print("用户删除成功")
#     else:
#         print("用户删除失败")
