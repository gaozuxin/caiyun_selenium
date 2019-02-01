# coding=utf8

import smtplib
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
import unittest
import time, os

from common.my_logger import logger


class Email(object):

    # ==============定义发送邮件 ===============

    def send_mail(file, file_new):
        f = open(file_new, 'rb')
        # 读取测试报告正文
        mail_body = f.read()
        f.close()
        smtpserver = 'smtp.qq.com'  # 发送邮箱服务器
        # 发送邮箱用户/密码(登录邮箱操作)
        username = '120983257@qq.com'
        passwd = 'passwd'
        sender = '120983257@qq.com'  # 发送邮箱
        receiver = ['gaozuxin@yeah.net', 'gaozuxin@jiuqi.com.cn']  # 接收邮箱
        logger.info(("[{}]Receiving mailbox:{}".format(os.path.basename(__file__), receiver)))
        tname = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        header = u'%s 接口自动化测试报告 ' % tname

        # 只发正文，不发附件
        subject = '自动化测试报告'  # 发送主题
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['Header'] = header
        msg['From'] = sender
        msg['To'] = ",".join(receiver)

        # 连接发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, passwd)  # 登录邮箱
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
        smtp.quit()

    # ======================查找最新的测试报告==========================

    def new_report(file, testreport):
        # 方式1：
        # lists = os.listdir(testreport)
        # lists.sort(key = lambda fn: os.path.getmtime(testreport + '\\' + fn))
        # file_new = os.path.join(testreport,lists[-1])
        # print(file_new)
        # return file_new

        # 方式2：
        dirs = os.listdir(testreport)
        dirs.sort()
        newreportname = dirs[-1]
        logger.info("[{}]The new report name:{}".format(os.path.basename(__file__), newreportname))
        file_new = os.path.join(testreport, newreportname)
        return file_new


# if __name__ == '__main__':
#     # 获取当前的项目目录UskidInterface
#     testdir = os.path.dirname(os.path.dirname(__file__))
#
#     test_dir = os.path.join(testdir, r'E:\jiuqi_python\python_selenium')
#     test_report = os.path.join(testdir, 'report')
#
#     now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
#     filename = test_report + '/result_' + now + '.html'
#     fp = open(filename, 'wb')
#
#     # stream放生成报告的路径
#     runner = HTMLTestRunner(stream=fp, title="测试报告", description='用例执行情况：')
#     # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#     # runner.run(discover)
#     fp.close()
#
#     new_reportn = new_report(test_report)
#     print(new_reportn)
#     # send_mail(new_report)
