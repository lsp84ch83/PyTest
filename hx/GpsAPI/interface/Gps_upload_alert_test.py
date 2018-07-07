#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/4/26 14:13
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import unittest
import requests
import json
import time

class GpsUploadAlert(unittest.TestCase):
    def setUp(self):
        self.bash_url = 'http://api-maintenance-hx.hollo.cn/api/alarm_list/'
        # 获取当前时间戳
        self.new = int(time.time())

    def tearDown(self):
        pass


