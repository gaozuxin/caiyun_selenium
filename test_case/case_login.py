import unittest, sys, time

import os

from common.chrome_browser import driver
from common.my_logger import logger
from common.my_mysql import mysql
from common.other import one_browser_window
from framework.caiyun.index_page import IndexPage
from framework.caiyun.login_page import LoginPage


class CaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("****************************************start****************************************")
        cls.loginpage = LoginPage(driver)
        cls.indexpage = IndexPage(driver)

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
    def test_login_001(self):
        """用户登录"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_login()

        login_data = [
            {"usr": "13683066505", "pwd": "gzx123456", "code": "A1b8S", "show_info": "用户名/手机号或密码错误！"},
            {"usr": "18201112814", "pwd": "gzx123456", "code": "A1b8S", "show_info": "登录成功"},
            {"usr": "18201112814", "pwd": "gzx12345", "code": "A1b8S", "show_info": "用户名/手机号或密码错误！"},
            {"usr": "gaozuxin", "pwd": "gzx123456", "code": "A1b8S", "show_info": "登录成功"},

        ]
        for index in range(len(login_data)):
            self.loginpage.login(login_data[index]['usr'], login_data[index]['pwd'], login_data[index]['code'])
            time.sleep(2)
            show_info_l = self.loginpage.showinfo_login()
            logger.info("[{}]期望：{}；实际：{}".format(os.path.basename(__file__), login_data[index]['show_info'],
                                                 show_info_l))
            driver.delete_all_cookies()
            self.assertEqual(login_data[index]['show_info'], show_info_l, msg="用户登录，登录提示信息有误")
            time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_login_002(self):
        """用户名登录验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_login()
        usr_data = [
            {'usr': '', 'show_info': '此处不能为空'},
            {'usr': '_____', 'show_info': ''},
            {'usr': 'a', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': 'a_', 'show_info': ''},
            {'usr': '123456789012345678901', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': '12345678901234567890', 'show_info': ''},
            {'usr': '</>', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': '1gao高_', 'show_info': ''}
        ]
        for index in range(len(usr_data)):
            self.loginpage.input_username(usr_data[index]['usr'])
            self.loginpage.switch_verifyimg()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_username()
            logger.info("[{}]用户名：{}；期望：{}；实际：{}".format(os.path.basename(__file__), usr_data[index]['usr'],
                                                            usr_data[index]['show_info'],show_info_l))
            self.assertIn(usr_data[index]['show_info'], show_info_l, msg="用户登录，用户名提示信息有误")
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_login_003(self):
        """密码注册验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_login()
        pwd_data = [
            {'pwd': '', 'show_info': '此处不能为空'},
            {'pwd': 'a2345q', 'show_info': ''},
            {'pwd': 'qwerty', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': '12345q', 'show_info': ''},
            {'pwd': '1234q', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': 'qwert1', 'show_info': ''},
            {'pwd': '1234567890123456', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': '123456789012345q', 'show_info': ''},
            {'pwd': '123456789012345qq', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': '123456ab9012345q', 'show_info': ''},
            {'pwd': '__11__', 'show_info': '密码中必须包含6-16位字母、数字组合'}
        ]
        for index in range(len(pwd_data)):
            self.loginpage.input_password(pwd_data[index]['pwd'])
            self.loginpage.switch_verifyimg()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_password()
            logger.info("[{}]密码：{}；期望：{}；实际：{}".format(os.path.basename(__file__), pwd_data[index]['pwd'],
                                                        pwd_data[index]['show_info'],show_info_l))
            self.assertIn(pwd_data[index]['show_info'], show_info_l, msg="登录用户，密码提示信息有误")
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_login_004(self):
        """图片验证码注册校验"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_login()
        vrfcode_data = [
            {'code': '', 'show_info': '此处不能为空'},
            {'code': 'ab12', 'show_info': ''},
        ]
        for index in range(len(vrfcode_data)):
            self.loginpage.input_verifycode(vrfcode_data[index]['code'])
            self.loginpage.switch_verifyimg()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_verifycode()
            logger.info("[{}]'图片验证码'：{}；期望：{}；实际：{}".format(os.path.basename(__file__), vrfcode_data[index]['code'],
                                                          vrfcode_data[index]['show_info'],show_info_l))
            self.assertIn(vrfcode_data[index]['show_info'], show_info_l, msg="登录用户，图片验证码提示信息有误")
            time.sleep(1)
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_regist_001(self):
        """新用户注册"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        sql = "delete from user_info where phone='18637607203';"
        flag = mysql.update(sql)
        if flag:
            logger.info("用户删除成功")
        else:
            logger.error("用户删除失败")
        self.loginpage.open_regist()
        self.loginpage.regist('gaozuxin', 'gzx123456', '18637607203', '9274', 'A1b8S')
        self.loginpage.take_screenshot()
        islogin = self.indexpage.get_loginuser()
        if islogin == 'gaozuxin':
            logger.info('注册并登录成功')
        else:
            logger.error('注册并登录失败')
            time.sleep(2)
        self.indexpage.click_exit_userbtn()
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_regist_002(self):
        """用户名注册验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_regist()
        usr_data = [
            {'usr': '', 'show_info': '此处不能为空'},
            {'usr': '_____', 'show_info': ''},
            {'usr': 'a', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': 'a_', 'show_info': ''},
            {'usr': '123456789012345678901', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': '12345678901234567890', 'show_info': ''},
            {'usr': '</>', 'show_info': '用户名只能包含2位以上20位以下数字、英文、中文、下划线'},
            {'usr': '1gao高_', 'show_info': ''}
        ]
        for index in range(len(usr_data)):
            self.loginpage.input_regist_username(usr_data[index]['usr'])
            self.loginpage.switch_regist_img()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_registuser()
            logger.info("[{}]用户名：{}；期望：{}；实际：{}".format(os.path.basename(__file__), usr_data[index]['usr'],
                                                            usr_data[index]['show_info'],show_info_l))
            self.assertIn(usr_data[index]['show_info'], show_info_l, msg="注册用户，用户名提示信息有误")
            time.sleep(1)

        self.loginpage.regist('gaozuxin', 'gzx123456', '13683066505', '9274', 'A1b8S')
        # show_info_r = self.loginpage.showinfo_regist()
        # self.assertEqual('用户名已存在，请更换', show_info_r, msg="注册用户，用户名错误提示信息有误")
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_regist_003(self):
        """密码注册验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_regist()
        pwd_data = [
            {'pwd': '', 'show_info': '此处不能为空'},
            {'pwd': 'a2345q', 'show_info': ''},
            {'pwd': 'qwerty', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': '12345q', 'show_info': ''},
            {'pwd': '1234q', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': 'qwert1', 'show_info': ''},
            {'pwd': '1234567890123456', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': '123456789012345q', 'show_info': ''},
            {'pwd': '123456789012345qq', 'show_info': '密码中必须包含6-16位字母、数字组合'},
            {'pwd': '123456ab9012345q', 'show_info': ''},
            {'pwd': '__11__', 'show_info': '密码中必须包含6-16位字母、数字组合'}
        ]
        for index in range(len(pwd_data)):
            self.loginpage.input_regist_password(pwd_data[index]['pwd'])
            self.loginpage.switch_regist_img()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_registpwd()
            logger.info("[{}]密码：{}；期望：{}；实际：{}".format(os.path.basename(__file__), pwd_data[index]['pwd'],
                                                        pwd_data[index]['show_info'],show_info_l))
            self.assertIn(pwd_data[index]['show_info'], show_info_l, msg="注册用户，密码提示信息有误")
            time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_regist_004(self):
        """手机号注册验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_regist()
        mob_data = [
            {'mob': '', 'show_info': '此处不能为空'},
            {'mob': '13001112814', 'show_info': ''},
            {'mob': '182011128141', 'show_info': '请填写有效的手机号'},
            {'mob': '18201112814', 'show_info': ''},
            {'mob': '1730111281', 'show_info': '请填写有效的手机号'},
            {'mob': '17301112814', 'show_info': ''},
            {'mob': '11001112814', 'show_info': '请填写有效的手机号'},
            {'mob': '17601112814', 'show_info': ''},
            {'mob': '1820111281>', 'show_info': '请填写有效的手机号'},
            {'mob': '18901112814', 'show_info': ''},
            {'mob': '1820111281q', 'show_info': '请填写有效的手机号'}
        ]
        for index in range(len(mob_data)):
            self.loginpage.input_regist_mobile(mob_data[index]['mob'])
            self.loginpage.switch_regist_img()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_registmobile()
            logger.info("[{}]手机号：{}；期望：{}；实际：{}".format(os.path.basename(__file__), mob_data[index]['mob'],
                                                       mob_data[index]['show_info'],show_info_l))
            self.assertIn(mob_data[index]['show_info'], show_info_l, msg="注册用户，手机号提示信息有误")
            time.sleep(1)
        self.loginpage.input_regist_mobile('18637607203')
        self.loginpage.click_get_verifycode() #获取验证码
        # show_info_r = self.loginpage.showinfo_regist()
        # self.assertEqual('手机号已存在', show_info_r, msg="注册用户，手机号错误提示信息有误")
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_regist_005(self):
        """短信注册码注册验证"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_regist()
        code_data = [
            {'code': '', 'show_info': '此处不能为空'},
            {'code': '1234', 'show_info': ''},
            {'code': '1234a', 'show_info': '请填写数字'},
            {'code': '1234', 'show_info': ''},
            {'code': '</>', 'show_info': '请填写数字'},
            {'code': '12345', 'show_info': ''},
            {'code': '\\t', 'show_info': '请填写数字'}
        ]
        for index in range(len(code_data)):
            self.loginpage.input_regist_code(code_data[index]['code'])
            self.loginpage.switch_regist_img()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_registcode()
            logger.info("[{}]短信注册码：{}；期望：{}；实际：{}".format(os.path.basename(__file__), code_data[index]['code'],
                                                        code_data[index]['show_info'],show_info_l))
            self.assertIn(code_data[index]['show_info'], show_info_l, msg="注册用户，短信注册码提示信息有误")

        self.loginpage.regist('gaoxin', 'gzx123456', '13683066505', '92745', 'A1b8S')
        # show_info_r = self.loginpage.showinfo_regist()
        # self.assertEqual('手机注册码错误', show_info_r, msg="注册用户，短信注册码错误提示信息有误")
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')

    # @unittest.skip
    def test_regist_006(self):
        """图片验证码注册校验"""
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '开始执行======================*')
        one_browser_window()
        self.loginpage.open_regist()
        vrfcode_data = [
            {'code': '', 'show_info': '此处不能为空'},
            {'code': 'ab12', 'show_info': ''},
        ]
        for index in range(len(vrfcode_data)):
            self.loginpage.input_regist_verifycode(vrfcode_data[index]['code'])
            self.loginpage.switch_regist_img()
            time.sleep(1)
            show_info_l = self.loginpage.showinfo_registvrfcode()
            logger.info("[{}]'图片验证码'：{}；期望：{}；实际：{}".format(os.path.basename(__file__), vrfcode_data[index]['code'],
                                                          vrfcode_data[index]['show_info'],show_info_l))
            self.assertIn(vrfcode_data[index]['show_info'], show_info_l, msg="注册用户，图片验证码提示信息有误")

        self.loginpage.regist('gaoxin', 'gzx123456', '13683066505', '9274', 'A1b8SS')
        # show_info_r = self.loginpage.showinfo_regist()
        # self.assertEqual('验证码错误', show_info_r, msg="注册用户，图片验证码提示信息有误")
        time.sleep(3)
        logger.info('*======================用例' + sys._getframe().f_code.co_name + '执行结束======================*')


if __name__ == '__main__':
    unittest.main()
