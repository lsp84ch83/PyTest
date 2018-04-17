#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 10:20
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import requests
import unittest

class GetEventListTest(unittest.TestCase):
    # 查询发布会接口
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/get_event_list/'

    def test_get_event_null(self):
        # 发布会id为空
        r = requests.get(self.url, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_error(self):
        # 发布会id错误
        r = requests.get(self.url, params={'eid':'123'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_success(self):
        # 发布会id为1，查询正确
        r = requests.get(self.url, params={'eid':'1'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'], '红米5 发布会')
        self.assertEqual(result['data']['address'], '北京会展中心')
        self.assertEqual(result['data']['start_time'], '2018-09-22T14:00:00')


if __name__ == '__main__':
    unittest.main()
