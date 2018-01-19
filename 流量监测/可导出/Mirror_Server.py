#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 21:54
# @Author  : Soner
# @version :
# @license : Copyright(C), Your Company

import time
import subprocess
import xlwt
import os

def getUid(package_name):#获取UID
    cmd = 'adb shell dumpsys package ' + package_name + ' | findstr userId'
    p1 = subprocess.Popen(cmd, shell = True,
    stdout=subprocess.PIPE, stderr = subprocess.PIPE)#用adb获取信息
    uidLongString = str(p1.stdout.read().strip(), encoding="utf-8")
    uidLongList = uidLongString.split("=")
    uid = uidLongList[1]
    return uid[0:5]

def getFlowFromUid(packagename, uid=None):
    '''
    # 通过应用uid，获取应用当前消耗的流量
    # return (rcv,snd)
    '''
    if uid is None:
        uid = getUid(packagename)
    cmd = 'adb shell cat /proc/net/xt_qtaguid/stats | findstr %s' % uid
    std = os.popen(cmd)
    net_rcv_bck = []
    net_rcv_front = []
    net_snd_bck = []
    net_snd_front = []

    lo_rcv_bck = []
    lo_rcv_front = []
    lo_snd_bck = []
    lo_snd_front = []

    for line in std:
        data = line.split()
        if 'ccmni0' in line:
            background_flow = int(data[4]) == 0
            if background_flow:
                net_rcv_bck.append(int(data[5]))
                net_snd_bck.append(int(data[7]))
            else:
                net_rcv_front.append(int(data[5]))
                net_snd_front.append(int(data[7]))
        elif 'lo' in line:
            background_flow = int(data[4]) == 0
            if background_flow:
                lo_rcv_bck.append(int(data[5]))
                lo_snd_bck.append(int(data[7]))
            else:
                lo_rcv_front.append(int(data[5]))
                lo_snd_front.append(int(data[7]))
    return sum(net_rcv_bck), sum(net_rcv_front), sum(net_snd_bck), sum(net_snd_front), \
            sum(lo_rcv_bck), sum(lo_rcv_front), sum(lo_snd_bck), sum(lo_snd_front)

time_end =259200 # 72个小时时间，单位秒
col =0
row =0

book_Mirror_Server = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建新的工作簿Mirror

sheet_load_Mirror_Server = book_Mirror_Server.add_sheet('流量', cell_overwrite_ok=True)  # 创建新的sheet，并命名为LOAD

sheet_load_Mirror_Server.write(row, col, "时间")
sheet_load_Mirror_Server.write(row, col + 1, "网络下行(KB)")
sheet_load_Mirror_Server.write(row, col + 2, "网络上行(KB)")
sheet_load_Mirror_Server.write(row, col + 3, "网络总流量(KB)")
sheet_load_Mirror_Server.write(row, col + 4, "本地下行(KB)")
sheet_load_Mirror_Server.write(row, col + 5, "本地上行(KB)")
sheet_load_Mirror_Server.write(row, col + 6, "本地总流量(KB)")

# ----------------- 需要监测的包名 -----------------
package_name_Mirror_Server= "cn.hollo.mirror.service"
uid = (getUid(package_name_Mirror_Server))[0:5]
try:
    uid_sdk = getUid(package_name_Mirror_Server)
    print(time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time())) +'  uid =  '+str(uid_sdk))
except:
    print('获取Mirror-uid失败')

row =1
col =0
s = 1
net_bck_start_rx, net_front_start_rx, net_bck_start_tx, net_front_start_tx, \
lo_bck_start_rx, lo_front_start_rx, lo_bck_start_tx, lo_front_start_tx = getFlowFromUid(package_name_Mirror_Server, uid)

net_start_rx = net_bck_start_rx + net_front_start_rx
net_start_tx = net_bck_start_tx + net_front_start_tx
lo_start_rx = lo_bck_start_rx + lo_front_start_rx
lo_start_tx = lo_bck_start_tx + lo_front_start_tx

while   time_end > 0:

    net_bck_end_rx, net_front_end_rx, net_bck_end_tx, net_front_end_tx, \
    lo_bck_end_rx, lo_front_end_rx, lo_bck_end_tx, lo_front_end_tx = getFlowFromUid(package_name_Mirror_Server, uid)

    net_end_rx = net_bck_end_rx + net_front_end_rx
    net_end_tx = net_bck_end_tx + net_front_end_tx
    lo_end_rx = lo_bck_end_rx + lo_front_end_rx
    lo_end_tx = lo_bck_end_tx + lo_front_end_tx

    net_flow_rx, net_flow_tx = net_end_rx - net_start_rx, net_end_tx - net_start_tx
    lo_flow_rx, lo_flow_tx = lo_end_rx - lo_start_rx, lo_end_tx - lo_start_tx
    net_rx_kb, net_tx_kb = round(net_flow_rx / 1024, 3), round(net_flow_tx / 1024, 3)
    lo_rx_kb, lo_tx_kb = round(lo_flow_rx / 1024, 3), round(lo_flow_tx / 1024, 3)

    timeNow = time.strftime('%Y-%m-%d   %H:%M:%S', time.localtime(time.time()))  # 获取当前时间

    sheet_load_Mirror_Server.write(row, col, timeNow)  # 写入时间
    sheet_load_Mirror_Server.write(row, col + 1, net_rx_kb)  # 写入网络下行(KB)
    sheet_load_Mirror_Server.write(row, col + 2, net_tx_kb)  # 写入网络上行(KB)
    sheet_load_Mirror_Server.write(row, col + 3, round(net_rx_kb + net_tx_kb, 3))  # 写入网络总流量(KB)
    sheet_load_Mirror_Server.write(row, col + 4, lo_rx_kb)  # 写入本地上行(KB)
    sheet_load_Mirror_Server.write(row, col + 5, lo_tx_kb)  # 写入本地下行(KB)
    sheet_load_Mirror_Server.write(row, col + 6, round(lo_rx_kb + lo_tx_kb, 3))  # 写入本地总流量(KB)
    book_Mirror_Server.save(r"d:\Mirror_Server_Folw.xls")

    print("---------- %s ----------" % row)
    print(
          '网络下行：', net_rx_kb, 'KB\t',
          '网络上行：', net_tx_kb, 'KB\t',
          '网络总流量', round(net_rx_kb + net_tx_kb, 3), 'KB\t\t',
          '本地下行：', lo_rx_kb, 'KB\t',
          '本地上行：', lo_tx_kb, 'KB\t',
          '本地总流量', round(lo_rx_kb + lo_tx_kb, 3), 'KB\t'
          )

    row = row +1
    time.sleep(10)  # 控制监测频率
    time_end -=10
    s +=1
    if time_end <=0:
        print("---------- END ----------")