#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/6 16:07
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from Selenium.Automatic.public import Login

class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://mail.126.com")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test1_login(self):
        username = "ziwuxuan"
        password = "lsp84ch83"
        # 调用登录
        Login().user_login(self.driver, username, password)
        # 调用退出
        Login().user_logout(self.driver)
        self.driver.quit()