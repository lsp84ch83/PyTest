#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 16:31
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import logging
import  os

logging.getLogger().setLevel(logging.DEBUG)
# Training data
logging.basicConfig(filename = os.path.join('./interface/'+ 'log.txt'), level = logging.DEBUG) # 把log日志保存为log.txt
logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')


# 指定测试用例目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义报告存放的位置
    filenames = './report/' + now + '_result.html'
    fp = open(filenames, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,  # 报告文件地址
                            title='GPS接口自动化测试', # 报告标题
                            description="接口地址：http://api-maintenance-hx.hollo.cn/device_info/", #报告描述
                            tester='李君' #执行人员
                            )
    runner.run(testsuit)
    fp.close()

'''
    # 发送邮箱服务器
    mail_host = "smtp.qq.com"
    # 发送邮箱用户/密码
    mail_user = '317152347@qq.com'
    mail_pass = 'rxsqygisnojybhhb'

    # 接收邮箱
    receivers = '13521895260@163.com'

    # 发送邮件主题
    subject = '接口测试报告'
    msgRoot = MIMEMultipart('related')
    # 邮件正文内容
    msgRoot.attach(MIMEText('系统邮件，请勿回复！！！', 'plain', 'utf-8'))
    msgRoot['Subject'] = Header(subject, 'utf-8')
    # 添加附件
    sendfile = open("F:\\PyTest\\GpsAPI\\report\\%s_result.html" %now,'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s_result.html"'%now
    msgRoot.attach(att)

    try:
        # 连接发送邮件
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, msgRoot.as_string())
        print('发送成功')
    except smtplib.SMTPException as err:
        print('发送失败')
        print(str(err))
    finally:
        smtpObj.quit()
'''