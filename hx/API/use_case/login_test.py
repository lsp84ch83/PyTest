#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/5/28 11:25

__author__ = 'Soenr'

import unittest
import requests
import json
import time


class sign_in(unittest.TestCase):
    def setUp(self):
        self.url = "http://eam-dev.hollo.cn/api/test_login"

    def test_api_sign_success(self):
        '''登录成功'''
        payload = {
            "username":"lijun",
            "password":"96e79218965eb72c92a549dd5a330112",
            "access_token":""
        }
        r = requests.post(self.url,data=json.dumps(payload),headers={"Content-Type":'application/json'})
        self.resule = r.json()
        self.assertEqual(self.resule['code'],0)
        self.assertEqual(self.resule['msg'],'操作成功')

    def test_api_sign_no_injection(self):
        '''检测是否存在注入'''
        payload = {
            "username": "' or 1=1",
            "password": "96e79218965eb72c92a549dd5a330112",
            "access_token": ""
        }
        r = requests.post(self.url, data=json.dumps(payload), headers={"Content-Type": 'application/json'})
        self.resule = r.json()
        self.assertEqual(self.resule['code'], 10001)
        self.assertEqual(self.resule['msg'], '帐号或密码错误')