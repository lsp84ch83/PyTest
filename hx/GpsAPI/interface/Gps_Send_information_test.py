#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/4/25 17:47
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import unittest
import requests
import json
import time

class GpsSend(unittest.TestCase):
    ''' GPS上传信息 '''
    def setUp(self):
        self.base_url = "http://api-maintenance-hx.hollo.cn/device_info/"
        # 获取当前时间戳
        self.new = int(time.time())


    def tearDown(self):
        pass

    def test_Api_all_null(self):
        ''' 所有参数为空 '''
        payload = {
            "positioning_mode": "",
            "signal_intensity": "",
            "electric_quantity": "",
            "voltage": "",
            "device_code": "",
            "dismantle_status":"",
            "gps": {
                "lat": "",
                "lng": "",
                "at": "",
                "speed": "",
                "direction": ""
                }
            }
        r = requests.post(self.base_url, data=json.dumps(payload),headers={'Content-Type': 'application/json'})
        self.result = r.json()
        self.assertEqual(self.result['code'], -1)
        self.assertEqual(self.result['msg'], '参数错误')

    def test_Api_Arbitrarily_null(self):
        ''' 任意参数为空 '''
        payload = {
            "positioning_mode": "",
            "signal_intensity": 18,
            "electric_quantity": 74,
            "voltage": 2.93558,
            "device_code": "8597412541457",
            "dismantle_status": 0,
                "gps": {
                "lat": 39.95716858,
                "lng": 116.32652283,
                "at": self.new,
                "speed": 0,
                "direction": 1
                }
            }
        r = requests.post(self.base_url, data=json.dumps(payload),headers={'Content-Type': 'application/json'})
        self.result = r.json()
        self.assertEqual(self.result['code'], -1)
        self.assertEqual(self.result['msg'], '参数错误')

    def test_Api_Location_Gps(self):
        ''' 定位模式为GPS '''
        payload = {
            "positioning_mode": "gps",
            "signal_intensity": 18,
            "electric_quantity": 74,
            "voltage": 2.93558,
            "device_code": "8597412541457",
            "dismantle_status": 0,
            "gps": {
                "lat": 39.95716858,
                "lng": 116.32652283,
                "at": self.new,
                "speed": 0,
                "direction": 1
                }
            }
        r = requests.post(self.base_url, data=json.dumps(payload),headers={'Content-Type': 'application/json'})
        self.result = r.json()
        self.assertEqual(self.result['code'], 0)
        self.assertEqual(self.result['msg'], 'ok')

    def test_Api_Location_base_station(self):
        ''' 定位模式为基站 '''
        payload = {
            "positioning_mode": "基站",
            "signal_intensity": 18,
            "electric_quantity": 74,
            "voltage": 2.93558,
            "device_code": "8597412541457",
            "dismantle_status": 0,
            "gps": {
                "lat": 39.95716858,
                "lng": 116.32652283,
                "at": self.new,
                "speed": 0,
                "direction": 1
                }
            }
        r = requests.post(self.base_url, data=json.dumps(payload),headers={'Content-Type': 'application/json'})
        self.result = r.json()
        self.assertEqual(self.result['code'], 0)
        self.assertEqual(self.result['msg'], 'ok')

    def test_Api_Location_Unknown(self):
        ''' 定位模式为未知 '''
        payload = {
            "positioning_mode": "5g",
            "signal_intensity": 18,
            "electric_quantity": 88,
            "voltage": 2.93558,
            "device_code": "8597412541457",
            "dismantle_status": 0,
            "gps": {
                "lat": 39.95716858,
                "lng": 116.32652283,
                "at": self.new,
                "speed": 0,
                "direction": 1
                }
            }
        r = requests.post(self.base_url, data=json.dumps(payload),headers={'Content-Type': 'application/json'})
        self.result = r.json()
        self.assertEqual(self.result['code'], -1)
        self.assertEqual(self.result['msg'], '报歉〜出问题了')

    def test_Api_dismantle_alert(self):
        ''' 处于拆除报警状态 '''
        payload = {
            "positioning_mode": "gps",
            "signal_intensity": 18,
            "electric_quantity": 78,
            "voltage": 2.93558,
            "device_code": "8597412541457",
            "dismantle_status": 1,
            "gps": {
                "lat": 39.95716858,
                "lng": 116.32652283,
                "at": self.new,
                "speed": 0,
                "direction": 1
                }
            }
        r = requests.post(self.base_url, data=json.dumps(payload),headers={'Content-Type': 'application/json'})
        self.result = r.json()
        self.assertEqual(self.result['code'], 0)
        self.assertEqual(self.result['msg'], 'ok')



if __name__ == '__main__':
    unittest.main()