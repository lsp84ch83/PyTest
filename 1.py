#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 15:49
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
# coding=utf-8
import subprocess
import time

fo = open(r"D:\foo.txt", "w")
# # 获取进程ID
# getProcessIdcmd = 'adb shell ps | findstr cn.com.haoluo.www'
# p = subprocess.Popen(getProcessIdcmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# content = p.stdout.readlines()
# if len(content) == 1:
#     processId = content[0].split()[1]
# else:
#     print("not get processID")
# # 获取进程对应的UID
# getUidcmd = 'adb shell cat /proc/' + processId + '/status | findstr Uid'
#
# p = subprocess.Popen(getUidcmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# content = p.stdout.readlines()
# uidList = content[0].strip().split('\t')
# print(uidList)
# uid = uidList[1]
uid = "10344"
# 获取UID对应的Traffic
getTrafficcmd = 'adb shell cat /proc/net/xt_qtaguid/stats | findstr ' + uid

for i in range(10000):
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    traffic_initial = [0] * 16
    traffic_prefix = []
    p = subprocess.Popen(getTrafficcmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        ll = line.strip()
        ll2 = ll.replace(' ', ',')
        ll2_list = ll2.split(',')
        traffic_list = ll2_list[5:]
        traffic_prefix = ll2_list[0:4]
        traffic_list_int = [int(e) for e in traffic_list]

        traffic_initial = [x + y for x, y in zip(traffic_initial, traffic_list_int)]
        # print traffic_list
        print(currentTime + "," + ll2)
    retval = p.wait()
    print(traffic_initial)
    traffic_list_str = [str(e) for e in traffic_initial]
    print(traffic_prefix + traffic_list_str)
    traffic = ','.join(traffic_prefix + traffic_list_str)
    print(currentTime + ',' + traffic)
    fo.write(currentTime + ',' + traffic + '\n')
    time.sleep(60)
    print('--------------')
fo.close()