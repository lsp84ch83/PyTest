#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 16:08
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
class Login():
    # 登录
    def user_login(self, driver):
        # 切换到内页
        driver.switch_to_frame("x-URS-iframe")
        # 登录
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("ziwuxuan")
        #sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("lsp84ch83")
        #sleep(1)
        driver.find_element_by_id("dologin").click()
        #sleep(3)

    def user_logout(self, driver):
        # 退出
        driver.find_element_by_xpath("/html/body/header/div[1]/ul[1]/li[18]/a").click()
        driver.find_element_by_class_name("relogin").click()