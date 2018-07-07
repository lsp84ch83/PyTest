#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/6/8 14:23
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import unittest
import xlrd
import time
from iwebshop.modular import openurl, login

class Logintest(unittest.TestCase):
    
    def setUp(self):
        self.driver = openurl.open()
        self.wb = xlrd.open_workbook(r"F:\PyTest\iwebshop\data\user.xlsx")   # 打开Excel
        self.sh = self.wb.sheet_by_index(0) # 获取工作表

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login_succes(self):
        ''' 用户密码均正确 '''
        username = self.sh.cell(0,0).value
        password = self.sh.cell(0,1).value
        login.login(self.driver, username, password)

    def test_login_password_error(self):
        ''' 密码错误 '''
        username = self.sh.cell(1,0).value
        password = self.sh.cell(1,1).value
        login.login(self.driver, username, password)

if __name__ == '__main__':
    unittest.main()