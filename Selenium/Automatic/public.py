#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/6 16:08
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from time import sleep
class Login():
    # 登录
    def user_login(self, driver, username, password):
        # 切换到内页
        driver.switch_to_frame("x-URS-iframe")
        # 登录
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(username)
        sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        sleep(1)
        driver.find_element_by_id("dologin").click()
        sleep(3)

    def user_logout(self, driver):
        # 退出
        driver.find_element_by_xpath("/html/body/header/div[1]/ul[1]/li[18]/a").click()
        driver.find_element_by_class_name("relogin").click()
        driver.switch_to_default_content()  # 返回上一层farm框